"""
Run this in python 3 to read in the python 2 pickle passband file and save it as a python 3 pickle.
"""

import pickle
import glob
import time
import os

for legacy_pb in glob.glob('*.pb'):
    # Read in the pickled passband:
    with open(legacy_pb+'.pkl2', 'rb') as f:
        pb = pickle.load(f, encoding='latin1')

    # Save as a protocol-3 pickle:
    with open(legacy_pb+'3', 'wb') as f:
        pickle.dump(pb, f, protocol=3)

    # Delete the conv file:
    os.remove(legacy_pb+'.pkl2')
