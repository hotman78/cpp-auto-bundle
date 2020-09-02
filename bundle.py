#!/usr/bin/env python3
import sys
import re
import os.path
path=sys.argv[1]
included=set()
ret=""
def oepn_file(path):
    included.add(path)
    global ret
    with open(path) as f:
        l=f.readlines()
        for e in l:
            m=re.search(r'#include.*"..*"',e)
            if m==None:
                ret+=e
            else:
                tmp=os.path.abspath(os.path.join(os.path.dirname(path),re.sub(r'"','',re.sub(r'#include.*?"','',m.group()))))
                if tmp not in included:
                    oepn_file(tmp)
                    ret+='\n\n'
oepn_file(path)
print(ret)