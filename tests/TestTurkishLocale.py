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
        locale = 'tr_TR'
        self.ptc = pdt.Constants(locale)
        self.cal = pdt.Calendar(self.ptc)

    def testTurkishDate(self):
        expected = datetime.datetime.now() - datetime.timedelta(days=7)
        parsed = self.cal.parseDT('bir Hafta önce')
        parsed = [parsed[0].timetuple(), parsed[1]]
        self.assertExpectedResult(parsed, (expected.timetuple(), 1))

    def testTurkishDate3LetterShortMonth(self):
        parsed = self.cal.parseDT('08 Eyl 2014 17:29:00')
        parsed = [parsed[0].timetuple(), parsed[1]]
        self.assertExpectedResult(
            parsed,
            (datetime.datetime(2014, 9, 8, 17, 29).timetuple(), 3),
        )

if __name__ == "__main__":
    unittest.main()
