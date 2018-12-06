#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time as t
import argparse as ap

parser = ap.ArgumentParser()
parser.add_argument('extension')
parser.add_argument('-p', '--path')
args = parser.parse_args()
extension = str(args.extension)

from binge import binger

def testfuntion(files,i):
    t.sleep(1)

binger(testfuntion, extension, args.path)