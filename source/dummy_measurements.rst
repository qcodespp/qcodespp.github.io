Getting started
===============

In the following we will set up a Jupyter notebook to collect and plot data from a dummy instrument to understand the basic usage of qcodes++. No measurement hardware is required.

Setup
-----
Assuming you installed qcodes++ as described in the `installation instructions <installation.html>`_, you can start Jupyter lab from the Anaconda prompt or command line by activating the environment::

    conda activate qcodespp

and starting Jupyter lab::

    jupyter lab

This will open a Jupyter lab window in your browser. In the Jupyter lab, create a new Python 3 notebook and copy the following code into it

.. code-block:: python

    import qcodespp as qc   
    from qcodespp.instrument_drivers.dummy import DummyMeasurementInstrument

This code imports the top level of the qcodes++ package, and the DummyInstrument driver. In general the instrument drivers are python classes which can be used to create a specific connection with a specific instrument. In this case, we can easily 'connect' to our DummyInstrument by running:

.. code-block:: python

    instrument = DummyMeasurementInstrument(name='instrument')

As discussed in the `background <background.html>`_ section, qcodes has a virtual ``Station`` which contains all the instruments and parameters. We can initialise the Station and add our instrument to it by running:

.. code-block:: python

    station = qc.Station(add_variables(globals()))

This command creates a Station object and checks all the python variables defined in the notebook. If the variable is a qcodes Instrument or Parameter, it is added to the Station.

We should also tell qcodes where to save the data. This is done by running:

.. code-block:: python

    qc.set_data_folder('data')

Getting and setting parameters
------------------------------

The dummy instrument has two outputs for providing voltages, and two inputs for measuring voltages from the imaginary device. You can set the output by putting a number in brackets, e.g.

.. code-block:: python

    instrument.output1(1.0)

or

.. code-block:: python

    instrument.output2(1.56)

and read the value it is set to by leaving the brackets empty, e.g.

.. code-block:: python

    instrument.output1()

or

.. code-block:: python

    instrument.output2()

To read the input values, again use empty brackets, e.g.

.. code-block:: python

    instrument.input1()

or 

.. code-block:: python

    instrument.input2()

Running a measurement
----------------------
So far no data has been collected; we've just communicated with the instrument. To collect data, we need to create a `Loop` object, which defines the independent parameter(s) that we want to vary. In this case, we will vary the output1 parameter from 0 to 10 volts in steps of 1 volt, and measure the input1 parameter at each step. We can do this by running: