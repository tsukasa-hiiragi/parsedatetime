# -*- coding: utf-8 -*-
"""
Test parsing of simple date and times using the Turkish locale
"""
from __future__ import unicode_literals

import sys
import time
import datetime
import parsedatetime as pdt
from . import utils

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest


class test(unittest.TestCase):

    @utils.assertEqualWithComparator
    def assertExpectedResult(self, result, check, **kwargs):
        return utils.compareResultByTimeTuplesAndFlags(result, check, **kwargs)

    def setUp(self):
        locale = 'ar_AR'
        self.ptc = pdt.Constants(locale)
        self.cal = pdt.Calendar(self.ptc)

    def testArabianDateTime(self):
        now = datetime.datetime.now()
        expected = datetime.datetime(
            day=now.day-1,
            month=now.month,
            year=now.year,
            hour=21,
            minute=44,
        )
        parsed = self.cal.parseDT('يوم أمس 21:44')
        parsed = [parsed[0].timetuple(), parsed[1]]
        self.assertExpectedResult(parsed, (expected.timetuple(), 3))

if __name__ == "__main__":
    unittest.main()
