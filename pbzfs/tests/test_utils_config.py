#!/usr/bin/env python3

import sys
try:
    from ..utils import config
except:
    sys.path.append("../")
    from utils import config

if __name__ == "__main__":
    test_config = config.pbz_read_conf("../../conf/demo.pbz")
    print(test_config)
    for x in test_config:
        print("rsync -rav -e ssh %s %s"%(x["source"],x["targe"]))
    pass
