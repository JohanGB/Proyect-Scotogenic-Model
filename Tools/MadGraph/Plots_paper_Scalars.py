import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from organizer import *
import scipy as scp


#read data from the csv files from both delta files
data_30_500=pd.read_csv(
    '/home/gardila/Singlet_Doublet_ScotoU1_UABDM/Data_CSVs/Scalars/XS_500_D30.csv', delimiter=',')
#data_50_500=pd.read_csv(
    #'/home/gardila/Singlet_Doublet_ScotoU1_UABDM/Data_CSVs/Scalars/XS_500_D50.csv', delimiter=',')

#Pass data to numpy
data_30_500= data_30_500.to_numpy()
#data_50_500= data_50_500.to_numpy()

#extract the data 
M_DM_30_500 = data_30_500[:,0]
XS_Full_30_500 = data_30_500[:,1]
Delta_M_30_500 = np.abs((np.abs(data_30_500[:,2])-np.abs(data_30_500[:,3])))
VEV_30_500 = data_30_500[:,4]
#pass the Yukawas to floats
y11_30_500 = data_30_500[:,5]
y12_30_500= data_30_500[:,6]
y13_30_500= data_30_500[:,7]
for i in range(len(y11_30_500)):
    y11_30_500[i]= complex(y11_30_500[i])
    y12_30_500[i]= complex(y12_30_500[i])
    y13_30_500[i]= complex(y13_30_500[i])
y1i_30_500= np.abs(y11_30_500)**2+np.abs(y12_30_500)**2+np.abs(y13_30_500)**2
lam1_30_500 = data_30_500[:,8]

#M_DM_50_500 = data_50_500[:,0]
#XS_Full_50_500 = data_50_500[:,1]
#Delta_M_50_500 = np.abs(np.abs(data_50_500[:,2])-np.abs(data_50_500[:,3]))
#VEV_50_500 = data_50_500[:,4]
#pass the Yukawas to floats
#y11_50_500 = data_50_500[:,5]
#y12_50_500 = data_50_500[:,6]
#y13_50_500= data_50_500[:,7]
#for i in range(len(y11_50_500)):
 #   y11_50_500[i]= complex(y11_50_500[i])
  #  y12_50_500[i]= complex(y12_50_500[i])
   # y13_50_500[i]= complex(y13_50_500[i])
#y1i_50_500= np.abs(y11_50_500)**2+np.abs(y12_50_500)**2+np.abs(y13_50_500)**2
#lam1_50_500 = data_50_500[:,8]

# #scatter plot for the XS vs M_DM for both deltas
# f1=plt.figure(figsize=(5,4))
# plt.plot([],[], ' ', label='generate p p > etai w ll n')
# plt.axhline(y=1.367e-5, color='purple', linestyle='--', label=r'$\sigma(\mathcal{L}=3000$ fb$^{-1}$).')
# plt.axhline(y=1.367e-4, color='orange', linestyle='--', label=r'$\sigma(\mathcal{L}=300$ fb$^{-1}$).')
# plt.axhline(y=2.99e-1, color='cyan', linestyle='--', label=r'$\sigma(\mathcal{L}=137$ fb$^{-1}$). ')
# plt.scatter(M_DM_30_500, XS_Full_30_500, c='black',marker='o' ,s=10, alpha= 0.7, label=r'$\Delta m(N_1,\eta_R)<30GeV$')
# #plt.scatter(M_DM_50_500, XS_Full_50_500, c='r', marker='x',s=10, alpha=0.7, label=r'$\Delta m(N_1,\eta_R)<50GeV$')
# plt.legend( bbox_to_anchor=(1.65, 1.02), loc='upper right' )
# plt.grid()
# plt.xlabel(r'M$_{DM}$(GeV)')
# plt.ylabel(r'$\sigma$(pb)')
# plt.yscale('log')
# plt.title(r'$\sigma$ vs M$_{DM}$')
# plt.savefig('XSvsM_ScalarDM_DELTA30_DELTA50_MH2_500.pdf', bbox_inches='tight')

# f2=plt.figure(figsize=(5,4))
# plt.plot([],[], ' ', label='generate p p > etai w ll n')
# plt.scatter(Delta_M_30_500, XS_Full_30_500, c='black',marker='o' ,s=10, alpha=0.7, label=r'$\Delta m(N_1,\eta_R)<30GeV$')
# #plt.scatter(Delta_M_50_500, XS_Full_50_500, c='r', marker='x',s=10, alpha=0.7, label=r'$\Delta m(N_1,\eta_R)<50GeV$')
# plt.legend( bbox_to_anchor=(1.65, 1.02), loc='upper right' )
# plt.grid()
# plt.xlabel(r'$\Delta m(N_1,\eta_R)$(GeV)')
# plt.ylabel(r'$\sigma$(pb)')
# plt.yscale('log')
# plt.title(r'$\sigma$ vs $\Delta m(N_1,\eta_R)$')
# plt.savefig('XSvsDeltaM_ScalarDM_DELTA30_DELTA50_MH2_500.pdf', bbox_inches='tight')

# f3=plt.figure(figsize=(5,4))
# ax = f3.add_subplot(111, projection='3d')
# ax.scatter(M_DM_30_500, XS_Full_30_500,Delta_M_30_500, c='black', marker='o', s=10, alpha=0.7, label=r'$\Delta m(N_1,\eta_R)<30GeV$')
# #ax.scatter(M_DM_50_500,XS_Full_50_500,Delta_M_50_500, c='r', marker='x', s=10, alpha=0.7, label=r'$\Delta m(N_1,\eta_R)<50GeV$')
# ax.set_xlabel(r'M$_{DM}$(GeV)')
# ax.set_zlabel(r'$\Delta m(N_1,\eta_R)$(GeV)')
# ax.set_ylabel(r'$\sigma$(pb)')
# plt.legend( bbox_to_anchor=(1.65, 1.02), loc='upper right' )
# plt.title(r'$\sigma$ vs M$_{DM}$ vs $\Delta m(N_1,\eta_R)$')
# plt.savefig('XSvsMvsDelta_3D_ScalarDM_DELTA30_DELTA50_MH2_500.pdf', bbox_inches='tight')

# f4=plt.figure(figsize=(5,4))
# plt.plot([],[], ' ', label='generate p p > etai w ll n')
# plt.scatter(y1i_30_500, XS_Full_30_500, c='black',marker='o' ,s=10, alpha=0.7, label=r'$\Delta m(N_1,\eta_R)<30GeV$')
# plt.scatter(y1i_50_500, XS_Full_50_500, c='r', marker='x',s=10, alpha=0.7, label=r'$\Delta m(N_1,\eta_R)<50GeV$')
# plt.legend( bbox_to_anchor=(1.65, 1.02), loc='upper right' )
# plt.grid()
# plt.xlabel(r'$\sum_i|y_{1i}|^2$')
# plt.ylabel(r'$\sigma$(pb)')
# plt.yscale('log')
# plt.title(r'$\sigma$ vs $\sum_i|y_{1i}|^2$')
# plt.savefig('XSvsYukawas_ScalarDM_DELTA30_DELTA50_MH2_500.pdf', bbox_inches='tight')

# f5=plt.figure(figsize=(5,4))
# plt.plot([],[], ' ', label='generate p p > etai w ll n')
# plt.scatter(lam1_30_500, XS_Full_30_500, c='black',marker='o' ,s=10, alpha=0.7, label=r'$\Delta m(N_1,\eta_R)<30GeV$')
# plt.scatter(lam1_50_500, XS_Full_50_500, c='r', marker='x',s=10, alpha=0.7, label=r'$\Delta m(N_1,\eta_R)<50GeV$')
# plt.legend( bbox_to_anchor=(1.65, 1.02), loc='upper right' )
# plt.grid()
# plt.xlabel(r'$\lambda_1$')
# plt.ylabel(r'$\sigma$(pb)')
# plt.yscale('log')
# plt.title(r'$\sigma$ vs $\lambda_1$')
# plt.savefig('XSvsLam1_ScalarDM_DELTA30_DELTA50_500.pdf', bbox_inches='tight')


#put the M_DM, XS_Full, Delta_M, VEV, y1j, lam1 back together in a pandas df 
df_30_500 = pd.DataFrame({'M_DM': M_DM_30_500, 'XS_Full': XS_Full_30_500, 'Delta_M': Delta_M_30_500, 'VEV': VEV_30_500, 'y1i': y1i_30_500, 'lam1': lam1_30_500})
#df_50_500 = pd.DataFrame({'M_DM': M_DM_50_500, 'XS_Full': XS_Full_50_500, 'Delta_M': Delta_M_50_500, 'VEV': VEV_50_500, 'y1i': y1i_50_500, 'lam1': lam1_50_500})

# #plot the correlation matrix
# f6 = plt.figure(figsize=(5,4))
# corr = df_30_500.corr()
# sns.heatmap(corr, annot=True, cmap='coolwarm')
# plt.title('Correlation Matrix for Delta 30')
# plt.savefig('CorrMat_Delta30_MH2_500.pdf', bbox_inches='tight')

# f7 = plt.figure(figsize=(5,4))
# corr = df_50_500.corr()
# sns.heatmap(corr, annot=True, cmap='coolwarm')
# plt.title('Correlation Matrix for Delta 50')
# plt.savefig('CorrMat_Delta50_MH2_500.pdf', bbox_inches='tight')

#Now for the 246 GeV case

#read data from the csv files from both delta files
data_30_246=pd.read_csv(
    '/home/gardila/Singlet_Doublet_ScotoU1_UABDM/Data_CSVs/Scalars/XS_246_D30.csv', delimiter=',')
#data_50_246=pd.read_csv(
    #'/home/gardila/Singlet_Doublet_ScotoU1_UABDM/Data_CSVs/Scalars/XS_246_D50.csv', delimiter=',')
#Pass data to numpy
data_30_246= data_30_246.to_numpy()
#data_50_246= data_50_246.to_numpy()
#extract the data
M_DM_30_246 = data_30_246[:,0]
XS_Full_30_246 = data_30_246[:,1]
Delta_M_30_246 = np.abs((np.abs(data_30_246[:,2])-np.abs(data_30_246[:,3])))
VEV_30_246 = data_30_246[:,4]
lam1_30_246 = data_30_246[:,8]

# M_DM_50_246 = data_50_246[:,0]
# XS_Full_50_246 = data_50_246[:,1]
# Delta_M_50_246 = np.abs(np.abs(data_50_246[:,2])-np.abs(data_50_246[:,3]))
# VEV_50_246 = data_50_246[:,4]
# lam1_50_246 = data_50_246[:,8]

#pass the Yukawas to floats
y11_30_246 = data_30_246[:,5]
y12_30_246= data_30_246[:,6]
y13_30_246= data_30_246[:,7]
for i in range(len(y11_30_246)):
    y11_30_246[i]= complex(y11_30_246[i])
    y12_30_246[i]= complex(y12_30_246[i])
    y13_30_246[i]= complex(y13_30_246[i])
y1i_30_246= np.abs(y11_30_246)**2+np.abs(y12_30_246)**2+np.abs(y13_30_246)**2

# y11_50_246 = data_50_246[:,5]
# y12_50_246= data_50_246[:,6]
# y13_50_246= data_50_246[:,7]
# for i in range(len(y11_50_246)):
#     y11_50_246[i]= complex(y11_50_246[i])
#     y12_50_246[i]= complex(y12_50_246[i])
#     y13_50_246[i]= complex(y13_50_246[i])
# y1i_50_246= np.abs(y11_50_246)**2+np.abs(y12_50_246)**2+np.abs(y13_50_246)**2
#scatter plot for the XS vs M_DM for both deltas
f8=plt.figure(figsize=(5,4))
plt.plot([],[], ' ', label='generate p p > etai w ll n')
plt.axhline(y=2.99e-4, color='cyan', linestyle='--', label=r'Proj. Sensit. @ 137 fb$^{-1}$. ')
plt.axhline(y=1.367e-4, color='orange', linestyle='--', label=r'Proj. Sensit.@ 300 fb$^{-1}$.')
plt.axhline(y=1.367e-5, color='purple', linestyle='--', label=r'Proj. Sensit. @ 3000 fb$^{-1}$.')
plt.scatter(M_DM_30_246, XS_Full_30_246, c='blue',marker='o' ,s=10, alpha= 0.7, label=r'$m_{h_2}=246$ GeV')
plt.scatter(M_DM_30_500, XS_Full_30_500, c='r',marker='o' ,s=10, alpha= 0.7, label=r'$m_{h_2}=500$ GeV')
#plt.scatter(M_DM_50_246, XS_Full_50_246, c='r', marker='x',s=10, alpha=0.7, label=r'$\Delta m(N_1,\eta_R)<50GeV$')
plt.legend(loc='upper right', fontsize='x-small')
#plt.grid(ls=':')
plt.xlabel(r'M$_{DM}$(GeV)')
plt.ylabel(r'$\sigma$(pb)')
plt.yscale('log')
plt.xlim(np.min(M_DM_30_246), 1500)
plt.ylim (1E-22, 1E-2)
#plt.title(r'$\sigma$ vs M$_{DM}$')
plt.savefig('XSvsM_ScalarDM_DELTA30_MH2_246_500.pdf', bbox_inches='tight')

# f9=plt.figure(figsize=(5,4))
# plt.plot([],[], ' ', label='generate p p > etai w ll n')
# plt.scatter(Delta_M_30_246, XS_Full_30_246, c='black',marker='o' ,s=10, alpha=0.7, label=r'$\Delta m(N_1,\eta_R)<30GeV$')
# #plt.scatter(Delta_M_50_246, XS_Full_50_246, c='r', marker='x',s=10, alpha=0.7, label=r'$\Delta m(N_1,\eta_R)<50GeV$')
# plt.legend( bbox_to_anchor=(1.65, 1.02), loc='upper right' )
# plt.grid()
# plt.xlabel(r'$\Delta m(N_1,\eta_R)$(GeV)')
# plt.ylabel(r'$\sigma$(pb)')
# plt.yscale('log')
# plt.title(r'$\sigma$ vs $\Delta m(N_1,\eta_R)$')
# plt.savefig('XSvsDeltaM_ScalarDM_DELTA30_DELTA50_MH2_246.pdf', bbox_inches='tight')

# f10=plt.figure(figsize=(5,4))
# ax = f10.add_subplot(111, projection='3d')
# ax.scatter(M_DM_30_246, XS_Full_30_246,Delta_M_30_246, c='black', marker='o', s=10, alpha=0.7, label=r'$\Delta m(N_1,\eta_R)<30GeV$')
# #ax.scatter(M_DM_50_246,XS_Full_50_246,Delta_M_50_246, c='r', marker='x', s=10, alpha=0.7, label=r'$\Delta m(N_1,\eta_R)<50GeV$')
# ax.set_xlabel(r'M$_{DM}$(GeV)')
# ax.set_zlabel(r'$\Delta m(N_1,\eta_R)$(GeV)')
# ax.set_ylabel(r'$\sigma$(pb)')
# plt.legend( bbox_to_anchor=(1.65, 1.02), loc='upper right' )
# plt.title(r'$\sigma$ vs M$_{DM}$ vs $\Delta m(N_1,\eta_R)$')
# plt.savefig('XSvsMvsDelta_3D_ScalarDM_DELTA30_DELTA50_MH2_246.pdf', bbox_inches='tight')

# f11=plt.figure(figsize=(5,4))
# plt.plot([],[], ' ', label='generate p p > etai w ll n')
# plt.scatter(y1i_30_246, XS_Full_30_246, c='black',marker='o' ,s=10, alpha=0.7, label=r'$\Delta m(N_1,\eta_R)<30GeV$')
# plt.scatter(y1i_50_246, XS_Full_50_246, c='r', marker='x',s=10, alpha=0.7, label=r'$\Delta m(N_1,\eta_R)<50GeV$')
# plt.legend( bbox_to_anchor=(1.65, 1.02), loc='upper right' )
# plt.grid()
# plt.xlabel(r'$\sum_i|y_{1i}|^2$')
# plt.ylabel(r'$\sigma$(pb)')
# plt.yscale('log')
# plt.title(r'$\sigma$ vs $\sum_i|y_{1i}|^2$')
# plt.savefig('XSvsYukawas_ScalarDM_DELTA30_DELTA50_MH2_246.pdf', bbox_inches='tight')

# f12=plt.figure(figsize=(5,4))
# plt.plot([],[], ' ', label='generate p p > etai w ll n')
# plt.scatter(lam1_30_246, XS_Full_30_246, c='black',marker='o' ,s=10, alpha=0.7, label=r'$\Delta m(N_1,\eta_R)<30GeV$')
# plt.scatter(lam1_50_246, XS_Full_50_246, c='r', marker='x',s=10, alpha=0.7, label=r'$\Delta m(N_1,\eta_R)<50GeV$')
# plt.legend( bbox_to_anchor=(1.65, 1.02), loc='upper right' )
# plt.grid()
# plt.xlabel(r'$\lambda_1$')
# plt.ylabel(r'$\sigma$(pb)')
# plt.yscale('log')
# plt.title(r'$\sigma$ vs $\lambda_1$')
# plt.savefig('XSvsLam1_ScalarDM_DELTA30_DELTA50_246.pdf', bbox_inches='tight')

#put the M_DM, XS_Full, Delta_M, VEV, y1j, lam1 back together in a pandas df
df_30_246 = pd.DataFrame({'M_DM': M_DM_30_246, 'XS_Full': XS_Full_30_246, 'Delta_M': Delta_M_30_246, 'VEV': VEV_30_246, 'y1i': y1i_30_246, 'lam1': lam1_30_246})
#df_50_246 = pd.DataFrame({'M_DM': M_DM_50_246, 'XS_Full': XS_Full_50_246, 'Delta_M': Delta_M_50_246, 'VEV': VEV_50_246, 'y1i': y1i_50_246, 'lam1': lam1_50_246})

#plot the correlation matrix
# f13 = plt.figure(figsize=(5,4))
# corr = df_30_246.corr()
# sns.heatmap(corr, annot=True, cmap='coolwarm')
# plt.title('Correlation Matrix for Delta 30')
# plt.savefig('CorrMat_Delta30_MH2_246.pdf', bbox_inches='tight')

# f14 = plt.figure(figsize=(5,4))
# corr = df_50_246.corr()
# sns.heatmap(corr, annot=True, cmap='coolwarm')
# plt.title('Correlation Matrix for Delta 50')
# plt.savefig('CorrMat_Delta50_MH2_246.pdf', bbox_inches='tight')


#import the data from the xsbefdecay d30 csv FOR 500 GeV
XSBefDecay_500_30= pd.read_csv('/home/gardila/Singlet_Doublet_ScotoU1_UABDM/Data_CSVs/Scalars/XSBefDecay_500_D30.csv')

#import the for the remaining befdecay files
#XSBefDecay_500_50 = pd.read_csv('/home/gardila/Singlet_Doublet_ScotoU1_UABDM/Data_CSVs/Scalars/XSBefDecay_500_D50.csv')
#XSBefDecay_246_50 = pd.read_csv('/home/gardila/Singlet_Doublet_ScotoU1_UABDM/Data_CSVs/Scalars/XSBefDecay_246_D50.csv')
XSBefDecay_246_30 = pd.read_csv('/home/gardila/Singlet_Doublet_ScotoU1_UABDM/Data_CSVs/Scalars/XSBefDecay_246_D30.csv')

#extract the MDM and XS values
MDMBD_500_30 = XSBefDecay_500_30['MDM']
XSBD_500_30 = XSBefDecay_500_30['XS']
#sort the MDM and their corresponding XS without using zip
MDMBD_500_30, XSBD_500_30 = zip(*sorted(zip(MDMBD_500_30, XSBD_500_30)))
#convert the sorted MDM and XS to numpy arrays
MDMBD_500_30 = np.array(MDMBD_500_30)
XSBD_500_30 = np.array(XSBD_500_30)


#pass the mass values to floats
M_DM_30_500 = M_DM_30_500.astype(float)
#M_DM_50_500 = M_DM_50_500.astype(float)
#M_DM_50_246 = M_DM_50_246.astype(float)
M_DM_30_246 = M_DM_30_246.astype(float)


#extract the MDM and XS values
# MDMBD_500_50 = XSBefDecay_500_50['MDM']
# XSBD_500_50 = XSBefDecay_500_50['XS']
# MDMBD_246_50 = XSBefDecay_246_50['MDM']
# XSBD_246_50 = XSBefDecay_246_50['XS']
MDMBD_246_30 = XSBefDecay_246_30['MDM']
XSBD_246_30 = XSBefDecay_246_30['XS']

#use scipy to interpolate the data
fBD_500_30 = scp.interpolate.interp1d(MDMBD_500_30, XSBD_500_30, kind='cubic')
# fBD_500_50 = scp.interpolate.interp1d(MDMBD_500_50, XSBD_500_50, kind='cubic')
# fBD_246_50 = scp.interpolate.interp1d(MDMBD_246_50, XSBD_246_50, kind='cubic')
fBD_246_30 = scp.interpolate.interp1d(MDMBD_246_30, XSBD_246_30, kind='cubic')


#normalize the XSFull to the XSBD
XSNORM_30_500 = XS_Full_30_500/fBD_500_30(M_DM_30_500)
# XSNORM_50_500 = XS_Full_50_500/fBD_500_50(M_DM_50_500)
# XSNORM_50_246 = XS_Full_50_246/fBD_246_50(M_DM_50_246)
XSNORM_30_246 = XS_Full_30_246/fBD_246_30(M_DM_30_246)



#scatter plot for the XSBD vs M_DM for both deltas
f15=plt.figure(figsize=(5,4))
plt.plot([],[], ' ', label=r'$\text{pp}\to \eta_I +\eta_R$')
plt.scatter(MDMBD_246_30, XSBD_246_30, c='blue', marker='o',s=10, alpha=0.7, label=r'M$_{h_2}$=246 GeV')
plt.scatter(MDMBD_500_30, XSBD_500_30, c='r',marker='o' ,s=10, alpha= 0.7, label=r'M$_{h_2}$=500 GeV')
# plt.scatter(MDMBD_500_50, XSBD_500_50, c='r', marker='x',s=10, alpha=0.7, label=r'M$_{h_2}$=500 GeV,$\Delta m(N_1,\eta_R)<$ 50 GeV')
# plt.scatter(MDMBD_246_50, XSBD_246_50, c='b', marker='v',s=10, alpha=0.7, label=r'M$_{h_2}$=246 GeV, $\Delta m(N_1,\eta_R)<$ 50 GeV')
plt.legend(loc='upper right', fontsize='x-small')
#plt.grid(ls=':')
plt.xlabel(r'M$_{DM}$(GeV)')
plt.ylabel(r'$\sigma$(pb)')
plt.yscale('log')
plt.xlim(130, 1500)
#plt.title(r'$\sigma$ vs M$_{DM}$')
plt.savefig('XSBefDecayvsM_ScalarDM_DELTA30_DELTA50_MH2_500_246.pdf', bbox_inches='tight')

#scatter plot of the normalized data given above 
f16=plt.figure(figsize=(5,4))
plt.plot([],[], ' ', label=r'$\text{pp}\to \eta_I +\eta_R$')
plt.scatter(M_DM_30_246, XSNORM_30_246, c='blue', marker='o',s=10, alpha=0.7, label=r'M$_{h_2}$=246 GeV')
plt.scatter(M_DM_30_500, XSNORM_30_500, c='r',marker='o' ,s=10, alpha= 0.7, label=r'M$_{h_2}$=500 GeV')
# plt.scatter(M_DM_50_500, XSNORM_50_500, c='r', marker='x',s=10, alpha=0.7, label=r'M$_{h_2}$=500 GeV, $\Delta m(N_1,\eta_R)<50$ GeV')
# plt.scatter(M_DM_50_246, XSNORM_50_246, c='b', marker='v',s=10, alpha=0.7, label=r'M$_{h_2}$=246 GeV, $\Delta m(N_1,\eta_R)<50$ GeV')
#plt.legend( bbox_to_anchor=(1.79, 1.02), loc='upper right' )
plt.legend(loc='upper right', fontsize='x-small')
#plt.grid(ls=':')
plt.xlabel(r'M$_{DM}$(GeV)')
plt.ylabel(r'$\beta$')
plt.yscale('log')
plt.xlim(130, 1500)
#plt.title(r'$\beta$ vs M$_{DM}$')
plt.savefig('NORMXS.pdf', bbox_inches='tight')

#unify all the interpolated  XS data into a single array
XS_Normalized = np.concatenate((XSNORM_30_500, XSNORM_30_246))
#find the maximum value of the normalized XS
max_XS = np.max(XS_Normalized)
#find the minimum value of the normalized XS
min_XS = np.min(XS_Normalized)
print('The maximum BR is: ', max_XS)
print('The minimum BR is: ', min_XS)

#Start the betas

top_xs_band= XSBD_246_30*max_XS
min_xs_band= XSBD_246_30*min_XS



# #scatter plot for the XSBD vs M_DM 
# f17=plt.figure(figsize=(5,4))
# plt.plot([],[], ' ', label='generate p p > etai w ll n')
# plt.axhline(y=1.367e-5, color='purple', linestyle='--', label=r'$\sigma(\mathcal{L}=3000$ fb$^{-1}$).')
# plt.axhline(y=1.367e-4, color='orange', linestyle='--', label=r'$\sigma(\mathcal{L}=300$ fb$^{-1}$).')
# plt.axhline(y=2.99e-1, color='cyan', linestyle='--', label=r'$\sigma(\mathcal{L}=137$ fb$^{-1}$). ')
# plt.scatter(M_DM_30_246, top_xs_band, color='blue', marker='P', label=r'$\beta_{max}$= $1.837 \times 10^{-5}$')
# plt.scatter(M_DM_30_246, min_xs_band, color='blue', marker='D', label=r'$\beta_{min}$= $6.215 \times 10^{-16}$')
# plt.scatter(M_DM_30_246, XS_Full_30_246, c='black',marker='o' ,s=10, alpha= 0.7, label=r'M$_{h_2}$=246 GeV')
# plt.scatter(M_DM_30_500, XS_Full_30_500, c='r', marker='o',s=10, alpha=0.7, label=r'M$_{h_2}$=500 GeV')
# plt.legend( bbox_to_anchor=(1.8, 1.02), loc='upper right' )
# plt.grid(ls=':')
# plt.xlabel(r'M$_{DM}$(GeV)')
# plt.ylabel(r'$\sigma$(pb)')
# plt.yscale('log')
# plt.xlim(130, 1500)
# plt.title(r'$\sigma$ vs M$_{DM}$')
# plt.savefig('XSvsM_ScalarDM_DELTA30_DELTA50_MH2_246_500_BETAS.pdf', bbox_inches='tight')

#copy the M_DM_50_246 
M_DM_30_246_COPY_max= M_DM_30_246.copy()
M_DM_30_246_COPY_min= M_DM_30_246.copy()
#sort the M_DM_50_246_COPY and the bands
M_DM_30_246_COPY_max, top_xs_band = zip(*sorted(zip(M_DM_30_246_COPY_max, top_xs_band)))
M_DM_30_246_COPY_min, min_xs_band = zip(*sorted(zip(M_DM_30_246_COPY_min, min_xs_band)))

#interpolate the top and bottom bands
fBD_top = scp.interpolate.interp1d(M_DM_30_246, top_xs_band, kind='cubic')
fBD_min = scp.interpolate.interp1d(M_DM_30_246, min_xs_band, kind='cubic')


#create the bands using Cristian's method
x_max= M_DM_30_500

#pass the data before decay to floats
XSBefDecay_500_30= XSBefDecay_500_30['XS']
XSBefDecay_500_30= XSBefDecay_500_30.astype(float)

degree=5
y_max= XSBefDecay_500_30

coeff_max= np.polyfit(x_max, np.log(y_max), degree)

poli_max= np.poly1d(coeff_max)



x_max_fit= np.linspace(min(x_max), 1490, 1000)


y_max_fit= poli_max(x_max_fit)

x_min= M_DM_30_246
y_min= XSBefDecay_246_30['XS']
y_min= y_min.astype(float)

coeff_min= np.polyfit(x_min, np.log(y_min), 5)
poli_min= np.poly1d(coeff_min)

x_min_fit= np.linspace(min(x_min), 1490, 1000)
y_min_fit= poli_min(x_min_fit)





#plot just the interpolated bands
# f18=plt.figure(figsize=(5,4))
# plt.plot([],[], ' ', label='generate p p > etai w ll n')
# plt.axhline(y=1.367e-5, color='purple', linestyle='--', label=r'$\sigma(\mathcal{L}=3000$ fb$^{-1}$).')
# plt.axhline(y=1.367e-4, color='orange', linestyle='--', label=r'$\sigma(\mathcal{L}=300$ fb$^{-1}$).')
# plt.axhline(y=2.99e-1, color='cyan', linestyle='--', label=r'$\sigma(\mathcal{L}=137$ fb$^{-1}$). ')
# plt.plot(M_DM_30_246_COPY_max,  fBD_top(M_DM_30_246), color='blue', linestyle='--', label=r'$\sigma_0\times\beta_{max}=\sigma_0 (2.27\times 10^{-5})$')
# plt.plot(M_DM_30_246_COPY_min,  fBD_min(M_DM_30_246), color='blue', linestyle='--', label=r'$\sigma_0\times\beta_{min}=\sigma_0 (1.66\times 10^{-15})$')
# plt.legend( bbox_to_anchor=(1.65, 1.02), loc='upper right' )
# plt.grid(ls=':')
# plt.xlim(130, 1500)
# plt.xlabel(r'M$_{DM}$(GeV)')
# plt.ylabel(r'$\sigma$(pb)')
# plt.yscale('log')
# plt.title(r'$\sigma$ vs M$_{DM}$')
# plt.savefig('BETAS.pdf', bbox_inches='tight')

#repeat the band plot with the new interpolated betas
print(np.min(XS_Full_30_246))   

f19=plt.figure(figsize=(5,4))
#plt.grid(ls=':')

plt.plot([],[], ' ', label=r'$\text{pp}\to \eta_I+W^\pm+N_1+\ell$')
plt.axhline(y=2.99e-4, color='cyan', linestyle='--', label=r'Proj. Sensit. @ 137 fb$^{-1}$. ')
plt.axhline(y=1.367e-4, color='orange', linestyle='--', label=r'Proj. Sensit. @ 300 fb$^{-1}$.')
plt.axhline(y=1.367e-5, color='purple', linestyle='--', label=r'Proj. Sensit. @ 3000 fb$^{-1}$.')
#plt.plot(M_DM_30_246_COPY_max,  fBD_top(M_DM_30_246), color='blue', linestyle='--', label=r'$\sigma_0\times\beta_{max}=\sigma_0 (2.27\times 10^{-5})$')
#plt.plot(M_DM_30_246_COPY_min,  fBD_min(M_DM_30_246), color='blue', linestyle='--', label=r'$\sigma_0\times\beta_{min}=\sigma_0 (1.66\times 10^{-15})$')
plt.fill_between(x_max_fit, min_XS*np.exp(y_max_fit), max_XS*np.exp(y_max_fit), color='grey', alpha=0.3, label=r'Preferred by $\Omega h^2$')
plt.scatter(M_DM_30_246, XS_Full_30_246, c='blue',marker='o' ,s=8, alpha= 0.7, label=r'M$_{h_2}$=246 GeV')
plt.scatter(M_DM_30_500, XS_Full_30_500, c='r', marker='o',s=8, alpha=0.7, label=r'M$_{h_2}$=500 GeV')
plt.legend(loc='upper right', fontsize='x-small')
plt.xlabel(r'M$_{DM}$(GeV)')
plt.ylabel(r'$\sigma$(pb)')
plt.xlim(np.min(M_DM_30_246), 1500)
plt.ylim (1E-22, 1E-2)
plt.yscale('log')
#plt.title(r'$\sigma$ vs M$_{DM}$')
plt.savefig('XSvsM_ScalarDM_DELTA30_DELTA50_MH2_246_500_BETAS_INTER.pdf', bbox_inches='tight')

#get the lam5 values

lam5_30_246=( data_30_246[:,3]**2 - data_30_246[:,0]**2 )/(246**2)

lam5_30_500=( data_30_500[:,3]**2 - data_30_500[:,0]**2 )/(246**2)

#scatter the full xs vs lam5
f20=plt.figure(figsize=(5,4))
plt.plot([],[], ' ', label=r'$\text{pp}\to \eta_I+W^\pm+N_1+\ell$')
plt.scatter(lam5_30_246, XS_Full_30_246, c='blue',marker='o' ,s=10, alpha=0.7, label=r'M$_{h_2}$=246 GeV')
plt.scatter(lam5_30_500, XS_Full_30_500, c='r',marker='o' ,s=10, alpha=0.7, label=r'M$_{h_2}$=500 GeV')
plt.legend(loc='upper right', fontsize='x-small')
#plt.grid(ls=':')
plt.xlim(0, 1)
plt.xlabel(r'$\lambda_5$')
plt.ylabel(r'$\sigma$(pb)')
plt.yscale('log')
#plt.title(r'$\sigma$ vs $\lambda_5$')
plt.savefig('XSvsLam5_ScalarDM_DELTA30_DELTA50_MH2_246_500.pdf', bbox_inches='tight')


#plot the fit data  
# f21=plt.figure(figsize=(5,4))
# plt.plot([],[], ' ', label='generate p p > etai w ll n')
# plt.scatter(M_DM_30_500, XSBefDecay_500_30, c='black',marker='o' ,s=10, alpha= 0.7, label=r'M$_{h_2}$=246 GeV')
# plt.plot(x_max_fit, np.exp(y_max_fit), color='blue', linestyle='--', label=r'$\sigma_0\times\beta_{max}=\sigma_0 (2.27\times 10^{-5})$')
# plt.legend(loc='upper right', fontsize='x-small')
# #plt.grid(ls=':')
# plt.xlabel(r'M$_{DM}$(GeV)')
# plt.ylabel(r'$\sigma$(pb)')
# plt.yscale('log')
# plt.xlim(130, 1500)
# #plt.title(r'$\sigma$ vs M$_{DM}$')
# plt.savefig('XSBefDecayvsM_ScalarDM_DELTA30_DELTA50_MH2_246_FIT.pdf', bbox_inches='tight')



