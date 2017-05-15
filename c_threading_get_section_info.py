#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import threading

import sys
from public.city import City
from public.mysqlpooldao import MysqlDao
from public.redispooldao import RedisDao
import pymysql
import traceback

pymysql.install_as_MySQLdb()
from lxml import etree
import requests
import simplejson

city_list = City.city_list
mysql_dao = MysqlDao()
redis_dao = RedisDao()

redis_key = 'gaode:20170209_gaode_dianping_sectionl'


def get_singlepage_info(base_city_name, target_url, lastpage):
    # if lastpage > 1:
    target1 = target_url.split('page=')[0]
    target2 = target_url.split('page=')[1]
    target3 = target2.split('&')[1]
    page = lastpage
    while True:
        if page <= 0:
            break
        true_url = target1 + "page=" + str(page) + "&" + target3
        print true_url
        res = requests.get(true_url)
        if res.status_code == 200:
            req = res.json()
            if 'count' in req:
                shop_count = req['count']

                if shop_count:
                    if int(str(shop_count)) <> 0:
                        if 'pois' in req:
                            single_shop_infos = req['pois']
                            for single_shop_info in single_shop_infos:
                                shop_id = shop_name = shop_type = type_code = tag = shop_address = shop_location = shop_telephone = province = city = district = business_area = average_cost = rating = u'无'
                                shop_id = single_shop_info['id']
                                shop_name = single_shop_info['name']
                                # print (shop_name)
                                shop_type = single_shop_info['type']
                                type_code = single_shop_info['typecode']
                                tags = single_shop_info['tag']
                                if tags == []:
                                    tag = ''
                                else:
                                    f = lambda x: x.strip()
                                    tagss = [f(x) for x in tags]
                                    tag = ''.join(tagss).replace('"', '')
                                # print tag
                                shop_address = single_shop_info['address']
                                if shop_address == []:
                                    shop_address = ''
                                shop_location = single_shop_info['location']
                                shop_telephone = single_shop_info['tel']
                                if shop_telephone == []:
                                    shop_telephone = ''
                                province = single_shop_info['pname']
                                city = single_shop_info['cityname']
                                district = single_shop_info['adname']
                                business_area = single_shop_info['business_area']
                                if business_area == []:
                                    business_area = ''
                                average_costs = single_shop_info['biz_ext']['cost']
                                if average_costs:
                                    average_cost = average_costs
                                ratings = single_shop_info['biz_ext']['rating']
                                if ratings:
                                    rating = ratings
                                # print city,base_city_name
                                if city == base_city_name:
                                    #     print '#############################################一样的城市名字,可以写进数据库'
                                    # print shop_id,shop_name,shop_type,shop_address,shop_location,shop_telephone,city,district,business_area
                                    today = time.strftime('%Y-%m-%d')
                                    sql = ('INSERT IGNORE INTO `c_gaode_dianping_shop_info`'
                                           '(`shop_id`,`shop_name`,`shop_type`,`type_code`,`tag`,`shop_address`,`shop_location`,`shop_telephone`,`average_cost`,`rating`,`province`,`city`,`district`,`business_area`,`catch_date`)'
                                           'VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'
                                           ) % (
                                              shop_id, shop_name, shop_type, type_code, tag, shop_address,
                                              shop_location,
                                              shop_telephone, average_cost, rating, province, city, district,
                                              business_area,today)

                                    print(sql)
                                    # try:
                                    mysql_dao.execute(sql)
                                    # except:
                                    #     raise Exception('throw error')
                    else:
                        print u'该页没有店铺'
                else:
                    pass
        else:
            raise Exception('throw error')
        page = page - 1


def get_lastpage(url):
    res = requests.get(url)
    if res.status_code == 200:
        req_json = res.json()
        status = int(req_json['status'])
        if status == 1:
            total_shopnum = req_json['count']
            if total_shopnum:
                total_shopnum = int(total_shopnum)
                # print total_shopnum
                if total_shopnum == 0:
                    lastpage = 1
                else:
                    total_shopnum = int(total_shopnum)
                    if total_shopnum % 20 == 0:
                        lastpage = total_shopnum / 20
                    else:
                        lastpage = (total_shopnum / 20) + 1
                if lastpage < 100:
                    lastpage = lastpage
                else:
                    lastpage = 100
                return lastpage
            else:
                pass


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        while True:
            print self.name
            section_list_json = redis_dao.lpop(redis_key)
            if section_list_json is None:
                break
            section_list = simplejson.loads(section_list_json)
            id = section_list[0]
            base_city_name = section_list[1]
            section_left_x = section_list[2]
            section_left_y = section_list[3]
            section_right_x = section_list[4]
            section_right_y = section_list[5]
            type = section_list[8]
            section_coordinate = str(section_left_x) + ',' + str(section_left_y) + '|' + str(
                section_right_x) + ',' + str(section_right_y)
            # print section_coordinate
            # print base_city_name,section_coordinate,
            params = {
                # 'key' : '912aecbc35746bcec867c964d7c21a6f',
                # 'key' : '0402ce37d60834ba99b15b47847bf982',
                # 'key' : 'ba3f6a57ff6748abcd5ad050018d805d',
                'key': '5bc08640fe580844bb8403c8496f36be',  ##########此为无限量的key
                # 'key': 'c64fa783f1fe649c0f8c7ff97dfde1d7',
                'polygon': section_coordinate,
                'types': type,
                'offset': '20',
                'page': 1,
                'output': 'JSON',
                'extensions': 'all'
            }
            url = 'http://restapi.amap.com/v3/place/polygon'
            res = requests.get(url, params=params)
            if res.status_code == 200:
                target_url = res.url
                # print target_url
                lastpage = get_lastpage(target_url)
                # print u'最后一页为' + str(lastpage)
                try:
                    get_singlepage_info(base_city_name, target_url, lastpage)
                except Exception as e:
                    traceback.print_exc()
                    print(e)
                    continue
                sql1 = 'UPDATE `a_gaode_section_longitude_latitude` SET `status`="1" WHERE (`id`="%s")' % (id)
                # print(sql1)
                try:
                    mysql_dao.execute(sql1)
                except:
                    pass

# threads = []
# for i in range(1,6):
#     num = "Thread" + str(i)
#     thread = myThread(num)
#     threads.append(thread)
#
# for thread in threads:
#     thread.start


# 创建新线程
thread1 = myThread("Threading1")
thread2 = myThread("Threading2")
thread3 = myThread("Threading3")
thread4 = myThread("Threading4")
# thread5 = myThread()


# 开启线程
thread1.start()
thread2.start()
thread3.start()
thread4.start()
# thread5.start()


print "Exiting Main Thread"
