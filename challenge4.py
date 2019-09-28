#! /usr/python3

import sys
import re
import requests



def read_webpage(url):
  code = '44827'
  count = 0
  while code:
    my_req = requests.get(url + code)
    url_content = str(my_req.content)
    url_itself = my_req.url
    code = ''.join(re.findall(r'\d+',url_content))
    with open('numbers.txt','a') as f:
      code_list = f.write(code + '\n')
      count += 1
    if bool(code) == False:
      print(url_content)
      code = input('what are the new digits: ')
      if code == False: break
  return (url_content, code, count)



if __name__ == '__main__':
  print(read_webpage(sys.argv[1]))
