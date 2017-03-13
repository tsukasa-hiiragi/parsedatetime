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

Weekdays = [
    'Pazartesi', 'Salı', 'Çarşamba', 'Perşembe',
    'Cuma', 'Cumartesi', 'Pazar',
]
shortWeekdays = [
    'Pzt', 'Sal', 'Çrs', 'Prs', 'Cum', 'Cmt',
]
# library does not know how to conjugate words
# библиотека не умеет спрягать слова
Months = [
    'Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz',
    'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık',
]
shortMonths = [
    u'Oc', u'Şu', u'Mar', u'Ni', u'May', u'Ha',
    u'Te', u'Ağ', u'Ey', u'Ek', u'Ka', u'Ar',
]
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
