#! /usr/bin/env python2
#
# This file is part of khmer, http://github.com/ged-lab/khmer/, and is
# Copyright (C) Michigan State University, 2009-2013. It is licensed under
# the three-clause BSD license; see doc/LICENSE.txt.
# Contact: khmer-project@idyll.org
#
import khmer
import sys
import os

K = 32


def main():
    ht = khmer.new_hashbits(32, 1, 1)
    ht.load_tagset(sys.argv[1])
    print 'loaded!'
    ht.print_tagset(os.path.basename(sys.argv[1]) + '.txt')


if __name__ == '__main__':
    main()
