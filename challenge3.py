#! /usr/python3

import sys
import string
import re

def find_pattern(file):
  with open(file,'r') as f:
    f_gen = (line for line in f.readlines())
  my_pattern = re.compile(r'[a-z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][a-z]')
  match_list = [ my_pattern.search(line) for line in f_gen]
  match_list = [ match.group(1) for match in match_list if match ]
  return "".join(match_list)



if __name__ == '__main__':
  list_of_matches = find_pattern(sys.argv[1])
  print(list_of_matches)


