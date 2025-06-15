Comparing qcodes++ and QCoDeS
=============================

Things that are the same
------------------------

**1) All top level classes and functions in QCoDeS are directly inherited in qcodes++.** All of these behave exactly the same way as in QCoDeS, so you can use them without change. If you used to do, e.g.

.. code-block:: python

    import qcodes as qc
    from qcodes import Instrument, Station

you can now do

.. code-block:: python

    import qcodespp as qc
    from qcodespp import Instrument, Station

and the rest of your code will work as before. Even though Parameter and Station have additions, they do not change the functionality of the original classes, so you can use them as you would in QCoDeS.

For lower level classes/functions, the situation is a bit different, since these cannot be easily inherited. You cannot for example do:

.. code-block:: python

    from qcodespp.dataset import DataSetType

since anything with a '.' after qcodes doesn't necessarily exist in qcodes++, and vice versa. However, you probably don't need to touch these lower level classes/functions, *except* of course for the instrument drivers. There, you always have to work out which package you want to import the driver from: qcodes++, QCoDeS or qcodes_contrib_drivers. However.....

**2) qcodes++ relies mainly on instrument drivers from QCoDeS and the qcodes_contrib_drivers.** In fact the instrument drivers included in qcodes++ are hopefully only here temporarily, and will be pulled back into QCoDeS or the qcodes_contrib_drivers in the near future.

The big difference: Data structure
----------------------------------

**In summary**: If you only ever do 1D or 2D measurements, qcodes++ makes it easy to obtain, visualise and share data. If you want to do more complex measurements, you may prefer QCoDeS.

**In detail**: The qcodes++ dataset, ``DataSetPP``, is a text-based dataset, where all the data is stored in numpy arrays of pre-determined shape. There are big advantages:

* ``DataSetPP`` is very easy to use and open across all platforms and programs.
* Knowing in advance the possible data shapes allows us to write advanced plotting tools that work for all 1D and 2D datasets.
* Ditto for the looping functions; the qcodes++ ``Loop`` contains a lot of checks and balances developed over the years to try to prevent common mistakes.

However, there is potentially one big disadvantage:

* The ``DataSetPP`` `is not as flexible as the QCoDeS <https://microsoft.github.io/Qcodes/dataset/dataset_design.html>`__ ``DataSet``, which allows you to store any type of data in any shape. The QCoDeS ``DataSet`` does not presuppose certain shapes and forms, which mean you can just dump and kind of data in any shape you want. This is really great if you are pushing the boundaries of what kind of experiments you want to do, and already have a fair bit of experience with python. However, as with any piece of software, this flexibility comes with a steeper learning curve, and means you may have to develop your own plotting and analysis tools.

**The good news**: If you install qcodes++, you can use both datasets and measurement philosophies side-by-side!

Small differences in existing classes
-------------------------------------

**The ``Station`` class has the following additional functions:**

* Upon init, ``Station`` accepts the argument ``add_variables=vars`` where ``vars`` can be e.g. ``globals()`` or ``locals()``. This feature looks through ALL previously declared variables within the vars, and if the varible is a Parameter or instance, it adds it to the Station. This means you don't have to do ``station.add_component()`` for every Instrument and Parameter. Just declare them before declaring the Station and use ``station = Station(add_variables=globals())``.

* ``.set_measurement(*actions)`` sets a series of actions (usually Parameters) to be performed when ``station.measure()`` is called.

* ``communication_time()`` measures the average time it takes to perform the action in ``.set_measurement()``.Typically this is just how long it takes to call the ``.get()`` functions of all the Parameters, giving you some idea of how long it takes the computer to communicate with the instruments.

**The ``Parameter`` class has the following additional functions:**

* ``.move()`` 'moves' the parameter to a new value in the given number of steps, without taking data. Useful if you want to set a sensitive parameter, e.g. a gate voltage, where using ``.set()`` could damage the sample.

* ``.sweep()`` same as in QCoDeS, but with the addition that if the start value of the sweep is different to the current value, it will warn the user.

* ``.logsweep()`` sweeps the parameter in a log10 scale.

* ``.returnsweep()`` sweeps the parameter up and down, i.e. first sweeps to the end value, then back to the start value.

* ``.arbsweep()`` accepts a list of a values, rather than a start and end value, and sweeps the parameter through these values.

**``MultiParameterWrapper`` makes it easy to create a ``MultiParameter`` from existing Parameters.**

See the `MultiParameterWrapper documentation <https://qcodespp.github.io/parameters.html#multiparameter-and-multiparameterwrapper>`__ for more details.