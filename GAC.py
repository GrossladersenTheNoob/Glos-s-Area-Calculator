
import time
import sys
import datetime
from calVie import *
from cred import *
from cal import *
from spl import spl
from qNcon import *
creNdate()
spl()
def secLan():
    a = float(input("Select language:\n"
                    "1. English\n"
                    "2. Vietnamese\n"
                    "Enter only number\n"
                    "Chọn ngôn ngữ: \n"
                    "1. Tiếng Anh \n"
                    "2. Tiếng Việt\n"
                    "Nhập số\n"
                    ""))

    if a == 1:
        calEng()
    elif a == 2:
        cal()
    else:
        print("Oatws"
            "a")
        time.sleep(1)
        sys.exit()
secLan()
quitOrCon()

