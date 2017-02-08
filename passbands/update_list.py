import json
import os
from glob import glob
import marshal

def load_passband(fname):
    f = open(fname, 'rb')
    struct = marshal.load(f)
    f.close()

    info = {}
    info['fname'] = os.path.basename(fname)
    info['atms'] = struct['atmlist']

    return struct['pbset']+':'+struct['pbname'], info

pbtable = {}

for fname in glob('./*pb'):
   print "loading {}...".format(fname)
   key, info = load_passband(fname)
   pbtable[key] = info

# keep this for legacy sake, for now (development version before Feb 8 will require this)
f = open('list_online_passbands', 'w')
f.write(json.dumps({k: v['fname'] for k,v in pbtable.items()}))
f.close()

f = open('list_online_passbands_full', 'w')
f.write(json.dumps(pbtable))
f.close()