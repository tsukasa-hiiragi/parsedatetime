# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .base import *  # noqa

# don't use an unicode string
# Simplified Chinese
localeID = 'zh_CN'
dateSep = ['-', '.', '/']
timeSep = [':']
meridian = []
usesMeridian = False
uses24 = True

Weekdays = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天|星期日']
shortWeekdays = ['周一|礼拜一', '周二|礼拜二', '周三|礼拜三', '周四|礼拜四', '周五|礼拜五', '周六|礼拜六', '星期日|星期日|礼拜日']

Months = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']

shortMonths = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']

dateFormats = {
    'full': 'EEEE, dd MMMM yyyy',
    'long': 'dd MMMM yyyy',
    'medium': 'dd-MM-yyyy',
    'short': 'dd-MM-yy',
}

timeFormats = {
    'full': 'HH:mm:ss v',
    'long': 'HH:mm:ss z',
    'medium': 'HH:mm:ss',
    'short': 'HH:mm',
}

numbers = {
    '零': 0,
    '一': 1,
    '二': 2,
    '三': 3,
    '四': 4,
    '五': 5,
    '六': 6,
    '七': 7,
    '八': 8,
    '九': 9,
    '十': 10,
}

dp_order = ['d', 'm', 'y']

decimal_mark = '.'

units = {
    'seconds': ['秒'],
    'minutes': ['分', '分钟'],
    'hours': ['时', '小时', '钟头' ],
    'days': ['天', '日'],
    'weeks': ['周', '星期'],
    'months': ['月'],
    'years': ['年'],
}

Modifiers = {
    '前': -1,
}

dayOffsets = {
    '明天': 1,
    '今天': 0,
    '昨天': -1
}
