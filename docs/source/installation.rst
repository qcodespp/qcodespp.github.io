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

Windows shortcuts
-----------------
On Windows, you can add desktop and start menu shortcuts for both Jupyter lab and `offline plotting <https://qcodespp.github.io/offline_plotting.html>`__. Make sure you are in the qcodespp environment and run:

``qcodespp create_shortcuts``

Usually you just want to select option 1.

Updating
--------
To update qcodes++ to the latest version, run:

``pip install -U qcodespp``

Additionally...
---------------
- If you will use drivers from `qcodes_contrib_drivers <https://qcodespp.github.io/visa.html#where-are-the-drivers>`__ you can install them with ``pip install qcodes_contrib_drivers``.

- If you will use Zurich Instruments instruments, you need to install the ZI python API with ``pip install zhinst zhinst-qcodes``.

- If you will use VISA instruments (e.g. ones that communicate via GPIB, USB, RS232) you should install the NI VISA and GPIB(488.2) backends from the National Instruments website `here <https://www.ni.com/en/support/downloads/drivers/download.ni-visa.html>`__ and `here <https://www.ni.com/en/support/downloads/drivers/download.ni-488-2.html>`__. Keysight also offers a VISA backend, available `here <https://www.keysight.com/zz/en/lib/software-detail/computer-software/io-libraries-suite-downloads-2175637.html?jmpid=zzfindiosuite>`__.

- If the qcodes++ install fails, you may need to install `Visual Studio C++ build tools. <https://visualstudio.microsoft.com/downloads/>`__. After following the link, go to *Tools for Visual Studio* and then *Build Tools for Visual Studio*.

GitHub install
--------------
If you prefer to be as up-to-date as possible, or wish to contribute, you can install qcodes++ directly from the GitHub repository. First, install the `git client <https://git-scm.com/>`__ and open a Git Bash instance. Then cd ('change directory') to the desired directory (usually C:/git on Windows) and clone the repository:

.. code-block:: bash
    
    cd C:/git
    git clone https://github.com/qcodes/qcodespp.git

Then, in an Anaconda prompt (or terminal if you are using miniconda), create and activate the environment as described above, and install qcodes++ in editable mode:

.. code-block:: bash
    
    conda create -n qcodespp python
    conda activate qcodespp
    pip install -e C:/git/qcodespp

To get updated with the latest pushes to the main branch, use Git Bash to cd to the install directory and pull:

.. code-block:: bash
    
    cd C:/git/qcodespp
    git pull

To contribute, please fork the repository on GitHub, clone your fork, create a new branch for your changes, and make a pull request when you are done. `i.e. just the standard procedure for contributing to git projects <https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project>`__.