#!/usr/bin/env python3
import os
import re

#the_month = range(1,13)
#the_days = range(1,32)
#print(os.getcwd())
os.chdir("../../")
#print(os.getcwd())
the_conf_data = []
with open('conf/demo.pbz') as f:
    for l in f:
        if(l[0] != '#'):
            the_conf_data.append(l.strip())
f.close()

def conf_parse_freq(freq_origin_str):
    freq_temp = {"freq_unit":"day","freq_value":cf_data}
    if(freq_origin_str[0] == r"+"):
        freq_temp_value = ""
        for cf_date_str in freq_origin_str[1:]:
            if(not cf_date_str.isdigit()):
                freq_temp_unit = cf_date_str.lower()
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
                freq_temp_value += cf_date_str
        freq_temp["freq_unit"],freq_temp["freq_value"] = freq_temp["freq_unit"] == "Y" and ("M",int(freq_temp_value)*12) or (freq_temp["freq_unit"],int(freq_temp_value))
        #print(freq_temp)
    elif (freq_origin_str[3].find(r"|")):
        pass
    else:
        print("Fixme!!")
    return freq_temp
    #pdz_config = {"jobname":res[0],"source":res[1],"target":res[2],"freq":res[3]}
    #print(pdz_config)

pattern = re.compile(r"\s*")
pdz_config = []
for cf_data in the_conf_data:
    res = pattern.split(cf_data)
    job_config = {"jobname":res[0],"source":res[1],"targe":res[2],"freq":conf_parse_freq(res[3])}
    pdz_config.append(job_config)
print(pdz_config)


