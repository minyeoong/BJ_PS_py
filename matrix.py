import numpy as np
import math
m = np.array([[-1-3**(1/2), -1+3**(1/2)],
            [ 1, 1]])
m_inv = np.linalg.inv(m)
print(m)
print(m_inv)

