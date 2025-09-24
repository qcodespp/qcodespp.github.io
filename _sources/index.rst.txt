qcodes++ documentation
======================

qcodes++ (aka qcodespp, qcpp, qc++) is a python package to run scientific experiments. qcodes++ is built on top of `QCoDeS <https://qcodes.github.io/Qcodes/>`__, both extending capabilities and preserving older features.

QCoDeS is a Python-based data acquisition framework developed by the
Copenhagen / Delft / Sydney / Microsoft quantum computing consortium.
It contains a huge range of drivers for communicating with instruments,
and a flexible - but complex - database-based method for collecting data
and running measurement loops.

The qcodes++ package provides a user-friendly frontend to the solid backend of QCoDeS. 
If you have always wanted to run your measurements using python but found QCoDeS too 
daunting, qcodes++ is the package for you. qcodes++ features:

* Simple yet powerful methods for running experiments and storing data
* True live plotting featuring sub-second, point-by-point updates without performance impact
* A feature-rich offline plotting/analysis tool for publication-quality figures, including curve fitting, making linecuts of 2D data, smoothing, taking derivatives and more
* Text-based data storage for easy access and long-term stability
* Improvements to core QCoDeS functionalities (e.g. Station, Parameters) to streamline data acquisition, protect (meta)data integrity and minimise user error
* Improved drivers for certain instruments
* and other user-friendliness improvements

The source code is available `on GitHub <https://github.com/qcodespp/qcodespp>`__, and the following documentation will guide you on how to quickly and easily start running measurements. Issue reporting, feedback and contributions are more than welcome through the GitHub repository.

The name: In addition to being a really stupid pun on q(c++), it reflects the fact that really we just want 
to add some nice features to the main package, and also it makes me happy because in our lab we have, totally 
coincidentally, always named our plotting windows pp, e.g. pp = qc.live_plot().

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
   autoapi/index