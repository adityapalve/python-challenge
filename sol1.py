def sol_problem_1(s):
  res = []
  for char in s:
    if char.isalpha():
      offset = 65 if char.isupper() else 97
      res.append(chr(((ord(char)-offset+2)% 26)+offset))
    else:
      res.append(char)
  
  return ''.join(res)

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
d = {
  "k":"m",
  "o":"q",
  "e":"g"
  }
# a = s.translate(str.maketrans(d))
# print(a)
# print(sol_problem_1(s))
# url = "http://www.pythonchallenge.com/pc/def/map.html"
# print(sol_problem_1(url))