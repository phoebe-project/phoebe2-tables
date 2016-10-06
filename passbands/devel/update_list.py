import json
import os
from glob import glob
from phoebe.atmospheres import passbands


for fname in glob('./*pb'):
   print fname
   passbands.init_passband(fname)

f = open('list_online_passbands', 'w')
f.write(json.dumps({k: os.path.basename(v['fname']) for k,v in passbands._pbtable.items()}))
f.close()
