Installation
============
Installing python
-----------------
`Python <https://en.wikipedia.org/wiki/Python_(programming_language)>`__ is a popular programming language that is known for being intuitive and easy to learn. The standard python libraries cover a huge range of programming tasks, but what really makes python popular is the ability to easily create and add packages, which provide additional capabilities. For example, the scipy package contains extremely useful scientific features such as least squares fitting, and the matplotlib package is a fantastic tool for generating publication-quality figures.

QCoDeS and qcodes++ operate within python and need a working python installation to run. The recommended way to install python is via `Anaconda <https://www.anaconda.com/products/distribution>`__ or `miniconda <https://docs.conda.io/en/latest/miniconda.html>`__, which provides a framework and tools for managing python packages. An important feature of Anaconda and miniconda is that they allow you to create isolated environments, which means you can have different versions of python and different sets of packages installed in each environment. This is very useful for avoiding conflicts between packages, and for keeping your main python installation clean.

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

Continue with the `getting started <dummy_measurements.html>`_ tutorial to learn how to use qcodes++.
Remember to activate the qcodespp environment before starting Jupyter lab.

Additionally...
---------------

- If you are going to use VISA instruments (e.g. ones that communicate via GPIB, USB, RS232) you should install the NI VISA and GPIB(488.2) backends from the National Instruments website `here <https://www.ni.com/en/support/downloads/drivers/download.ni-visa.html>`__ and `here <https://www.ni.com/en/support/downloads/drivers/download.ni-488-2.html>`__.

- If the qcodes install fails, you may need to install `Visual Studio C++ build tools. <https://visualstudio.microsoft.com/downloads/>`__. After following the link, go to *Tools for Visual Studio* and then *Build Tools for Visual Studio*.