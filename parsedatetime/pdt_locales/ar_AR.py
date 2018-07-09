# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .base import *  # noqa

# don't use an unicode string
localeID = 'ar_AR'
dateSep = ['.', '-', '/']
uses24 = False

timeFormats = {
    'long': timeFormats['full'],
}

dp_order = ['m', 'd', 'y']


dayOffsets = {
    'دیروز' : -1,
    'يوم أمس': -1,
    'امروز': 0,
    'اليوم': 0,
    'فردا': 1
}

Months = [
    'يناير',
    'فبراير',
    'مارس',
    'أبريل',
    'مايو',
    'يونيو',
    'يوليو',
    'أغسطس',
    'سبتمبر',
    'أكتوبر',
    'نوفمبر',
    'ديسمبر',
]

Modifiers = {
    'منذ': -1,
}

#TODO: Translate other units too.
units = {
    'seconds': ['ثانية'],
    'minutes': ['دقيقة', 'دقائق'],
    'hours': ['ساعة', 'ساعات'],
    'days': ['يوم','أيام'],
    'weeks': ['أسبوع'],
    'months': ['شهر'],
    'years': ['عام', 'سنة'],
}

