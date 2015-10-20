#!/bin/csh                        
cd /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/OUTDIR/job_JOBNUMBER/
eval `scram runtime -csh`
cd -
mkdir TEMP
cd TEMP/
cp /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/*.sh .
cp -r /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/patches/ .
./create_powheg_tarball.sh MODEL POWHEGINPUT JHUGEN NEVENTS SEED
rm powhegboxV2_July2015*/work/POWHEG-BOX/*.tgz
rm powhegboxV2_July2015*/work/powhegboxV2_*.tar.gz
rm powhegboxV2_July2015*/work/POWHEG-BOX/*/JHUGenerator.v*.tar.gz
rm -rf powhegboxV2_July2015*/work/POWHEG-BOX/*/JHUGenMELA/
cd ..
cp -r TEMP/* /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/OUTDIR/job_JOBNUMBER/ 
cd /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/OUTDIR/job_JOBNUMBER/
mv MODEL_tarball.tar.gz TARBALLNAME_tarball.tar.gz
