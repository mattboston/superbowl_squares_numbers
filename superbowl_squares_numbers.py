#!/usr/bin/env python

# Copyright 2018 Matt Shields <matt@shields.tv>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random

teams = [ 'Philadelphia Eagles', 'New England Patriots' ]
all_numbers = range(10)

print("All numbers that will be used: %s" % all_numbers)
print("")

for team in teams:
  random_numbers = str(sorted(all_numbers, key=lambda k: random.random()))
  print("The numbers for the %s are: %s" % (team,random_numbers))
  print
