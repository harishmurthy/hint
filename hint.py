#! bin/python

import random

_table = ["%c" % x for x in range(ord('A'),ord('Z')+1)]
_table = _table + ["%c" % x for x in range(ord('a'),ord('z')+1)]
_table = _table + ["%c" % x for x in range(ord('0'),ord('9')+1)]

_pows = [len(_table)**x for x in range(1,10)]

_numdigits = 1

_counter = 0

_mem = {}

_collision = 0

def gethint():
  global _table
  global _pows
  global _numdigits
  global _counter
  global _mem
  global _collision
  h = ''
  for x in range(_numdigits):
    h = h + random.choice(_table)
  while h in _mem:
    h = ''
    print('collision ' + str(_collision))
    _collision = _collision + 1
    for x in range(_numdigits):
      h = h + random.choice(_table)
  _counter = _counter + 1
  if _counter in _pows:
    _numdigits = _numdigits + 1
  _mem[h] = _counter
  return h

if __name__ == "__main__":
  for x in range(1000):
    print(gethint())
