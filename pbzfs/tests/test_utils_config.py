#!/usr/bin/env python3

import sys
try:
    from ..utils import config
    print("import a")
except:
    sys.path.append("../")
    from utils import config
    print("import b")

if __name__ == "__main__":
    print(config.pbz_read_conf("../../conf/demo.pbz"))
    pass
