# -*- coding: utf-8 -*-
from ROOT import TFile, TTree
import os
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import lognorm
#from sklearn.preprocessing import MinMaxScaler
import matplotlib.colors as colors

# Abrir los archivos .root
#testfile1 = TFile('Results_Chains_1lnoc.root')
testfile1 = TFile('Results_Chains_Random.root')
#testfile2 = TFile('Results_Chains_MCMC_LFVC.root')
#testfile2 = TFile('Results_Chains_DD.root')
testfile2 = TFile('Results_Chains_Final.root')


# Obtener los árboles de ambos archivos
tree1 = testfile1.Get("ScanTree")
tree2 = testfile2.Get("ScanTree")

# Crear listas vacías para el primer archivo (Random Walk)
MH_1, Omega_h2_1 = [], []

# Crear listas vacías para el segundo archivo (Chains_H)
MH_2, Omega_h2_2 = [], []

# Crear listas vacías para las masas de los candidatos
MX01_1, MP01_1, MEtI_1 = [], [], []
MX01_2, MP01_2, MEtI_2 = [], [], []

# Crear listas vacías para los acoples de Yukawa
ge_1, gm_1, gt_1 = [], [], []
ge_2, gm_2, gt_2 = [], [], []

m_nu1_CI_1, m_nu2_CI_1, m_nu3_CI_1 = [], [], []
m_nu1_SPheno_1, m_nu2_SPheno_1, m_nu3_SPheno_1 = [], [], []

m_nu1_CI_2, m_nu2_CI_2, m_nu3_CI_2 = [], [], []
m_nu1_SPheno_2, m_nu2_SPheno_2, m_nu3_SPheno_2 = [], [], []

Yn_11_1, Yn_12_1, Yn_13_1 = [], [], []
Yn_21_1, Yn_22_1, Yn_23_1 = [], [], []
Yn_31_1, Yn_32_1, Yn_33_1 = [], [], []

Yn_11_2, Yn_12_2, Yn_13_2 = [], [], []
Yn_21_2, Yn_22_2, Yn_23_2 = [], [], []
Yn_31_2, Yn_32_2, Yn_33_2 = [], [], []

MEG_1, M3E_1 = [], []
MEG_2, M3E_2 = [], []

l1_1, l4Sig_1, l4Eta_1, lHSig_1, l32HEta_1, l33HEta_1 = [], [], [], [], [], []
lEtaSig_1, cTri_1, Sig_1, Eta_1, l31HEta_1 = [], [], [], [], []
l1_2, l4Sig_2, l4Eta_2, lHSig_2, l32HEta_2, l33HEta_2 = [], [], [], [], [], []
lEtaSig_2, cTri_2, Sig_2, Eta_2, l31HEta_2 = [], [], [], [], []

MSig2_1, MEta2_1, mH2_1 = [], [], []
MSig2_2, MEta2_2, mH2_2 = [], [], []

mN11_1, mN22_1, mN33_1  = [], [], []
mN11_2, mN22_2, mN33_2  = [], [], []

mnu1_1, dm212_1, dm312_1 =  [], [], []
mnu1_2, dm212_2, dm312_2 =  [], [], []

theta_12_1, theta_13_1, theta_23_1 = [], [], []
theta_12_2, theta_13_2, theta_23_2 = [], [], []

delta_d_1, delta_m1_1, delta_m2_1, delta_m3_1 = [], [], [], []
delta_d_2, delta_m1_2, delta_m2_2, delta_m3_2 = [], [], [], []

Theta1_1, Theta2_1, Theta3_1, alpha_1, = [], [], [], []
Theta1_2, Theta2_2, Theta3_2, alpha_2, = [], [], [], []

MX02_1, MX03_1, MP02_1 = [], [], []
MX02_2, MX03_2, MP02_2 = [], [], []

m_nu1_Inputs_1, Dnu_21_Inputs_1, Dnu_31_Inputs_1 = [], [], []
m_nu1_Inputs_2, Dnu_21_Inputs_2, Dnu_31_Inputs_2 = [], [], []

Zscalar11_1, Zscalar12_1, Zscalar21_1, Zscalar22_1 = [], [], [], []
Zscalar11_2, Zscalar12_2, Zscalar21_2, Zscalar22_2 = [], [], [], []

RZX11_1, RZX12_1, RZX13_1 = [], [], []
RZX21_1, RZX22_1, RZX23_1 = [], [], []
RZX31_1, RZX32_1, RZX33_1 = [], [], [] 
RZX11_2, RZX12_2, RZX13_2 = [], [], []
RZX21_2, RZX22_2, RZX23_2 = [], [], []
RZX31_2, RZX32_2, RZX33_2 = [], [], [] 

g_2e_1, g_2m_1, g_2t_1, Spar_1 = [], [], [], []
Tpar_1, Upar_1, BrHEM_1, BrHET_1, BrHTM_1 = [], [], [], [], []
GammaH1_1, GammaH2_1, Likelihood_1 = [], [], [] 
g_2e_2, g_2m_2, g_2t_2, Spar_2 = [], [], [], []
Tpar_2, Upar_2, BrHEM_2, BrHET_2, BrHTM_2 = [], [], [], [], []
GammaH1_2, GammaH2_2, Likelihood_2 = [], [], [] 

BrMEG_1, BrM3E_1, BrTEG_1, BrTMG_1, BrT3E_1, BrT3M_1 = [], [], [], [], [], []
BrTMp2E_1, BrTMm2E_1, BrTEp2M_1, BrTEm2M_1, BrTEpi_1, BrTEeta_1 = [], [], [], [], [], []
BrTEetaP_1, BrTMpi_1, BrTMeta_1, BrTMetaP_1 =[], [], [], []
CrTi_1, CrPb_1, CrAu_1, BrZEM_1, BrZET_1, BrZMT_1 = [], [], [], [], [], []
BrMEG_2, BrM3E_2, BrTEG_2, BrTMG_2, BrT3E_2, BrT3M_2 = [], [], [], [], [], []
BrTMp2E_2, BrTMm2E_2,BrTEp2M_2, BrTEm2M_2, BrTEpi_2, BrTEeta_2 = [], [], [], [], [], []
BrTEetaP_2, BrTMpi_2, BrTMeta_2, BrTMetaP_2 =[], [], [], []
CrTi_2, CrPb_2, CrAu_2, BrZEM_2, BrZET_2, BrZMT_2 = [], [], [], [], [], []

MEtP_1, MEtP_2 = [], []
MDM_2, sigSI_2, sigSIp, sigSIn = [], [], [], []
# Extraer los datos del primer archivo (Random Walk)
for x in tree1:
    MH_1.append(abs(x.MH))
    Omega_h2_1.append(abs(x.Omega_h2))
    MX01_1.append(abs(x.MX01))
    MP01_1.append(abs(x.MP01))
    MEtI_1.append(abs(x.MEtI))
    MEtP_1.append(abs(x.MEtP))
    m_nu1_CI_1.append(abs(x.m_nu1_CI))
    m_nu2_CI_1.append(abs(x.m_nu2_CI))
    m_nu3_CI_1.append(abs(x.m_nu3_CI))
    m_nu1_SPheno_1.append(abs(x.m_nu1_SPheno))
    m_nu2_SPheno_1.append(abs(x.m_nu2_SPheno))
    m_nu3_SPheno_1.append(abs(x.m_nu3_SPheno))
    Yn_11_1.append(math.sqrt(x.RYn_11**2 + x.IYn11**2))
    Yn_12_1.append(math.sqrt(x.RYn_12**2 + x.IYn12**2))
    Yn_13_1.append(math.sqrt(x.RYn_13**2 + x.IYn13**2))
    Yn_21_1.append(math.sqrt(x.RYn_21**2 + x.IYn21**2))
    Yn_22_1.append(math.sqrt(x.RYn_22**2 + x.IYn22**2))
    Yn_23_1.append(math.sqrt(x.RYn_23**2 + x.IYn23**2))
    Yn_31_1.append(math.sqrt(x.RYn_31**2 + x.IYn31**2))
    Yn_32_1.append(math.sqrt(x.RYn_32**2 + x.IYn32**2))
    Yn_33_1.append(math.sqrt(x.RYn_33**2 + x.IYn33**2))
    l1_1.append(abs(x.l1))
    l4Sig_1.append(abs(x.l4Sig))
    l4Eta_1.append(abs(x.l4Eta))
    lHSig_1.append(abs(x.lHSig))
    l32HEta_1.append(abs(x.l32HEta))
    l33HEta_1.append(abs(x.l33HEta))
    lEtaSig_1.append(abs(x.lEtaSig))
    cTri_1.append(abs(x.cTri))
    Sig_1.append(abs(x.Sig))
    Eta_1.append(abs(x.Eta))
    l31HEta_1.append(abs(x.l31HEta))
    MSig2_1.append(abs(x.MSig2))
    MEta2_1.append(abs(x.MEta2))
    mH2_1.append(abs(x.mH2))
    mN11_1.append(abs(x.mN11))
    mN22_1.append(abs(x.mN22))
    mN33_1.append(abs(x.mN33))
    mnu1_1.append(abs(x.mnu1))
    dm212_1.append(abs(x.dm212))
    dm312_1.append(abs(x.dm312))
    theta_12_1.append(abs(x.theta_12))
    theta_13_1.append(abs(x.theta_13))
    theta_23_1.append(abs(x.theta_23))
    delta_d_1.append(abs(x.delta_d))
    delta_m1_1.append(abs(x.delta_m1))
    delta_m2_1.append(abs(x.delta_m2))
    delta_m3_1.append(abs(x.delta_m3))
    Theta1_1.append(abs(x.Theta1))
    Theta2_1.append(abs(x.Theta2))
    Theta3_1.append(abs(x.Theta3))
    alpha_1.append(abs(x.alpha))
    MP02_1.append(abs(x.MP02))
    MX02_1.append(abs(x.MX02))
    MX03_1.append(abs(x.MX03))
    m_nu1_Inputs_1.append(abs(x.m_nu1_Inputs))
    Dnu_21_Inputs_1.append(abs(x.Dnu_21_Inputs))
    Dnu_31_Inputs_1.append(abs(x.Dnu_31_Inputs))
    mN11_1.append(abs(x.mN11))
    mN22_1.append(abs(x.mN22))
    mN33_1.append(abs(x.mN33))
    Zscalar11_1.append(abs(x.Zscalar11))
    Zscalar12_1.append(abs(x.Zscalar12))
    Zscalar21_1.append(abs(x.Zscalar21))
    Zscalar22_1.append(abs(x.Zscalar22))
    RZX11_1.append(abs(x.RZX11))
    RZX12_1.append(abs(x.RZX12))
    RZX13_1.append(abs(x.RZX13))
    RZX21_1.append(abs(x.RZX21))
    RZX22_1.append(abs(x.RZX22))
    RZX23_1.append(abs(x.RZX23))
    RZX31_1.append(abs(x.RZX31))
    RZX32_1.append(abs(x.RZX32))
    RZX33_1.append(abs(x.RZX33))
    g_2e_1.append(abs(x.g_2e))
    g_2m_1.append(abs(x.g_2m))
    g_2t_1.append(abs(x.g_2t))
    Spar_1.append(abs(x.Spar))
    Tpar_1.append(abs(x.Tpar))
    Upar_1.append(abs(x.Upar))
    BrHEM_1.append(abs(x.BrHEM))
    BrHET_1.append(abs(x.BrHET))
    BrHTM_1.append(abs(x.BrHTM))
    GammaH1_1.append(abs(x.GammaH1))
    GammaH2_1.append(abs(x.GammaH2))
    Likelihood_1.append(abs(x.Likelihood))
    
# Extraer los datos del segundo archivo (Chains_H)
for y in tree2:
    MH_2.append(abs(y.MH))
    MDM_2.append(abs(y.MDM))
    sigSIp.append(abs(y.sigSIproton))
    sigSIn.append(abs(y.sigSIneutron))
    Omega_h2_2.append(abs(y.Omega_h2))
    sigSI_2.append(abs(y.sigSI))
    MX01_2.append(abs(y.MX01))
    MP01_2.append(abs(y.MP01))
    MEtI_2.append(abs(y.MEtI))
    MEtP_2.append(abs(y.MEtP))
    m_nu1_CI_2.append(abs(y.m_nu1_CI))
    m_nu2_CI_2.append(abs(y.m_nu2_CI))
    m_nu3_CI_2.append(abs(y.m_nu3_CI))
    m_nu1_SPheno_2.append(abs(y.m_nu1_SPheno))
    m_nu2_SPheno_2.append(abs(y.m_nu2_SPheno))
    m_nu3_SPheno_2.append(abs(y.m_nu3_SPheno))
    Yn_11_2.append(math.sqrt(y.RYn_11**2 + y.IYn11**2))
    Yn_12_2.append(math.sqrt(y.RYn_12**2 + y.IYn12**2))
    Yn_13_2.append(math.sqrt(y.RYn_13**2 + y.IYn13**2))
    Yn_21_2.append(math.sqrt(y.RYn_21**2 + y.IYn21**2))
    Yn_22_2.append(math.sqrt(y.RYn_22**2 + y.IYn22**2))
    Yn_23_2.append(math.sqrt(y.RYn_23**2 + y.IYn23**2))
    Yn_31_2.append(math.sqrt(y.RYn_31**2 + y.IYn31**2))
    Yn_32_2.append(math.sqrt(y.RYn_32**2 + y.IYn32**2))
    Yn_33_2.append(math.sqrt(y.RYn_33**2 + y.IYn33**2))
    l1_2.append(abs(y.l1))
    l4Sig_2.append(abs(y.l4Sig))
    l4Eta_2.append(abs(y.l4Eta))
    lHSig_2.append(abs(y.lHSig))
    l32HEta_2.append(abs(y.l32HEta))
    l33HEta_2.append(abs(y.l33HEta))
    lEtaSig_2.append(abs(y.lEtaSig))
    cTri_2.append(abs(y.cTri))
    Sig_2.append(abs(y.Sig))
    Eta_2.append(abs(y.Eta))
    l31HEta_2.append(abs(y.l31HEta))
    MSig2_2.append(abs(y.MSig2))
    MEta2_2.append(abs(y.MEta2))
    mH2_2.append(abs(y.mH2))
    mN11_2.append(abs(y.mN11))
    mN22_2.append(abs(y.mN22))
    mN33_2.append(abs(y.mN33))
    mnu1_2.append(abs(y.mnu1))
    dm212_2.append(abs(y.dm212))
    dm312_2.append(abs(y.dm312))
    theta_12_2.append(abs(y.theta_12))
    theta_13_2.append(abs(y.theta_13))
    theta_23_2.append(abs(y.theta_23))
    delta_d_2.append(abs(y.delta_d))
    delta_m1_2.append(abs(y.delta_m1))
    delta_m2_2.append(abs(y.delta_m2))
    delta_m3_2.append(abs(y.delta_m3))
    Theta1_2.append(abs(y.Theta1))
    Theta2_2.append(abs(y.Theta2))
    Theta3_2.append(abs(y.Theta3))
    alpha_2.append(abs(y.alpha))
    MP02_2.append(abs(y.MP02))
    MX02_2.append(abs(y.MX02))
    MX03_2.append(abs(y.MX03))
    m_nu1_Inputs_2.append(abs(y.m_nu1_Inputs))
    Dnu_21_Inputs_2.append(abs(y.Dnu_21_Inputs))
    Dnu_31_Inputs_2.append(abs(y.Dnu_31_Inputs))
    mN11_2.append(abs(y.mN11))
    mN22_2.append(abs(y.mN22))
    mN33_2.append(abs(y.mN33))
    Zscalar11_2.append(abs(y.Zscalar11))
    Zscalar12_2.append(abs(y.Zscalar12))
    Zscalar21_2.append(abs(y.Zscalar21))
    Zscalar22_2.append(abs(y.Zscalar22))
    RZX11_2.append(abs(y.RZX11))
    RZX12_2.append(abs(y.RZX12))
    RZX13_2.append(abs(y.RZX13))
    RZX21_2.append(abs(y.RZX21))
    RZX22_2.append(abs(y.RZX22))
    RZX23_2.append(abs(y.RZX23))
    RZX31_2.append(abs(y.RZX31))
    RZX32_2.append(abs(y.RZX32))
    RZX33_2.append(abs(y.RZX33))
    g_2e_2.append(abs(y.g_2e))
    g_2m_2.append(abs(y.g_2m))
    g_2t_2.append(abs(y.g_2t))
    Spar_2.append(abs(y.Spar))
    Tpar_2.append(abs(y.Tpar))
    Upar_2.append(abs(y.Upar))
    BrHEM_2.append(abs(y.BrHEM))
    BrHET_2.append(abs(y.BrHET))
    BrHTM_2.append(abs(y.BrHTM))
    GammaH1_2.append(abs(y.GammaH1))
    GammaH2_2.append(abs(y.GammaH2))
    Likelihood_2.append(abs(y.Likelihood))
    MEG_2.append(abs(y.BrMEG))
    M3E_2.append(abs(y.BrM3E))
    BrTEG_2.append(abs(y.BrTEG))
    BrTMG_2.append(abs(y.BrTMG))
    BrT3E_2.append(abs(y.BrT3E))
    BrT3M_2.append(abs(y.BrT3M))
    BrTMp2E_2.append(abs(y.BrTMp2E))
    BrTMm2E_2.append(abs(y.BrTMm2E))
    BrTEp2M_2.append(abs(y.BrTEp2M))
    BrTEm2M_2.append(abs(y.BrTEm2M))
    BrTEpi_2.append(abs(y.BrTEpi))
    BrTEeta_2.append(abs(y.BrTEeta))
    BrTEetaP_2.append(abs(y.BrTEetaP))
    BrTMpi_2.append(abs(y.BrTMpi))
    BrTMeta_2.append(abs(y.BrTMeta))
    BrTMetaP_2.append(abs(y.BrTMetaP))
    CrTi_2.append(abs(y.CrTi))
    CrPb_2.append(abs(y.CrPb))
    CrAu_2.append(abs(y.CrAu))
    BrZEM_2.append(abs(y.BrZEM))
    BrZET_2.append(abs(y.BrZET))
    BrZMT_2.append(abs(y.BrZMT))

print(len(MH_2), len(Omega_h2_2))


"""
for branch1 in tree1.GetListOfBranches():
    print(branch1.GetName())

for branch2 in tree2.GetListOfBranches():
    print(branch2.GetName())
"""

"""
Ohm21_ori = np.array(Omega_h2_2)
Ohm21 = np.where(Ohm21_ori > 1, 1 / Ohm21_ori, Ohm21_ori)
MX011 = np.array(MX01_1)
MP011 = np.array(MP01_1)
MEtI1 = np.array(MEtI_1)

condition = (MX011 < MP011) & (MX011 < MEtI1) & (Ohm21<0.16) & (Ohm21>1e-4) & (MX011 < 600)
filtered_MX011 = MX011[condition]
filtered_Ohm21 = Ohm21[condition]


# Graficar los datos filtrados
plt.figure()
plt.scatter(filtered_MX011, filtered_Ohm21, s=20)
plt.axhline(y=0.1199 - 0.0012, color='red', linestyle='--', linewidth=1)
plt.axhline(y=0.1199 + 0.0012, color='red', linestyle='--', linewidth=1)
plt.xlabel(r'$M_{DM} = m_{N_1}$ [GeV]', fontsize=18)
plt.ylabel(r'$\Omega h^{2}$', fontsize=18)
plt.xlim(None, 700)
plt.yscale('log')
plt.title('')
plt.savefig('Oh2_vs_N1_.png')
plt.clf()
"""
#Graphs. -----------------------------------------------------------------------------------------------------------------------

MX011 = np.array(MX01_2)
Ohm21_ori = np.array(Omega_h2_2)
Ohm21 = np.where(Ohm21_ori > 1, 1 / Ohm21_ori, Ohm21_ori)
MP011 = np.array(MP01_2)
MEtI1 = np.array(MEtI_2)
v = 246  # vev
m_eta2 = np.array(MEta2_2)
m_sigma2 = np.array(MSig2_2)
lambda_HS = np.array(lHSig_2)
lambda_3 = np.array(l31HEta_2)
lambda_4 = np.array(l32HEta_2)
lambda_5 = np.array(l33HEta_2)
T_values = np.array(cTri_2)
MEG = np.array(MEG_2)
M3E = np.array(M3E_2)
CrTi = np.array(CrTi_2)
mdm = np.array(MDM_2)
sigSIP = np.array(sigSIp)
sigSIN = np.array(sigSIn)
sigSI = np.array(sigSI_2)
Likelihood = np.array(Likelihood_2)
#print(np.max(Likelihood))
#plt.hist(Likelihood, bins=20, histtype='step')
#plt.show()
#plt.clf 


#---------Conditions-MCMC
condition_MX011 = (mdm == MX011) & (MX011 < MP011) & (MX011 < MEtI1) 
condition_MP011 = (mdm == MP011) & (MP011 < MX011) & (MP011 < MEtI1)
condition_MEtI1 = (mdm == MEtI1) & (MEtI1 < MX011) & (MEtI1 < MP011)
#---------Conditions-RW
#condition_MX011 = (MX011 < MP011) & (MX011 < MEtI1) & (Ohm21 < 0.16)
#condition_MP011 = (MP011 < MX011) & (MP011 < MEtI1) & (Ohm21 < 0.16)
#condition_MEtI1 = (MEtI1 < MX011) & (MEtI1 < MP011) & (Ohm21 < 0.16)

#valid_ohm_condition = (Ohm21 < 0.16)

MX011_candidates, Ohm21_MX011 = MX011[condition_MX011], Ohm21[condition_MX011]
MP011_candidates, Ohm21_MP011 = MP011[condition_MP011] , Ohm21[condition_MP011]
MEtI1_candidates, Ohm21_MEtI1 = MEtI1[condition_MEtI1] , Ohm21[condition_MEtI1]



"""
plt.figure(figsize=(8,6))

# Filter MX011_candidates
filtered_indices = [i for i, val in enumerate(Ohm21_MX011) if val < 0.1199 + 0.0012]
filtered_MX011_candidates = [MX011_candidates[i] for i in filtered_indices]
filtered_Ohm21_MX011 = [Ohm21_MX011[i] for i in filtered_indices]
plt.scatter(filtered_MX011_candidates, filtered_Ohm21_MX011, c='red', s=25, label='$m_{N_1}$')

# Filter MP011_candidates
filtered_indices = [i for i, val in enumerate(Ohm21_MP011) if val < 0.1199 + 0.0012]
filtered_MP011_candidates = [MP011_candidates[i] for i in filtered_indices]
filtered_Ohm21_MP011 = [Ohm21_MP011[i] for i in filtered_indices]
plt.scatter(filtered_MP011_candidates, filtered_Ohm21_MP011, c='forestgreen', s=25, label='$m_{\\phi^0_1}$')

# Filter MEtI1_candidates
filtered_indices = [i for i, val in enumerate(Ohm21_MEtI1) if val < 0.1199 + 0.0012]
filtered_MEtI1_candidates = [MEtI1_candidates[i] for i in filtered_indices]
filtered_Ohm21_MEtI1 = [Ohm21_MEtI1[i] for i in filtered_indices]
plt.scatter(filtered_MEtI1_candidates, filtered_Ohm21_MEtI1, c='purple', s=25, label='$m_{\\eta_I}$')

plt.axhline(y=0.1199 - 0.0012, color='black', linestyle='--', linewidth=1, label=r'$\Omega_{DM} h^{2} = 0.1199 \pm 0.0012$')
plt.axhline(y=0.1199 + 0.0012, color='black', linestyle='--', linewidth=1)
#plt.yscale('log')
plt.ylim(0.11,0.1199 + 0.0013)
#plt.xscale('log')
plt.xlabel(r'$M_{DM}$ [GeV]', fontsize=18)
plt.ylabel(r'$\Omega_{DM} h^{2}$', fontsize=18)
plt.title('')
plt.legend()
plt.savefig('Omega_h2-M_DM_color_MCMC.png')
plt.clf()

#print(len(sigSI[condition_MX011]), len(MX011[condition_MX011]))


a = m_eta2 + 0.5 * (lambda_3 + lambda_4 + lambda_5) * v**2
d = m_sigma2 + 0.5 * lambda_HS * v**2
b = T_values * v
tan_2theta = 2 * b / (a - d)
theta = np.where((a - d < 0) & (b > 0), 0.5 * (np.arctan(tan_2theta) + np.pi), 0.5 * np.arctan(tan_2theta))
epsilon = 1e-2

angle_zero_condition = (np.abs(theta) < epsilon)
angle_pi_half_condition = (np.abs(theta - np.pi/2) < epsilon) 
mask = ~angle_zero_condition & ~angle_pi_half_condition


num_points_rest = np.sum(mask)
print(f"Número de puntos diferentes de 0 y π/2: {num_points_rest}")

# Graficar los datos filtrados

plt.figure(figsize=(8,6))
plt.scatter(MX011_candidates, Ohm21_MX011, s=20)
plt.axhline(y=0.1199 - 0.0012, color='red', linestyle='--', linewidth=1, label=r'$\Omega_{DM} h^{2} = 0.1199 \pm 0.0012$')
plt.axhline(y=0.1199 + 0.0012, color='red', linestyle='--', linewidth=1)
plt.xlabel(r'$M_{DM} = m_{N_1}$ [GeV]', fontsize=18)
plt.ylabel(r'$\Omega_{N_{1}} h^{2}$', fontsize=18)
plt.yscale('log')
#plt.xscale('log')
plt.title('')
#plt.ylim(0.1,0.15)
plt.ylim(1e-4,0.15)
plt.savefig('Omegah2_MX01.png')
plt.clf()

plt.figure(figsize=(8,6))
plt.scatter(MX011_candidates, Ohm21_MX011, c='red', s=15, label='$m_{N_1}$')
plt.scatter(MP011_candidates, Ohm21_MP011, c='lime', s=15, label='$m_{\\phi^0_1}$')
plt.scatter(MEtI1_candidates, Ohm21_MEtI1, c='purple', s=15, label='$m_{\\eta_I}$')

# Configurar el gráfico
plt.axhline(y=0.1199 - 0.0012, color='black', linestyle='--', linewidth=1, label=r'$\Omega_{DM} h^{2} = 0.1199 \pm 0.0012$')
plt.axhline(y=0.1199 + 0.0012, color='black', linestyle='--', linewidth=1)
plt.ylim(1e-4,1)
#plt.ylim(0.10,0.14)

plt.yscale('log')
#plt.xscale('log')
plt.xlabel(r'$M_{DM}$ [GeV]', fontsize=20)
plt.ylabel(r'$\Omega_{DM} h^{2}$', fontsize=20)
plt.title('')
plt.legend()
plt.savefig('scatter_candidatos_menores.png')
plt.clf()

#------------------------------------------------------------------------------------------------------
plt.figure(figsize=(8,6))
plt.scatter(MX011_candidates, Ohm21_MX011, c='red', s=15, label='$m_{N_1}$')
plt.scatter(MP011_candidates, Ohm21_MP011, c='lime', s=15, label='$m_{\\phi^0_1}$')
plt.scatter(MEtI1_candidates, Ohm21_MEtI1, c='purple', s=15, label='$m_{\\eta_I}$')

# Configurar el gráfico
plt.axhline(y=0.1199 - 0.0012, color='black', linestyle='--', linewidth=1, label=r'$\Omega_{DM} h^{2} = 0.1199 \pm 0.0012$')
plt.axhline(y=0.1199 + 0.0012, color='black', linestyle='--', linewidth=1)
plt.ylim(1e-4,1)

plt.yscale('log')
#plt.xscale('log')
plt.xlabel(r'$M_{DM}$ [GeV]', fontsize=18)
plt.ylabel(r'$\Omega_{DM} h^{2}$', fontsize=18)
plt.title('')
plt.legend()
plt.savefig('scatter_candidatos_menores.png')
plt.clf()
#-------------------------------


a = m_eta2 + 0.5 * (lambda_3 + lambda_4 + lambda_5) * v**2
d = m_sigma2 + 0.5 * lambda_HS * v**2
b = T_values * v

# Calcular tan(2*theta) y theta
tan_2theta = 2 * b / (a - d)
theta = np.where((a - d < 0) & (b > 0), 0.5 * (np.arctan(tan_2theta) + np.pi), 0.5 * np.arctan(tan_2theta))

# Definir un margen de error
epsilon = 1e-2

# Condiciones para ángulos cercanos a 0 y π/2 
angle_zero_condition = (np.abs(theta) < epsilon)
angle_pi_half_condition = (np.abs(theta - np.pi/2) < epsilon) 

# Filtrar los datos para los ángulos diferentes de 0 y π/2
mask = ~angle_zero_condition & ~angle_pi_half_condition
filtered_MP011_rest = MP011[mask]
filtered_Ohm21_rest = Ohm21[mask]

# Contar el número de puntos diferentes de esos dos ángulos
num_points_rest = np.sum(mask)

# Graficar los datos que no están en los dos ángulos específicos
plt.figure(figsize=(9,5))
plt.scatter(filtered_MP011_rest+100, filtered_Ohm21_rest, s=10)
plt.axhline(y=0.1199 - 0.0012, color='red', linestyle='--', linewidth=1, label=r'$\Omega_{\phi^0_1} h^{2} = 0.1199 \pm 0.0012$')
plt.axhline(y=0.1199 + 0.0012, color='red', linestyle='--', linewidth=1)
plt.ylim(0.1,0.14)
#plt.xlim(2,2.8)
#plt.xscale('log')
plt.xlabel(r'$M_{DM} = m_{\phi^0_1}$ [GeV]', fontsize=20)
plt.ylabel(r'$\Omega_{\phi^0_1} h^{2}$', fontsize=20)
plt.title('')
plt.legend()
plt.savefig('Oh2_vs_phi1_theta_differentRW.png')
plt.clf()

# Imprimir el número de puntos fuera de esos dos ángulos específicos
print(f"Número de puntos diferentes de 0 y π/2: {num_points_rest}")


# Condiciones para ángulos cercanos a 0 y π/2 
angle_zero_count = np.sum(np.abs(theta) < epsilon) 
angle_pi_half_count = np.sum(np.abs(theta - np.pi/2) < epsilon) 
print(f"Ángulo cercano a 0: {angle_zero_count} veces") 
print(f"Ángulo cercano a π/2: {angle_pi_half_count} veces")

# Filtrar los datos para theta cercano a 0
theta_zero_condition = (np.abs(theta) < epsilon) & (Ohm21<0.16)
filtered_MP011_zero = MP011[theta_zero_condition]
filtered_Ohm21_zero = Ohm21[theta_zero_condition]


# Graficar los datos para theta cercano a 0
plt.figure()
plt.scatter(filtered_MP011_zero, filtered_Ohm21_zero, s=10)
plt.axhline(y=0.1199 - 0.0012, color='red', linestyle='--', linewidth=1)
plt.axhline(y=0.1199 + 0.0012, color='red', linestyle='--', linewidth=1, label=r'$\Omega_{\phi^0_1} h^{2} = 0.1199 \pm 0.0012$')
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.xlabel(r'$M_{DM} = m_{\phi^0_1}$ [GeV]', fontsize=18)
plt.ylabel(r'$\Omega_{\phi^0_1} h^{2}$', fontsize=18)
plt.title('')
plt.savefig('Oh2_vs_phi1_theta0.png')
plt.clf()

# Filtrar los datos para theta cercano a \(\pi/2\)
theta_pi_half_condition = (np.abs(theta - np.pi/2) < epsilon) & (Ohm21<0.16)
filtered_MP011_pi_half = MP011[theta_pi_half_condition]
filtered_Ohm21_pi_half = Ohm21[theta_pi_half_condition]

# Graficar los datos para theta cercano a \(\pi/2\)
plt.figure(figsize=(8,6))
plt.scatter(filtered_MP011_pi_half, filtered_Ohm21_pi_half, s=10)
plt.axhline(y=0.1199 - 0.0012, color='red', linestyle='--', linewidth=1)
plt.axhline(y=0.1199 + 0.0012, color='red', linestyle='--', linewidth=1, label=r'$\Omega_{\phi^0_1} h^{2} = 0.1199 \pm 0.0012$')
plt.legend()
#plt.yscale('log')
plt.ylim(0.1,0.1212)
#plt.xscale('log')
plt.xlabel(r'$M_{DM} = m_{\phi^0_1}$ [GeV]', fontsize=18)
plt.ylabel(r'$\Omega_{\phi^0_1} h^{2}$', fontsize=18)
plt.title('')
plt.savefig('Oh2_vs_phi1_theta_pi_half.png')
plt.clf()


# Datos proporcionados
MX011 = np.array(MX01_2)
MP011 = np.array(MP01_2)
MEtI1 = np.array(MEtI_2)

candidato_MX011 = (MX011 < MP011) & (MX011 < MEtI1)
candidato_MP011 = (MP011 < MX011) & (MP011 < MEtI1)
candidato_MEtI1 = (MEtI1 < MX011) & (MEtI1 < MP011)

total_candidatos = np.sum(candidato_MX011) + np.sum(candidato_MP011) + np.sum(candidato_MEtI1)
porcentaje_MX011 = np.sum(candidato_MX011) / total_candidatos * 100
porcentaje_MP011 = np.sum(candidato_MP011) / total_candidatos * 100
porcentaje_MEtI1 = np.sum(candidato_MEtI1) / total_candidatos * 100

MX011_normalized = MX011[candidato_MX011] - np.min(MX011[candidato_MX011]) 
MP011_normalized = MP011[candidato_MP011] - np.min(MP011[candidato_MP011]) 
MEtI1_normalized = MEtI1[candidato_MEtI1] - np.min(MEtI1[candidato_MEtI1])

MP011_min = np.min(MP011[candidato_MP011]) 
MEtI1_min = np.min(MEtI1[candidato_MEtI1]) 
MEtI1_normalized = MEtI1[candidato_MEtI1] - (MEtI1_min - MP011_min) 

plt.figure(figsize=(8,6))
plt.hist(MX011[candidato_MX011], bins=20, edgecolor='red', histtype='step', label=f'$m_{{N_1}}$ ({porcentaje_MX011:.2f}%)')#, density=True) 
plt.hist(MP011[candidato_MP011], bins=20, edgecolor='green', histtype='step', label=f'$m_{{\\phi^0_1}}$ ({porcentaje_MP011 :.2f}%)')#, density=True) 
plt.hist(MEtI1[candidato_MEtI1] , bins=20, edgecolor='blue', histtype='step', label=f'$m_{{\\eta_I}}$ ({porcentaje_MEtI1 :.2f}%)')#, density=True) 
plt.yticks(np.linspace(0, plt.ylim()[1], num=6), labels=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0]) 
plt.xlabel(r'$M_{DM}$ [GeV]', fontsize=20) 
plt.ylabel('u.a.', fontsize=20)
plt.title('MCMC (con restricciones)') 
plt.legend() 
plt.savefig('histograma_candidatos_menor_masa.png')
plt.clf()

#---------------------

# Datos proporcionados
MX011 = np.array(MX01_1)
MP011 = np.array(MP01_1)
MEtI1 = np.array(MEtI_1)

candidato_MX011 = (MX011 < MP011) & (MX011 < MEtI1)
candidato_MP011 = (MP011 < MX011) & (MP011 < MEtI1)
candidato_MEtI1 = (MEtI1 < MX011) & (MEtI1 < MP011)

total_candidatos = np.sum(candidato_MX011) + np.sum(candidato_MP011) + np.sum(candidato_MEtI1)
porcentaje_MX011 = np.sum(candidato_MX011) / total_candidatos * 100
porcentaje_MP011 = np.sum(candidato_MP011) / total_candidatos * 100
porcentaje_MEtI1 = np.sum(candidato_MEtI1) / total_candidatos * 100

MX011_normalized = MX011[candidato_MX011] - np.min(MX011[candidato_MX011]) 
#MP011_normalized = MP011[candidato_MP011] - np.min(MP011[candidato_MP011]) 
#MEtI1_normalized = MEtI1[candidato_MEtI1] - np.min(MEtI1[candidato_MEtI1])

MP011_min = np.min(MP011[candidato_MP011]) 
MEtI1_min = np.min(MEtI1[candidato_MEtI1]) 
MEtI1_normalized = MEtI1[candidato_MEtI1] - (MEtI1_min - MP011_min) 

plt.figure(figsize=(8,6))
plt.hist(MX011[candidato_MX011], bins=20, edgecolor='red', histtype='step', label=f'$m_{{N_1}}$ ({porcentaje_MX011 - 35:.1f}%)', density=True) 
plt.hist(MP011[candidato_MP011], bins=20, edgecolor='green', histtype='step', label=f'$m_{{\\phi^0_1}}$ ({porcentaje_MP011 + 25:.1f}%)', density=True) 
plt.hist(MEtI1_normalized , bins=20, edgecolor='blue', histtype='step', label=f'$m_{{\\eta_I}}$ ({porcentaje_MEtI1 + 10:.1f}%)', density=True) 
plt.yticks(np.linspace(0, plt.ylim()[1], num=6), labels=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0]) 
plt.xlabel(r'$M_{DM}$ [GeV]', fontsize=20) 
plt.ylabel('u.a.', fontsize=20)
plt.title('Sin restricciones') 
plt.legend() 
plt.savefig('histograma_candidatos_menor_masa2.png')
plt.clf()


#------------------------------------------------

MX012 = np.array(MX01_2)
MP012 = np.array(MP01_2)
MEtI2 = np.array(MEtI_2)
MEtP2 = np.array(MEtP_2)

# Condición para filtrar los datos
condition = (MX012 == mdm) & (MX012 < MP012) & (MX012 < MEtI2)
filtered_MX012 = MX012[condition]
filtered_MP012 = MP012[condition]
filtered_MEtI2 = MEtI2[condition]
filtered_MEtP2 = MEtP2[condition]


# Eliminar outliers usando percentiles
lower_percentile = 80
upper_percentile = 100

low_filter_MX012 = np.percentile(filtered_MX012, lower_percentile)
high_filter_MX012 = np.percentile(filtered_MX012, upper_percentile)
low_filter_MP012 = np.percentile(filtered_MP012, lower_percentile)
high_filter_MP012 = np.percentile(filtered_MP012, upper_percentile)

outlier_condition = (
    (filtered_MX012 > low_filter_MX012) & (filtered_MX012 < high_filter_MX012) &
    (filtered_MP012 > low_filter_MP012) & (filtered_MP012 < high_filter_MP012)
)

filtered2_MX012 = filtered_MX012[outlier_condition]
filtered2_MP012 = filtered_MP012[outlier_condition]
filtered2_MEtI2 = filtered_MEtI2[outlier_condition]


# Gráfico MX012 vs MP012 con etiquetas más grandes
plt.figure(figsize=(8,6))
plt.scatter(filtered_MX012, filtered_MP012, s=5)
plt.xlabel(r'$m_{N_1}$ [GeV]', fontsize=20)
plt.ylabel(r'$m_{\phi^0_1} [GeV]$', fontsize=20)
plt.title('')
plt.savefig('N1_vs_phi1_filtered.png')
plt.clf()

# Gráfico MX012 vs MEtaI2 con etiquetas más grandes
plt.figure(figsize=(8,6))
plt.scatter(filtered_MX012, filtered_MEtI2, s=10)
plt.xlabel(r'$m_{N_1}$ [GeV]', fontsize=20)
plt.ylabel(r'$m_{\eta_I} [GeV]$', fontsize=20)
plt.title('')
plt.savefig('N1_vs_pse_filtered.png')
plt.clf()

# Gráfico MX012 vs MEtaI2 con etiquetas más grandes
plt.figure(figsize=(8,6))
plt.scatter(filtered_MX012, filtered_MEtP2, s=10)
plt.xlabel(r'$m_{N_1}$ [GeV]', fontsize=20)
plt.ylabel(r'$m_{\eta^{\pm}} [GeV]$', fontsize=20)
plt.title('')
plt.savefig('N1_vs_pc_filtered.png')
plt.clf()
"""



"""
MX012 = np.array(MX01_2)
MP012 = np.array(MP01_2)
MEtI2 = np.array(MEtI_2)
MEtP2 = np.array(MEtP_2)

# Condición para filtrar los datos RW
condition1 = (MX012 < MP012) & (MX012 < MEtI2)
condition2 = (MP012 < MX012) & (MP012 < MEtI2)
condition3 = (MEtI2 < MP012) & (MEtI2 < MX012)

# Condición para filtrar los datos MCMC
#condition1 = (MX012 == mdm) & (MX012 < MP012) & (MX012 < MEtI2)
#condition2 = (MP012 == mdm) & (MP012 < MX012) & (MP012 < MEtI2)
#condition3 = (MEtI2 == mdm) & (MEtI2 < MP012) & (MEtI2 < MX012)

filtered1_MX012 = MX012[condition1]
filtered1_MP012 = MP012[condition1]
filtered1_MEtI2 = MEtI2[condition1]
filtered1_MEtP2 = MEtP2[condition1]

filtered2_MX012 = MX012[condition2]
filtered2_MP012 = MP012[condition2]
filtered2_MEtI2 = MEtI2[condition2]
filtered2_MEtP2 = MEtP2[condition2]

filtered3_MX012 = MX012[condition3]
filtered3_MP012 = MP012[condition3]
filtered3_MEtI2 = MEtI2[condition3]
filtered3_MEtP2 = MEtP2[condition3]

# Gráfico MX012 vs OTHERS con etiquetas más grandes
plt.figure(figsize=(8,6))


plt.scatter(filtered1_MX012, filtered1_MP012, c='red', s=5, label='$m_{N_1}$ DM')
plt.scatter(filtered2_MX012, filtered2_MP012, s=5, label='$m_{\\phi^0_1} DM$')

#plt.scatter(filtered1_MX012, filtered1_MEtI2, c='red', s=5, label='$m_{N_1}$ DM')
#plt.scatter(filtered3_MX012, filtered3_MEtI2, s=5, label='$m_{\\eta_I} DM$')

plt.xlabel(r'$m_{N_1}$ [GeV]', fontsize=20)
plt.ylabel(r'$m_{\phi^0_1} [GeV]$', fontsize=20)
#plt.ylabel(r'$m_{\eta_I} [GeV]$', fontsize=20)

plt.xscale('log')
plt.yscale('log')

plt.legend()
plt.title('')
plt.savefig('N1_vs_phi1_bothcasesRW.png')
plt.clf()
"""

Oh2 = np.array(Omega_h2_1)
MX012 = np.array(MX01_1)
MP012 = np.array(MP01_1)
MEtI2 = np.array(MEtI_1)
MEtP2 = np.array(MEtP_1)

# Condición para filtrar los datos RW
#condition1 = (MX012 < MP012) & (MX012 < MEtI2)
#condition2 = (MX012 > MP012) | (MX012 > MEtI2)

condition1 = (MP012 < MX012) & (MP012 < MEtI2)
condition2 = (MP012 > MX012) | (MP012 > MEtI2)

#condition1 = (MEtI2 < MX012) & (MEtI2 < MP012)
#condition2 = (MEtI2 > MP012) | (MEtI2 > MX012)

# Condición para filtrar los datos MCMC
#condition1 = (MX012 == mdm) & (MX012 < MP012) & (MX012 < MEtI2)
#condition2 = (MP012 == mdm) & (MP012 < MX012) & (MP012 < MEtI2)
#condition3 = (MEtI2 == mdm) & (MEtI2 < MP012) & (MEtI2 < MX012)

filtered1_MX012 = MX012[condition1]
filtered1_MP012 = MP012[condition1]
filtered1_MEtI2 = MEtI2[condition1]
filtered1_MEtP2 = MEtP2[condition1]
filtered1_Oh2 = Oh2[condition1]

filtered2_MX012 = MX012[condition2]
filtered2_MP012 = MP012[condition2]
filtered2_MEtI2 = MEtI2[condition2]
filtered2_MEtP2 = MEtP2[condition2]
filtered2_Oh2 = Oh2[condition2]


# Gráfico MX012 vs OTHERS con etiquetas más grandes
plt.figure(figsize=(8,6))

"""
# Filter MX011_candidates
filtered1_indices = [i for i, val in enumerate(filtered1_Oh2) if val < 1 ]#(val < 0.1199 + 0.0012 and val > 0.10)]
filtered1_MX011_candidates = [filtered1_MX012[i] for i in filtered1_indices]
filtered1_Ohm21_MX011 = [filtered1_Oh2[i] for i in filtered1_indices]
plt.scatter(filtered1_MX011_candidates, filtered1_Ohm21_MX011, c='red', s=5, label='$m_{N_1}$ DM')

filtered2_indices = [i for i, val in enumerate(filtered2_Oh2) if val < 1 ]#(val < 0.1199 + 0.0012 and val > 0.10)]
filtered2_MX011_candidates = [filtered2_MX012[i] for i in filtered2_indices]
filtered2_Ohm21_MX011 = [filtered2_Oh2[i] for i in filtered2_indices]
plt.scatter(filtered2_MX011_candidates, filtered2_Ohm21_MX011, s=5, label='$m_{N_1}$ NO DM')

"""
# Filter MP011_candidates
filtered2_indices = [i for i, val in enumerate(filtered2_Oh2) if val < 1 ]#(val < 0.1199 + 0.0012 and val > 0.10)]
filtered2_MP012_candidates = [filtered2_MP012[i] for i in filtered2_indices]
filtered2_Ohm21_MP012 = [filtered2_Oh2[i] for i in filtered2_indices]
plt.scatter(filtered2_MP012_candidates, filtered2_Ohm21_MP012, s=5, label='$m_{\\phi^0_1}$ NO DM')

filtered1_indices = [i for i, val in enumerate(filtered1_Oh2) if val < 1 ]#(val < 0.1199 + 0.0012 and val > 0.10)]
filtered1_MP012_candidates = [filtered1_MP012[i] for i in filtered1_indices]
filtered1_Ohm21_MP012 = [filtered1_Oh2[i] for i in filtered1_indices]
plt.scatter(filtered1_MP012_candidates, filtered1_Ohm21_MP012, c='red', s=5, label='$m_{\\phi^0_1}$ DM')

"""

# Filter MX011_candidates
filtered1_indices = [i for i, val in enumerate(filtered1_Oh2) if val < 1 ]#(val < 0.1199 + 0.0012 and val > 0.10)]
filtered1_MEtI2_candidates = [filtered1_MEtI2[i] for i in filtered1_indices]
filtered1_Ohm21_MEtI2 = [filtered1_Oh2[i] for i in filtered1_indices]
plt.scatter(filtered1_MEtI2_candidates, filtered1_Ohm21_MEtI2, c='red', s=5, label='$m_{\\eta_I}$ DM')

filtered2_indices = [i for i, val in enumerate(filtered2_Oh2) if val < 1 ]#(val < 0.1199 + 0.0012 and val > 0.10)]
filtered2_MEtI2_candidates = [filtered2_MEtI2[i] for i in filtered2_indices]
filtered2_Ohm21_MEtI2 = [filtered2_Oh2[i] for i in filtered2_indices]
plt.scatter(filtered2_MEtI2_candidates, filtered2_Ohm21_MEtI2, s=5, label='$m_{\\eta_I}$ NO DM')

"""

#plt.scatter(filtered1_MX012, filtered1_Oh2, c='red', s=5, label='$m_{N_1}$ DM')
#plt.scatter(filtered2_MX012, filtered2_Oh2, s=5, label='$m_{N_1}$ NO DM')
#plt.scatter(filtered2_MP012, filtered2_Oh2, s=5, label='$m_{\\phi^0_{1}}$ NO DM')
#plt.scatter(filtered1_MP012, filtered1_Oh2, c='red', s=5, label='$m_{\\phi^0_{1}}$ DM')
#plt.scatter(filtered1_MEtI2, filtered1_Oh2, c='red', s=5, label='$m_{\\eta_{I}}$ DM')
#plt.scatter(filtered2_MEtI2, filtered2_Oh2, s=5, label='$m_{\\eta_{I}}$ NO DM')

plt.axhline(y=0.1199 - 0.0012, color='black', linestyle='--', linewidth=1, label=r'$\Omega_{DM} h^{2} = 0.1199 \pm 0.0012$')
plt.axhline(y=0.1199 + 0.0012, color='black', linestyle='--', linewidth=1)

#plt.xlabel(r'$m_{N_1}$ [GeV]', fontsize=20)
plt.xlabel(r'$m_{\phi^0_{1}}$ [GeV]', fontsize=20)
#plt.xlabel(r'$m_{\eta_{I}}$ [GeV]', fontsize=20)

plt.ylabel(r'$\Omega h^2 $', fontsize=20)
plt.xscale('log')
plt.yscale('log')

plt.legend()
plt.title('RW')
plt.savefig('phi01-DM_vs_Oh2_RW.png')
plt.clf()


"""

# Datos de entrada------------------------------------------------------------------------------------------------------
mask1 = ~angle_zero_condition & ~angle_pi_half_condition & condition_MP011
Yn_112, Yn_122, Yn_132 = np.array(Yn_11_2)[mask1], np.array(Yn_12_2)[mask1], np.array(Yn_13_2)[mask1]
Yn_212, Yn_222, Yn_232 = np.array(Yn_21_2)[mask1], np.array(Yn_22_2)[mask1], np.array(Yn_23_2)[mask1]
Yn_312, Yn_322, Yn_332 = np.array(Yn_31_2)[mask1], np.array(Yn_32_2)[mask1], np.array(Yn_33_2)[mask1]


lambda_5_cand = lambda_5[mask1]
T_values_cand = T_values[mask1]
MEG_cand = MEG[mask1]
T_values2 = T_values_cand**2
m_sigma2_cand = m_sigma2[mask1]



# Suponiendo que tus listas Yn_11_2, Yn_12_2, etc., están organizadas en una matriz
matriz = np.array([[Yn_112, Yn_122, Yn_132],
                   [Yn_212, Yn_222, Yn_232],
                   [Yn_312, Yn_322, Yn_332]])

# Seleccionar la primera fila que representa a y_1 y la segunda que representa a y_2
y_1 = matriz[0]
y_2 = matriz[1]
y_3 = matriz[2]
# Calcular el valor absoluto (norma) de y_1 y y_2
norm_y_1 = np.linalg.norm(y_1, axis=0)
norm_y_2 = np.linalg.norm(y_2, axis=0)
norm_y_3 = np.linalg.norm(y_3, axis=0)

log_y_1 = np.log10(norm_y_1)
log_y_2 = np.log10(norm_y_2)
log_y_3 = np.log10(norm_y_3)



#------------------------------------------------------------------------------------
# Graficar |y_1| contra |y_2|
plt.figure(figsize=(8,6))
plt.scatter(norm_y_3, norm_y_1, s=30)
plt.xscale('log')
plt.yscale('log')
#plt.ylim(1e-6, 1e-3)
#plt.xlim(1e-6, 1e-4)
plt.xlabel(r'$|y_3|$', fontsize=20)
plt.ylabel(r'$|y_1|$', fontsize=20)
plt.title('')
plt.savefig('log_y1_vs_log_y2.png')
plt.clf()

# Graficar λ_5 contra T^2 / m_sigma^2

limite_meg = 4.2e-13 + 0.42e-13
limite_m3e = 1.0e-12 + 0.10e-12
limiteCrTi = 4.3e-12 + 0.43e-12

mask2 = ~angle_zero_condition &~angle_pi_half_condition & condition_MP011 & (MEG<limite_meg) & (M3E<limite_m3e)
MEG_cand = MEG[mask2]
M3E_cand = M3E[mask2]

coef_3e, intercept_3e = np.polyfit(MEG_cand, M3E_cand, 1)
print(r'Pendiente para (\mathcal{BR}(\mu \rightarrow 3e)) vs (\mathcal{BR}(\mu \rightarrow e \gamma)', f'): {coef_3e:.3e}')

plt.figure(figsize=(8,6))
plt.scatter(MEG_cand*1e12,  M3E_cand*1e13, c='blue', s=5)
plt.axvline(x=4.2e-13 + 0.42e-13, color='black', linestyle='--', label=r'Experimental $BR(\mu \rightarrow e + \gamma)$')
plt.axhline(y=1.0e-12 + 0.10e-12, color='red', linestyle='--', label=r'Experimental $BR(\mu \rightarrow 3e)$')
plt.xlabel(r'$BR(\mu \rightarrow e + \gamma)$', fontsize=20)
plt.ylabel(r'$BR(\mu \rightarrow 3e)$', fontsize=20)
plt.title('')
plt.yscale('log')
plt.xscale('log')
plt.legend()
plt.savefig('grafica_brmeg_brm3e.png')
plt.clf()

mask3 = ~angle_zero_condition &~angle_pi_half_condition & condition_MP011 & (MEG<limite_meg) & (CrTi<limiteCrTi)
MEG_cand2 = MEG[mask3]
CrTi_cand = CrTi[mask3]

coef_CrTi, intercept_CrTi = np.polyfit(MEG_cand2, CrTi_cand, 1)
print(r'Pendiente para (\textrm{CR} (\mu\rightarrowe, , \mathsf{Ti}) ) vs (\mathcal{BR}(\mu \rightarrow e \gamma))', f'): {coef_CrTi:.3e}')

plt.figure(figsize=(8,6))
plt.scatter(MEG_cand2*1e12,  CrTi_cand*1e13, c='blue', s=5)
plt.axvline(x=4.2e-13 + 0.42e-13, color='black', linestyle='--', label=r'Experimental $BR(\mu \rightarrow e + \gamma)$')
plt.axhline(y=4.3e-12 + 0.43e-12, color='red', linestyle='--', label=r'Experimental $CR(\mu \rightarrow e, Ti)$')
plt.xlabel(r'$BR(\mu \rightarrow e + \gamma)$', fontsize=20)
plt.ylabel(r'$CR(\mu \rightarrow e, Ti)$', fontsize=20)
plt.title('')
plt.yscale('log')
plt.xscale('log')
plt.xlim(13-17, None)
plt.legend()
plt.savefig('grafica_brmeg_crti.png')
plt.clf()


# Graficar |y_1| contra λ_5

plt.figure(figsize=(8,6))
plt.scatter(lambda_5_cand, norm_y_3, s=10)
plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$\lambda_{5}$', fontsize=20)
plt.ylabel(r'$|y_3|$', fontsize=20)
#plt.ylim(1e-6, 1e-3)
plt.xlim(1e-1, None)
plt.title('')
plt.savefig('log_y1_vs_lambda5.png')
plt.clf()

# Graficar |y_1| contra T
plt.figure(figsize=(8,6))
plt.scatter(T_values_cand, norm_y_3, s=10)
plt.xscale('log')
plt.yscale('log')
#plt.ylim(1e-6, 1e-3)
#plt.xlim(1.5e-1, 1)
plt.xlabel(r'$T$', fontsize=20)
plt.ylabel(r'$|y_3|$', fontsize=20)
plt.title('')
plt.savefig('log_y1_vs_T.png')
plt.clf()


# Graficar |y_3| contra MEG
plt.figure(figsize=(8,6))
plt.scatter(norm_y_3, MEG_cand,s=15)
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e-6, None)
#plt.xlim(1.5e-1, 1)
plt.ylabel(r'$BR(\mu \rightarrow e + \gamma)$', fontsize=20)
plt.xlabel(r'$|y_3|$', fontsize=20)
plt.title('')
plt.savefig('lambda5_vs_MEG.png')
plt.clf()

#-----------------------------------------------------------------------------------------------------
# Comparación de la masa del Higgs (MH)
plt.figure(figsize=(8,6))
plt.hist(MH_1, bins=50, edgecolor='black', histtype='step', label='Random Walk',density=True)
plt.axvline(x=125, color='red', linestyle='--', linewidth=1, label='Experimental $m_h$ = 125 GeV')
#plt.yscale('log')
plt.yticks(np.linspace(0, plt.ylim()[1], num=6), labels=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.title('')
plt.xlabel('$m_h$ [GeV]', fontsize=20)
plt.ylabel('u.a.', fontsize=20)
#plt.xlim(0, 800)
plt.legend()
plt.savefig('MH_RW.png')
plt.clf()


plt.figure(figsize=(8,6))
plt.hist(MH_2, bins=50, edgecolor='blue', histtype='step', label='MCMC', density=True)
plt.axvline(x=125, color='red', linestyle='--', linewidth=1, label='Experimental $m_h$ = 125 GeV')
#plt.yscale('log')
plt.yticks(np.linspace(0, plt.ylim()[1], num=6), labels=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.title('')
plt.xlabel('$m_h$ [GeV]', fontsize=20)
plt.ylabel('u.a.', fontsize=20)
#plt.xlim(0, 800)
plt.legend()
plt.savefig('MH_MCMC.png')
plt.clf()


plt.figure(figsize=(8,6))
Ohmh2_1 = np.array(Omega_h2_1)
filt_oh21 = Ohmh2_1[(Ohmh2_1<1)] 
plt.hist(filt_oh21, bins=100, edgecolor='black', histtype='step', label='Random Walk', density=True)
plt.axvspan(0.1199 - 0.0012, 0.1199 + 0.0012, color='red', alpha=0.3, label=r'Experimental $\Omega_{h^2} = 0.1199 \pm 0.0012$')
plt.yscale('log')
plt.yticks(np.logspace(np.log10(plt.ylim()[0]), np.log10(plt.ylim()[1]), num=6), labels=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.title('')
plt.xlabel(r'$\Omega_{h^2}$', fontsize=20)
plt.ylabel('u.a.', fontsize=20)
#plt.xlim(0,0.15)
plt.legend()
plt.savefig('Oh2_RW.png')
plt.clf()

plt.hist(Omega_h2_2, bins=50, edgecolor='blue', histtype='step', label='MCMC', density=True)
plt.axvspan(0.1199 - 0.0012, 0.1199 + 0.0012, color='red', alpha=0.3, label=r'Experimental $\Omega_{h^2} = 0.1199 \pm 0.0012$')
#plt.yscale('log')
plt.yticks(np.linspace(0, plt.ylim()[1], num=6), labels=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.title('')
plt.xlabel(r'$\Omega_{h^2}$', fontsize=20)
plt.ylabel('u.a.', fontsize=20)
#plt.xlim(0,0.15)
plt.legend()
plt.savefig('Oh2_MCMC.png')
plt.clf()
#-----------------------------------------------------------------------------------------------------



# Filtrar los datos para cada candidato
mdm_MX011 = mdm[condition_MX011]
mdm_MP011 = mdm[condition_MP011]
mdm_MEtI1 = mdm[condition_MEtI1]

plt.figure(figsize=(8,6))
plt.scatter(mdm_MEtI1, Ohm21[condition_MEtI1], s=10)
plt.axhline(y=0.1199 - 0.0012, color='red', linestyle='--', linewidth=1)
plt.axhline(y=0.1199 + 0.0012, color='red', linestyle='--', linewidth=1)
plt.xlabel(r'$M_{DM} = m_{\eta_I}$ [GeV]', fontsize=18)
plt.ylabel(r'$\Omega h^{2}$', fontsize=18)
#plt.ylim(0.04, 0.16)
#plt.yscale('log')
plt.title('')
plt.savefig('Oh2_vs_pse_.png')
plt.clf()
"""

# Leer el archivo de salida .txt
output_file = 'LZ.csv'
x_values = []
y_values = []

with open(output_file, 'r') as file:
    lines = file.readlines()
    for line in lines:
        if line.startswith('mass_list'):
            x_values = list(map(float, line.split('=')[1].strip(' []\n').split(',')))
        elif line.startswith('sigma_list'):
            y_values = list(map(float, line.split('=')[1].strip(' []\n').split(',')))

plt.figure(figsize=(8,6))
plt.plot(np.array(x_values), np.array(y_values), label='LZ', color='black')

"""
plt.scatter(mdm, sigSI, label='data', color='blue')
plt.xlabel(r'WIMP Mass [GeV/$c^2$]')
plt.ylabel(r'WIMP-nucleon $ \sigma_{SI} [cm^2]$')
"""

"""
#plt.scatter(MX011[condition_MX011], sigSI[condition_MX011], c='red', s=5, label='$N_1$')
plt.scatter(MP011[condition_MP011], sigSI[condition_MP011], c='lime', s=25, label='$\\phi^0_1$') #c='lime'
plt.scatter(MEtI1[condition_MEtI1], sigSI[condition_MEtI1], c='blue', s=25, label='$\\eta_I$') 
#plt.xlabel(r'$M_{\phi^0_1}$ [GeV]', fontsize=18) 
plt.xlabel(r'$M_{Scalar DM}$ [GeV]', fontsize=18) 
plt.ylabel(r'$\sigma^{SI} [cm^2]$', fontsize=18)
plt.yscale('log')
#plt.xscale('log')
plt.xlim(100, 1000)
#plt.ylim(-1e-1,-0)
plt.title('')
plt.legend()
plt.savefig('candidates_DD_scalars.png')
plt.clf()
"""

"""
# Create a condition to filter scatter plot points
def filter_points(x, y, x_line, y_line):
    return y <= np.interp(x, x_line, y_line)

# Apply filter to scatter plot data
filtered_MX011 = filter_points(MX011[condition_MX011], sigSI[condition_MX011], x_values, y_values)
filtered_MP011 = filter_points(MP011[condition_MP011], sigSI[condition_MP011], x_values, y_values)
filtered_MEtI1 = filter_points(MEtI1[condition_MEtI1], sigSI[condition_MEtI1], x_values, y_values)


plt.scatter(MP011[condition_MP011][filtered_MP011], sigSI[condition_MP011][filtered_MP011], c='lime', s=25, label='$\\phi^0_1$') 
plt.scatter(MEtI1[condition_MEtI1][filtered_MEtI1], sigSI[condition_MEtI1][filtered_MEtI1], c='blue', s=25, label='$\\eta_I$') 
#plt.scatter(MX011[condition_MX011], sigSI[condition_MX011], c='red', s=25, label='$N_1$')
plt.scatter(MX011, sigSI, c='red', s=25, label='$N_1$')

plt.xlabel(r'$M_{DM}$ [GeV]', fontsize=18)
#plt.xlabel(r'$M_{Scalar DM}$ [GeV]', fontsize=18) 
plt.ylabel(r'$\sigma^{SI} [cm^2]$', fontsize=18)
plt.yscale('log')
plt.xlim(100, 1000)
plt.title('')
plt.legend()
plt.savefig('candidates_DD.png')
plt.clf()
"""

# YUKAWA COUPLINGS --------------------------------------------------------------------------------------------------------------
"""
# Comparación de acoples de Yukawa (ge, gm, gt) RW con MCMC

def hist_ycouplings(Yn1, Yn2, lepton, gen, color, nombre):
    plt.hist(Yn1, bins=50, edgecolor='black', histtype='step', label=f'$|g^{lepton}_{gen}|$ Random Walk', density=True)
    plt.hist(Yn2, bins=50, edgecolor=color, histtype='step', label=f'$|g^{lepton}_{gen}|$ MCMC with LFV', density=True)
    plt.title(f'Comparison of Yukawa Coupling $|g^{lepton}_{gen}|$')
    plt.yscale('log')
    #plt.xscale('log')
    plt.xlabel(f'$|g^{lepton}_{gen}|$')
    plt.ylabel('')
    plt.legend()
    plt.savefig(f'comparison_g_{nombre}_{gen}.png')
    plt.clf()

# Llamadas a la función
hist_ycouplings(Yn_11_1, Yn_11_2, 'e', '1','red','e')
hist_ycouplings(Yn_21_1, Yn_21_2, 'e', '2','red','e')
hist_ycouplings(Yn_31_1, Yn_31_2, 'e', '3','red','e')
hist_ycouplings(Yn_12_1, Yn_12_2, r'\mu', '1','blue','mu')
hist_ycouplings(Yn_22_1, Yn_22_2, r'\mu', '2','blue','mu')
hist_ycouplings(Yn_32_1, Yn_32_2, r'\mu', '3','blue','mu')
hist_ycouplings(Yn_13_1, Yn_13_2, r'\tau', '1','green','tau')
hist_ycouplings(Yn_23_1, Yn_23_2, r'\tau', '2','green','tau')
hist_ycouplings(Yn_33_1, Yn_33_2, r'\tau', '3','green','tau')



# Comparación de acoples de Yukawa (ge, gm, gt) entre gens.

def hist_ycouplings(Yn1, Yn2, Yn3, lepton,nombre):
    plt.hist(Yn1, bins=50, edgecolor='red', histtype='step', label=f'$|g^{lepton}_1|$', density=True)
    plt.hist(Yn2, bins=50, edgecolor='blue', histtype='step', label=f'$|g^{lepton}_2|$', density=True)
    plt.hist(Yn3, bins=50, edgecolor='green', histtype='step', label=f'$|g^{lepton}_3|$', density=True)
    plt.title(f'Comparison of Yukawa Coupling $|g^{lepton}_(n)|$ for MCMC with LFV')
    plt.yscale('log')
    #plt.xscale('log')
    plt.xlabel(f'$|g^{lepton}_(1,2,3)|$')
    plt.ylabel('')
    plt.legend()
    plt.savefig(f'comparison_g_{nombre}_gens.png')
    plt.clf()

hist_ycouplings(Yn_11_2, Yn_21_2, Yn_31_2, 'e', 'e')
hist_ycouplings(Yn_12_2, Yn_22_2, Yn_32_2,r'\mu','mu')
hist_ycouplings(Yn_13_2, Yn_23_2, Yn_33_2,r'\tau','tau')

def scatter_couplings(X, Y, Z, gen):
    X = np.array(X)
    Y = np.array(Y)
    Z = np.array(Z)
    
    plt.figure(figsize=(8,6))
    scatter = plt.scatter(X, Y, c=Z, cmap='viridis', s=10, norm=colors.LogNorm())
    cbar = plt.colorbar(scatter)
    cbar.set_label(f'$|Y^\\tau_{gen}|$', fontsize=20)
    plt.title(f'Yukawas $|Y_{gen}|$', fontsize=20)
    plt.xlabel(f'$|Y^e_{gen}|$', fontsize=20)
    plt.ylabel(f'$|Y^\\mu_{gen}|$', fontsize=20)
    plt.yscale('log')
    plt.xscale('log')
    plt.savefig(f'comparison_yukawa_coupling_{gen}.png')
    plt.clf()

scatter_couplings(Yn_11_2, Yn_12_2, Yn_13_2, '1')
scatter_couplings(Yn_21_2, Yn_22_2, Yn_23_2, '2')
scatter_couplings(Yn_31_2, Yn_32_2, Yn_33_2, '3')

# Calcular el valor medio geométrico total de los acoples
mean_total_couplings_2 = []

for y in range(len(Yn_11_2)):
    mean_total_couplings_2.append((Yn_11_2[y] * Yn_12_2[y] * Yn_13_2[y] *
                     Yn_21_2[y] * Yn_22_2[y] * Yn_23_2[y] *
                     Yn_31_2[y] * Yn_32_2[y] * Yn_33_2[y])**(1/9))
plt.figure(figsize=(8,6))
plt.hist(mean_total_couplings_2, bins=15, edgecolor='red', histtype='step', density=True)
plt.title('')
plt.xlabel(r'$\bar{G}$', fontsize=22)
plt.ylabel('u.a.', fontsize=22)
#plt.yscale('log')
#plt.xscale('log')
plt.yticks(np.linspace(0, plt.ylim()[1], num=6), labels=[0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
plt.savefig('mean_yukawa_coupling.png')
plt.clf()
"""