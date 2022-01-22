

from qutip.bloch import Bloch
"""
Import the Bloch Sphere from the Bloch Module of the QuTiP.
"""

from matplotlib import pyplot as plt


from mpl_toolkits.mplot3d import Axes3D

figure, axes = plt.subplots(figsize=(5, 5), subplot_kw=dict(projection='3d'))

#axes.axis("square")

bloch_sphere_3d = Bloch(fig=figure, axes=axes)

bloch_sphere_3d.xlabel[0] = "$\\left|+\\right>$"
bloch_sphere_3d.xlabel[1] = "$\\left|-\\right>$"

bloch_sphere_3d.ylabel[0] = "$\\left|+i\\right>$"
bloch_sphere_3d.ylabel[1] = "$\\left|-i\\right>$"

bloch_sphere_3d.zlabel[0] = "$\\left|0\\right>$"
bloch_sphere_3d.zlabel[1] = "$\\left|1\\right>$"

bloch_sphere_3d.render(fig=figure, axes=axes) # render to the correct subplot

# set title for the axis
axes.set_title('TITLE goes here', y=1.1, fontsize=20)

# You can anything else you want to the axis as well!
#ax.annotate('TEXT', xy=(0.1, 0.9), xytext=(0.1, 0.7), xycoords='axes fraction',
#            fontsize=15, color='r', ha='center',)

plt.show()


"""
bloch_sphere_3d = Bloch()

bloch_sphere_3d.clear()

bloch_sphere_3d.view[0] = -50
bloch_sphere_3d.view[1] = 30

bloch_sphere_3d.make_sphere()


bloch_sphere_3d.xlabel[0] = "$\\left|+\\right>$"
bloch_sphere_3d.xlabel[1] = "$\\left|-\\right>$"

bloch_sphere_3d.ylabel[0] = "$\\left|+i\\right>$"
bloch_sphere_3d.ylabel[1] = "$\\left|-i\\right>$"

bloch_sphere_3d.zlabel[0] = "$\\left|0\\right>$"
bloch_sphere_3d.zlabel[1] = "$\\left|1\\right>$"

bloch_sphere_3d.plot_axes_labels()
bloch_sphere_3d.plot_axes()

bloch_sphere_3d.show()

bloch_sphere_3d.fig.savefig("aaaa.png", format="png", transparent=True)
"""
