import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.colors import ListedColormap


# Target Composition
dataArray = [[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.299586, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
[np.nan, np.nan, np.nan, 0.664053, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.021196, np.nan],
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.00662804, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.000642609, np.nan, np.nan, np.nan, np.nan, np.nan],
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.00789, np.nan, np.nan, np.nan, np.nan, np.nan]]

'''
# Return Composition of E2
dataArray = [[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.299586, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
[np.nan, np.nan, np.nan, 0.664053, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
[np.nan, 0.021196, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.00662804, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
[np.nan, np.nan, np.nan, np.nan, np.nan, 0.000642609, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
[np.nan, np.nan, np.nan, np.nan, np.nan, 0.00789, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]
'''
'''
# Return Compostion of E6
dataArray = [[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.299586, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
[np.nan, np.nan, np.nan, 0.664053, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.021196, np.nan],
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.00662804, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.000642609, np.nan, np.nan, np.nan, np.nan, np.nan],
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.00789, np.nan, np.nan, np.nan, np.nan, np.nan]]
'''
plt.xticks(range(1,18))
ax = sns.heatmap(dataArray,annot=True,square=True, cmap="Reds", vmin=0.000001, vmax=1, linewidths=.5, fmt=".2g",cbar=False, annot_kws={"size": 8})
ax.set_xticklabels([0, 10, 20, 30, 40, 50, 60, 70, 80, 100, 110, 120, 130, 140, 150, 160, 170, 180])
ax.set_yticklabels(['Val', 'Thr', 'Ala', 'Ile', 'Leu', 'Met'], rotation=0)
ax.set_xlabel(r'$\theta$' " Vaule")
ax.set_ylabel("Amino Acids")
#ax.set_title("Target Composition for One Run of Mixed Amino Acids with " r'$\theta$' " Expanded from " r'$0^{\circ}$' " to " r'$180^{\circ}$')
#ax.set_title("Return Composition of E1 for One Run of Mixed Amino Acids with " r'$\theta$' " Expanded from " r'$0^{\circ}$' " to " r'$180^{\circ}$')
#ax.set_title("Return Composition of E6 for One Run of Mixed Amino Acids with " r'$\theta$' " Expanded from " r'$0^{\circ}$' " to " r'$180^{\circ}$')
#ax.set_xticklabels([r'$0^{\circ}$', r'$10^{\circ}$', r'$20^{\circ}$', r'$30^{\circ}$', r'$40^{\circ}$', r'$50^{\circ}$', r'$60^{\circ}$', r'$70^{\circ}$', r'$80^{\circ}$', r'$100^{\circ}$', r'$110^{\circ}$', r'$120^{\circ}$', r'$130^{\circ}$', r'$140^{\circ}$', r'$150^{\circ}$', r'$160^{\circ}$', r'$170^{\circ}$', r'$180^{\circ}$'])
plt.show()


