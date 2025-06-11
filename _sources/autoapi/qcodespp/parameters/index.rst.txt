qcodespp.parameters
===================

.. py:module:: qcodespp.parameters

.. autoapi-nested-parse::

   A collection of functions that get added to the QCoDeS Parameter class.

   In addition, two wrapper classes are provided to easily create ArrayParameters and MultiParameters.



Classes
-------

.. autoapisummary::

   qcodespp.parameters.ArrayParameterWrapper
   qcodespp.parameters.MultiParameterWrapper


Functions
---------

.. autoapisummary::

   qcodespp.parameters.move
   qcodespp.parameters.sweep
   qcodespp.parameters.logsweep
   qcodespp.parameters.arbsweep
   qcodespp.parameters.returnsweep
   qcodespp.parameters.set_data_type


Module Contents
---------------

.. py:function:: move(self, end_value, steps=101, step_time=0.03)

   Move the parameter to a new value in a number of steps without taking data.

   Args:
       end_value (float): The value to move to.

       steps (int, optional): Number of steps to take. Defaults to 101.

       step_time (float, optional): Time in seconds between each step. Defaults to 0.03.


.. py:function:: sweep(self, start, stop, step=None, num=None, print_warning=True)

   Create a collection of parameter values to be iterated over.

   Requires `start` and `stop` and (`step` or `num`)
   The sign of `step` is not relevant.

   Args:
       start (Union[int, float]): The starting value of the sequence.

       stop (Union[int, float]): The end value of the sequence.

       step (Optional[Union[int, float]]):  Spacing between values.

       num (Optional[int]): Number of values to generate.

   Returns:
       SweepFixedValues: collection of parameter values to be iterated over

   Examples:
       >>> sweep(0, 10, num=5)
        [0.0, 2.5, 5.0, 7.5, 10.0]
       >>> sweep(5, 10, step=1)
       [5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
       >>> sweep(15, 10.5, step=1.5)
       >[15.0, 13.5, 12.0, 10.5]


.. py:function:: logsweep(self, start, stop, num=None, print_warning=True)

   Create a collection of parameter values to be iterated over in a log scale

   Requires `start` and `stop` and or `num`. Note that `step` cannot be used here.

   Args:
       start (Union[int, float]): The starting value of the sequence.

       stop (Union[int, float]): The end value of the sequence.

       num (Optional[int]): Number of values to generate.

   Returns:
       SweepFixedValues: collection of parameter values to be iterated over


.. py:function:: arbsweep(self, setpoints, print_warning=True)

   Create a collection of parameter values to be iterated over from a list of arbitrary values.

   Args:
       setpoints (list or array): The setpoints to sweep over.

   Returns:
       SweepFixedValues: collection of parameter values to be iterated over

   Example:
       >>> values = [0.0, 2.5, 5.0, 7.5, 10.0]
       >>> loop=qc.Loop(parameter.arbsweep(values),delay=0.1).each(*station.measure())


.. py:function:: returnsweep(self, start, stop, step=None, num=None, print_warning=True)

   Create a collection of parameter values to be iterated over,
   where the parameter sweeps from `start` to `stop` and then back up to `start`.

   The total number of points will be `2*num-1` if `num` is provided,
   or `2*(stop-start)/step+1` if `step` is provided.

   Args:
       start (Union[int, float]): The starting value of the sequence.

       stop (Union[int, float]): The end value of the sequence.

       step (Optional[Union[int, float]]):  Spacing between values.

       num (Optional[int]): Number of values to generate.

   Returns:
       SweepFixedValues: collection of parameter values to be iterated over


.. py:function:: set_data_type(self, data_type=float)

   Should no longer be necessary: marked for deprecation.

   Set the data type of the parameter. Gets passed to DataArray and the underlying numpy ndarray.

   Args:
       data_type : The data type of the parameter. Can be 'float' or 'str'.


.. py:class:: ArrayParameterWrapper(name=None, label=None, unit=None, instrument=None, shape=None, get_cmd=None)

   Bases: :py:obj:`qcodes.parameters.ArrayParameter`


   Wrapper to easily declare ArrayParameters.

   Args:
       name (str, optional): Name of the ArrayParameter. Defaults to None.

       label (str, optional): Label for the ArrayParameter. Defaults to None.

       unit (str, optional): Unit for the ArrayParameter. Defaults to None.

       instrument (Instrument, optional): Instrument this ArrayParameter belongs to. Defaults to None.

       shape (tuple, optional): Shape of the array. If not provided, it will be inferred from the get_cmd.

       get_cmd (callable, optional): Function that returns the array data. If provided, shape will be inferred from its output.

   Usage:
       Example usage where an instrument has a get_buffer() function which returns an array

       VoltageBuffer=qc.ArrayParameterWrapper(name='VoltageBuffer',
                                           label='Voltage',
                                           unit='V',
                                           get_cmd=VoltageInstrument.get_buffer)


.. py:class:: MultiParameterWrapper(parameters, name=None, instrument=None)

   Bases: :py:obj:`qcodes.parameters.MultiParameter`


   Class to wrap multiple pre-existing parameters into MultiParameter. Enables getting, setting, sweeping and moving.

   Args:
       parameters (list or tuple): List of Parameters to wrap.

       name (str, optional): Name of the MultiParameter.

       instrument (Instrument, optional): Instrument this MultiParameter belongs to, if any.

   Examples:
       multi_param = MultiParameterWrapper((param1, param2, param3), name='multi_param', instrument=my_instrument)

       Get values
       >>> values = multi_param()

       Set all constituent parameters to the same value
       >>> multi_param(value)

       Set each parameter to different values
       >>> multi_param([1.0, 2.0, 3.0])

       Move to new values
       >>> multi_param.move([new_value1, new_value2, new_value3])

       Sweeping all parameters with the same start and stop values
       >>> multi_param.sweep(start_val, stop_val, num=num)

       Sweeping each parameter with different start and stop values
       >>> multi_param.sweep([start_val1, start_val2], [stop_val1, stop_val2], num=num)

       When used in a qcodespp Loop, if all parameters are swept with the same values, 
       the setpoint array will be the setpoints.
       If the parameters are swept with different values, the setpoints will be indices, 
       and the constituent parameters will be automatically added to the measurement, so that 
       each parameter gets measured at each setpoint.


   .. py:attribute:: parameters


   .. py:attribute:: labels
      :value: ()



   .. py:attribute:: units
      :value: ()



   .. py:method:: get_raw()

      ``get_raw`` is called to perform the actual data acquisition from the
      instrument. This method should either be overwritten to perform the
      desired operation or alternatively for :class:`.Parameter` a
      suitable method is automatically generated if ``get_cmd`` is supplied
      to the parameter constructor. The method is automatically wrapped to
      provide a ``get`` method on the parameter instance.



   .. py:method:: set_raw(values)

      ``set_raw`` is called to perform the actual setting of a parameter on
      the instrument. This method should either be overwritten to perform the
      desired operation or alternatively for :class:`.Parameter` a
      suitable method is automatically generated if ``set_cmd`` is supplied
      to the parameter constructor. The method is automatically wrapped to
      provide a ``set`` method on the parameter instance.



   .. py:method:: move(end_values, steps=101, step_time=0.03)


   .. py:method:: sweep(start_vals, stop_vals, num)


