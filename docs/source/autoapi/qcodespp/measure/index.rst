qcodespp.measure
================

.. py:module:: qcodespp.measure


Classes
-------

.. autosummary::

   qcodespp.measure.Measure


Module Contents
---------------

.. py:class:: Measure(*measure, setpoints=None, use_threads=False, station=None, name=None, use_timer=False)

   Bases: :py:obj:`qcodes.metadatable.Metadatable`


   Create a ``DataSetPP`` from a single (non-looped) set of measured parameters.

   ``Measure`` is used to measure a set of parameters at a single point in time.
   The typical use case is where the parameter(s)'s get function(s) return(s) an array, e.g. 
   an oscilloscope trace, or a spectrum analyser trace. 
   The array shape(s) do not need to be known and can change between measurements.
   The parameters to be measured are provided at init or through station.set_measurement().
   Optionally, setpoints may be provided, but this is usually not required nor recommended.
   If no setpoints are provided, dummy setpoints are created for each dimension found in the 
   measured parameters (recommended, see Args documentation below).

   ``Measure.run()`` executes the measurement, and returns and saves a ``DataSetPP``

   Examples:
       Measure two parameters:

       >>> station.set_measurement(array_param1, array_param2)
       >>> data = Measure(name='Name for dataset filename').run()

       Measure two parameters twice, changing some value in between:

       >>> station.set_measurement(array_param1, array_param2)
       >>> measure = Measure()
       >>> data=measure.run(name='instrument parameter value = 0')
       >>> instrument.some_parameter(1.0)  # Set some parameter to a value
       >>> data=measure.run(name='instrument parameter value = 1')

       Iteratively:

       >>> station.set_measurement(array_param1, array_param2)
       >>> measure = Measure()
       >>> for i in range(10):
       >>>     instrument.some_parameter(i)  # Set some parameter to a value
       >>>     data=measure.run(name=f'iteration {i}')

   Args:
       *measure (Optional, Sequence[Parameter]): Sequence of gettable Parameters.
           If no actions are provided, the default station.measure() is used.

       name (Optional, str): String to send to the filename of the DataSet.

       setpoints (Optional, Sequence[Parameter or Array]): sequence of setpoint arrays
           use for the DataSetPP. Can be array(s) of values, or gettable Parameter(s). 
           If not provided, dummy setpoints are created for each dimension found in the parameters.
           Providing a setpoint parameter may be useful if you measure a parameter that is considered the 
           independent variable. e.g. time on an oscilloscope, or a voltage ramp on a source. live_plot 
           and offline_plotting will then be able to plot the correct dependencies automatically. However; 
           it can be tricky to get all the dimensions right, so in most instances it's better to just pass 
           all measured parameters to the parameters argument, and then plot whatever parameter against 
           whatever other parameter manually.

       station (Optional, Station): The ``Station`` to use if not the default.

       use_threads (Optional, bool): Use threading to parallelize getting parameters from instruments.

       use_timer (Optional, bool, default False): The default station.measure() includes a timer parameter, 
           which is useful for Loops but essentially useless here. If you really want it, set use_timer=True.


   .. py:attribute:: station


   .. py:attribute:: use_threads
      :value: False



   .. py:attribute:: setpoints
      :value: None



   .. py:attribute:: name
      :value: None



   .. py:attribute:: use_timer
      :value: False



   .. py:attribute:: actions
      :value: ()



   .. py:method:: each(*actions)

      Set the actions to be performed in this measurement.

      Actions can be added during init, however this method is provided to make the Measure class 
      look like a Loop, where actions are added with .each(), and it makes somehow sense gramatically.

      Args:
          actions: a sequence of actions to perform. Any action that is
              valid in a ``Loop`` can be used here. If an action is a gettable
              ``Parameter``, its output will be included in the DataSetPP.
              If no actions are provided, the default station.measure() is used.



   .. py:method:: run_temp(**kwargs)

      Wrapper to run this measurement as a temporary data set



   .. py:method:: run(plot=None, name=None, use_threads=None, quiet=False, station=None, **kwargs)

      Run the actions in this measurement and return their data as a DataSetPP

      Args:
          plot (Optional[Sequence[Parameter,str]]): a list of parameters to plot. 
              Provide the parameter, or parameter full_name as a string.

          name (Optional[str]): Filename, minus counter, date and time.
              Overwrites any name provided at init.

          quiet (Optional[bool]): Set True to not print anything except
              errors. Default False.

          station (Optional[Station]): the ``Station`` this measurement
              pertains to. Defaults to ``Station.default`` if one is defined.
              Only used to supply metadata.

          use_threads (Optional[bool]): whether to parallelize ``get``
              operations using threads. Default False.

          kwargs are passed to data_set.new_data. The key ones are:

          location (Optional[Union[str, False]]): the location of the
              DataSetPP, a string whose meaning depends on formatter and io,
              or False to only keep in memory. May be a callable to provide
              automatic locations. If omitted, will use the default
              DataSetPP.location_provider

          formatter (Optional[Formatter]): For writing to file. Default 
              is GnuplotFormat, can be set in DataSetPP.default_formatter

          io (Optional[io_manager]): io manager for DataSetPP object.

      returns:
          a DataSetPP object containing the results of the measurement



   .. py:method:: snapshot_base(update=False)

      Override this with the primary information for a subclass.



