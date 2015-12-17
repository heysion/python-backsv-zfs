#!/usr/bin/env python3
import os
import re

the_month = range(1,13)
the_days = range(1,32)
print(os.getcwd())
os.chdir("../../")
print(os.getcwd())
the_conf_data = []
with open('conf/demo.pbz') as f:
    for l in f:
        the_conf_data.append(l.strip())
f.close()
#print the_conf_data
pindex = 0
for x in the_conf_data:
    if x[0] == '#':
        del the_conf_data[pindex]
    pindex = pindex + 1;
print the_conf_data

pattern = re.compile(r"\s*")
for x in the_conf_data:
    res = pattern.split(x)
    pdz_config = {"jobname":res[0],"source":res[1],"target":res[2],"frequency":res[3]}
    print(pdz_config)


