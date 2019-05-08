import math
import sys
from os import rename

import requests

print(sys.version)
print(sys.executable)


def greeting(who):
    greeting = 'Hello, {}'.format(who)
    return greeting


r = requests.get('https://google.com')
print(r.status_code)
