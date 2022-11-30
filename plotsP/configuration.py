#tag = 'new_vbf_16_2'
tag = 'new_vbf_16'

outputFile   = f"mkShapes__{tag}.root"
outputFolder = f"rootFiles"

path = "/eos/user/g/gpizzati/www/rdf/2016_tot/"


# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py' 

# file with list of samples
samplesFile = 'samples.py' 

# file with list of samples
plotFile = 'plot.py' 

# luminosity to normalize to (in 1/fb)
#lumi = 35.9
lumi = 36.33

batchFolder = f'condor2_{tag}'
