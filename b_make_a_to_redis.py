# -*-coding:utf-8-*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import simplejson

from public.mysqlpooldao import MysqlDao
from public.redispooldao import RedisDao

redis_key = 'baidu:20170210_bd_square_list'
mysql_dao = MysqlDao()
redis_dao = RedisDao()

if __name__ == '__main__':
    sql = 'SELECT * FROM `20170210_bd_square_list` WHERE `status`=0'
    shop_lists = mysql_dao.execute(sql)
    for shop_list in shop_lists:
        shop_list_json = simplejson.dumps(shop_list)
        redis_dao.rpush(redis_key, shop_list_json)
        print(shop_list_json)
