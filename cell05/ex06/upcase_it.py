#!/usr/bin/env python3

import sys
if len(sys.argv) > 1:
    print(' '.join(sys.argv[1:]).upper())
else:
    print("none")