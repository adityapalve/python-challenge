import re
import pprint
def sol():
  with open ('text2.txt', 'r') as file:
    text  = file.read()
  

  pattern = re.findall('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', text)
  
  # Using list comprehension
  s = ''.join([i[len(i)//2] for i in pattern])
  # with Lambda
  s_2= "".join(list(map(lambda i: i[len(i)//2],pattern)))
  print(s, s_2)
sol()