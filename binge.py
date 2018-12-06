#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Minimal UNDERFed wrapper for everyday tasks.
    @author: Saumil Shah'''

import os
import gc
import sys

def progress(i, number, files):
    
    '''Displays a progressbar, which updates
    as loop iterates through files.'''

    c1 = int( ((i)*50) / number )
    pr = str(int( ((i)*100)/number ))
    bar = '\r[{}{}] {:>3s}% {}...\t'.format('#'*c1,'-'*(50-c1),
                                             pr, files[i][:5])
    sys.stdout.write(bar)
    sys.stdout.flush()

def binger(func, extension, path):
    
    '''Makes a sorted list of all the files
    with given extension, and path. Performs
    given function on all the files.'''

    if path == None: os.chdir(os.getcwd())
    else: os.chdir(path)

    files=[]
    for f in os.listdir(path):
            if f.endswith(extension):
                files.append(f)
    files.sort()
    number = len(files)

    print ()
    print (' {}'.format('='*70))
    print (' {:^70s}'.format('File-list'))
    print (' {}'.format('='*70))
    for f in files:
        print (' {:^70s}'.format(f))
    print (' {}'.format('='*70))
    total = 'Total {} {} file(s) were found.'.format(number, extension)
    print (' {:^70s}'.format(total))
    print (' {}'.format('='*70))
    print ()

    for i in range(number):
        gc.collect()
        progress(i,number,files)
        func(files,i)

    bar = '\r[{}] 100% - Done! -\n'.format('#'*50)
    sys.stdout.write(bar)
    sys.stdout.flush()