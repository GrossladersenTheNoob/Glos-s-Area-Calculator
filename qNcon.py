import sys
import time

from cal import *
def quitOrCon():
  sussy = input("Hệ thống: Bạn còn muốn sử dụng?\n1. Có\n2. Không\n(1/2)")
  if sussy.isnumeric():
    sussy = int(sussy)
    if sussy == 2:
      print("Ok")
       
      sys.exit()
    if sussy >= 3:
      print("T tri r nha")
       
      sys.exit()
    else:
      cal()
  elif not(sussy.isnumeric()):
    print("T tri r do")
     
    sys.exit()