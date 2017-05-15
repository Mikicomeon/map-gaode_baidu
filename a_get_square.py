# -*-coding:utf-8-*-

import sys
import traceback
from public.mysqlpooldao import MysqlDao
from public.city import City
from public.headers import Headers

reload(sys)
sys.setdefaultencoding('utf-8')
mysql_dao = MysqlDao()

def get_square_jw(city_name, start_lat, start_lng, end_lat, end_lng, lat_space, lng_space):
    for j in range(50):
        for i in range(50):
            down_jw = str(start_lat) + ',' + str(start_lng + lng_space*i)
            up_jw = str(start_lat + lat_space) + ',' + str(start_lng + lng_space*(i+1))
            jw = (down_jw + ',' + up_jw)
            # print i, down_jw, up_jw
            sql = (
                      "insert ignore into "
                      "20170210_bd_square_list "
                      "(city, jw, start_lat, start_lng, end_lat, end_lng, lat_space, lng_space)"
                      "values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                  ) % (city_name, jw, start_lat, start_lng, end_lat, end_lng, lat_space, lng_space)
            print sql
            mysql_dao.execute(sql)


        start_lat = start_lat + lat_space



if __name__ == '__main__':
    city_list = City.city_list
    district = City.district
    for (city_name, city_id) in city_list.items():
        #print city_name
        location = district[city_name]
        start_lat = location['start_lat']
        start_lng = location['start_lng']
        end_lat = location['end_lat']
        end_lng = location['end_lng']
        lat_space = (end_lat - start_lat) * 0.02
        lng_space = (end_lng - start_lng) * 0.02

        print city_name, start_lng, start_lat, end_lng, end_lat, lat_space, lng_space
        try:
            get_square_jw(city_name, start_lat, start_lng, end_lat, end_lng, lat_space, lng_space)
        except Exception as e:
            traceback.print_exc()
            print e