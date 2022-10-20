from collections import defaultdict
import pprint
dicts={'a':{'b':{}},'d':{'e':{}},'f':{'g':{}}}
new_dict={}
flipped = defaultdict(dict)
for k,v in dicts.items():
    for subkey,subvalue in v.items():
        flipped[subkey][k]=subvalue
pprint.pprint(dict(flipped))

