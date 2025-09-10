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

What is being plotted?
----------------------
Each ``DataSetPP`` consists of a number of ``DataArray`` elements, which hold the stored data for each ``Parameter``. What you are *actually* plotting is data from these ``DataArray`` elements. When you declare your ``loop``, a summary of the ``DataSetPP`` is printed, showing the ``array_id`` for each ``DataArray`` and its ``shape``. You can access the ``DataSetPP`` for a particular loop via ``loop.data_set``, and the individual ``DataArray`` elements via e.g. ``loop.data_set.param1`` or ``loop.data_set.arrays['param1']``.

This is important to understand for the next bit!

add
---

The ``add`` method allows the most control over subplots.

.. code-block:: python

    pp=qc.live_plot()
    pp.add(param1, title='Parameter 1', name='Parameter 1', subplot=0)
    pp.add(param2, title='Parameter 2', name='Parameter 2', subplot=1)

The first argument to ``add`` can be:

1. A ``DataArray`` object, such as ``loop.data_set.param1``.
2. An ``array_id`` string, e.g. ``'param1'``.
3. A ``Parameter`` object, if the ``DataSetPP`` has only one ``DataArray`` per ``Parameter``.

Method 1 always works. Method 2 will almost always work, and Method 3 can work in simple cases. Methods 2 and 3 work by looking for the ``array_id`` or ``Parameter`` name *in the most recently created* ``DataSetPP``, and then adding the relevant ``DataArray``. This means these methods only work if the ``DataSetPP`` of interest was indeed the last created ``DataSetPP``. Otherwise, you can supply the ``data_set`` argument to specify which ``DataSetPP`` to use.

.. code-block:: python

    pp.add('example_array_id', title='Parameter 1', name='Parameter 1', subplot=2, data_set=old_loop.data_set)

After you have set up the plot as you prefer, you can run the loop without any arguments, i.e. ``data=loop.run()``.

Some tricks
-----------

To add multiple elements to the same subplot, simply use the same index for ``subplot=``.

.. code-block:: python

    pp.add(param1, title='Parameter 1', name='Parameter 1', subplot=0)
    pp.add(param2, title='Parameter 2', name='Parameter 2', subplot=0)

By default, the provided dataset element is plotted as the y-axis for 1D plots and the z-axis for 2D plots, with the independent variables plotted on their respective axes. You can also specify the x-axis (and y-axis for 2D plots) explicitly by providing the appropriate number of dataset elements as arguments, e.g.:

.. code-block:: python
    
    pp.add(data.paramx, data.paramy, data.paramz, title='Parameter 1', name='Parameter 1', subplot=0)
    pp.add('paramx2','paramy2','paramz2', title='Parameter 2', name='Parameter 2', subplot=1)

You can of course add data from a *different* ``DataSetPP``. This is most commonly desired if you want to run a new experiment and plot it alongside a previous experiment's data. Simply define a new loop, but *not* a new plot window.

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

Similarly to ``add``, ``add_subplots()`` will also accept any of ``DataArray``, ``array_id`` or ``Parameter``. So far we just provided ``Parameter`` because it's usually easiest, but in some situations you may want to use ``DataArray`` or ``array_id``. For example, in ``loop2dUD``, each ``Parameter`` has two corresponding ``DataArray`` elements. While ``add`` doesn't know which one to plot, and therefore won't let you supply a ``Parameter`` at all, ``add_subplots`` will do the opposite; it will plot both ``DataArray`` elements. If you only want to plot one, you can specify e.g. using the ``array_id``:

.. code-block:: python

    pp.add_subplots('currentX_1','voltageX_2')

In some cases it is *necessary* to supply either the ``DataArray`` or the ``array_id``; one example is for ``MultiParameters`` where each component of the ``MultiParameter`` generates a corresponding ``DataArray``. But since a component of a ``MultiParameter`` is not itself a ``Parameter``, you must of course use either ``DataArray`` or ``array_id``.

Finally, you can mix and match as you please. The following will work just fine:

.. code-block:: python

    pp.add_subplots('currentX_1',voltageX,loop.data_set.resistance)

A little secret that hopefully you never have to know
-----------------------------------------------------
``live_plot`` works by setting the ``publisher`` attribute of the ``DataSetPP`` to the ``Plot`` object. This enables the ``DataSetPP`` to send the data *from memory* to the plot, and bypasses saving to disk; part of the reason the plotting is so fast. In almost every case I can think of, this works automatically. When you create a new ``DataSetPP``, that ``DataSetPP`` becomes the 'active' dataset, and any subsequent calls to ``add`` or ``add_subplots`` sets the active dataset's publisher to the plot being added to. Therefore, as long as you use ``add`` or ``add_subplots`` after creating the ``DataSetPP`` you want to add, and before creating a new ``DataSetPP``, you don't have to worry about it. But if there is some edge case, where you cannot do things in this order, use e.g. ``data.publisher=pp`` to set the publisher manually.