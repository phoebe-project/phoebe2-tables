import json
import os
from glob import glob
from phoebe.atmospheres import passbands


for fname in glob('./*pb'):
   print fname
   passbands.init_passband(fname)

# keep this for legacy sake, for now (development version before Feb 8 will require this)
f = open('list_online_passbands', 'w')
f.write(json.dumps({k: os.path.basename(v['fname']) for k,v in passbands._pbtable.items()}))
f.close()

f = open('list_online_passbands_full', 'w')
f.write(json.dumps({k: {'fname': os.path.basename(v['fname']), 'atms': v['atms']} for k,v in passbands._pbtable.items()}))
f.close()