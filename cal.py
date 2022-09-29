
from cred import *
from multiprocessing import parent_process
import time
import sys
from urllib.parse import parse_qs
from qNcon import *

def calEng():
  a = input("Select the shape you want to calculate the area:\n1. Rectangle\n2. Square\n3. Triangle\n4. Rhombus\n5. Trapezoid\n(enter number only):\n")

  if a.isnumeric() and int(a) <= 5 :
    a = int(a)
    print("Alr")
    if a == 1:
      print("(enter number only)")
      b = float(input("Enter length: "))
      c = float(input("Enter width: "))
      d = float(b * c)
      if c >= b:
        print("I can't 💀")

        quitOrCon()
      else:
        print("System: Answer = " + str(d))
        quitOrCon()
    if a == 2:
      print("(enter number only)")
      e = float(input("Enter the side of the square: "))
      f = float(e * e)
      print("System: Answer = "+ str(f))
      quitOrCon()
    if a == 3:
      print("(enter number only)")
      g = float(input("System: Enter height: "))
      h = float(input("System: Enter bottom length: "))
      i = float((g * h) / 2)
      print("System: Answer = " + str(i))
      quitOrCon()
    if a == 4:
      print("(enter number only)")
      j = float(input("System: Enter the length of the first diagonal: "))
      k = float(input("System: Enter the length of the second diagonal: "))
      l = float((j * k) / 2)
      print("System: Answer = " + str(l))
      quitOrCon()
    if a == 5:
      m = float(input("System: Enter the length of the first bottom: "))
      n = float(input("System: Enter second bottom length: "))
      p = float(input("System: Enter height: "))
      q = (m + n / 2) * p
      print("System: Answer " + str(q))
    else:
      sys.exit()


      