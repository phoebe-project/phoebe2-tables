import json
import os
import sys
from glob import glob
from astropy.io import fits

def load_passband(fname):
    with fits.open(fname) as f:
        header = f['primary'].header

        info = {}
        info['fname'] = os.path.basename(fname)
        info['atms'] = eval(header['atmlist'], {'__builtins__':None}, {})
        info['timestamp'] = header['timestmp']

        pbname = header['pbset']+':'+header['pbname']

    return pbname, info

pbtable = {}

for fname in glob('./*.fits*'):
   print("loading {}...".format(fname))
   key, info = load_passband(fname)
   pbtable[key] = info

fname = 'list_online_passbands_full_fits'

print("writing to {}".format(fname))
with open(fname, 'w') as f:
    f.write(json.dumps(pbtable))
