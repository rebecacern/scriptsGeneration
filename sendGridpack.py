import os, commands, time

csh_template = 'templateSend.csh'

mass = "115"

#gg
outdir = "submission_gridpack_gg_"+mass+"_October_22"
model = 'gg_H_quark-mass-effects'
powinput ='/afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/gg_H_quark-mass-effects_JHUGen_HWW2L2Nu_NNPDF30_13TeV/gg_H_quark-mass-effects_NNPDF30_13TeV_M'+mass+'.input'
tarball = 'gg_H_quark-mass-effects_HWW2L2Nu_M'+mass
jhuinput = '/afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/gg_H_quark-mass-effects_JHUGen_HWW2L2Nu_NNPDF30_13TeV/JHUGen_gg_H_WW2L2Nu_M'+mass+'.input'

#VBF
#outdir = "submission_gridpack_VBF_"+mass+"_October_22"
#model = 'VBF_H'
#powinput ='/afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/VBF_H_JHUGen_HWW2L2Nu_NNPDF30_13TeV/VBF_H_M'+mass+'_NNPDF30_13TeV.input'
#tarball = 'VBF_HWW2L2Nu_M'+mass
#jhuinput = '/afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/genproductions/bin/Powheg/production/V2/13TeV/Higgs/VBF_H_JHUGen_HWW2L2Nu_NNPDF30_13TeV/JHUGen_VBF_H_WW2L2Nu_M'+mass+'.input'


nevents = '100'
njobs = 1

if (not os.path.exists(outdir)):
    os.system('mkdir '+outdir)

startDir = os.getcwd()
os.chdir(outdir)

def processCmd(cmd, quite = 0):
    #    print cmd                                                                                                                                               
    status, output = commands.getstatusoutput(cmd)
    if (status !=0 and not quite):
        print 'Error in processing command:\n   ['+cmd+']'
        print 'Output:\n   ['+output+'] \n'
    return output

for job in range(1,njobs+1):

    os.system('mkdir job_'+str(job))
    os.chdir('job_'+str(job))

    str_job = str(job)
    csh_job = csh_template.replace('templateGridpack','jobGridpack_'+str(job))

    output = processCmd('cp ../../'+csh_template+' '+csh_job)
    output = processCmd("sed -i 's~OUTDIR~"+outdir+"~g' "+csh_job)
    output = processCmd("sed -i 's~JOBNUMBER~"+str(job)+"~g' "+csh_job)
    output = processCmd("sed -i 's~MODEL~"+str(model)+"~g' "+csh_job)
    output = processCmd("sed -i 's~TARBALL~"+str(tarball)+"~g' "+csh_job)
    output = processCmd("sed -i 's~POWHEGINPUT~"+str(powinput)+"~g' "+csh_job)
    output = processCmd("sed -i 's~JHUGEN~"+str(jhuinput)+"~g' "+csh_job)
    output = processCmd("sed -i 's~NEVENTS~"+str(nevents)+"~g' "+csh_job)
    output = processCmd("sed -i 's~SEED~10"+str(job)+"~g' "+csh_job)

    print 'submitting job',str(job)
    cmd = 'bsub -q 1nd '+csh_job
 
    output = processCmd(cmd)
    while ('error' in output):
        print 'unable to submit...'
        time.sleep(1.0);
        output = processCmd(cmd)
        if ('error' not in output):
            print output
            print 'Submitting after retry - job '+str(job)
    print output

    os.chdir(startDir+'/'+outdir)

os.chdir(startDir)

