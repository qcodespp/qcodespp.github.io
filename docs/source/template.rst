Template for measurements
=========================

To be filled out with a minimal working example of connecting to instruments, running 1d and 2d sweeps, and defining custom parameters.

See if it's possible to do it with a legit jupyter notebook

import qcodespp as qc
qc.listVISAinstruments()

----

import qcodespp as qc
from qcodespp.instrument_drivers.QDevil.QDAC2 import QDac2
from qcodespp.instrument_drivers.ZI.ZIMFLI import ZIMFLI

etc

define a resistance

qc.set_data_folder('data')

# remember to define all instruments and parameters before defining the station to ensure all metadata is saved
station=qc.Station(add_variables=globals())

-----
1d loop, IV curve, simples

1d loop, gate voltage where leakage current is measured and stopped if leakage current is too high.

2d loop, bias spec

