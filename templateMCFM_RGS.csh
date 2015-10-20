#!/bin/csh                  
cd /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/
eval `scram runtime -csh`
cd /afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/MCFM-7.0/Bin
/afs/cern.ch/work/r/rebeca/hww_signal_gridpacks_II/CMSSW_7_1_14/src/MCFM-7.0/Bin
setenv LD_LIBRARY_PATH {$LD_LIBRARY_PATH}:/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf6/6.1.5-cms/lib
setenv LHAPATH {$LHAPATH}:/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf6/6.1.5-cms/share/LHAPDF/
setenv PATH {$PATH}:/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf6/6.1.5/bin/
setenv PATH {$PATH}:/cvmfs/cms.cern.ch/slc6_amd64_gcc481/external/lhapdf6/6.1.5-cms//lhapdf/bin/
./mcfm
