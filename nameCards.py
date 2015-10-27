import os, commands, time
from gamma_sm import *

def nameCards(tag):

    mass=tag.replace('.0','')
    f_mass=float(mass)

    ## ggH
    os.system('cp /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/inputCards/gg_H_quark-mass-effects_NNPDF30_13TeV_TEMPLATE.input /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/gg_H_quark-mass-effects_JHUGen_HWW2L2Nu_NNPDF30_13TeV/gg_H_quark-mass-effects_NNPDF30_13TeV_M'+mass+'.input')
    os.system("sed -i 's~MASS~"+mass+"~g' /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/gg_H_quark-mass-effects_JHUGen_HWW2L2Nu_NNPDF30_13TeV/gg_H_quark-mass-effects_NNPDF30_13TeV_M"+mass+".input")
    gamma = str(gamma_sm[f_mass])
    os.system("sed -i 's~WIDTH~"+gamma+"D0~g' /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/gg_H_quark-mass-effects_JHUGen_HWW2L2Nu_NNPDF30_13TeV/gg_H_quark-mass-effects_NNPDF30_13TeV_M"+mass+".input")
    hfact = 0.1*f_mass+47.5
    os.system("sed -i 's~HFACT~"+str(hfact)+"d0~g' /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/gg_H_quark-mass-effects_JHUGen_HWW2L2Nu_NNPDF30_13TeV/gg_H_quark-mass-effects_NNPDF30_13TeV_M"+mass+".input")
    os.system('cp /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/inputCards/JHUGen_gg_H_WW2L2Nu_TEMPLATE.input  /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/gg_H_quark-mass-effects_JHUGen_HWW2L2Nu_NNPDF30_13TeV/JHUGen_gg_H_WW2L2Nu_M'+mass+'.input') 
    os.system("sed -i 's~MASS~"+mass+"~g' /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/gg_H_quark-mass-effects_JHUGen_HWW2L2Nu_NNPDF30_13TeV/JHUGen_gg_H_WW2L2Nu_M"+mass+".input")
   
    ## VBF
    #os.system('cp /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/inputCards/VBF_H_TEMPLATE_NNPDF30_13TeV.input /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/VBF_H_JHUGen_HWW2L2Nu_NNPDF30_13TeV/VBF_H_M'+mass+'_NNPDF30_13TeV.input')
    #os.system("sed -i 's~MASS~"+mass+"d0~g' /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/VBF_H_JHUGen_HWW2L2Nu_NNPDF30_13TeV/VBF_H_M"+mass+"_NNPDF30_13TeV.input")
    #gamma = str(gamma_sm[f_mass])
    #os.system("sed -i 's~WIDTH~"+gamma+"d0~g' /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/VBF_H_JHUGen_HWW2L2Nu_NNPDF30_13TeV/VBF_H_M"+mass+"_NNPDF30_13TeV.input")
    #os.system('cp /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/gg_H_quark-mass-effects_JHUGen_HWW2L2Nu_NNPDF30_13TeV/JHUGen_gg_H_WW2L2Nu_M'+mass+'.input /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/VBF_H_JHUGen_HWW2L2Nu_NNPDF30_13TeV/JHUGen_VBF_H_WW2L2Nu_M'+mass+'.input') 
   
    # WH

    # Wplus
    #os.system('cp /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/inputCards/HWplusJ_HanythingJ_NNPDF30_13TeV_TEMPLATE.input /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/HWJ_JHUGen_HWW2L2Nu_NNPDF30_13TeV/HWplusJ_HanythingJ_NNPDF30_13TeV_M'+mass+'.input')
    #os.system("sed -i 's~MASS~"+mass+"d0~g' /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/HWJ_JHUGen_HWW2L2Nu_NNPDF30_13TeV/HWplusJ_HanythingJ_NNPDF30_13TeV_M"+mass+".input")
    #gamma = str(gamma_sm[f_mass])
    #os.system("sed -i 's~WIDTH~"+gamma+"d0~g' /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/HWJ_JHUGen_HWW2L2Nu_NNPDF30_13TeV/HWplusJ_HanythingJ_NNPDF30_13TeV_M"+mass+".input")
    #os.system('cp /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/gg_H_quark-mass-effects_JHUGen_HWW2L2Nu_NNPDF30_13TeV/JHUGen_gg_H_WW2L2Nu_M'+mass+'.input /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/HWJ_JHUGen_HWW2L2Nu_NNPDF30_13TeV/JHUGen_WH_WW2L2Nu_M'+mass+'.input') 
    
    ## Wminus
    #os.system('cp /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/HWJ_JHUGen_HWW2L2Nu_NNPDF30_13TeV/HWminusJ_HanythingJ_NNPDF30_13TeV_TEMPLATE.input /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/HWJ_JHUGen_HWW2L2Nu_NNPDF30_13TeV/HWminusJ_HanythingJ_NNPDF30_13TeV_M'+mass+'.input')
    #os.system("sed -i 's~MASS~"+mass+"d0~g' /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/HWJ_JHUGen_HWW2L2Nu_NNPDF30_13TeV/HWminusJ_HanythingJ_NNPDF30_13TeV_M"+mass+".input")
    #gamma = str(gamma_sm[f_mass])
    #os.system("sed -i 's~WIDTH~"+gamma+"d0~g' /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/HWJ_JHUGen_HWW2L2Nu_NNPDF30_13TeV/HWminusJ_HanythingJ_NNPDF30_13TeV_M"+mass+".input")
    #os.system('cp /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/gg_H_quark-mass-effects_JHUGen_HWW2L2Nu_NNPDF30_13TeV/JHUGen_gg_H_WW2L2Nu_M'+mass+'.input /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/HWJ_JHUGen_HWW2L2Nu_NNPDF30_13TeV/JHUGen_WH_WW2L2Nu_M'+mass+'.input') 
    
    # ZH
    #os.system('cp /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/HZJ_JHUGen_HZZ2LX_NNPDF30_13TeV/HZJ_HanythingJ_NNPDF30_13TeV_TEMPLATE.input /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/HZJ_JHUGen_HZZ2LX_NNPDF30_13TeV/HZJ_HanythingJ_NNPDF30_13TeV_M'+mass+'.input')
    #os.system("sed -i 's~MASS~"+mass+"d0~g' /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/HZJ_JHUGen_HZZ2LX_NNPDF30_13TeV/HZJ_HanythingJ_NNPDF30_13TeV_M"+mass+".input")
    #gamma = str(gamma_sm[f_mass])
    #os.system("sed -i 's~WIDTH~"+gamma+"d0~g' /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/HZJ_JHUGen_HZZ2LX_NNPDF30_13TeV/HZJ_HanythingJ_NNPDF30_13TeV_M"+mass+".input")
    #os.system('cp /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/HZJ_JHUGen_HZZ2LX_NNPDF30_13TeV/JHUGen_ZH_HZZ2LX_TEMPLATE.input /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/HZJ_JHUGen_HZZ2LX_NNPDF30_13TeV/JHUGen_ZH_HZZ2LX_M'+mass+'.input')
    #os.system("sed -i 's~MASS~"+mass+"~g' /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/HZJ_JHUGen_HZZ2LX_NNPDF30_13TeV/JHUGen_ZH_HZZ2LX_M"+mass+".input")
    

#for mass in [115,120,124,125,126,130,135,140,145,150,155,160,165,170,175,180,190,200]:    
for mass in [105,115,120,124,125,126,130,135,140,145,150,155,160,165,170,175,180,190,200,210,230,250,270,300,350,400,450,500,550,600,700,800,900,1000]:
    nameCards(str(mass))
