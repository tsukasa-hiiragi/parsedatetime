# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .base import *  # noqa

# don't use an unicode string
localeID = 'es'
dateSep = ['/', '.', '-']
usesMeridian = False
uses24 = True
decimal_mark = '.'

Weekdays = [
    'lunes', 'martes', 'miércoles',
    'jueves', 'viernes', 'sábado', 'domingo',
]
shortWeekdays = [
    'lun', 'mar', 'mié',
    'jue', 'vie', 'sáb', 'dom',
]
Months = [
    'enero', 'febrero', 'marzo',
    'abril', 'mayo', 'junio',
    'julio', 'agosto', 'septiembre',
    'octubre', 'noviembre', 'diciembre',
]
shortMonths = [
    'ene', 'feb', 'mar',
    'abr', 'may', 'jun',
    'jul', 'ago', 'sep',
    'oct', 'nov', 'dic',
]
dateFormats = {
    'full': "EEEE d' de 'MMMM' de 'yyyy",
    'long': "d' de 'MMMM' de 'yyyy",
    'medium': "dd-MMM-yy",
    'short': "d/MM/yy",
}

timeFormats = {
    'full': "HH'H'mm' 'ss z",
    'long': "HH:mm:ss z",
    'medium': "HH:mm:ss",
    'short': "HH:mm",
}

dp_order = ['d', 'm', 'y']

dayOffsets['ayer'] = -1
dayOffsets['hoy'] = 0

Modifiers = {
    'hace': -1,
    'from': 1
}

#TODO: Translate other units too.
units = {
    'seconds': ['segund', 'segundos', 'seg', 's'],
    'minutes': ['minuto', 'minutos', 'min', 'm'],
    'hours': ['hora', 'horas', 'hr', 'h'],
    'days': ['día', 'días'],
    'weeks': ['week', 'weeks', 'wk', 'w'],
    'months': ['month', 'months', 'mth'],
    'years': ['year', 'years', 'yr', 'y']
}
