#!/usr/bin/python
import itertools
#from sys import argv

user_list = raw_input("Enter the aflksdjfalsdf: ")
user_list = (s.strip() for s in user_list.split(','))

with open('datafile') as infile, open('output', 'w') as outfile:
    for r in itertools.product((l.rstrip() for l in infile), user_list):
        mixed = ''.join(r)
        print(mixed)
        outfile.write(mixed + '\n')
