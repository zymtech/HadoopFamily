# -*- coding: utf-8 -*-

import sys

for line in sys.stdin:
    try:
        jobline = line.split('\t',3)
        print '%s\t%s' % ('!'+jobline[2], jobline[3])
    except BaseException:
        pass