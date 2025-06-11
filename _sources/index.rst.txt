qcodes++ documentation
======================

Welcome to the qcodes++ documentation. qcodes++ is a python package to run scientific experiments. qcodes++ is built on top of  `QCoDeS <https://qcodes.github.io/Qcodes/>`__, both preserving old features and extending capabilities.

QCoDeS is a Python-based data acquisition framework developed by the
Copenhagen / Delft / Sydney / Microsoft quantum computing consortium.
It contains a huge range of drivers for communicating with instruments,
and a flexible - but complex - database-based method for collecting data
and running measurement loops.

This package, qcodes++ (aka qcodespp, qcpp, qc++), provides user-friendly
frontend to the solid backend of qcodes. If you have always wanted to run 
your measurements using python but found qcodes too daunting, qcodes++ is 
the package for you. Qcodes++ features

* Text-based data (i.e. readable by e.g. notepad, excel, origin pro, etc)
* A simple yet powerful method for taking data and running measurements and loops
* True live plotting and an integrated offline plotting/analysis tool
* Improvements to core qcodes functions (e.g. Station, Parameters) to streamline data acquisition, protect (meta)data integtrity and minimise user error
* Improved drivers for certain instruments
* and other user-friendliness improvements outlined in the following.

The source code is available `here <https://github.com/qcodespp/qcodespp>`__.

.. toctree::
   :maxdepth: 3
   :caption: Contents:

   background
   installation
   dummy_measurements
   more_features
   parameters
   visa
   data_analysis
   offline_plotting
   measure
   advanced
   differences_from_qcodes
   autoapi/index