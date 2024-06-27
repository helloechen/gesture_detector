import numpy as np
import matplotlib.pyplot as plt

G = 6.67430e-11  
c = 299792458    

M = 1.989e30  
Rs = 2 * G * M / c**2 

x = np.linspace(-Rs*10, Rs*10, 1000)
y = np.linspace(-Rs*10, Rs*10, 1000)
X, Y = np.meshgrid(x, y)

Z = np.sqrt((2 * G * M) / np.sqrt(X**2 + Y**2))

plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10, 10))
cf = plt.contourf(X, Y, Z, levels=50, cmap='inferno')
plt.colorbar(cf, label='该点处的逃逸速度 (m/s)')

circle = plt.Circle((0, 0), Rs, color='white', linestyle='--', fill=False, linewidth=2)
plt.gcf().gca().add_artist(circle)

plt.text(0, Rs+0.1*Rs, '黑洞视界\n(Rs)', fontname='SimHei',horizontalalignment='center', fontsize=12, color='white')
plt.text(-Rs*9, Rs*9, f'所模拟的黑洞质量(约为太阳质量): {M:.2e} kg\n史瓦西半径: {Rs:.2e} m',fontname='SimHei' ,fontsize=12, color='white', verticalalignment='top')
plt.text(-Rs*9, -Rs*9, '本模拟由该物理研究小组成员原创，由Python模拟和可视化',fontname='SimHei' , fontsize=12, color='white', horizontalalignment='left', verticalalignment='bottom')

plt.title('黑洞逃逸速度等高线', fontname='SimHei')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')

plt.show()
