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

    datafiles=qc.load_data_nums([x*2+12 for x in range(4)])

To load a filepath directly,

.. code-block:: python

    data=qc.load_data('path/to/datafile')

When imported into the notebook, you can use ``data.param_name`` to access the data from a specific parameter. Other information, e.g. name, unit, etc is available using e.g. ``data.Voltage.unit``. The data are also stored in a dictionary under ``data.arrays``, which means you can address arrays via strings, e.g. ``data.arrays['Voltage']``, which is useful for programattically addressing them (e.g. in a loop).

Each of these ``DataArray`` elements inside the ``DataSetPP`` at heart are just ``numpy.ndarray`` objects with some extra details ontop. They will mostly behave like numpy arrays, but if you want to access the underlying ``ndarray`` directly, use ``data.param_name.ndarray``.

``data.metadata`` is a `python dictionary <https://docs.python.org/3/tutorial/datastructures.html#dictionaries>`__ containing the metadata saved by the ``Station``. It contains, among other things, *the value of every single parameter of every single instrument declared in ``station`` when the measurement started*. This is extremely useful two years into your project and you forgot which lock-in time constant you used. This is the entire point of creating the ``Station`` and ensuring that you keep it updated. The `offline_plotting <https://qcodespp.github.io/offline_plotting.html>`__ also offers an easy-to-use tool for metadata exploration.

Incomplete DataSets
^^^^^^^^^^^^^^^^^^^

If you terminate a ``Loop`` before it finishes, the remaining data will be `NaNs <https://numpy.org/doc/stable/reference/constants.html#numpy.nan>`__. Upon load, NaNs are 'removed' from the arrays by finding the first NaN index, N, in the innermost independent parameter. Columns with an index larger than N-1 will be stripped from the arrays. If the measurement was stopped mid-column, this column will **not** be loaded to ensure the data behaves nicely for e.g. `matplotlib pcolormesh <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pcolormesh.html>`__. If this is not the desired behaviour, use ``remove_incomplete=False`` in any of the above load functions. Data on disk is not affected.

Plotting and analysis
---------------------

For cases not covered by the built-in live_plot and offline_plotting, you will likely prepare plots using a package like matplotlib inside a Jupyter notebook. There are a few useful functions in qcodes++ to help you with this.

- You can use the functions in ``qcodespp.plotting.analysis_tools`` to plot nice colorplots and line plots with nicely colored lines.

- You can use the fitting and filter functions from ``qcodespp.plotting.offline_plotting.fits`` and ``qcodespp.plotting.offline_plotting.filters`` either directly, or as inspiration for your own fitting and filtering functions.

See API (`analysis_tools <https://qcodespp.github.io/autoapi/qcodespp/plotting/analysis_tools/index.html>`__, `fits <https://qcodespp.github.io/autoapi/qcodespp/plotting/offline/fits/index.html>`__, `filters <https://qcodespp.github.io/autoapi/qcodespp/plotting/offline/filters/index.html>`__) and/or `source code <https://github.com/qcodespp/qcodespp/tree/main/qcodespp/plotting>`__ to see how to use them.