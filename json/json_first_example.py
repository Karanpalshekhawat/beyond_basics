"""
Javascript Object notation
common dataformat for storing information
"""

import json

with open('states.json', 'r') as f:
    states_info = json.load(f)

print(type(states_info))

for state in states_info['states']:
    print(state['name'], state['abbreviation'])

for state in states_info['states']:
    del state['area_codes']

with open('new_states.json', 'w') as f:
    json.dump(states_info, f, indent=2, sort_keys=True)
