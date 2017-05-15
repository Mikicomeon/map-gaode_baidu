# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import simplejson
import random
import json
import datetime
from public.mysqlpooldao import MysqlDao
from public.redispooldao import RedisDao

redis_key = 'gaode:20170214_gaode_shop_info'
mysql_dao = MysqlDao()
redis_dao = RedisDao()

class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


if __name__ == '__main__':
    sql = 'SELECT * FROM `c_gaode_dianping_shop_info` WHERE `status`=0 limit 100000'
    print sql
    section_lists = list(mysql_dao.execute(sql))
    random.shuffle(section_lists)
    for section_list in section_lists:
        section_list_json = json.dumps(section_list,cls=CJsonEncoder)
        # print section_list_json
        redis_dao.rpush(redis_key, section_list_json)
        print(section_list_json)


