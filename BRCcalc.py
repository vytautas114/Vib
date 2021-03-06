#!/home/vytautas/anaconda3/bin/python
import matplotlib as mpl
import argparse
import matplotlib.pyplot as plt
from spektrasBRCfran import spektras
# import sys
# import numpy as np
# import matplotlib
# import scipy
# import scipy.integrate
# from scipy.interpolate import griddata
# import datetime
# import subprocess
#mpl.use('Agg')


cdict3 = {'red': ((0.0, 0.0, 0.0),
                  (0.25, 0.0, 0.0),
                  (0.5, 0.8, 1.0),
                  (0.75, 1.0, 1.0),
                  (1.0, 0.4, 1.0)),

          'green': ((0.0, 0.0, 0.0),
                    (0.25, 0.0, 0.0),
                    (0.5, 0.9, 0.9),
                    (0.75, 0.0, 0.0),
                    (1.0, 0.0, 0.0)),

          'blue': ((0.0, 0.0, 0.4),
                   (0.25, 1.0, 1.0),
                   (0.5, 1.0, 0.8),
                   (0.75, 0.0, 0.0),
                   (1.0, 0.0, 0.0))
          }

#plt.register_cmap(name='BlueRed3', data=cdict3)

# s,om,j,T,virpnum2=[float(i) for i in (sys.argv[1:])]
parser = argparse.ArgumentParser()
parser.add_argument("S", type=float, help="Huang Rhys factor")
parser.add_argument("Om", type=float, help="Frequency of mode, cm^-1")
parser.add_argument("T", type=float, help="Temperature in kelvin")
parser.add_argument("Nq", type=int, help="Number of allowed vibrational quanta in system")
parser.add_argument("-a", "--outp", type=str, default="")
args = parser.parse_args()
# answer = args.x**args.y

s = args.S
om = args.Om
T = args.T
virpnum2 = args.Nq
app_name = args.outp


# s=float(sys.argv[1])
# om=float(sys.argv[2])
# T=float(sys.argv[3])
# virpnum2=int(sys.argv[4])
fig, ax = plt.subplots(figsize=(8, 6))
vardas = 'abs_vib_' + str(s) + '_' + str(om) + '_' + str(T) + 'K_' + str(virpnum2) + '_' + app_name
print(vardas)
spektras(ax, s, om, T, Kvsk=virpnum2, nam="BRC_scan/" + vardas)
ax.set_xlim([10000, 15000])


fig.savefig('BRC_scan/' + vardas + '.png', dpi=300)
# cmd = ['cp outr.txt spekt/'+vardas+'_redfieldrez.txt']
# subprocess.Popen(cmd, shell=True).wait()
# cmd = ['cp outasr.txt spekt/'+vardas+'_redfieldout.txt']
# subprocess.Popen(cmd, shell=True).wait()

# print(datetime.datetime.now())
# cmd = ['../uqcfp/bin/tba.calculator_3rd_levels input_level2d outl2d.txt > outasl2d.txt']
# subprocess.Popen(cmd,shell=True).wait()

# print(datetime.datetime.now())

# file2=open("outl2d.txt")

# l1 = []
# l2=[]
# n=0
# for line in file2:
#     if n<1:
#         n+=1
#         continue
#     else:
#         l1.append(line.split())
# file2.close()
# l1=np.array(l1).astype(np.float)
# l1=l1.transpose()
# l1[1]=l1[1]*-1
# x=np.arange(11000,14000,30)
# y=np.arange(11000,14000,30)
# X,Y=np.meshgrid(x,y)
# zi = griddata((l1[1], l1[0]),l1[3]*-1,(X, Y),method='linear')

# vardas='2d_'+str(s)+'_'+str(om)+'_'+str(j)+'_'+str(T)+'K_'+str(virpnum2)
# cmd = ['cp input_level2d spekt/'+vardas+'_input.txt']
# subprocess.Popen(cmd,shell=True).wait()
# cmd = ['cp outl2d.txt spekt/'+vardas+'_rezult.txt']
# subprocess.Popen(cmd,shell=True).wait()
# cmd = ['cp outasl2d.txt spekt/'+vardas+'_output.txt']
# subprocess.Popen(cmd,shell=True).wait()

# skk=40
# pj=1
# #ii=int(10000000/860)#12450
# #ii=np.arange(11000,14000,10)[np.diag(zi/(1*zi.max()))>0.65][0]
# plt.figure()
# plt.contourf(X,Y,zi/(1*zi.max()),np.arange(-pj,pj+2*pj/skk,2*pj/skk), cmap='BlueRed3')
# plt.colorbar()
# skk=20
# plt.contour(X,Y,zi/(1*zi.max()),np.arange(-pj,pj+2*pj/skk,2*pj/skk),colors=('k',))
# plt.plot(x,y,'k-',linewidth=1.5)
# plt.axes().set_aspect('equal','box-forced')


# #vardas='2d_'+str(s)+'_'+str(om)+'_'+str(j)+'_'+str(T)+'K_'+str(virpnum2)
# plt.savefig('spekt/'+vardas+'.png')
