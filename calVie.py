
from multiprocessing import parent_process
import time
import sys
from urllib.parse import parse_qs
from qNcon import *
def cal():
  a = input("Chọn hình muốn tính diện tích\n1. Hình chữ nhật\n2. Hình vuông\n3. Hình tam giác\n4. Hình thoi\n5. Hình thang\n(nhập số):\n")

  if a.isnumeric() and int(a) <= 5 :
    a = int(a)
    print("ok")
    if a == 1:
      print("(Lưu ý chỉ nhập số)")
      b = float(input("Nhập chiều dài: "))
      c = float(input("Nhập chiều rộng: "))
      d = float(b * c)
      if c >= b:
        print("Tao tri r nha")
         
        quitOrCon()
      else:
        print("Kết quả = " + str(d))
        quitOrCon()
    if a == 2:
      print("(Lưu ý chỉ nhập số)")
      e = float(input("Nhập cạnh: "))
      f = float(e * e)
      print("Hệ thống: Kết quả = "+ str(f))
      quitOrCon()
    if a == 3:
      print("(Lưu ý chỉ nhập số)")
      g = float(input("Hệ thống: Nhập chiều cao: "))
      h = float(input("Hệ thống: Nhập độ dài đáy (maybe đày): "))
      i = float((g * h) / 2)
      print("Kết quả = " + str(i))
      quitOrCon()
    if a == 4:
      print("(Lưu ý chỉ nhập số)")
      j = float(input("Hệ thống: Nhập độ dài đường chéo thứ nhất: "))
      k = float(input("Hệ thống: Nhập độ dài đường chéo thứ hai: "))
      l = float((j * k) / 2)
      print("Kết quả = " + str(l))
      quitOrCon()
    if a == 5:
      m = float(input("Hệ thống: Nhập độ dài đáy thứ nhất: "))
      n = float(input("Hệ thống: Nhập độ dài đáy thứ hai: "))
      p = float(input("Hệ thống: Nhập chiều cao: "))
      q = (m + n / 2) * p
      print("Kết quả " + str(q))
    else:
      sys.exit()


      