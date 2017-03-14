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

shortMonths = ['oc', 'şu', 'mar', 'ni', 'may', 'ha', 'te', 'ağ',
               'ey', 'ek', 'ka', 'ar']

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
