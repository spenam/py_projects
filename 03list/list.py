import numpy as np

a=np.random.rand(10)*40
a=np.asarray([round(x) for x in a])
print(a)
print("####")
print(a[a<20])
