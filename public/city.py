# -*-coding:utf-8-*-

from collections import OrderedDict

class City:
    city_list = OrderedDict(
            [
                (u'上海', 1),
                (u'三亚', 345),
                (u'长沙', 344),
                (u'丽江', 279),
                (u'昆明', 267),
                (u'贵阳', 258),
                (u'东莞', 219),
                (u'佛山', 208),
                (u'珠海', 206),
                (u'郑州', 160),
                (u'威海', 152),
                (u'烟台', 148),
                (u'南昌', 134),
                (u'合肥', 110),
                (u'台州', 108),
                (u'绍兴', 104),
                (u'嘉兴', 102),
                (u'温州', 101),
                (u'南通', 94),
                (u'常州', 93),
                (u'哈尔滨', 79),
                (u'长春', 70),
                (u'太原', 35),
                (u'石家庄', 24),
                (u'海口', 23),
                (u'济南', 22),
                (u'青岛', 21),
                (u'大连', 19),
                (u'沈阳', 18),
                (u'西安', 17),
                (u'武汉', 16),
                (u'厦门', 15),
                (u'福州', 14),
                (u'无锡', 13),
                (u'宁波', 11),
                (u'天津', 10),
                (u'重庆', 9),
                (u'成都', 8),
                (u'深圳', 7),
                (u'苏州', 6),
                (u'南京', 5),
                (u'广州', 4),
                (u'杭州', 3),
                (u'北京', 2),
            ]
    )
    city_list_bak = {
        u'沈阳': 18,
        u'青岛': 21,
        u'成都': 8,
        u'西安': 17,
        u'大连': 19,
        u'重庆': 9,
        u'北京': 2,
        u'天津': 10,
        u'上海': 1,
        u'杭州': 3,
        u'宁波': 11,
        u'广州': 4,
        u'深圳': 7,
        u'南京': 5,
        u'苏州': 6,
        u'武汉': 16,
        u'厦门': 15,
        u'长沙': 344,
        u'三亚': 345,
        u'南通': 94,
        u'南昌': 134,
        u'烟台': 148,
        u'哈尔滨': 79,
        u'长春': 70,
        u'珠海': 206,
        u'佛山': 208,
        u'济南': 22,
        u'石家庄': 24,
        u'海口': 23,
        u'威海': 152,
        u'温州': 101,
        u'台州': 108,
        u'昆明': 267,
        u'丽江': 279,
        u'无锡': 13,
        u'绍兴': 104,
        u'嘉兴': 102,
        u'贵阳': 258,
        u'太原': 35,
        u'郑州': 160,
        u'合肥': 110,
        u'东莞': 219,
        u'福州': 14,
        u'常州': 93
    }
    city_spa_pingyin_bak = [(u'丽江', 'http://www.dianping.com/search/category/279/50/g158'),
                              (u'北京', 'http://www.dianping.com/search/category/2/50/g158'),
                              (u'天津', 'http://www.dianping.com/search/category/10/50/g158'),
                              (u'沈阳', 'http://www.dianping.com/search/category/18/50/g158'),
                              (u'大连', 'http://www.dianping.com/search/category/19/50/g158'),
                              (u'长春', 'http://www.dianping.com/search/category/70/50/g158'),
                              (u'哈尔滨', 'http://www.dianping.com/search/category/79/50/g158'),
                              (u'石家庄', 'http://www.dianping.com/search/category/24/50/g158'),
                              (u'太原', 'http://www.dianping.com/search/category/35/50/g158'),
                              (u'呼和浩特', 'http://www.dianping.com/search/category/46/50/g158'),
                              (u'廊坊', 'http://www.dianping.com/search/category/33/50/g158'),
                              (u'上海', 'http://www.dianping.com/search/category/1/50/g158'),
                              (u'杭州', 'http://www.dianping.com/search/category/3/50/g158'),
                              (u'南京', 'http://www.dianping.com/search/category/5/50/g158'),
                              (u'苏州', 'http://www.dianping.com/search/category/6/50/g158'),
                              (u'无锡', 'http://www.dianping.com/search/category/13/50/g158'),
                              (u'济南', 'http://www.dianping.com/search/category/22/50/g158'),
                              (u'厦门', 'http://www.dianping.com/search/category/15/50/g158'),
                              (u'宁波', 'http://www.dianping.com/search/category/11/50/g158'),
                              (u'福州', 'http://www.dianping.com/search/category/14/50/g158'),
                              (u'青岛', 'http://www.dianping.com/search/category/21/50/g158'),
                              (u'合肥', 'http://www.dianping.com/search/category/110/50/g158'),
                              (u'常州', 'http://www.dianping.com/search/category/93/50/g158'),
                              (u'扬州', 'http://www.dianping.com/search/category/12/50/g158'),
                              (u'温州', 'http://www.dianping.com/search/category/101/50/g158'),
                              (u'绍兴', 'http://www.dianping.com/search/category/104/50/g158'),
                              (u'嘉兴', 'http://www.dianping.com/search/category/102/50/g158'),
                              (u'烟台', 'http://www.dianping.com/search/category/148/50/g158'),
                              (u'威海', 'http://www.dianping.com/search/category/152/50/g158'),
                              (u'镇江', 'http://www.dianping.com/search/category/98/50/g158'),
                              (u'南通', 'http://www.dianping.com/search/category/94/50/g158'),
                              (u'金华', 'http://www.dianping.com/search/category/105/50/g158'),
                              (u'徐州', 'http://www.dianping.com/search/category/92/50/g158'),
                              (u'潍坊', 'http://www.dianping.com/search/category/149/50/g158'),
                              (u'淄博', 'http://www.dianping.com/search/category/145/50/g158'),
                              (u'临沂', 'http://www.dianping.com/search/category/155/50/g158'),
                              (u'马鞍山', 'http://www.dianping.com/search/category/114/50/g158'),
                              (u'台州', 'http://www.dianping.com/search/category/108/50/g158'),
                              (u'泰州', 'http://www.dianping.com/search/category/99/50/g158'),
                              (u'济宁', 'http://www.dianping.com/search/category/150/50/g158'),
                              (u'泰安', 'http://www.dianping.com/search/category/151/50/g158'),
                              (u'成都', 'http://www.dianping.com/search/category/8/50/g158'),
                              (u'武汉', 'http://www.dianping.com/search/category/16/50/g158'),
                              (u'郑州', 'http://www.dianping.com/search/category/160/50/g158'),
                              (u'长沙', 'http://www.dianping.com/search/category/344/50/g158'),
                              (u'南昌', 'http://www.dianping.com/search/category/134/50/g158'),
                              (u'贵阳', 'http://www.dianping.com/search/category/258/50/g158'),
                              (u'西宁', 'http://www.dianping.com/search/category/313/50/g158'),
                              (u'重庆', 'http://www.dianping.com/search/category/9/50/g158'),
                              (u'西安', 'http://www.dianping.com/search/category/17/50/g158'),
                              (u'昆明', 'http://www.dianping.com/search/category/267/50/g158'),
                              (u'兰州', 'http://www.dianping.com/search/category/299/50/g158'),
                              (u'乌鲁木齐', 'http://www.dianping.com/search/category/325/50/g158'),
                              (u'银川', 'http://www.dianping.com/search/category/321/50/g158'),
                              (u'广州', 'http://www.dianping.com/search/category/4/50/g158'),
                              (u'深圳', 'http://www.dianping.com/search/category/7/50/g158'),
                              (u'佛山', 'http://www.dianping.com/search/category/208/50/g158'),
                              (u'珠海', 'http://www.dianping.com/search/category/206/50/g158'),
                              (u'东莞', 'http://www.dianping.com/search/category/219/50/g158'),
                              (u'三亚', 'http://www.dianping.com/search/category/345/50/g158'),
                              (u'海口', 'http://www.dianping.com/search/category/23/50/g158'),
                              (u'南宁', 'http://www.dianping.com/search/category/224/50/g158'),
                              (u'惠州', 'http://www.dianping.com/search/category/213/50/g158'),
                              ]

    city_spa_pingyin = {
        u'沈阳': 'http://www.dianping.com/search/category/18/50/g158',
        u'无锡': 'http://www.dianping.com/search/category/13/50/g158',
        u'台州': 'http://www.dianping.com/search/category/108/50/g158',
        u'哈尔滨': 'http://www.dianping.com/search/category/79/50/g158',
        u'扬州': 'http://www.dianping.com/search/category/12/50/g158',
        u'淄博': 'http://www.dianping.com/search/category/145/50/g158',
        u'廊坊': 'http://www.dianping.com/search/category/33/50/g158',
        u'厦门': 'http://www.dianping.com/search/category/15/50/g158',
        u'兰州': 'http://www.dianping.com/search/category/299/50/g158',
        u'青岛': 'http://www.dianping.com/search/category/21/50/g158',
        u'临沂': 'http://www.dianping.com/search/category/130/50/g158',
        u'长春': 'http://www.dianping.com/search/category/70/50/g158',
        u'昆明': 'http://www.dianping.com/search/category/267/50/g158',
        u'佛山': 'http://www.dianping.com/search/category/208/50/g158',
        u'宁波': 'http://www.dianping.com/search/category/11/50/g158',
        u'长沙': 'http://www.dianping.com/search/category/344/50/g158',
        u'天津': 'http://www.dianping.com/search/category/10/50/g158',
        u'丽江': 'http://www.dianping.com/search/category/279/50/g158',
        u'北京': 'http://www.dianping.com/search/category/2/50/g158',
        u'嘉兴': 'http://www.dianping.com/search/category/102/50/g158',
        u'烟台': 'http://www.dianping.com/search/category/148/50/g158',
        u'福州': 'http://www.dianping.com/search/category/14/50/g158',
        u'马鞍山': 'http://www.dianping.com/search/category/114/50/g158',
        u'西安': 'http://www.dianping.com/search/category/17/50/g158',
        u'上海': 'http://www.dianping.com/search/category/1/50/g158',
        u'东莞': 'http://www.dianping.com/search/category/219/50/g158',
        u'银川': 'http://www.dianping.com/search/category/321/50/g158',
        u'西宁': 'http://www.dianping.com/search/category/313/50/g158',
        u'济南': 'http://www.dianping.com/search/category/22/50/g158',
        u'乌鲁木齐': 'http://www.dianping.com/search/category/325/50/g158',
        u'三亚': 'http://www.dianping.com/search/category/345/50/g158',
        u'海口': 'http://www.dianping.com/search/category/23/50/g158',
        u'威海': 'http://www.dianping.com/search/category/152/50/g158',
        u'南宁': 'http://www.dianping.com/search/category/224/50/g158',
        u'镇江': 'http://www.dianping.com/search/category/98/50/g158',
        u'泰州': 'http://www.dianping.com/search/category/99/50/g158',
        u'石家庄': 'http://www.dianping.com/search/category/24/50/g158',
        u'南昌': 'http://www.dianping.com/search/category/134/50/g158',
        u'深圳': 'http://www.dianping.com/search/category/7/50/g158',
        u'成都': 'http://www.dianping.com/search/category/8/50/g158',
        u'绍兴': 'http://www.dianping.com/search/category/104/50/g158',
        u'重庆': 'http://www.dianping.com/search/category/9/50/g158',
        u'珠海': 'http://www.dianping.com/search/category/206/50/g158',
        u'潍坊': 'http://www.dianping.com/search/category/149/50/g158',
        u'泰安': 'http://www.dianping.com/search/category/151/50/g158',
        u'南通': 'http://www.dianping.com/search/category/94/50/g158',
        u'广州': 'http://www.dianping.com/search/category/4/50/g158',
        u'太原': 'http://www.dianping.com/search/category/35/50/g158',
        u'温州': 'http://www.dianping.com/search/category/101/50/g158',
        u'大连': 'http://www.dianping.com/search/category/19/50/g158',
        u'南京': 'http://www.dianping.com/search/category/5/50/g158',
        u'徐州': 'http://www.dianping.com/search/category/92/50/g158',
        u'贵阳': 'http://www.dianping.com/search/category/258/50/g158',
        u'郑州': 'http://www.dianping.com/search/category/160/50/g158',
        u'苏州': 'http://www.dianping.com/search/category/6/50/g158',
        u'常州': 'http://www.dianping.com/search/category/93/50/g158',
        u'呼和浩特': 'http://www.dianping.com/search/category/46/50/g158',
        u'济宁': 'http://www.dianping.com/search/category/150/50/g158',
        u'武汉': 'http://www.dianping.com/search/category/16/50/g158',
        u'合肥': 'http://www.dianping.com/search/category/110/50/g158',
        u'惠州': 'http://www.dianping.com/search/category/213/50/g158',
        u'杭州': 'http://www.dianping.com/search/category/3/50/g158',
        u'金华': 'http://www.dianping.com/search/category/105/50/g158'
    }

    district = {
        u'无锡': {
            'start_lat': 31.126323, 'start_lng': 119.526079, 'end_lat': 31.991554, 'end_lng': 120.61071},
        u'台州': {
            'start_lat': 28.00603, 'start_lng': 120.296471, 'end_lat': 29.345939, 'end_lng': 121.986246},
        u'哈尔滨': {
            'start_lat': 44.067361, 'start_lng': 125.69553, 'end_lat': 46.680372, 'end_lng': 130.247069},
        u'厦门': {
            'start_lat': 24.389872, 'start_lng': 117.892558, 'end_lat': 24.912885, 'end_lng': 118.460432},
        u'长春': {
            'start_lat': 43.269971, 'start_lng': 124.550081, 'end_lat': 45.258161, 'end_lng': 127.100891},
        u'青岛': {
            'start_lat': 35.53364, 'start_lng': 119.519511, 'end_lat': 37.152706, 'end_lng': 121.413038},
        u'天津': {
            'start_lat': 38.561403, 'start_lng': 116.71421, 'end_lat': 40.259068, 'end_lng': 118.074648},
        u'昆明': {
            'start_lat': 24.390988, 'start_lng': 102.175208, 'end_lat': 26.548795, 'end_lng': 103.680037},
        u'佛山': {
            'start_lat': 22.651013, 'start_lng': 112.397536, 'end_lat': 23.578044, 'end_lng': 113.398197},
        u'宁波': {
            'start_lat': 28.84642, 'start_lng': 120.883912, 'end_lat': 30.45634, 'end_lng': 122.315886},
        u'长沙': {
            'start_lat': 27.853941, 'start_lng': 111.903209, 'end_lat': 28.667365, 'end_lng': 114.267743},
        u'沈阳': {
            'start_lat': 41.205929, 'start_lng': 122.43222, 'end_lat': 43.04927, 'end_lng': 123.820087},
        u'北京': {
            'start_lat': 39.445587, 'start_lng': 115.430282, 'end_lat': 41.066884, 'end_lng': 117.513171},
        u'嘉兴': {
            'start_lat': 30.25204, 'start_lng': 120.302546, 'end_lat': 31.036507, 'end_lng': 121.547912},
        u'烟台': {
            'start_lat': 36.565858, 'start_lng': 119.561404, 'end_lat': 38.467154, 'end_lng': 121.933365},
        u'福州': {
            'start_lat': 25.213386, 'start_lng': 118.391178, 'end_lat': 26.644976, 'end_lng': 120.539396},
        u'威海': {
            'start_lat': 36.679975, 'start_lng': 121.183403, 'end_lat': 37.615718, 'end_lng': 122.732668},
        u'上海': {
            'start_lat': 30.676443, 'start_lng': 120.862372, 'end_lat': 31.8733, 'end_lng': 122.006022},
        u'合肥': {
            'start_lat': 31.509658, 'start_lng': 116.694157, 'end_lat': 32.540838, 'end_lng': 117.889904},
        u'三亚': {
            'start_lat': 18.121885, 'start_lng': 108.938477, 'end_lat': 18.62931, 'end_lng': 109.817277},
        u'海口': {
            'start_lat': 19.529476, 'start_lng': 110.076013, 'end_lat': 20.185752, 'end_lng': 110.715645},
        u'西安': {
            'start_lat': 33.699932, 'start_lng': 107.633933, 'end_lat': 34.749336, 'end_lng': 109.828903},
        u'东莞': {
            'start_lat': 22.661484, 'start_lng': 113.528657, 'end_lat': 23.149034, 'end_lng': 114.265529},
        u'石家庄': {
            'start_lat': 37.444982, 'start_lng': 113.529719, 'end_lat': 38.770419, 'end_lng': 115.490061},
        u'南昌': {
            'start_lat': 28.163177, 'start_lng': 115.445118, 'end_lat': 29.179678, 'end_lng': 116.572049},
        u'深圳': {
            'start_lat': 22.240159, 'start_lng': 113.68352, 'end_lat': 22.857826, 'end_lng': 114.658659},
        u'成都': {
            'start_lat': 30.099735, 'start_lng': 103.029961, 'end_lat': 31.440826, 'end_lng': 104.899181},
        u'绍兴': {
            'start_lat': 29.230704, 'start_lng': 119.895488, 'end_lat': 30.292648, 'end_lng': 121.238048},
        u'重庆': {
            'start_lat': 28.166366, 'start_lng': 105.296455, 'end_lat': 32.207209, 'end_lng': 110.206934},
        u'珠海': {
            'start_lat': 21.785928, 'start_lng': 113.067677, 'end_lat': 22.460216, 'end_lng': 114.417799},
        u'杭州': {
            'start_lat': 29.194759, 'start_lng': 118.351441, 'end_lat': 30.572175, 'end_lng': 120.728369},
        u'南通': {
            'start_lat': 31.619976, 'start_lng': 120.208864, 'end_lat': 32.717331, 'end_lng': 122.005714},
        u'广州': {
            'start_lat': 22.521906, 'start_lng': 112.968521, 'end_lat': 23.935576, 'end_lng': 114.065814},
        u'太原': {
            'start_lat': 37.46253, 'start_lng': 111.522487, 'end_lat': 38.426669, 'end_lng': 113.162732},
        u'温州': {
            'start_lat': 27.019485, 'start_lng': 119.63179, 'end_lat': 28.617172, 'end_lng': 121.379221},
        u'大连': {
            'start_lat': 38.684456, 'start_lng': 120.926965, 'end_lat': 40.210115, 'end_lng': 123.541316},
        u'南京': {
            'start_lat': 31.235331, 'start_lng': 118.369429, 'end_lat': 32.618713, 'end_lng': 119.247036},
        u'贵阳': {
            'start_lat': 26.189885, 'start_lng': 106.131285, 'end_lat': 27.361274, 'end_lng': 107.286029},
        u'郑州': {
            'start_lat': 34.267764, 'start_lng': 112.727878, 'end_lat': 34.99457, 'end_lng': 114.229607},
        u'苏州': {
            'start_lat': 30.764191, 'start_lng': 119.925155, 'end_lat': 32.040481, 'end_lng': 121.39356},
        u'常州': {
            'start_lat': 31.158402, 'start_lng': 119.147396, 'end_lat': 32.065029, 'end_lng': 120.208386},
        u'武汉': {
            'start_lat': 29.972313, 'start_lng': 113.707018, 'end_lat': 31.367044, 'end_lng': 115.087233},
        u'济南': {
            'start_lat': 36.035482, 'start_lng': 116.230434, 'end_lat': 37.545278, 'end_lng': 117.753944},
        u'丽江': {
            'start_lat': 25.991142, 'start_lng': 99.38848, 'end_lat': 27.930522, 'end_lng': 101.520375}
        }