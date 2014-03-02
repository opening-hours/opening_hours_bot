#!/usr/bin/env python
# encoding: utf-8

import re

wrong = '1200-2300'

regex = re.compile(r'\A(?P<start_hour>[0-1][0-9]|2[0-4])(?P<start_min>[:1-5][0-9]|0[0-9])\s*(?P<sep>-)\s*(?P<end_hour>[0-1][0-9]|2[0-4])(?P<end_min>[:1-5][0-9]|0[0-9])\Z')

re_object = re.search(regex, wrong)
bot_right_val = '%s:%s%s%s:%s' % (
        re_object.group('start_hour'), re_object.group('start_min'),
        re_object.group('sep'),
        re_object.group('end_hour'), re_object.group('end_min')
        )
print '%s -> %s' % (wrong, bot_right_val)
