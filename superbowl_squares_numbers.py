#!/usr/bin/env python

import random

teams = [ 'Philadelphia Eagles', 'New England Patriots' ]
all_numbers = range(10)

print("All numbers that will be used: %s" % all_numbers)
print("")

for team in teams:
  random_numbers = str(sorted(all_numbers, key=lambda k: random.random()))
  print("The numbers for the %s are: %s" % (team,random_numbers))
  print
