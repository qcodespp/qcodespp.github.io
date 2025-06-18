qcodespp
========

.. py:module:: qcodespp


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/qcodespp/actions/index
   /autoapi/qcodespp/data/index
   /autoapi/qcodespp/instrument_drivers/index
   /autoapi/qcodespp/loops/index
   /autoapi/qcodespp/measure/index
   /autoapi/qcodespp/parameters/index
   /autoapi/qcodespp/plotting/index
   /autoapi/qcodespp/station/index
   /autoapi/qcodespp/utils/index
   /autoapi/qcodespp/version/index


Attributes
----------

.. autosummary::

   qcodespp.config
   qcodespp.__version__


Classes
-------

.. autosummary::

   qcodespp.Station
   qcodespp.Loop
   qcodespp.Measure
   qcodespp.Task
   qcodespp.Wait
   qcodespp.BreakIf
   qcodespp.Plot
   qcodespp.MultiParameterWrapper
   qcodespp.ArrayParameterWrapper


Functions
---------

.. autosummary::

   qcodespp.loop1d
   qcodespp.loop2d
   qcodespp.loop2dUD
   qcodespp.live_plot
   qcodespp.offline_plotting
   qcodespp.new_data
   qcodespp.load_data
   qcodespp.load_data_num
   qcodespp.load_data_nums
   qcodespp.set_data_format
   qcodespp.set_data_folder
   qcodespp.listVISAinstruments


Package Contents
----------------

.. py:data:: config
   :type:  qcodes.configuration.Config

.. py:class:: Station(*components: qcodes.metadatable.MetadatableWithName, add_variables: Any = None, config_file: str | Sequence[str] | None = None, use_monitor: bool | None = None, default: bool = True, update_snapshot: bool = True, inc_timer: bool = True, **kwargs: Any)

   Bases: :py:obj:`qcodes.Station`


   A representation of the physical measurement setup/station.

   This class is a wrapper around the QCoDeS Station class, adding functionality
   for automatic addition of instruments and parameters, and providing a
   measurement method that can be used to measure parameters in the station.

   Args:
       components: List of Instruments, Parameters, or other components to add to the station.

       add_variables: Automatically adds previously defined Instruments and Parameters to the station.
       Typically, add_variables=globals() to look through all previously defined variables.

       config_file: Path to YAML files to load the station config from.
           - If only one yaml file needed to be loaded, it should be passed
             as a string, e.g., '~/station.yaml'
           - If more than one yaml file needed, they should be supplied as
             a sequence of strings, e.g. ['~/station1.yaml', '~/station2.yaml']

       use_monitor: Should the QCoDeS monitor be activated for this station.

       default: Is this station the default?

       update_snapshot: Immediately update the snapshot of each component as it is added to the Station.

       inc_timer: Include a timer parameter in the station and the default measurement.



   .. py:attribute:: components
      :type:  dict[str, qcodes.metadatable.MetadatableWithName]


   .. py:attribute:: use_monitor
      :value: None



   .. py:attribute:: default_measurement
      :type:  List
      :value: []



   .. py:method:: auto_add(variables, add_instruments: bool = True, add_parameters: bool = True, update_snapshot: bool = True)

      Automatically add previously defined instruments and parameters to the station. Usually, auto_add=globals().

      Args:
          variables: Dictionary of variables to check for Instruments and Parameters. e.g. globals(), locals(), etc.
          
          add_instruments: If True, add Instruments to the station.
          
          add_parameters: If True, add Parameters to the station.
          
          update_snapshot: If True, update the snapshot of each component as it is added to the Station.



   .. py:method:: snapshot_base(update: bool = False, params_to_skip_update: Sequence[str] = None) -> dict

      State of the station as a JSON-compatible dict.

      Note: in the station contains an instrument that has already been
      closed, not only will it not be snapshotted, it will also be removed
      from the station during the execution of this function.

      Args:
          update (bool): If True, update the state by querying the
           all the children: f.ex. instruments, parameters, components, etc.
           If False, just use the latest values in memory.

      Returns:
          dict: base snapshot



   .. py:method:: set_measurement(*actions, check_in_station=True)

      Save a set of ``*actions``` as the default measurement for this Station.

      These actions will be executed by default by a Loop if this is the
      default Station, and any measurements among them can be done once
      by .measure

      Args:
          *actions: parameters to set as default  measurement



   .. py:method:: communication_time(measurement_num=5, return_average=True)

      Estimate how long it takes to communicate with the instruments in the station.

      Args:
          measurement_num: Number of measurements to take to estimate the communication time.
              Default is 1, but can be set to a higher number for more accurate estimates.
          return_average: Whether to return the average of the measurements or the entire list.
      Returns:
          Either the average communication time or the list of communication times for each measurement.



   .. py:method:: measurement(*actions)

      Measure the default measurement, or parameters in actions.

      Args:
          *actions: parameters to mesure



   .. py:method:: measure(*actions, timer=None)

      Pass the default measurement to a loop after previously setting it with set_measurement.

      Example:
          station.set_measurement(param1, param2)
          loop = Loop(instrument.parameter.sweep(1, 10, 1),delay=0.1).each(*station.measure())



   .. py:method:: __getitem__(key)

      Shortcut to components dict.



   .. py:attribute:: delegate_attr_dicts
      :value: ['components']


      A list of names (strings) of dictionaries
      which are (or will be) attributes of ``self``,
      whose keys should be treated as attributes of ``self``.



.. py:data:: __version__
   :value: '0.1.2'


.. py:class:: Loop(sweep_values, delay=0, snake=False, station=None, progress_interval=None, progress_bar=True)

   Bases: :py:obj:`qcodes.utils.metadata.Metadatable`


   Create a measurement loop to sweep over a parameter and store measured data from other
   parameters. The results are stored in a qcodespp.data.data_set.DataSetPP container.

   Args:
       sweep_values: a SweepValues or compatible object describing what
           parameter to set in the loop and over what values
       delay: a number of seconds to wait after setting a value before
           continuing. 0 (default) means no waiting and no warnings. > 0
           means to wait, potentially filling the delay time with monitoring,
           and give an error if you wait longer than expected.
       progress_interval: show progress of the loop every x seconds. Default
           is None (no output)

   After creating a Loop, you attach one or more ``actions`` to it, making an
   ``ActiveLoop``

   ``actions`` is a sequence of things to do at each ``Loop`` step: that can be
   a ``Parameter`` to measure, a ``Task`` to do (any callable that does not
   yield data), ``Wait`` times, or another ``ActiveLoop`` or ``Loop`` to nest
   inside this one.


   .. py:attribute:: sweep_values


   .. py:attribute:: delay
      :value: 0



   .. py:attribute:: station
      :value: None



   .. py:attribute:: nested_loop
      :value: None



   .. py:attribute:: actions
      :value: None



   .. py:attribute:: then_actions
      :value: ()



   .. py:attribute:: bg_task
      :value: None



   .. py:attribute:: bg_final_task
      :value: None



   .. py:attribute:: bg_min_delay
      :value: None



   .. py:attribute:: progress_interval
      :value: None



   .. py:attribute:: progress_bar
      :value: True



   .. py:attribute:: snake
      :value: False



   .. py:method:: __getitem__(item)

      Retrieves action with index `item`

      Args:
          item: actions index

      Returns:
          loop.actions[item]



   .. py:method:: loop(sweep_values, delay=0)

      Nest another loop inside this one.

      Args:
          sweep_values ():
          delay (int):

      Examples:
          >>> Loop(sv1, d1).loop(sv2, d2).each(*a)

          is equivalent to:

          >>> Loop(sv1, d1).each(Loop(sv2, d2).each(*a))

      Returns: a new Loop object - the original is untouched



   .. py:method:: each(*actions)

      Perform a set of actions at each setpoint of this loop.

      Args:
          *actions (Any): actions to perform at each setpoint of the loop

      Each action can be:

      - a Parameter to measure
      - a Task to execute
      - a Wait
      - another Loop or ActiveLoop




   .. py:method:: with_bg_task(task, bg_final_task=None, min_delay=0.01)

      Attaches a background task to this loop.

      Args:
          task: A callable object with no parameters. This object will be
              invoked periodically during the measurement loop.

          bg_final_task: A callable object with no parameters. This object will be
              invoked to clean up after or otherwise finish the background
              task work.

          min_delay (default 0.01): The minimum number of seconds to wait
              between task invocations.
              Note that if a task is doing a lot of processing it is recommended
              to increase min_delay.
              Note that the actual time between task invocations may be much
              longer than this, as the task is only run between passes
              through the loop.



   .. py:method:: validate_actions(*actions)
      :staticmethod:


      Whitelist acceptable actions, so we can give nice error messages
      if an action is not recognized



   .. py:method:: run(*args, **kwargs)

      shortcut to run a loop with the default measurement set
      stored by Station.set_measurement



   .. py:method:: run_temp(*args, **kwargs)

      shortcut to run a loop in the foreground as a temporary dataset
      using the default measurement set



   .. py:method:: then(*actions, overwrite=False)

      Attach actions to be performed after the loop completes.

      These can only be ``Task`` and ``Wait`` actions, as they may not generate
      any data.

      returns a new Loop object - the original is untouched

      This is more naturally done to an ActiveLoop (ie after .each())
      and can also be done there, but it's allowed at this stage too so that
      you can define final actions and share them among several ``Loops`` that
      have different loop actions, or attach final actions to a Loop run

      TODO:
          examples of this ? with default actions.

      Args:
          *actions: ``Task`` and ``Wait`` objects to execute in order

          overwrite: (default False) whether subsequent .then() calls (including
              calls in an ActiveLoop after .then() has already been called on
              the Loop) will add to each other or overwrite the earlier ones.
      Returns:
          a new Loop object - the original is untouched



   .. py:method:: snapshot_base(update=False)

      State of the loop as a JSON-compatible dict.

      Args:
          update (bool): If True, update the state by querying the underlying
           sweep_values and actions. If False, just use the latest values in
           memory.

      Returns:
          dict: base snapshot



.. py:function:: loop1d(sweep_parameter, start, stop, num, delay, device_info='', instrument_info='', measure=None, plot=None, run=False)

   Create a 1D loop, the associated data set, and optionally, live plotting.

   A 1D loop has a single independent parameter, swept over a range of values.
   At each point in the loop, a set of parameters is measured, either those
   given as the argument measure, or the default measurement set by
   station.set_measurement

   In addition to creating the loop, this function also
   initiates the data set and live plotting window.

   Args:
       sweep_parameter (Parameter): The qcodes parameter to sweep over.

       start (float): the start value of the sweep.

       stop (float): the stop value of the sweep.

       num (int): the number of points in the sweep.

       delay (float): the number of seconds to wait after setting a value before measuring.

       device_info (str): a string with information about the device

       instrument_info (str): a string with information about the setup that will not
           be captured by the metadata (e.g. voltage dividers, preamp settings)

       measure (list): a list of parameters to measure at each point in the
           loop. If None, will use the default measurement set by the default station

       plot (list): a list of parameters to plot at each point in the loop.

       run (bool, default False): run the loop immediately after creation.

   Returns:
       The ActiveLoop. The data is accessible as loop.data_set. This can then be used
           for plotting, if necessary, e.g. pp=qc.live_plot(loop.data_set,params_to_plot)


.. py:function:: loop2d(sweep_parameter, start, stop, num, delay, step_parameter, step_start, step_stop, step_num, step_delay, snake=False, step_action=None, device_info='', instrument_info='', measure=None, plot=None, run=False)

   Create a 2D loop, the associated data set, and optionally, live plotting.

   A 2D loop has two independent parameters, a 'sweep' parameter and a 'step' parameter.
   At each point in the step parameter, the sweep parameter performs a loop.

   Args:
       sweep_parameter (Parameter): The qcodes parameter to sweep over.

       start (float): the start value of the sweep.

       stop (float): the stop value of the sweep.

       num (int): the number of points in the sweep.

       delay (float): the number of seconds to wait after setting a value before
           measuring.

       step_parameter (Parameter): The parameter to step over.

       step_start (float): the start value of the step.

       step_stop (float): the stop value of the step.

       step_num (int): the number of points in the step.

       step_delay (float): the number of seconds to wait after setting a value before
           starting the inner loop.

       snake (bool, default False): Whether to run a normal raster scan (False) or a snake scan (True). If True, the inner loop will
           be run in reverse order on every other step of the outer loop.

       step_action: an action (e.g. qcodes Task) to run at each point in the step loop AFTER the step parameter
           has been set, but BEFORE the inner loop starts

       device_info (str): a string with information about the device

       instrument_info (str): a string with information about the setup that will not
           be captured by the metadata (e.g. voltage dividers, preamp settings)

       measure (list): a list of parameters to measure at each point in the
           loop. If None, will use the default measurement set by the default station

       plot (list): a list of parameters to plot at each point in the loop.

       run (bool, default False): run the loop immediately after creation.

   Returns:
       The ActiveLoop. The data is accessible as loop.data_set. This can then be used
           for plotting, if necessary, e.g. pp=qc.live_plot(loop.data_set,params_to_plot)


.. py:function:: loop2dUD(sweep_parameter, start, stop, num, delay, step_parameter, step_start, step_stop, step_num, step_delay, step_action=None, fast_down=False, device_info='', instrument_info='', measure=None, plot=None, run=False)

   Create a 2D loop where at each point in the step parameter, the sweep parameter performs a loop
   in two directions: up and down. Create also a data set, and optionally, live plotting.

   Args:
       sweep_parameter (Parameter): The qcodes parameter to sweep over.

       start (float): the start value of the sweep.

       stop (float): the stop value of the sweep.

       num (int): the number of points in the sweep.

       delay (float): the number of seconds to wait after setting a value before
           measuring.

       step_parameter (Parameter): The parameter to step over.

       step_start (float): the start value of the step.

       step_stop (float): the stop value of the step.

       step_num (int): the number of points in the step.

       step_delay (float): the number of seconds to wait after setting a value before
           starting the inner loop.

       step_action: an action (e.g. qcodes Task) to run at each point in the step loop AFTER 
           the step parameter has been set, but BEFORE the inner loop starts

       fast_down (int): If provided, the down loop will be shortened by this factor.

       device_info (str): a string with information about the device

       instrument_info (str): a string with information about the setup that will not
           be captured by the metadata (e.g. voltage dividers, preamp settings)

       measure (list): a list of parameters to measure at each point in the
           loop. If None, will use the default measurement set by the default station

       plot (list): a list of parameters to plot at each point in the loop.

       run (bool, default False): run the loop immediately after creation.

   Returns:
       The ActiveLoop. The data is accessible as loop.data_set. This can then be used
           for plotting, if necessary, e.g. pp=qc.live_plot(loop.data_set,params_to_plot)


.. py:class:: Measure(setpoints=None, parameters=None, use_threads=False, station=None, name=None, timer=False)

   Bases: :py:obj:`qcodes.metadatable.Metadatable`


   Class to create a ``DataSetPP`` from a single (non-looped) set of measured parameters.

   ``Measure`` is used to measure a set of parameters at a single point in time.
   The typical use case is where the parameter(s)'s get function(s) return(s) an array, e.g. 
   an oscilloscope trace, or a spectrum analyser trace.
   At init, you can provide the parameters to measure and (optionally) setpoints. If no parameters are 
   provided, the default station.measure() is used.
   If no setpoints are provided, dummy setpoints are created for each dimension
   found in the parametersn (recommended, see below).

   ``Measure.run()`` will execute the measurement, and return and save a ``DataSetPP``

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
       parameters (Optional, Sequence[Parameter]): Sequence of gettable Parameters.
           If no actions are provided, the default station.measure() is used.

       name (Optional, str): String to send to the filename of the DataSet.

       station (Optional, Station): The ``Station`` to use if not the default.

       use_threads (Optional, bool): Use threading to parallelize getting parameters from instruments.

       setpoints (Optional, Sequence[Parameter or Array]): sequence of setpoint arrays
           use for the DataSetPP. Can be array(s) of values, or gettable Parameter(s). 
           If not provided, dummy setpoints are created for each dimension found in the parameters.
           Providing a setpoint parameter may be useful if you measure a parameter that is considered the 
           independent variable. e.g. time on an oscilloscope, or a voltage ramp on a source. live_plot 
           and offline_plotting will then be able to plot the correct dependencies automatically. However; 
           it can be tricky to get all the dimensions right, so in most instances it's better to just pass 
           all measured parameters to the parameters argument, and then plot whatever parameter against 
           whatever other parameter manually. 

       timer (Optional, bool, default False): The default station.measure() includes a timer parameter, which is
           useful for Loops but essentially useless here. If you really want it, set timer=True.


   .. py:attribute:: station


   .. py:attribute:: use_threads
      :value: False



   .. py:attribute:: setpoints
      :value: None



   .. py:attribute:: name
      :value: None



   .. py:attribute:: timer
      :value: False



   .. py:attribute:: actions
      :value: None



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



   .. py:method:: run(name=None, params_to_plot=None, use_threads=None, quiet=False, station=None, publisher=None, **kwargs)

      Run the actions in this measurement and return their data as a DataSetPP

      Args:
          params_to_plot: a list of parameters to plot once the measurement is done.
              Can either be the DataArray objects, or the parameters themselves.
          quiet (Optional[bool]): Set True to not print anything except
              errors. Default False.

          station (Optional[Station]): the ``Station`` this measurement
              pertains to. Defaults to ``Station.default`` if one is defined.
              Only used to supply metadata.

          use_threads (Optional[bool]): whether to parallelize ``get``
              operations using threads. Default False.

          Other kwargs are passed along to data_set.new_data. The key ones
          are:

          location (Optional[Union[str, False]]): the location of the
              DataSetPP, a string whose meaning depends on formatter and io,
              or False to only keep in memory. May be a callable to provide
              automatic locations. If omitted, will use the default
              DataSetPP.location_provider

          name (Optional[str]): if location is default or another provider
              function, name is a string to add to location to make it more
              readable/meaningful to users

          formatter (Optional[Formatter]): knows how to read and write the
              file format. Default can be set in DataSetPP.default_formatter

          io (Optional[io_manager]): knows how to connect to the storage
              (disk vs cloud etc)

      returns:
          a DataSetPP object containing the results of the measurement



   .. py:method:: snapshot_base(update=False)

      Override this with the primary information for a subclass.



.. py:class:: Task(func, *args, **kwargs)

   Execute a function within a measurement Loop, e.g. .each(Task(func, *args, **kwargs)).

   The first argument should be a callable function, to which any subsequent
   args and kwargs (which are evaluated before the loop starts) are passed.

   e.g.:
   Define a function to wait for a temperature setpoint to be reached:

   >>> def wait_for_temperature(target_T, measured_T, tolerance):
   >>>     while abs(measured_T - target_T) > tolerance:
   >>>         time.sleep(1)

   Then use it in a Loop, inside each, before measuring.

   >>> loop = Loop(temperature_setpoint.sweep(0,2,101),delay=0.1).each(
   >>>     Task(wait_for_temperature, temperature_setpoint(), temperature(), 0.1),
   >>>     *station.measure())

   If the args and kwargs are also callable, then they are evaluated
   before being passed to the func.

   Args:
       func (callable): Function to executed
       *args: pass to func, after evaluation if callable
       **kwargs: pass to func, after evaluation if callable



   .. py:attribute:: func


   .. py:attribute:: args
      :value: ()



   .. py:attribute:: kwargs


   .. py:method:: __call__(**ignore_kwargs)


   .. py:method:: snapshot(update=False)

      Snapshots  task
      Args:
          update (bool): TODO not in use

      Returns:
          dict: snapshot



.. py:class:: Wait(delay)

   A simple class to tell a Loop to wait <delay> seconds.

   This is transformed into a Task within the Loop, such that
   it can do other things (monitor, check for halt) during the delay.

   But for use outside of a Loop, it is also callable (then it just sleeps)

   Args:
       delay: seconds to delay

   Raises:
       ValueError: if delay is negative


   .. py:attribute:: delay


   .. py:method:: __call__()


   .. py:method:: snapshot(update=False)

      Snapshots  delay
      Args:
          update (bool): TODO not in use

      Returns:
          dict: snapshot



.. py:class:: BreakIf(condition)

   Loop action that breaks out of the loop if a condition is truthy.

   Args:
       condition (callable): a callable taking no arguments.
           Can be a simple function that returns truthy when it's time to quit
   Raises:
       TypeError: if condition is not a callable with no aguments.

   Examples:
           >>> BreakIf(lambda: np.abs(chan1.curr()) >= 3e-9)


   .. py:attribute:: condition


   .. py:method:: __call__(**ignore_kwargs)


   .. py:method:: snapshot(update=False)

      Snapshots breakIf action
      Args:
          update (bool): TODO not in use

      Returns:
          dict: snapshot




.. py:class:: Plot(title=None, name=None)

   Class to create live plot instances.

   Most methods of this class should not be called directly; only add(), add_multiple(), clear() and close()
   should be used by the user.

   Args:
       title (str, optional): Title of the plot window.
       name (str, optional): Name of the plot instance. If not provided, a random UUID will be used.


   .. py:attribute:: context


   .. py:attribute:: socket


   .. py:attribute:: port
      :value: 8876



   .. py:attribute:: encoding
      :value: 'utf-8'



   .. py:attribute:: topic
      :value: 'qcodes.plot.00000000000000000000000000000000'



   .. py:attribute:: metadata


   .. py:attribute:: data_uuid
      :value: '00000000000000000000000000000000'



   .. py:attribute:: client_ready_event


   .. py:attribute:: control_task


   .. py:attribute:: control_port


   .. py:method:: publish(data, uuid=None)


   .. py:method:: publish_data(data, uuid, meta, arrays)


   .. py:method:: add_metadata(new_metadata, uuid=None)


   .. py:method:: store(loop_indices, ids_values, uuid)


   .. py:method:: save_metadata(metadata, uuid=None)


   .. py:method:: finalize(uuid=None)


   .. py:method:: new_client(name=None)


   .. py:method:: clear()


   .. py:method:: add_multiple(*z_params)

      Add multiple ``DataArray`` s to the ``Plot``.

      Args:
          *z_params (Sequence [DataArray]): DataArrays to be added to the Plot.
              Each DataArray is added to a separate subplot.



   .. py:method:: add(*args, x=None, y=None, z=None, subplot=0, name=None, title=None, position=None, relativeto=None, xlabel=None, ylabel=None, zlabel=None, xunit=None, yunit=None, zunit=None, silent=True, linecuts=False, symbol=None, size=None, **kwargs)

      Add a trace to the plot.

      Args:
          *args (DataArray): positional arguments, can be:
              - ``y`` or ``z``: specify just the 1D or 2D data independent parameter, with the setpoint
                  axis or axes implied from the DataSetPP setpoints.
              - ``x, y`` or ``x, y, z``: specify all axes of the data.
          x (DataArray, optional): x-axis data.
          y (DataArray, optional): y-axis data.
          z (DataArray, optional): z-axis data.
          subplot (int, optional): Subplot index to add the trace to. Defaults to 0.
          name (str, optional): Name of the trace. If not provided, the name of the DataArray will be used.
          title (str, optional): Title of the trace. If not provided, the name of the DataArray will be used.
          position (str): Position of the subplot in the plot window. Options are 'bottom', 'top', 'left', 'right', 'above', or 'below'.
          relativeto (str, optional): Position relative to which the subplot should be placed.
          xlabel (str, optional): Label for the x-axis. If not provided, the label of the DataArray will be used.
          ylabel (str, optional): Label for the y-axis. If not provided, the label of the DataArray will be used.
          zlabel (str, optional): Label for the z-axis. If not provided, the label of the DataArray will be used.
          xunit (str, optional): Unit for the x-axis. If not provided, the unit of the DataArray will be used.
          yunit (str, optional): Unit for the y-axis. If not provided, the unit of the DataArray will be used.
          zunit (str, optional): Unit for the z-axis. If not provided, the unit of the DataArray will be used.
          silent (bool, optional): If True, do not wait for the client to be ready. Defaults to True.
          linecuts (bool, optional): If True, plot line cuts instead of a 2D image. Defaults to False.
          symbol (str, optional): Symbol to use for the trace. Defaults to None.
          size (int, optional): Size of the symbol. Defaults to None.



   .. py:method:: expand_trace(args, kwargs)

      Complete the x, y (and possibly z) data definition for a trace.

      Also modifies kwargs in place so that all the data needed to fully specify the
      trace is present (ie either x and y or x and y and z)

      Both ``__init__`` (for the first trace) and the ``add`` method support multiple
      ways to specify the data in the trace:

      As args:
          - ``add(y)`` or ``add(z)`` specify just the main 1D or 2D data, with the setpoint
            axis or axes implied.
          - ``add(x, y)`` or ``add(x, y, z)`` specify all axes of the data.
      And as kwargs:
          - ``add(x=x, y=y, z=z)`` you specify exactly the data you want on each axis.
            Any but the last (y or z) can be omitted, which allows for all of the same
            forms as with args, plus x and z or y and z, with just one axis implied from
            the setpoints of the z data.

      This method takes any of those forms and converts them into a complete set of
      kwargs, containing all of the explicit or implied data to be used in plotting this trace.

      Args:
          args (Tuple[DataArray]): positional args, as passed to either ``__init__`` or ``add``
          kwargs (Dict(DataArray]): keyword args, as passed to either ``__init__`` or ``add``.
              kwargs may contain non-data items in keys other than x, y, and z.

      Raises:
         ValueError: if the shape of the data does not match that of args
         ValueError: if the data is provided twice



   .. py:method:: set_title(title)


   .. py:method:: set_cmap(cmap)


   .. py:method:: save(filename=None, subplot=None)


   .. py:method:: set_xlabel(label, subplot=0)


   .. py:method:: set_ylabel(label, subplot=0)


   .. py:method:: set_geometry(height, width, x0, y0)


   .. py:method:: close()


.. py:function:: live_plot(*args, data_set=None, data_items=None)

   Entry point for live plotting of qcodespp data.

   Args:
       *args (DataSetPP, DataArray, Parameter, list, tuple): Positional arguments can be:
           - ``DataSetPP``: The dataset to link to the live plot.
           - ``DataArray`` or ``Parameter``: The data items to plot.
           - A list or tuple of ``DataArray`` or ``Parameter`` objects to plot.
       data_set (``DataSetPP``, optional): The ``DataSetPP`` to link to the live plot.
           If not provided, it will try to use the default dataset.
           If no data_set, one can add items to the plot, but the data will not be tracked.
       data_items (Sequence[``DataArray``, ``Parameter``], optional): List of ``DataArray``
           or ``Parameter`` objects to plot. If not provided, nothing will be plotted initially,
           the user can use ``Plot.add()`` later.

   Returns:
       The ``Plot`` instance.


.. py:function:: offline_plotting(folder=None, link_to_default=True, use_thread=True)

   Entry point for qcodespp offline plotting. Call qcodespp.offline_plotting() to start the application.

   Args:
       folder (str): Path (inc relative) to a folder containing the data files to be plotted.
       link_to_default (bool): Link to the qcodespp default folder specified by qc.set_data_folder().
           Ignored if another folder is specified by folder.
       use_thread (bool): Runs the application in a separate thread or not. Default is True.
           Threading may cause problems on some systems, e.g. macOS.


.. py:function:: new_data(location=None, loc_record=None, name=None, overwrite=False, io=None, backup_location=None, force_write=False, **kwargs)

   Create a new DataSetPP, the text-based data set of qcodespp.

   Args:
       location (str or callable or False, optional): If you provide a string,
           it must be an unused location in the io manager. Can also be:

           - a callable ``location provider`` with one required parameter
             (the io manager), and one optional (``record`` dict),
             which returns a location string when called
           - ``False`` - denotes an only-in-memory temporary DataSetPP.

           Note that the full path to or physical location of the data is a
           combination of io + location. the default ``DiskIO`` sets the base
           directory, which this location is a relative path inside.
           Default ``DataSetPP.location_provider`` which is initially
           ``FormatLocation()``

       loc_record (dict, optional): If location is a callable, this will be
           passed to it as ``record``

       name (str, optional): overrides the ``name`` key in the ``loc_record``.

       overwrite (bool): Are we allowed to overwrite an existing location?
           Default False.

       io (io_manager, optional): base physical location of the ``DataSetPP``.
           Default ``DataSetPP.default_io`` is initially ``DiskIO('.')`` which
           says the root data directory is the current working directory, ie
           where you started the python session.

       arrays (Optional[List[qcodes.DataArray]): arrays to add to the DataSetPP.
               Can be added later with ``self.add_array(array)``.

       formatter (Formatter, optional): sets the file format/structure to
           write (and read) with. Default ``DataSetPP.default_formatter`` which
           is initially ``GNUPlotFormat()``.

       write_period (float or None, optional):seconds
           between saves to disk.
   Returns:
       A new ``DataSetPP`` object ready for storing new data in.


.. py:function:: load_data(location=None, formatter=None, io=None, include_metadata=True)

   Load an existing DataSetPP.

   Args:
       location (str, optional): the location to load from. Default is the
           current live DataSetPP.
           Note that the full path to or physical location of the data is a
           combination of io + location. the default ``DiskIO`` sets the base
           directory, which this location is a relative path inside.

       formatter (Formatter, optional): sets the file format/structure to
           read with. Default ``DataSetPP.default_formatter`` which
           is initially ``GNUPlotFormat()``.

       io (io_manager, optional): base physical location of the ``DataSetPP``.
           Default ``DataSetPP.default_io`` is initially ``DiskIO('.')`` which
           says the root data directory is the current working directory, ie
           where you started the python session.

   Returns:
       A new ``DataSetPP`` object loaded with pre-existing data.


.. py:function:: load_data_num(number, datafolder='data', delimiter='_', leadingzeros=3, include_metadata=True)

   Load a qcodespp DataSetPP using the counter as identifier.

   Typically qcodespp DataSetPPs are forced to use the format counter_name_date_time,
   where the counter is a zero-padded integer. This function will search for
   a folder with the given counter number, and load the data from it.

   Args:
       number (str or int): the dataset's counter number
       datafolder (str, optional): the folder to load from. Default is the
           current live DataSetPP.
           Note that the full path to or physical location of the data is a
           combination of io + location. the default ``DiskIO`` sets the base
           directory, which this location is a relative path inside.
       delimiter (str, optional): The character after the number. Almost always
           underscore but may be specified if necessary.

   Returns:
       A new ``DataSetPP`` object loaded with pre-existing data.


.. py:function:: load_data_nums(listofnumbers, datafolder='data', delimiter='_', leadingzeros=3, include_metadata=True)

   Loads numerous DataSetPPs from the specified folder by counter number.

   Args:
       litsofnumbers (list of strings or ints): list of desired dataset numbers.
       datafolder (str, optional): the folder to load from. Default is the
           current live DataSetPP.
           Note that the full path to or physical location of the data is a
           combination of io + location. the default ``DiskIO`` sets the base
           directory, which this location is a relative path inside.
       delimiter (str, optional): The character after the number. Almost always
           underscore but may be specified if necessary.

   Returns:
       An array containing ``DataSetPP`` objects loaded with pre-existing data.


.. py:function:: set_data_format(fmt='data/#{counter}_{name}_{date}_{time}')

   Set the default format for storing DataSetPPs. It is not recommended to alter this: instead use set_data_folder.

   Args:
       fmt (str): A format string for the location of the data, with wildcards determined by the FormatLocation class.


.. py:function:: set_data_folder(folder='data')

   Set the default folder for storing DataSetPPs.

   Args:
       folder (str): Folder name relative to the current working directory, e.g. location of the current
           Jupyter notebook. The folder will be created if it does not exist.


.. py:function:: listVISAinstruments(baudrates='qdac')

   List the VISA instruments connected to the computer. Deault baudrates checked are 9600 and 921600.

   Args:
       baudrates (int, str, list): The baudrate(s) to check for the instruments.
           - If an integer, it will check only that baudrate.
           - If a string, it can be 'qdac', 'standard', or 'all' to use predefined baudrate lists.
           - If a list, it should contain integers representing the baudrates to check.
   Returns:
       None: Prints the list of instruments and their identification strings.

   Details:
       If you are expecting instrument(s), e.g. QDAC, to communicate with a baudrate other than 9600,
       you can include the possible baudrates when calling the function. By default it also checks for the
       baudrate used by the qdac. If you want to check other baudrates, include them explicitly as a list,
       or use predefined lists 'standard' or 'all', with baudrates defined according the National Instruments standards.


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


