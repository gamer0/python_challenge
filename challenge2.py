#! /usr/python3.6


import string
import sys



def find_rare_characters(file):
  with open(file, 'r') as f:
    f_gen = ( line for line in f.readlines())
  result = [ char for line in f_gen for char in line if char in string.ascii_letters ]
  return result

if __name__ == '__main__':
  rare_char_list = find_rare_characters(sys.argv[1])
  print("".join(rare_char_list))
