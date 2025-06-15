Installation
============
Installing python
-----------------
QCoDeS and qcodes++ require a working python installation. The recommended way to install python is with `Anaconda <https://www.anaconda.com/products/distribution>`__ or `miniconda <https://docs.conda.io/en/latest/miniconda.html>`__. Both provide a framework and tools for managing python packages. An important feature of Anaconda and miniconda is that they allow you to create isolated environments, which means you can have different versions of python and different sets of packages installed in each environment. This is very useful for avoiding conflicts between packages, and for keeping your python installation clean.

Installing qcodes++
-------------------
After you have installed python using Anaconda or miniconda, you can create a new environment by opening the Anaconda prompt (or your terminal if you are using miniconda) and running the following command:

``conda create -n qcodespp python``

Then activate the environment:

``conda activate qcodespp``

and finally, install qcodes++:

``pip install qcodespp``

You can now run qcodes++ in a Jupyter notebook by starting Jupyter lab:

``jupyter lab``


Additionally...
---------------

- If you will use drivers from `qcodes_contrib_drivers <https://qcodespp.github.io/visa.html#where-are-the-drivers>`__ you can install them with ``pip install qcodes_contrib_drivers``.

- If you will use Zurich Instruments instruments, you need to install the ZI python API with ``pip install zhinst zhinst-qcodes``.

- If you will use VISA instruments (e.g. ones that communicate via GPIB, USB, RS232) you should install the NI VISA and GPIB(488.2) backends from the National Instruments website `here <https://www.ni.com/en/support/downloads/drivers/download.ni-visa.html>`__ and `here <https://www.ni.com/en/support/downloads/drivers/download.ni-488-2.html>`__.

- If the qcodes++ install fails, you may need to install `Visual Studio C++ build tools. <https://visualstudio.microsoft.com/downloads/>`__. After following the link, go to *Tools for Visual Studio* and then *Build Tools for Visual Studio*.