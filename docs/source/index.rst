qcodes++ documentation
======================

qcodes++ (aka qcodespp, qcpp, qc++) is a python package to run scientific experiments. qcodes++ is built on top of `QCoDeS <https://qcodes.github.io/Qcodes/>`__, both extending capabilities and preserving older features.

QCoDeS is a Python-based data acquisition framework developed by the
Copenhagen / Delft / Sydney / Microsoft quantum computing consortium.
It contains a huge range of drivers for communicating with instruments,
and a flexible - but complex - database-based method for collecting data
and running measurement loops.

The qcodes++ package provides a user-friendly
frontend to the solid backend of QCoDeS. If you have always wanted to run 
your measurements using python but found QCoDeS too daunting, qcodes++ is 
the package for you. qcodes++ features

* Text-based data (i.e. readable by e.g. notepad, excel, origin pro, etc)
* A simple yet powerful method for taking data and running measurements and loops
* True live plotting and an integrated offline plotting/analysis tool
* Improvements to core qcodes functions (e.g. Station, Parameters) to streamline data acquisition, protect (meta)data integtrity and minimise user error
* Improved drivers for certain instruments
* and other user-friendliness improvements

The source code is available `here <https://github.com/qcodespp/qcodespp>`__, and the following documentation will guide you on how to quickly and easily start running measurements.

The name: In addition to being a really stupid pun on q(c++), it reflects the fact that really we just want 
to add some nice features to the main package, and also it makes me happy because totally 
coincidentally we have always named our plotting windows pp, e.g. pp = qc.live_plot().

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   background
   installation
   dummy_measurements
   more_features
   parameters
   visa
   live_plot
   template
   data_analysis
   offline_plotting
   measure
   advanced
   differences_from_qcodes
   api/index