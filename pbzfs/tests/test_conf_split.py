#!/usr/bin/env python3
import os
import re
#os.chdir("../../")
#print(os.getcwd())
def pbz_read_conf_data(file_path):
    the_conf_data = []
    with open(file_path) as f:
        for l in f:
            if(l[0] != '#'):
                the_conf_data.append(l.strip())
    f.close()
    return the_conf_data

def pbz_parse_freq_conf(freq_origin_str):
    freq_temp = {"freq_unit":"day","freq_value":None}
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
    elif (freq_origin_str[3].find(r"|")):
        pass
    else:
        print("Fixme!!")
    return freq_temp

def pbz_config_to_dict(the_conf_data):
    pattern = re.compile(r"\s*")
    pbz_config = []
    for cf_data in the_conf_data:
        res = pattern.split(cf_data)
        job_config = {"jobname":res[0],"source":res[1],"targe":res[2],"freq":pbz_parse_freq_conf(res[3])}
        pbz_config.append(job_config)
    #print(pbz_config)
    return pbz_config

if __name__ == "__main__":
#    os.chdir("../../")
    config_path = "../../conf/demo.pbz"
    pbz_conf_data = pbz_read_conf_data(config_path)
    print(pbz_config_to_dict(pbz_conf_data))
    pass

