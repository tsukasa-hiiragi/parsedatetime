# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .base import *  # noqa

# don't use an unicode string
localeID = 'tr_TR'
dateSep = ['-', '.', '/']
timeSep = [':']
meridian = []
usesMeridian = False
uses24 = True

Weekdays = ['pazartesi', 'salı', 'çarşamba', 'perşembe',
            'cuma', 'cumartesi', 'pazar']
shortWeekdays = ['pzt', 'sal', 'çrs', 'prs', 'cum', 'cmt']

# library does not know how to conjugate words
# библиотека не умеет спрягать слова
Months = ['ocak', 'şubat', 'mart', 'nisan', 'mayıs', 'haziran',
 'temmuz', 'ağustos', 'eylül', 'ekim', 'kasım', 'aralık']

shortMonths = ['oc|oca', 'şu|şub', 'mar|ma', 'ni|nis', 'may|ma', 'ha|haz', 'te|tem', 'ağ|ağu',
               'ey|eyl', 'ek|eki', 'ka|kas', 'ar|ara']

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
    'bir': 1,
    'iki': 2,
    'üç': 3,
    'dört': 4,
    'beş': 5,
    'altı': 6,
    'yedi': 7,
    'sekiz': 8,
    'dokuz': 9,
    'on': 10,
}

dp_order = ['d', 'm', 'y']

decimal_mark = '.'

units = {
    'seconds': ['saniye'],
    'minutes': ['dakika'],
    'hours': ['saat'],
    'days': ['gün'],
    'weeks': ['hafta'],
    'months': ['ay'],
    'years': ['yıl', 'sene'],
}

Modifiers = {
    'önce': -1,
}

dayOffsets = {
    'yarın': 1,
    'bugün': 0,
    'dün': -1,
}
