Data loading and analysis
=========================

Loading data
------------

To load previously measured data, the easiest way is to load by the counter number.

.. code-block:: python

    qc.load_data_num(number)

Number can be a string or an integer. e.g.

.. code-block:: python

    data=qc.load_data_num(123) or data=qc.load_data_num(‘2’)

If the folder your data is in isn't just 'data', you can use the datafolder argument. Likewise, if underscore ('_') doesn't appear after the number in your data file names, you need to specify what does.

.. code-block:: python

    data=qc.load_data_num(123,datafolder='magneticfielddata',delimiter=' ')

But for most cases, you can simply exclude datafolder and delimiter to use the default values.

For loading multiple data files, use

.. code-block:: python

    qc.load_data_nums(listofnumbers,datafolder=”data”,delimiter='_')

e.g.

.. code-block:: python

    datafiles=qc.load_data_nums([2,123,436,20]) 

or even

.. code-block:: python

    datafiles=qc.load_data_nums(x*2+12 for x in range(4)) 


When imported into the notebook, you can use data.*param_name* to load the values of a specific parameter. These are actually all stored in a dictionary under data.arrays, which means you can easily pull the names, units, etc using the standard `python dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`__ tools.

data.metadata contains the metadata saved by station. **This is extremely useful, and basically the entire point of defining a station in the first place**. It contains, among other things, *the value of every single parameter of every single instrument declared in station when the measurement started*. Did you forget which lock-in frequency you were using? Did you make a mistake in the filename and write the wrong sweep range? Don't worry! data.metadata contains ALL this information and more. Go have a look! Again it’s a dictionary, which you can dive into and pull out the parameters regarding the instruments, loop information, etc.

Plotting and analysis
---------------------

For cases not covered by the built-in live_plot and offline_plotting, you will likely prepare plots using a package like matplotlib inside a Jupyter notebook. There are a few useful functions in qcodes++ to help you with this.

- You can use the functions in ``qcodespp.plotting.analysis_tools`` to plot nice colorplots and line plots with nicely colored lines.

- You can use the fitting and filter functions from ``qcodespp.plotting.offline_plotting.fits`` and ``qcodespp.plotting.offline_plotting.filters`` either directly, or as inspiration for your own fitting and filtering functions.

See API (`analysis_tools <https://qcodespp.github.io/autoapi/qcodespp/plotting/analysis_tools/index.html>`__, `fits <https://qcodespp.github.io/autoapi/qcodespp/plotting/offline/fits/index.html>`__, `filters <https://qcodespp.github.io/autoapi/qcodespp/plotting/offline/filters/index.html>`__) and/or `source code <https://github.com/qcodespp/qcodespp/tree/main/qcodespp/plotting>`__ to see how to use them.