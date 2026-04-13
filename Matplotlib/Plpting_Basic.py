# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 13:43:43 2026

@author: GoranAndrejevic
"""

import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(-np.pi, np.pi, 15)
C = np.cos(X)
S = np.sin(X)

# Create axes using coordinates
ax = plt.axes([0.1, 0.1, 0.8, 0.8])

# Plot cosine and sine
ax1 = ax.plot(X, C, 'bs:')   # Blue squares with dotted line
ax2 = ax.plot(X, S, 'ro-')   # Red circles with solid line

ax.legend(labels=('Cosine Function', 'Sine Function'), loc='upper left')
ax.set_title("Trigonometric Functions")
plt.show()

ax = plt.axes([0, 0, 1, 1])
# Plot cosine and sine
ax1 = ax.plot(X, C, 'bs:')   # Blue squares with dotted line
ax2 = ax.plot(X, S, 'ro-')   # Red circles with solid line

ax.legend(labels=('Cosine Function', 'Sine Function'), loc='upper left')
ax.set_title("Trigonometric Functions")
plt.show()
