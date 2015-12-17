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
#print the_conf_data

pattern = re.compile(r"\s*")
for x in the_conf_data:
    res = pattern.split(x)
    freq_origin_str = res[3]
    print(freq_origin_str)
    freq_temp = {"freq_unit":"day","freq_value":x}
    if(freq_origin_str[0] == r"+"):
        freq_temp_value = ""
        for x in freq_origin_str[1:]:
            if(not x.isdigit()):
                freq_temp_unit = x.lower()
                if(freq_temp_unit == "m"):
                    freq_temp["freq_unit"]="M"
                    break
                elif(freq_temp_unit == "y"):
                    freq_temp["freq_unit"] = "Y"
                    break
                elif(freq_temp_unit == "d"):
                    freq_temp["freq_unit"] = "D"
                    break
                else:
                    print("Fixme!!")
            else:
                freq_temp_value += x
        freq_temp["freq_unit"],freq_temp["freq_value"] = freq_temp["freq_unit"] == "Y" and ("M",int(freq_temp_value)*12) or (freq_temp["freq_unit"],int(freq_temp_value))
        #freq_temp["freq_value"]=(int(freq_temp_value))*12 if freq_temp["freq_unit"] == "M"  else freq_temp["freq_value"]=int(freq_temp_value)
        print(freq_temp)
        print("abc")
    elif (res[3].find(r"|")):
        print("123")
    else:
        print("Fixme!!")
    #pdz_config = {"jobname":res[0],"source":res[1],"target":res[2],"freq":res[3]}
    #print(pdz_config)


