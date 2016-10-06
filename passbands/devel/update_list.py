import json
from phoebe.atmospheres import passbands

passbands.init_passbands()

f = open('list_online_passbands', 'w')
f.write(json.dumps(passbands._pbtable.keys()))
f.close()
