from cantera import ck2cti
parser = ck2cti.Parser()
parser.convertMech('sandiego20161214_mechCK.txt', thermoFile='sandiego20160815_therm.txt', transportFile='sandiego20160815_trans.txt', phaseName='ucsd', outName=None, quiet=False, permissive=True)
