Comparing qcodes++ and QCoDeS
=============================

Things that are the same
------------------------

**1) All top level classes and functions in QCoDeS are directly inherited in qcodes++.** All of these behave exactly the same way as in QCoDeS, so you can use them without change. Even though Parameter and Station have additions, they do not change the functionality of the original classes, so you can use them as you would in QCoDeS.

**2) qcodes++ relies mainly on instrument drivers from QCoDes and the qcodes_contrib_drivers.** In fact the instrument drivers included in qcodes++ are hopefully only here temporarily, and will be pulled back into QCoDeS or the qcodes_contrib_drivers in the near future.

Small differences in existing classes:
--------------------------------------

**1) The ``Parameter`` class has the following additional functions:**

* ``.move()`` 'moves' the parameter to a new value in the given number of steps, without taking data. Useful if you want to set a sensitive parameter, e.g. a gate voltage, where using ``.set()`` could damage the sample.

* ``.sweep()`` same as in QCoDeS, but with the addition that if the start value of the sweep is different to the current value, it will warn the user.

* ``.logsweep()`` sweeps the parameter in a log10 scale.

* ``.returnsweep()`` sweeps the parameter up and down, i.e. first sweeps to the end value, then back to the start value.

* ``.arbsweep()`` accepts a list of a values, rather than a start and end value, and sweeps the parameter through these values.

**2) The ``Station`` class has the following additional functions:**

* Upon init, ``Station`` accepts the argument ``add_variables(vars)`` where ``vars`` can be e.g. ``globals()`` or ``locals()``. This feature looks through ALL previously declared variables within the vars, and if the varible is a Parameter or instance, it adds it to the Station. This means you don't have to do ``station.add_component()`` for every Instrument and Parameter. Just declare them before declaring the Station and use ``station = Station(add_variables=globals())``.

* ``.set_measurement(*actions)`` sets a series of actions (usually Parameters) to be performed when ``station.measure()`` is called.

* ``communication_time()`` measures the average time it takes to perform the action in ``.set_measurement()``.Typically this is just how long it takes to call the ``.get()`` functions of all the Parameters, giving you some idea of how long it takes the computer to communicate with the instruments.

Big differences
----------------

**1) The qcodes++ dataset, ``DataSetPP``, is a text-based dataset, where all the data is stored in numpy arrays.** The dataset is thus intrinsically much more limited than the QCoDeS dataset, since each array must be rectangular and store only one type of data. However, these 'limitations' have made it possible to develop the rich plotting capabilities of qcodes++. Knowing exactly what to expect (i.e. rectangular arrays filled with floats), we can really write general purpose plotting functions that work for all 1D and 2D dataset. Thus, if you only ever do 1D or 2D measurements, we think you will really enjoy the simplicity of qcodes++.

Indeed, the entire way of collecting data and setting up measurements is rather different. The best way to understand it is to check out the tutorials, starting from the `getting started <getting_started.html>`_ page.
