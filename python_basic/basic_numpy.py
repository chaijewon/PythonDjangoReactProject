# numpy
import numpy as np
#a=np.array([3,4,5])
#print(a.shape,a.ndim,a.dtype,a.itemsize,a.size)
#print(a)
a=[[1,2,3],[4,5,6]]
print(a)
b=np.array(a)
print(b.ndim) #배열의 열수
print(b.shape) #배열의 차원 => 2행 3열
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
print(x)
x = np.random.uniform(size=100)
x.reshape(20,5)
print(x)
s = np.random.normal(0, 1, 1000)

import matplotlib.pyplot as plt
plt.hist(s)
plt.show()

