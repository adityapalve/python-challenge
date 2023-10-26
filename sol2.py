# print(len(text))
import re 
import string

with open('text.txt', 'r') as file:
  text = file.read()

def sol_2(text):
# Some playing around with the string.
  # d = {}
  # for e in text:
  #   d[e] = d.get(e,0)+1
  # print(d)
  pattern = f"[{string.ascii_lowercase}]"
  matches = re.findall(pattern,text)
  print(matches)
  
sol_2(text)
