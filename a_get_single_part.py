# -*- coding:utf-8 -*-
import sys
from public.city import City
from public.mysqlpooldao import MysqlDao
import pymysql
pymysql.install_as_MySQLdb()

city_list = City.city_list
mysql_dao = MysqlDao()

if __name__ == '__main__':
    for city_list_single in city_list:
        base_city_name = city_list_single[0]
        i1 = city_list_single[1]
        i2 = city_list_single[2]
        j1 = city_list_single[3]
        j2 = city_list_single[4]
        space_i = (i2 - i1) / 4
        space_j = (j2 - j1) / 4
        # print i1,i2,j1,j2,space_i,space_j
        types = ['050000', '050100', '050101', '050102', '050103', '050104', '050105', '050106', '050107', '050108',
                 '050109', '050110', '050111', '050112', '050113', '050114', '050115', '050116', '050117', '050118',
                 '050119', '050120', '050121', '050122', '050123', '050200', '050201', '050202', '050203', '050204',
                 '050205', '050206', '050207', '050208', '050209', '050210', '050211', '050212', '050213', '050214',
                 '050215', '050216', '050217', '050300', '050301', '050302', '050303', '050304', '050305', '050306',
                 '050307', '050308', '050309', '050310', '050311', '050400', '050500', '050501', '050502', '050503',
                 '050504', '050600', '050700', '050800', '050900']
        for j in range(0, 4):
            for i in range(1, 5):
                for type_single in types:
                    section_left_x = i1 + space_i * (i - 1)
                    section_left_y = j1 + space_j * (j + 1)
                    section_rigth_x = i1 + space_i * i
                    section_right_y = j1 + space_j * j
                    start_left = str(i1) + ',' + str(j2)
                    start_right = str(i2) + ',' + str(j1)
                    type = type_single
                    # print base_city_name,section_left_x,section_left_y,section_rigth_x,section_right_y,start_left,start_right,type
                    sql = ('INSERT IGNORE INTO `a_gaode_section_longitude_latitude`'
                           '(`city_name`,`section_left_longitude_x`,`section_left_latitude_y`,`section_right_longitude_x`,`section_right_latitude_y`,`start_left`,`start_right`,`type`)'
                           'VALUES ("%s","%s","%s","%s","%s","%s","%s","%s")'
                           ) % (
                        base_city_name, section_left_x, section_left_y, section_rigth_x, section_right_y, start_left,start_right,type)
                    mysql_dao.execute(sql)
                    print(sql)
