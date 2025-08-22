Commonly used features
======================

station.set_measurement()
-------------------------

Instead of repeatedly supplying the ``measure`` argument to the loops, especially if you have many parameters, which you want to keep identical over many measurements, you can use the ``Station`` to store default measurement parameters. This is done by running:

.. code-block:: python

    station.set_measurement(instrument.input1, instrument.input2)

Now you do not need to specify ``measure`` in ``loop1d``, ``loop2d``, ``loop2dUD``.

Looping over time
-----------------
Often, you will want to monitor your parameters' evolution over time. To do this, make a custom 'stepper' ``Parameter`` to loop over, `as outlined here <https://qcodespp.github.io/parameters.html#stepper-parameter>`__.

Other kinds of actions
----------------------

The primary purpose of ``measure`` and ``station.set_measurement()`` is of course to tell qcodes++ what to measure. `However, what these functions are *really* doing is telling the loop to perform certain actions <advanced.html>`__. If the action is a parameter, then the loop performs parameter() and stores the data. However, there are other options:

Tasks
^^^^^

Within loops, you can also perform a ``qc.Task``, which is a method for introducing functions into the loop. For example, you could wait until your setup has reached a certain temperature before measuring the parameters using

.. code-block:: python

    def waitfortemp():
        while numpy.abs(instrument.measured_temp()-instrument.setpoint())>0.01:
            time.sleep(5)

    station.set_measurement(qc.Task(waitfortemp),param1,param2)

The loop will wait at each point for the measured temperature to be within 10 mK of the setpoint.

If the function requires arguments, pass them with e.g. ``qc.Task(function_name,0.02)``, not ``qc.Task(function_name(0.02))``. Note however that the function is only evaluated once, at loop definition, and is not evaluated at each point of the loop.

In ``loop2d`` and ``loop2dUD``, you can also to perform actions at each step of the step_parameter by using the ``step_action`` argument. For example, if you want to wait for the temperature to stabilise at each step of the step_parameter, you can do:

.. code-block:: python

    loop=qc.loop2d(sweep_parameter=instrument.output1,
                    start=0,stop=10,num=11,delay=0.1,
                    step_parameter=instrument.temperate_setpoint,
                    step_start=0,step_stop=10,step_num=11,step_delay=0.1,
                    device_info='dummy',
                    instrument_info='ACdiv=1e5 DCdiv=1e3 freq=123 Hz',
                    measure=[instrument.input1, instrument.input2, instrument.measured_temp],
                    step_action=qc.Task(waitfortemp))

Note how in this case, the task is not a part of the ``measure`` argument, (nor ``station.set_measurement()``), since we only want to run the task immediately after the step_parameter is set, not at every point of the sweep_parameter.

BreakIf
^^^^^^^

``qc.BreakIf`` allows the loop to be automatically stopped if a certain condition occurs. For example, if you are supplying a gate voltage and monitoring leakage current, and want to ensure leakage current doesn't exceed a certain value.

.. code-block:: python

    station.set_measurement(qc.BreakIf(lambda: np.abs(k1.curr())>2e-9),param1,param2)

``lambda`` is used to turn the statement ``k1.curr()>2e-9`` into a function with a Boolean output. You can also include ``BreakIf`` directly in the ``measure`` argument. You can also use ``or``, ``and``, etc

.. code-block:: python

    station.set_measurement(qc.BreakIf(lambda: np.abs(k1.curr())>2e-9 or np.abs(k2.curr())>1e-9))

If the loop gets broken during ``loop.run()``, ``loop.was_broken`` turns True. You can use this fact to automatically do something smart in the case of the loop breaking.

.. code-block:: python

    loop.run()
    if loop.was_broken:
        k1.volt.move(0)

See `the page on Parameters <parameters.html>`__ for more information about the ``move`` function.