Live plotting
=============

add_subplots
------------
As we've seen so far, if you just want to plot a ``Parameter`` in each of the subplots of the live plotting window, you can simply pass ``Parameters`` to ``loop.run()``. You can also pass them when you define the ``Loop`` using the ``plot`` argument, e.g.:

.. code-block:: python

    loop=qc.loop1d(sweep_parameter=qdac.ch01.volt,
               start=0,stop=1,num=101,delay=0.03,
               device_info='Device1',
               instrument_info=f'ACdiv=1e5 DCdiv=1e3 freq={li.osc0_freq():.6g} Hz',
               measure=[currentX, currentY, voltageX, voltageY, resistance],
               plot=[currentX,voltageX,resistance])

For more control over live plotting options, you can use the ``qc.live_plot()`` function which returns a ``qc.Plot`` object.

.. code-block:: python

    pp=qc.live_plot()


You can optionally initialise it with parameters to plot, as in ``loop.run()``.

.. code-block:: python

    pp=qc.live_plot(currentX,voltageX,resistance)

or equivalently, add them afterwards using ``add_subplots()``

.. code-block:: python

    pp=qc.live_plot()
    pp.add_subplots(currentX,voltageX,resistance)

Wait what are we plotting?
--------------------------
A quick word about the ``DataSetPP``: Each ``DataSetPP`` consists of a number of ``DataArray`` elements, which hold the stored data for each ``Parameter``. What you are *actually* plotting is data from these ``DataArray`` elements. When you declare your ``loop``, a summary of the ``DataSetPP`` is printed, showing the ``array_id`` for each ``DataArray`` and its ``shape``. You can access the ``DataSetPP`` for a particular loop via ``loop.data_set``, and the individual ``DataArray`` elements via e.g. ``loop.data_set.param1`` or ``loop.data_set.arrays['param1']``.

add
---

The ``add`` method allows the most control over subplots in the live plotting window.

.. code-block:: python

    pp=qc.live_plot()
    pp.add(param1, title='Parameter 1', name='Parameter 1', subplot=0)
    pp.add(param2, title='Parameter 2', name='Parameter 2', subplot=1)

The first argument to ``add`` can be many things. The most foolproof option is to supply a ``DataArray``, e.g. ``loop.data_set.param1``. However, assuming that the ``DataSetPP`` of interest was the last created ``DataSetPP``, you can supply the ``array_id`` as a string:

.. code-block:: python

    pp.add('param1', title='Parameter 1', name='Parameter 1', subplot=0)
    pp.add('param2', title='Parameter 2', name='Parameter 2', subplot=1)

or the ``Parameter`` object if the ``DataSetPP`` has only one ``DataArray`` per ``Parameter`` (this is not the case for e.g. ``loop2dUD`` and other advanced loop types!)

To add multiple elements to the same subplot, simply use the same index for ``subplot=``.

After you have set up the plot as you prefer, you can run the loop without any arguments, i.e. ``data=loop.run()``.

By default, the provided dataset element is plotted as the y-axis for 1D plots and the z-axis for 2D plots, with the independent variables plotted on their respective axes. You can also specify the x-axis (and y-axis for 2D plots) explicitly by providing the appropriate number of dataset elements as arguments, e.g.:

.. code-block:: python
    
    pp.add(data.paramx, data.paramy, data.paramz, title='Parameter 1', name='Parameter 1', subplot=0)
    pp.add('paramx2','paramy2','paramz2', title='Parameter 2', name='Parameter 2', subplot=1)

You can of course add data from a *different* ``DataSetPP``. If the ``DataSetPP`` was not the most recently defined, you will have to pass the ``DataArray``.

.. code-block:: python

    pp.add(new_data.param1, title='Parameter 1', name='Parameter 1', subplot=2)
    new_loop.run()

Otherwise, if you have defined a new ``Loop`` and new ``DataSetPP`` and want to add data to the previously defined ``live_plot`` window, just add it using any identifier (``DataArray``, ``array_id`` or ``Parameter``).

.. code-block:: python

    loop=qc.loop1d(sweep_parameter=qdac.ch01.volt,
               start=0,stop=1,num=101,delay=0.03,
               device_info='Device1',
               instrument_info=f'ACdiv=1e5 DCdiv=1e3 freq={li.osc0_freq():.6g} Hz',
               measure=[param1, param2]
    pp.add(param1, title='Parameter 1', name='Parameter 1', subplot=2)
    new_loop.run()

Back to add_subplots
--------------------

Similarly, ``add_subplots()`` will also accept as arguments any of ``DataArray``, ``array_id`` or ``Parameter``. So far we just provided ``Parameter`` because it's easiest, but in many situations you will want to use ``DataArray`` or ``array_id`` to avoid ambiguity.