# -*-coding:utf-8-*-

import requests
import math
import time
import simplejson
import traceback
from public.mysqlpooldao import MysqlDao
from public.redispooldao import RedisDao
from public.headers import Headers
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


def get_comment(city, shop_name, uid):
    headers = Headers.get_headers()
    url = 'http://map.baidu.com/detail?qt=ugccmtlist&from=mapwap&type=cater&orderBy=1&pageCount=20&uid=' + uid + '&pageIndex=1'
    m = 1
    while 1:
        req = requests.get(url, headers=headers)
        req.encoding = 'utf8'
        html = req.json()
        if html['errorNo'] == 0:
            break
        else:
            print 'sleep %s s' % m
            time.sleep(1 * m)
            m += 1

    if 'comment' in html:
        comment = html['comment']
        comment_avg_score = comment['comment_avg_score']
        #print comment_avg_score
        comment_num = u'无'
        try:
            comment_num = comment['comment_num']
        except:
            print(html)
            print req.status_code
        if comment_num == 0:
            print '0'
        else:
            page_num = math.ceil(comment_num * 0.05)
            print comment_num
            print page_num
            item = 1
            while item <= int(page_num):
                print '***************'
                page_url = 'http://map.baidu.com/detail?qt=ugccmtlist&from=mapwap&type=cater&orderBy=1&pageCount=20&uid=' + uid + '&pageIndex=' + str(item)
                #page_url = 'http://map.baidu.com/detail?qt=ugccmtlist&from=mapwap&type=cater&orderBy=1&pageCount=20&uid=a795b3e10c3401e9715e8041' + '&pageIndex=' + str(item)
                print page_url
                print '#####################'
                n = 1
                while 1:
                    page_req = requests.get(page_url, headers=headers)
                    page_req.encoding = 'utf8'
                    page_html = page_req.json()
                    if page_html['errorNo'] == 0:
                        break
                    else:
                        print 'sleep %s s' % n
                        time.sleep(1 * n)
                        n += 1
                if 'comment' in page_html:
                    page_comment = page_html['comment']

                    comment_list = page_comment['comment_list']
                    if len(comment_list) == 0:
                        break
                    else:
                        poi_id = user_name = comment_content = comment_time = comment_url = price = user_url = user_id = u'无'
                        environment_rating = service_rating = taste_rating = mark = source_name = comment_id = u'无'
                        for c in comment_list:
                            # 商户id
                            if 'poi_id' in c:
                                poi_id = c['poi_id']
                            # 用户名
                            if 'user_name' in c:
                                user_name = c['user_name'].replace('"', '').replace(u'😍','').replace(u'🐠','').replace(u'👍','').replace('\r\n', '').replace("'", "''").replace('\\', '')
                            # 评论内容
                            if 'content' in c:
                                comment_content = c['content'].replace('"', '').replace(u'😍','').replace(u'🐠','').replace(u'👍','').replace('\r\n', '').replace("'", "''").replace('\\', '')

                            # 评论时间
                            if 'date' in c:
                                comment_time = c['date']
                            # 评论url
                            if 'one_url' in c:
                                comment_url = c['one_url']
                            # 人均
                            if 'price' in c:
                                #print type(c['price'])
                                #if c['price'] != '0':
                                price = c['price']
                            print 'price:', price
                            # 用户url
                            if 'user_url' in c:
                                if c['user_url'] != '':
                                    user_url = c['user_url']
                                    # 用户id
                                    user_id = user_url.replace('http://www.dianping.com/member/', '')
                            # 环境
                            if 'environment_rating' in c:
                                environment_rating = c['environment_rating']
                            # 服务
                            if 'service_rating' in c:
                                service_rating = c['service_rating']
                            # 口味
                            if 'taste_rating' in c:
                                taste_rating = c['taste_rating']
                            mark = str(environment_rating) + '|' + str(service_rating) + '|' + str(taste_rating)
                            # 评论来源
                            if 'cn_name' in c:
                                source_name = c['cn_name']
                            # 评论id
                            if 'cmt_id' in c:
                                comment_id = c['cmt_id']
                            sql = (
                                      "insert ignore into "
                                      "20170210_bd_comment "
                                      "(city, shop_name, shop_uid, comment_id, user_id, poi_id, user_name,"
                                      "comment_content, comment_time, comment_url, price, user_url,"
                                      "mark, source_name, comment_num) "
                                      "values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', "
                                      "'%s', '%s', '%s', '%s', '%s')"
                                  ) % (city, shop_name, uid, comment_id, user_id, poi_id, user_name,
                                       comment_content, comment_time, comment_url, price, user_url,
                                       mark, source_name, comment_num)
                            print (sql)

                            mysql_dao.execute(sql)

                item += 1
    # else:
    #     print req.status_code
    #     raise Exception(u'抛出异常')


# def check_name(shop_name):
#     filt = (u'肯德基', u'麦当劳', u'必胜客', u'味千', u'馄饨', u'沙县', u'黄焖鸡', u'水饺')
#     for f in filt:
#         if f in shop_name:
#             return True
#     return False

if __name__ == '__main__':
    mysql_dao = MysqlDao()
    redis_dao = RedisDao()
    redis_key = 'baidu:20170210_bd_shop_list'
    while True:
        shop_str = redis_dao.lpop(redis_key)
        if shop_str == None:
            break
        shop = simplejson.loads(shop_str)
        id = shop[0]
        city = shop[1]
        uid = shop[2]
        shop_name = shop[3].replace("'", "''")
        detail_url = shop[4]
        # if check_name(shop_name):
        #     pass
        # else:
        try:
            get_comment(city, shop_name, uid)
        except Exception as e:
            traceback.print_exc()
            print(e)
            continue
        today = time.strftime('%Y-%m-%d')
        sql = 'UPDATE `20170210_bd_shop_list` SET `status`="1",`crawl_comment_date`="%s" WHERE (`id`="%s")' % (
            today, id)
        print(sql)
        mysql_dao.execute(sql)


