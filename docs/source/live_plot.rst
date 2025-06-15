Live plotting
=============

As we've seen so far, if you just want to plot a ``Parameter`` in each of the subplots of the live plotting window, you can simply pass the list of ``Parameters`` to ``loop.run()``. You can also pass them when you define the ``Loop`` using the ``plot`` argument, e.g.:

.. code-block:: python

    loop=qc.loop1d(sweep_parameter=qdac.ch01.volt,
               start=0,stop=1,num=101,delay=0.03,
               device_info='Device1',
               instrument_info=f'ACdiv=1e5 DCdiv=1e3 freq={li.osc0_freq():.6g} Hz',
               measure=[currentX, currentY, voltageX, voltageY, resistance],
               plot=[currentX,voltageX,resistance])

For more control over live plotting options, you can use the ``qc.live_plot`` function which returns a ``qc.Plot`` object and optionally links a specific ``DataSetPP`` to it.

.. code-block:: python

    pp=qc.live_plot(data)

where ``data`` will typically be ``loop.data_set``. To add elements of the ``DataSetPP`` to the plot, you use the ``add`` method:

.. code-block:: python

    pp.add(data.param1, title='Parameter 1', name='Parameter 1', subplot=0)
    pp.add(data.param2, title='Parameter 2', name='Parameter 2', subplot=1)

Note that ``add`` does *not* accept ``Parameters``, but rather only accepts ``DataSetPP`` elements, which can be accessed using e.g. ``data.param1`` or ``data.arrays['param1']``. To add multiple elements to the same subplot, simply use the same index for ``subplot=``.

After you have set up the plot as you prefer, you can run the loop without any arguments, i.e. ``data=loop.run()``.

By default, the provided dataset element is plotted as the y-axis for 1D plots and the z-axis for 2D plots, with the independent variables plotted on their respective axes. You can also specify the x-axis (and y-axis for 2D plots) explicitly by providing the appropriate number of dataset elements as arguments, e.g.:

.. code-block:: python
    
    pp.add(data.paramx, data.paramy, data.paramz, title='Parameter 1', name='Parameter 1', subplot=0)

If you want to continue to add data to the plot from a *different* ``DataSetPP``/``Loop``, you can do so by linking the plot to the new DataSetPP via the DataSetPP's ``publisher`` method. Some examples:

.. code-block:: python

    new_data.publisher=pp
    pp.add(new_data.param1, title='Parameter 1', name='Parameter 1', subplot=2)
    new_loop.run()

.. code-block:: python

    new_loop.data_set.publisher=pp
    pp.add(new_loop.data_set.param1, title='Parameter 1', name='Parameter 1', subplot=2)
    new_loop.run()

Finally, the ``add_multiple()`` method takes a list of ``DataSetPP`` elements and plots them in different subplots.

.. code-block:: python

    data = loop.data_set
    pp = qc.live_plot(data)
    pp.add_multiple(data.param1, data.param2, data.param3)
    loop.run()

The above behaviour is excatly the same as ``pp = qc.live_plot(data, [data.param1, data.param2, data.param3])``, but ``add_multiple()`` is useful if you want to add more elements to the plot later. Note that ``add_multiple()`` also accepts only ``DataSetPP`` elements, not ``Parameters``.