# -*- encoding: utf-8 -*-

"""
pdt_locales

All of the included locale classes shipped with pdt.
"""

from __future__ import absolute_import
from .icu import get_icu

locales = ['ar_AR', 'de_DE', 'en_AU', 'en_US', 'es', 'fr_FR', 'nl_NL', 'pt_BR', 'ru_RU', 'tr_TR', 'zh', 'zh_CN']

__locale_caches = {}

__all__ = ['get_icu', 'load_locale']


def load_locale(locale, icu=False):
    """
    Return data of locale
    :param locale:
    :return:
    """
    if locale not in locales:
        raise NotImplementedError("The locale '%s' is not supported" % locale)
    if locale not in __locale_caches:
        mod = __import__(__name__, fromlist=[locale], level=0)
        __locale_caches[locale] = getattr(mod, locale)
    return __locale_caches[locale]
