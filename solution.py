import string
import os
import random
import pprint
import json

with open ('auto.json') as opened_file:
    content = opened_file.read()
    data = json.loads(content)

initial_state = auto.json['initial']
inputs = auto.json['inputs']
rules = auto.json['rules']

next_state = initial_state
for n in range(len(inputs)):
    prev_state = next_state
    next_state = rules[next_state][inputs[n]]
    print(inputs[n], prev_state, next_state)
