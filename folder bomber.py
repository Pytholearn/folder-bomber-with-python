

#discord: https://discord.gg/xbN3XSHYjx
#youtube: https://www.youtube.com/@IIIHaZaRd
#pytholearn

#gen folder

from rand_string.rand_string import RandString
import os

while True:
  try:
    for i in range(10):
      os.mkdir(RandString("uppercase",16))
  except FileExistsError:
    pass



#del folder
# import os,shutil

# def delf(path):
#     for foln in os.listdir(path):
#         folpath = os.path.join(path,foln)
#         if os.path.isdir(folpath):
#             shutil.rmtree(folpath)
      
# dir_path = "H:\\python project\\folder bomber"

# delf(dir_path)

#discord: https://discord.gg/xbN3XSHYjx
#youtube: https://www.youtube.com/@IIIHaZaRd
#pytholearn