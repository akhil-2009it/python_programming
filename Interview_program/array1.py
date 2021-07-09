from array import *


vals = array('i', [1,3,4,6,3,7,2,8])


newvals = array(vals.typecode, (a for a in vals))

for e in newvals:
    print(e)