"""
Run this in python 2 to read in the marshalled passband file and save it as a legacy pickle.
"""

import marshal
import pickle
import glob
import time

for legacy_pb in glob.glob('*.pb'):
    # Read in the marshalled passband:
    with open(legacy_pb, 'rb') as f:
        lpb = marshal.load(f)

    # Add missing keys:
    lpb['originating_phoebe_version'] = 2.0
    lpb['version'] = 1.0
    lpb['comments'] = 'Converted from marshalled passband version.'
    lpb['reference'] = None
    lpb['timestamp'] = time.ctime()

    # Save as a protocol-1 pickle:
    with open(legacy_pb+'.pkl2', 'wb') as f:
        pickle.dump(lpb, f)
