cd /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/OUTDIR/job_JOBNUMBER/
eval `scram runtime -csh`
cp /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/*.sh .
cp -r /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/patches/ .
./create_powheg_tarball.sh MODEL POWHEGINPUT JHUGEN NEVENTS SEED
cd ..
cd /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/OUTDIR/job_JOBNUMBER/
mv MODEL_tarball.tar.gz TARBALL_tarball.tar.gz
