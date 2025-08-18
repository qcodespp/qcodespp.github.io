Parameters
==========

A ``Parameter`` represent a single value that can be set or read from an instrument. A ``Parameter`` can be simple, like a voltage or current, or more complex, like a waveform or a list of values. Either way, they are more than just a number; the have units, labels and other properties that help to keep track of what they represent. See `the QCoDeS documentation <https://microsoft.github.io/Qcodes/examples/Parameters/Parameters.html>`__ for more information.

Custom parameters
-----------------
An incredibly common task is to perform mathematical operations on ``Parameter`` s, e.g. dividing a voltage by a current to get a resistance. However, one cannot simply multiply or divide ``Parameter`` s like ``param1*param2``, since they are not just numbers, but objects with properies. You need to also tell the computer that if you divide a voltage by a current, you should get a resistance with unit Ohm. To do this, you create a new ``Parameter``, with the relevant labels and units, and provide (a) function(s) to get and set the new ``Parameter`` s. For example, to create a resistance ``Parameter`` from a two ``Parameter`` s named voltage and current, you can do:

.. code-block:: python

    resistance = qc.Parameter('resistance', unit='Ohm', label='Resistance',
                              get_cmd=lambda: voltage() / current())

where `lambda <https://docs.python.org/3/reference/expressions.html#lambda>`__ is a way to define a very simple function in python.

This is equivalent to:

.. code-block:: python

    def get_resistance():
        return voltage() / current()

    resistance = qc.Parameter('resistance', unit='Ohm', label='Resistance',
                              get_cmd=get_resistance)

Defining a custom ``get_cmd`` enables e.g. averaging, filtering, or any other operation that is not directly supported by the instrument.

.. code-block:: python

    import numpy as np
    import time

    def get_average_voltage():
        # Average as many readings as possible over 1 second
        voltages=[]
        start_time = time.time()
        while time.time() - start_time < 1:
            voltages.append(instrument1.voltage())
        return np.mean(voltages)

    average_voltage = qc.Parameter('average_voltage', unit='V', label='Average Voltage',
                                   get_cmd=get_average_voltage)

``Parameter`` s also accept a ``set_cmd`` argument, which defines how to set the value of the ``Parameter``, if relevant.

.. code-block:: python

    def set_feed(value):
        # Set the instrument output to a value scaled by the value at its input
        intrument.output(value * instrument.input())

    def get_feed():
        # Get the instrument output scaled by the value at its input
        return instrument.output() / instrument.input()

    feedparam = qc.Parameter('feedparam', unit='V', label='Voltage',
                              get_cmd=get_feed, set_cmd=set_feed)

`You can fully subclass <https://microsoft.github.io/Qcodes/examples/Parameters/Parameters.html>`__ the ``Parameter`` class, especially if you want to add more complex functionality, store information within the ``Parameter``, etc. If you create an attribute in your subclass, e.g. ``my_parameter.my_attribute = 'my_value'`` that you want to be saved in the ``DataSetPP`` metadata, extend ``my_parameter._meta_attrs`` with the attribute name, e.g. ``my_parameter._meta_attrs.append('my_attribute')``, ``my_parameter._meta_attrs.extend(['my_attribute1','my_attribute2','my_attribute3'])``.

Stepper Parameter: Sweeping time
--------------------------------

To loop over time, i.e. measure parameters at a regular interval without another independent parameter, qcodes++ provides a ``stepper`` parameter.

.. code-block:: python

    from qcodespp.parameters import stepper

In a loop, simply use ``stepper`` as the ``sweep_parameter`` and increment from e.g. 0 to 100 in 101 steps, and choose a suitable ``delay`` to define the measurement interval. If you want to measure as fast as possible, set the ``delay`` to e.g. 0.001; setting it to 0 can sometimes cause problems.

.. code-block:: python

    loop=qc.loop1d(sweep_param=stepper,
                    start=0,stop=100,num=101,delay=0.1,
                    name='example')

By default, the time since the start of the ``Loop`` is included in each ``DataSetPP`` as ``timer``, meaning you can always plot any parameter against time, including in `live plotting <https://qcodespp.github.io/live_plot.html>`__.

Scaling Parameters
------------------

For the special case of a scaling a parameter, there is ``qc.ScaledParameter``, which accepts a ``Parameter`` to scale and a scaling factor, which can be a scalar or a ``Parameter`` (`QCoDes docs <https://microsoft.github.io/Qcodes/api/parameters/index.html#qcodes.parameters.ScaledParameter>`__):

.. code-block:: python

    scaled_voltage = qc.ScaledParameter(instrument1.voltage,name='scaled_voltage', gain=1e-6,
                                        unit='uV', label='Scaled Voltage')

'Moving' Parameters
-------------------
Sometimes you want to sweep a parameter without taking data. This is useful if you want to set a sensitive parameter, e.g. a gate voltage, where using ``.set()`` could damage the sample. For this you can use

.. code-block:: python

    parameter.move(end_value,steps=101,step_time=0.03)

for example

.. code-block:: python

    k2400.volt.move(-1,steps=500,step_time=0.05)

or if you are happy with the default step number (101) and time (0.03 s), simply

.. code-block:: python

    k2400.volt.move(-0.25)

MultiParameter and MultiParameterWrapper
----------------------------------------
``MultiParameterWrapper`` enables easily setting, getting and sweeping multiple parameters. It is an extension of the ``MultiParameter`` `from QCoDeS <https://microsoft.github.io/Qcodes/examples/Parameters/MultiParameter.html>`__. To define it, simply provide a list of pre-existing parameters.

.. code-block:: python

    multi=qc.MultiParameterWrapper((parameter1,parameter2,parameter3),name='multi') 

You can get as usual with ``multi()``, which will return the values for all of the parameters. To set, you can either provide the same number of values as the number of parameters, e.g. ``multi((0.1,490,5.6))``, or a single value to set all contained parameters to the same value, e.g. multi(0)

To use it in a ``Loop``, provide multiple ``start`` and ``stop`` values, corresponding to each 
``Parameter``:

.. code-block:: python

    loop=qc.loop1d(sweep_param=multi,
                    start=(A,B,C),stop=(X,Y,Z),num=101,delay=0.1,
                    name='example') 

or if you want all contained ``Parameter`` s to sweep across the same values, simply provide a single value to each of ``start`` and ``stop``.

.. code-block:: python

    loop=qc.loop1d(sweep_param=multi,
                    start=X,stop=Y,num=101,delay=0.1,
                    name='example') 

In the case that each ``Parameter`` is sweeping different values, the resulting data.multi array will contain values from 0 to num-1, not the specified setpoints!! However, the parameters declared in MultiParameterWrapper will automatically be measured, meaning you will always know what the parameters were really doing, and can of course plot them.

One can also move the parameters

.. code-block:: python

    multi.move((0,0.1,4.5),steps=101,step_time=0.03)
    multi.move((0,0.1,4.5))
    multi.move(0)

If you provide a single value, all parameters will be moved to that single value. The parameters move sequentially, not simultaneously (in contrast to sweep where they move 'simultaneously')

Non-numerical Parameters
------------------------
If your parameter returns floats, integers or booleans, or arrays of any of these, the ``DataSetPP`` will store them just fine. However, if your parameter returns a string, you need to set a the ``data_type`` attribute of the parameter to ``str``. e.g. ``my_parameter.data_type = str``.

Storing of more complex objects such as dictionaries in the ``DataSetPP`` is not supported and probably never will be. If your instrument driver is returning such objects, make a custom ``Parameter`` (or ``MultiParameter``) to return arrays or tuples of floats and/or strings.