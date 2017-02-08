import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.colors import ListedColormap


# Target Composition
dataArray = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.299586, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0.664053, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.021196, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0.00662804, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.000642609, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.00789, 0, 0, 0, 0, 0]]
'''
# Return Composition of E1
dataArray = [[0, 0, 0, 0, 0, 0, 0.299586, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0.664053, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0.021196, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0.00662804, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0.000642609, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0.00789, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Return Compostion of E6
dataArray = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.299586, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0.664053, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.021196, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0.00662804, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.000642609, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.00789, 0, 0, 0, 0, 0]]
'''
plt.xticks(range(1,18))
ax = sns.heatmap(dataArray,annot=True,square=True, cmap="Reds", vmin=0.000001, vmax=1, linewidths=.5, fmt="g",cbar=False)
ax.set_xticklabels([r'$0^{\circ}$', r'$10^{\circ}$', r'$20^{\circ}$', r'$30^{\circ}$', r'$40^{\circ}$', r'$50^{\circ}$', r'$60^{\circ}$', r'$70^{\circ}$', r'$80^{\circ}$', r'$100^{\circ}$', r'$110^{\circ}$', r'$120^{\circ}$', r'$130^{\circ}$', r'$140^{\circ}$', r'$150^{\circ}$', r'$160^{\circ}$', r'$170^{\circ}$', r'$180^{\circ}$'])
ax.set_yticklabels(['Valine', 'Threonine', 'Alanine', 'Isoleucine', 'Leucine', 'Methionine'])
ax.set_xlabel(r'$\theta$' " Vaule")
ax.set_ylabel("Amino Acids")
ax.set_title("Target Composition for One Run of Mixed Amino Acids with " r'$\theta$' " Expanded from " r'$0^{\circ}$' " to " r'$180^{\circ}$')
#ax.set_title("Return Composition of E1 for One Run of Mixed Amino Acids with " r'$\theta$' " Expanded from " r'$0^{\circ}$' " to " r'$180^{\circ}$')
#ax.set_title("Return Composition of E6 for One Run of Mixed Amino Acids with " r'$\theta$' " Expanded from " r'$0^{\circ}$' " to " r'$180^{\circ}$')

plt.show()


