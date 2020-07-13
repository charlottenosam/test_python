import numpy as np
import matplotlib.pyplot as plt
import sys
print('Python version:',sys.version)

x = np.linspace(0,1)

plt.plot(x,x)

figname = 'plots/test.png'
plt.savefig(figname)

print('Saved figure to %s' % figname)