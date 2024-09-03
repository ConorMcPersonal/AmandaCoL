import os
import json

def new_filename(fname):
    changed = False
    replacements = {
        ' ': '_'
        , '(': ''
        , ")": '' 
    }
    for rep, repwith in replacements.items():
        if rep in fname:
            fname = fname.replace(rep, repwith)
            changed = True
    return (changed, fname)


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
            ch, newfname = new_filename(fname)
            if ch:
                os.rename('/'.join([webdir, fname]), '/'.join([webdir, newfname]))
            f.append('/'.join([webdir, newfname]))

print (json.dumps(f), ";")