# -*- coding: utf-8 -*-
import sys
import requests
import simplejson
reload(sys)
sys.setdefaultencoding('utf-8')
import traceback
import time
from public.mysqlpooldao import MysqlDao
from public.redispooldao import RedisDao
mysql_dao = MysqlDao()
redis_dao = RedisDao()

def get_comment_detail(shop_id,shop_name,lastpage,city_name):
    for page in range(lastpage,0,-1):
        target_url= 'http://ditu.amap.com/detail/get/reviewList?poiid=' + str(shop_id) + '&pagenum=' + str(page) + '&select_mode=4'
        print target_url
        res = requests.get(target_url)
        if res.status_code == 200:
            req = res.json()
            comments = req['data']['review_list']
            for comment in comments:
                comment_conent = comment_author = comment_time = comment_source = commment_url = comment_score = ''
                comment_id = 0
                comment_conents = comment['review']
                comment_conent = str(comment_conents).replace('"', '').replace(u'😍','').replace(u'🐠','').replace(u'👍','').replace('\r\n', '').replace("'", "''").replace('\\', '')
                comment_id = comment['review_id']
                comment_author = comment['author'].replace('"', '').replace(u'😍','').replace(u'🐠','').replace(u'👍','').replace('\r\n', '').replace("'", "''").replace('\\', '')
                comment_time = comment['time']
                comment_source = comment['src_name']
                commment_url = comment['review_wapurl']
                comment_score = comment['score']
                # print comment_id
                # print comment_conent, comment_author, comment_time, comment_source, commment_url, comment_score,shop_id,shop_name,city_name
                sql1 = 'INSERT IGNORE INTO `e_gaode_shop_comment_detail` (`comment_conent`,`comment_author`,`comment_time`,`comment_source`,`commment_url`,`comment_score`,`comment_id`,`shop_id`,`shop_name`,`city_name`) VALUE ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'% (
                    comment_conent,comment_author,comment_time,comment_source,commment_url,comment_score,comment_id,shop_id,shop_name,city_name
                )
                print sql1
                mysql_dao.execute(sql1)
        else:
            raise Exception('throw')


def get_comment_num(shop_id):
    url = 'http://ditu.amap.com/detail/get/reviewList?poiid=' + str(shop_id) + '&pagenum=1&select_mode=4'
    print url
    res = requests.get(url)
    # print res.status_code
    if res.status_code == 200:
        req = res.json()
        if 'new_count'in str(req):
            comment_num = req['data']['new_count']
            if comment_num == 0:
                lastpage = 0
            elif comment_num > 0 :
                if comment_num % 10 == 0:
                    lastpage = comment_num/10
                else:
                    lastpage = (comment_num/10) + 1
            return lastpage
        else:
            pass


if __name__ == '__main__':
    redis_key = 'gaode:20170214_gaode_shop_info'
    while True:
        shop_info = redis_dao.lpop(redis_key)
        if shop_info == None:
            break
        shop = simplejson.loads(shop_info)
        id = shop[0]
        shop_id = shop[1]
        shop_name = shop[2]
        city_name = shop[12]
        lastpage = get_comment_num(shop_id)
        if lastpage == 0:
            print 'no comment'
            today = time.strftime('%Y-%m-%d')
            sql = 'UPDATE `c_gaode_dianping_shop_info` SET `status`="1",`catch_comment_date`="%s" WHERE (`id`="%s")' % (
                today, id)
            print sql
            mysql_dao.execute(sql)
        else:
            print lastpage
            try:
                get_comment_detail(shop_id,shop_name,lastpage,city_name)
            except Exception as e:
                traceback.print_exc()
                print e
                continue
            today = time.strftime('%Y-%m-%d')
            sql = 'UPDATE `c_gaode_dianping_shop_info` SET `status`="1",`catch_comment_date`="%s" WHERE (`id`="%s")' % (
                today, id)
            print sql
            mysql_dao.execute(sql)








