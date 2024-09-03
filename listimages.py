import os
import json

f = []
layer = 1
w = os.walk(".")
exclude = {'back.png', 'fwd.png', 'Static3.png'}
for (dirpath, dirnames, filenames) in w:
    webdir = dirpath.replace("\\", "/")
    for fname in filenames:
        if fname in exclude:
            continue
        lfname = fname.lower()
        if lfname.endswith('.jpg') or lfname.endswith('jpeg') or lfname.endswith('png') or lfname.endswith('.gif'):
            f.append('/'.join([webdir, fname]))

print (json.dumps(f), ";")