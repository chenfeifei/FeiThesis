import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

'''
# Target Compostion 
dataArray = [[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.03218, np.nan],
[np.nan, 0.73929, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
[np.nan, np.nan, np.nan, 0.19745, np.nan, np.nan, np.nan, np.nan, np.nan],
[0.00173, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan], 
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.01819, np.nan],
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.01116, np.nan, np.nan]]
'''

# Return Composition 
dataArray = [[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.019308, np.nan],
[np.nan, 0.443574, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan], 
[np.nan, np.nan, np.nan, 0.11847, np.nan, np.nan, np.nan, np.nan, np.nan],  
[0.001038, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan], 
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.010914, np.nan], 
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.006696, np.nan, np.nan], 
[0.4, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]


'''
#chapter6_figure_three.png
dataArray = [[np.nan, np.nan, np.nan, np.nan, np.nan, 0.414239, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan], 
[np.nan, np.nan, 0.20722, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan], 
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.0304427, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan], 
[np.nan, np.nan, 0.0876989, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan], 
[np.nan, np.nan, np.nan, np.nan, 0.0123589, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan], 
[np.nan, np.nan, 0.0185461, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan], 
[0.229495, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]
'''
'''
#chapter6_figure_four.png
dataArray = [[np.nan, np.nan, np.nan, np.nan, np.nan, 0.27162, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.142619, np.nan, np.nan, np.nan, np.nan, np.nan], [np.nan, np.nan, 0.135875, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.0713442, np.nan, np.nan], 
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.0104812, np.nan, np.nan, 0.0199615, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan], 
[np.nan, np.nan, 0.0301941, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.0575048, np.nan, np.nan], 
[np.nan, np.nan, np.nan, np.nan, 0.00810383, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.00425508, np.nan, np.nan, np.nan, np.nan], 
[np.nan, np.nan, 0.0121608, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.00638527, np.nan, np.nan], 
[0.229495, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,np.nan, np.nan, np.nan, np.nan, np.nan]]
'''
'''
#chapter6_figure_five.png
dataArray = [[np.nan, np.nan, np.nan, np.nan, np.nan, 0.53762, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
[np.nan, np.nan, 0.26894, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.03951, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan], 
[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 0.11382, np.nan, np.nan], 
[np.nan, np.nan, np.nan, np.nan, 0.01604, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
[np.nan, np.nan, 0.02407, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]
'''

plt.xticks(range(1,18))
ax = sns.heatmap(dataArray,annot=True,square=True, cmap="Reds", vmin=0, vmax=1, linewidths=.5, fmt=".2g",cbar=False, annot_kws={"size": 8})
#ax.set_xticklabels([0, 10, 20, 30, 40, 50, 60, 70, 80, 100, 110, 120, 130, 140, 150, 160, 170, 180])
ax.set_xticklabels([0, 10, 20, 30, 40, 50, 60, 70, 80])
ax.set_yticklabels([' ', 'Val', 'Thr', 'Ala', 'Ile', 'Leu', 'Met'], rotation=0)
ax.set_xlabel(r'tilt' " Angle")
ax.set_ylabel("Amino Acids")

#ax.set_title("Target Composition for One Run of Mixed Amino Acids with " r'$\theta$' " Expanded from " r'$0^{\circ}$' " to " r'$180^{\circ}$')
#ax.set_title("Return Composition of E1 for One Run of Mixed Amino Acids with " r'$\theta$' " Expanded from " r'$0^{\circ}$' " to " r'$180^{\circ}$')
#ax.set_title("Return composition of Experiment 2 in one random run with experiments containing scaling factor and the mixed amino acids' candidates with " r'$\theta$' " expanded from " r'$0^{\circ}$' " to " r'$180^{\circ}$')

plt.savefig('chapter6_figure_two.png', dpi=100)


