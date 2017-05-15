# -*-coding:utf-8-*-

import requests
import traceback
import pymysql
import simplejson
import threading
import time
import math
from lxml import etree
from public.mysqlpooldao import MysqlDao
from public.redispooldao import RedisDao
from public.city import City
import sys

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

mysql_dao = MysqlDao()
redis_dao = RedisDao()
redis_key = 'baidu:20170210_bd_square_list'
ak = '8FmZyUmWHn5cYNZCtgAnuZ0iGQWlGkjr'
# 257c0efcef9b45a1b05ebf94d6e4e24c
# uwKQbWPtEPB6Q6aOuooq50KE1fDbHMgs
# 9MKbkaS7bFWVxGrWkrDSQbvAMy1bHscH
# 1FtTxyBFo6sGLplwVS7VFyq7KTypFRVM
# OpGXmbL7cqrYTBekvXOUXWFf3Y9L4DBL
# 8FmZyUmWHn5cYNZCtgAnuZ0iGQWlGkjr

def get_url(city_name, jw, list_id):
    url = 'http://api.map.baidu.com/place/v2/search?query=美食&page_size=20&page_num=0&scope=2&bounds=' + jw + '&output=json&ak=' + ak
    req = requests.get(url)
    if req.status_code == 200:
        #req.encoding = 'utf8'

        html = req.content
        #html = unicode(html, "utf8")
        ll = html.replace('', '').replace('', '')
        html = eval(ll) # 字符串转json
        try:
            total = html['total']
            print total
        except:
            print(html)
            print req.status_code
            raise Exception(u'抛出异常')
        if total == 0:
            print u'无'
        else:
            page_num = math.ceil(total * 0.05)
            print total
            print page_num
            item = 0
            while item < int(page_num):
                # for item in range(int(page_num)):
                page_url = 'http://api.map.baidu.com/place/v2/search?query=美食&page_size=20&page_num=' + str(item) + '&scope=2&bounds=' + jw + '&output=json&ak=' + ak
                print page_url
                page_req = requests.get(page_url)
                if page_req.status_code == 200:

                    page_html = page_req.content
                    page_ll = page_html.replace('', '').replace('', '')
                    page_html = eval(page_ll)  # 字符串转json
                    #page_html = page_req.json()

                    status = page_html['status']
                    message = page_html['message']
                    shops = page_html['results']

                    if len(shops) == 0:
                        break
                    else:
                        shop_name = shop_tel = shop_addr = shop_lat = shop_lng = street_id = shop_uid = detail = u'无'
                        detail_info = tag = shop_type = detail_url = overall_rating = price = shop_hours = taste_rating = u'无'
                        service_rating = environment_rating = facility_rating = hygiene_rating = technology_rating = u'无'
                        image_num = group_num = discount_num = comment_num = favorite_num = checkin_num = u'无'
                        # print i, down_jw, up_jw, total, status, message

                        for shop in shops:
                            if 'uid' in shop:
                                shop_uid = shop['uid']
                                if 'name' in shop:
                                    shop_name = shop['name'].replace("'", "''")
                                if 'location' in shop:
                                    if 'lat' and 'lng' in shop['location']:
                                        shop_lat = shop['location']['lat']
                                        shop_lng = shop['location']['lng']
                                if 'telephone' in shop:
                                    shop_tel = shop['telephone']
                                if 'address' in shop:
                                    shop_addr = shop['address'].replace('"', '').replace("'", "''").replace('\\', '')
                                if 'street_id' in shop:
                                    street_id = shop['street_id']
                                if 'detail' in shop:
                                    detail = shop['detail']
                                if 'detail_info' in shop:
                                    detail_info = shop['detail_info']
                                    if 'tag' in detail_info:
                                        tag = detail_info['tag']
                                    if 'type' in detail_info:
                                        shop_type = detail_info['type']
                                    if 'detail_url' in detail_info:
                                        detail_url = detail_info['detail_url']
                                    if 'price' in detail_info:
                                        price = detail_info['price']
                                    # if 'shop_hours' in detail_info:
                                    #     shop_hours = detail_info['shop_hours']
                                    if 'overall_rating' in detail_info:
                                        overall_rating = detail_info['overall_rating']
                                    # if 'taste_rating' in detail_info:
                                    #     taste_rating = detail_info['taste_rating']
                                    if 'service_rating' in detail_info:
                                        service_rating = detail_info['service_rating']
                                    if 'environment_rating' in detail_info:
                                        environment_rating = detail_info['environment_rating']
                                    # if 'facility_rating' in detail_info:
                                    #     facility_rating = detail_info['facility_rating']
                                    # if 'hygiene_rating' in detail_info:
                                    #     hygiene_rating = detail_info['hygiene_rating']
                                    # if 'technology_rating' in detail_info:
                                    #     technology_rating = detail_info['technology_rating']
                                    if 'image_num' in detail_info:
                                        image_num = detail_info['image_num']
                                    if 'groupon_num' in detail_info:
                                        group_num = detail_info['groupon_num']
                                    #print group_num
                                    # if 'discount_num' in detail_info:
                                    #     discount_num = detail_info['discount_num']
                                    if 'comment_num' in detail_info:
                                        comment_num = detail_info['comment_num']
                                    #print comment_num
                                        # if 'favorite_num' in detail_info:
                                        #     favorite_num = detail_info['favorite_num']
                                        # if 'checkin_num' in detail_info:
                                        #     checkin_num = detail_info['checkin_num']

                                    print city_name, shop_name, shop_tel, shop_uid, shop_lat, shop_lng, shop_addr, street_id, detail, jw, tag, shop_type, detail_url, price, overall_rating, service_rating, environment_rating, image_num, group_num, comment_num
                                    sql = (
                                              "insert ignore into "
                                              "20170210_bd_shop_list "
                                              "(city, shop_name, shop_tel, shop_uid, shop_lat, shop_lng, shop_addr, "
                                              "street_id, detail, jw, tag, type, detail_url, price, overall_rating, "
                                              "service_rating, environment_rating, image_num, group_num, comment_num) "
                                              "values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', "
                                              "'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                                          ) % (city_name, shop_name, shop_tel, shop_uid, shop_lat, shop_lng,
                                               shop_addr, street_id, detail, jw, tag, shop_type, detail_url, price,
                                               overall_rating, service_rating, environment_rating, image_num,
                                               group_num, comment_num)
                                    print (sql)
                                    mysql_dao.execute(sql)

                #time.sleep(1)
                item += 1
    else:
        print(req.status_code)
        raise Exception(u'抛出异常')


if __name__ == '__main__':
    while True:
        shop_list_json = redis_dao.lpop(redis_key)
        if shop_list_json is None:
            break
        shop_list = simplejson.loads(shop_list_json)
        list_id = shop_list[0]
        city_name = shop_list[1]
        jw = shop_list[2]

        # list_url = 'http://www.dianping.com/shanghai/hotel'
        try:
            get_url(city_name, jw, list_id)
        except Exception as e:
            traceback.print_exc()
            print(e)
            continue
        sql = 'UPDATE `20170210_bd_square_list` SET `status`="1" WHERE (`id`="%s")' % list_id
        print(sql)
        try:
            mysql_dao.execute(sql)
        except:
            pass
