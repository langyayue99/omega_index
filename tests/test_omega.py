import unittest

from context import omega_index
comms1 = {1: [5, 6, 7], 2: [3, 4, 5], 3: [6, 7, 8]}
comms2 = {1: [5, 6, 7], 2: [3, 4, 6], 3: [6, 7, 8]}
comms3 = {1: [5, 6, 7], 2: [6, 7, 8], 3: [3, 4, 5]}
comms4 = {0: ['1-t0', '2-t0', '3-t0', '4-t0', '1-t1', '2-t1',  '3-t1','4-t1', '1-t2','2-t2','3-t2','4-t2'],
          1: ['11-t1', '12-t1', '13-t1'],
          2: ['5-t2', '6-t2', '7-t2', '5-t0', '6-t0', '7-t0']}
comms5 = {1: ['11-t1', '12-t1', '13-t1'],
          2: ['1-t0', '2-t0', '3-t0', '4-t0', '1-t1', '2-t1',  '3-t1','4-t1', '1-t2','2-t2','3-t2','4-t2'],
          3: ['5-t2', '6-t2', '7-t2', '5-t0', '6-t0', '7-t0']}
omega = omega_index.Omega(comms4, comms5)
print omega.omega_score