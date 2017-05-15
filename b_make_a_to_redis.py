# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import simplejson
from public.mysqlpooldao import MysqlDao
from public.redispooldao import RedisDao

redis_key = 'gaode:20170209_gaode_dianping_sectionl'
mysql_dao = MysqlDao()
redis_dao = RedisDao()

if __name__ == '__main__':
    sql = 'SELECT * FROM `a_gaode_section_longitude_latitude` WHERE `status`=0'
    section_lists = mysql_dao.execute(sql)
    # print section_lists
    for section_list in section_lists:
        section_list_json = simplejson.dumps(section_list)
        print section_list_json
        redis_dao.rpush(redis_key, section_list_json)
        print(section_list_json)
