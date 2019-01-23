import json
import os
import sys
from glob import glob
import marshal
import pickle

"""
should be run separately under python2 (will create list_online_passbands_full) and python3 (will create list_online_passbands_full_pb3)
"""

def load_passband(fname):
    with open(fname, 'rb') as f:
        if sys.version_info[0] < 3:
            struct = marshal.load(f)
        else:
            struct = pickle.load(f)

    info = {}
    info['fname'] = os.path.basename(fname)
    info['atms'] = struct['atmlist']
    info['timestamp'] = struct.get('timestamp', None)

    return struct['pbset']+':'+struct['pbname'], info

pbtable = {}

for fname in glob('./*.pb' if sys.version_info[0] < 3 else './*.pb3'):
   print("loading {}...".format(fname))
   key, info = load_passband(fname)
   pbtable[key] = info

# dump dictionary for Python 2 or 3
if sys.version_info[0] < 3:
    fname = 'list_online_passbands_full'
else:
    fname = 'list_online_passbands_full_pb3'

print("writing to {}".format(fname))
with open(fname, 'w') as f:
    f.write(json.dumps(pbtable))
