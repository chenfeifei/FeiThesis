import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

'''
# Target Composition
dataArray = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.299586, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0.664053, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.021196, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0.00662804, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.000642609, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.00789, 0, 0, 0, 0, 0]]

# Return Composition of E1
dataArray = [[0, 0, 0, 0, 0, 0, 0.299586, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0.664053, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0.021196, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0.00662804, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0.000642609, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0.00789, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
'''
# Return Compostion of E6
dataArray = [[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.019308, np.nan],
[np.nan, 0.443574, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
[np.nan, np.nan, np.nan, 0.11847, np.nan, np.nan, np.nan, np.nan, np.nan],
[0.001038, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan], 
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.010914, np.nan],
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.006696, np.nan, np.nan],
[0.4, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]

plt.xticks(range(1,9))
ax = sns.heatmap(dataArray,annot=True,square=True, cmap="Reds", vmin=0, vmax=1, linewidths=.5, fmt="g")
#ax.set_xticklabels([0, 10, 20, 30, 40, 50, 60, 70, 80, 100, 110, 120, 130, 140, 150, 160, 170, 180])
ax.set_xticklabels([0, 10, 20, 30, 40, 50, 60, 70, 80])
ax.set_yticklabels(['Valine', 'Threonine', 'Alanine', 'Isoleucine', 'Leucine', 'Methionine'])
ax.set_xlabel(r'$\theta$' " Vaule")
ax.set_ylabel("Amino Acids")
#ax.set_title("Target Composition for One Run of Mixed Amino Acids with " r'$\theta$' " Expanded from " r'$0^{\circ}$' " to " r'$180^{\circ}$')
#ax.set_title("Return Composition of E1 for One Run of Mixed Amino Acids with " r'$\theta$' " Expanded from " r'$0^{\circ}$' " to " r'$180^{\circ}$')
ax.set_title("Result composition of Experiment 2 in one random run with experiments containing scaling factor of mixed amino acids with " r'$\theta$' " Expanded from " r'$0^{\circ}$' " to " r'$80^{\circ}$')

plt.show()


