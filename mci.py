import numpy as np 
import matplotlib.pyplot as plt 
np.random.seed(10)
a = 0
b = 1
N = 40
def f(x):
  return x
def mci(f, a, b, N):
  alpha = (b-a)/ N
  x = np.random.uniform(a, b, N)
  return alpha * f(x).sum()
u = np.zeros((N, ))
u[:] = np.array([mci(f, a, b, i) for i in range(1, N+1)])
x = np.arange(1, N+1)
u.mean() 
plt.bar(x, u[:])
plt.axhline(y = 0.5, color = 'b', linestyle = '-', label='Exact value: 0.5')
plt.axhline(y = u.mean(), color = 'r', linestyle = '-', label='Mean value of MCI for different N: {}'.format(round(u.mean(), 3)))
plt.xlabel('Sample size')
plt.ylabel('Numerical result of the integration')
plt.title('Results of integrating x from {} to {} using Monte Carlo Integration Method using different sample sizes N'.format(a, b))
plt.grid()
plt.legend()
plt.show()
