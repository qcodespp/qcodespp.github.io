More about Parameters
=====================

Parameters are the main way to interact with instruments in qcodes++. They represent a single value that can be set or read from an instrument. Parameters can be simple, like a voltage or current, or more complex, like a waveform or a list of values. Either way, they are more than just a number; the have units, labels and other properties that help to keep track of what they represent.

Custom parameters
-----------------
An incredibly common task is to perform mathematical operations on parameters, e.g. dividing a voltage by a current to get a resistance. However, one cannot simply multiply or divide parameters, since they are not just numbers, but objects with properties. Your computer has no way of knowing that if you divide a voltage by a current, you should get a resistance with unit Ohm. Instead, you can create a new parameter that is defined as a function of other parameters, where you can give it all this information. For example, to create a resistance parameter from a two Parameters named voltage and current, you can do:

.. code-block:: python

    resistance = qc.Parameter('resistance', unit='Ohm', label='Resistance',
                              get_cmd=lambda: voltage() / current())

where `lambda <https://docs.python.org/3/reference/expressions.html#lambda>`__ is a way to define a very simple function in python.

The more long form way to it (assuming now the voltage and current measurements come from different instruments) would be:

.. code-block:: python

    def get_resistance():
        return instrument1.voltage() / instrument2.current()

    resistance = qc.Parameter('resistance', unit='Ohm', label='Resistance',
                              get_cmd=get_resistance)

In both cases, we can see the parameter has a name, a unit, a label, and a get_cmd that defines how to get the value of the parameter. Parameters also accept a ``set_cmd`` argument, which defines how to set the value of the parameter, if relevant.

Defining custom get commands can also enable us to do things like averaging, filtering, or any other operation that is not directly supported by the instrument. e.g.

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

For the special case of a scaling a parameter, there is ``qc.ScaledParameter``, which accepts a base parameter and a scaling factor:

.. code-block:: python

    scaled_voltage = qc.ScaledParameter(instrument1.voltage,name='scaled_voltage', gain=1e-6,
                                        unit='uV', label='Scaled Voltage')

'Moving' Parameters
-------------------
Sometimes you want to sweep a parameter without taking data. This is Useful if you want to set a sensitive parameter, e.g. a gate voltage, where using ``.set()`` could damage the sample. For this you can use

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
MultiParameterWrapper enables easily setting, getting and sweeping multiple parameters. It is an extension of the MultiParameter from QCoDeS. To define it, simply provide a list of pre-existing parameters.

.. code-block:: python

    multi=qc.MultiParameterWrapper((parameter1,parameter2,parameter3),name='multi') 

You can get as usual with multi(), which will return the values for all of the parameters. To set, you can either provide the same number of values as the number of parameters, e.g. multi((0.1,490,5.6)), or a single value to set all contained parameters to the same value, e.g. multi(0)

To use it in a loop is just like for the standard Parameter except with multiple start and stop values corresponding to each parameter:

.. code-block:: python

    loop=qc.loop1d(sweep_param=multi,
                    start=(A,B,C),stop=(X,Y,Z),num=101,delay=0.1,
                    name='example') 

or if you want to sweep all contained parameters across the same values just provide a single value to each of start and stop.

.. code-block:: python

    loop=qc.loop1d(sweep_param=multi,
                    start=X,stop=Y,num=101,delay=0.1,
                    name='example') 

In the case that each parameter is sweeping different values, the resulting data.multi array will contain values from 0 to num-1, not the specified setpoints!! However, the parameters declared in MultiParameterWrapper will automatically be measured, meaning you will always know what the parameters were really doing, and can of course plot them.

One can also move the parameters

.. code-block:: python

    multi.move((0,0.1,4.5),steps=101,step_time=0.03)
    multi.move((0,0.1,4.5))
    multi.move(0)

If you provide a single value, all parameters will be moved to that single value. The parameters move sequentially, not simultaneously (in contrast to sweep where they move 'simultaneously')


Parameters inside Instruments
-----------------------------

How do I know which paramaters are available? There are many ways! If you kind of know what you're looking for, hit the tab key after typing the instrument name, e.g. ``instrument.`` and it will show you all the available functions of the instrument. Many of those functions will either be Parameters or SubModules. A SubModule might be a channel, and then the parameter you're interested in might be a part of that channel. This is the case for e.g. the Keithley 2600 Source Meters, since they have two channels. You need to do keithley.smua.volt() or keithley.smub.volt() to access the voltage parameter of the channel you're interested in.

You can list the Parameters of the instrument by running:

.. code-block:: python

    instrument.parameters

and the SubModules by running:

.. code-block:: python

    instrument.submodules

and of course the Parameters of any submodule by:

.. code-block:: python

    instrument.channel01.parameters

However, eventually you will be better off either reading the API for the driver (`here <https://microsoft.github.io/Qcodes/drivers_api/>`__  `here <https://qcodes.github.io/Qcodes_contrib_drivers/api/generated/qcodes_contrib_drivers.drivers.html>`__ or the source code. It's painful, I know, but it's still better than writing your own driver ;)