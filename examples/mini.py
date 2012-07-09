#!/usr/bin/env python
# -*- coding: windows-1251 -*-
# Copyright (C) 2005 Kiseliov Roman
__rev_id__ = """$Id: mini.py,v 1.3 2005/03/27 12:47:06 rvk Exp $"""

if __name__ == '__main__':
    from pyExcelerator import *

    w = Workbook()
    ws = w.add_sheet('Hey, Dude')
    w.save('mini.xls')

