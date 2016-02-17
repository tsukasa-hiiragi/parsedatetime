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
'امروز': 0,
'فردا': 1
}
