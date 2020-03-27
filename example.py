import numpy as np

from BargerPropagator import BargerPropagator

LengthParam = 0
ToType = 2
FromType = 2
DipAngle_degrees = 5.8
LengthParam = np.cos(np.radians(90.0 + DipAngle_degrees))

bp = BargerPropagator()
bp.DefinePath(LengthParam, 0)

Espace = np.linspace(0, 10, 1000)
Pspace = []
for E in Espace:
    bp.SetMNS(0.846, 0.093, 0.92,
              7.53e-5, 2.44e-3, 0.0,
              E, True, FromType)
    bp.propagate(ToType)
    prob = bp.GetProb(FromType, ToType)
    Pspace.append(prob)

import matplotlib.pyplot as plt
plt.plot(Espace, Pspace)
# plt.semilogx()
plt.ylim(0, 1)
plt.show()
