qcodespp
========

.. py:module:: qcodespp


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/qcodespp/actions/index
   /autoapi/qcodespp/cli/index
   /autoapi/qcodespp/data/index
   /autoapi/qcodespp/instrument_drivers/index
   /autoapi/qcodespp/loops/index
   /autoapi/qcodespp/measure/index
   /autoapi/qcodespp/parameters/index
   /autoapi/qcodespp/plotting/index
   /autoapi/qcodespp/scripts/index
   /autoapi/qcodespp/station/index
   /autoapi/qcodespp/utils/index
   /autoapi/qcodespp/version/index


Attributes
----------

.. autosummary::

   qcodespp.config
   qcodespp.__version__
   qcodespp.stepper


Classes
-------

.. autosummary::

   qcodespp.Station
   qcodespp.Measure
   qcodespp.Task
   qcodespp.Wait
   qcodespp.BreakIf
   qcodespp.DataSetPP
   qcodespp.MultiParameterWrapper
   qcodespp.ArrayParameterWrapper


Functions
---------

.. autosummary::

   qcodespp.offline_plotting
   qcodespp.param_monitor
   qcodespp.colorplot
   qcodespp.colored_traces
   qcodespp.load_2d_json
   qcodespp.export_2d_to_IG
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



   .. py:method:: add_components(components)


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



   .. py:method:: communication_time(measurement_num=5, return_average=True, include_callables=False)

      Estimate how long it takes to communicate with the instruments in the station.

      Args:
          measurement_num: Number of measurements to take to estimate the communication time.
              Default is 1, but can be set to a higher number for more accurate estimates.
          return_average: Whether to return the average of the measurements or the entire list.
          include_callables: Whether to estimate the time non-gettable callables takes. 
              These can be other allowable actions, e.g. qc.Task, qc.BreakIf. Usually they behave 
              unpredictably and it's best to exclude them.
      Returns:
          Either the average communication time or the list of communication times for each measurement.



   .. py:method:: measurement(*actions, include_callables=True)

      Measure the default measurement, or parameters in actions.

      Args:
          *actions: parameters to mesure
          include_callables (bool): Perform non-gettable actions, i.e. Task, BreakIf, etc.



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
   :value: '0.1.19'


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




.. py:function:: offline_plotting(folder=None, link_to_default=True, use_thread=True)

   Entry point for qcodespp offline plotting. From CLI: qcodespp offline_plotting. From notebooks: qcodespp.offline_plotting().

   Args:
       folder (str): Path (inc relative) to a folder containing the data files to be plotted.
       link_to_default (bool): Link to the qcodespp default folder specified by qc.set_data_folder().
           Ignored if another folder is specified by folder.
       use_thread (bool): Runs the application in a separate thread or not. Default is False.
           Threading may cause problems on some systems, e.g. macOS.


.. py:function:: param_monitor(*params, interval=0.2, maxlen=500, use_thread=True, ylabel=None, yunit=None)

   Entry point for qcodespp parameter monitoring. 
   Args:
       params (list): List of QCoDeS parameters to monitor.
       interval (int): Update interval in seconds.
       maxlen (int): Number of points to keep in the rolling window.
       use_thread (bool): Runs the application in a separate thread or not. Default is False.
           Threading may cause problems on some systems, e.g. macOS.
       ylabel (str): Label for the y-axis. Default is None, which will use 'Param value(s) (arb units)'.
       yunit (str): Unit for the y-axis. Default is None


.. py:function:: colorplot(x, y, z, figsize=0, cmap=0, labels=0, xlim=0, ylim=0, zlim=0, xmajor=0, xminor=0, ymajor=0, yminor=0, font_size=0, label_size=0, check_shapes=False)

   Make a nice colourplot from a three-dimensional data array using matplotlib. 

   Args:
       
       x: 1D or 2D array of x-coordinates
       
       y: 1D or 2D array of y-coordinates
       
       z: 2D array of z-values corresponding to the x and y coordinates.
       
       figsize (tuple, optional): Size of the figure in inches. Default is (8, 8).
       
       cmap (str, optional): Colormap to use for the plot. Default is 'hot'.
       
       labels (list, optional): Labels for the x, y, and z axes. Default is ['x', 'y', 'z'].
       
       xlim (tuple, optional): Limits for the x-axis. Default is None.
       
       ylim (tuple, optional): Limits for the y-axis. Default is None.
       
       zlim (tuple, optional): Limits for the z-axis (color scale). Default is None.
       
       xmajor (float, optional): Major tick interval for the x-axis. Default is None.
       
       xminor (float, optional): Minor tick interval for the x-axis. Default is None.
       
       ymajor (float, optional): Major tick interval for the y-axis. Default is None.
       
       yminor (float, optional): Minor tick interval for the y-axis. Default is None.
       
       font_size (int, optional): Font size for the axis labels. Default is 12.
       
       label_size (int, optional): Font size for the tick labels. Default is 12.

       check_shapes (bool, optional): If True, checks the shapes of x, y, and z arrays and transposes if necessary. Default is False.

   Returns:
       tuple: A tuple containing the figure, axis, and colorbar axis objects.



.. py:function:: colored_traces(x, y, offset=0, figsize=0, cmap=0, labels=0, xlim=0, ylim=0, style='-', xmajor=0, xminor=0, ymajor=0, yminor=0, font_size=0, label_size=0)

   Plot a series of 1D traces where the lines are colored according to a matplotlib colormap.

   Args:
       
       x: 1D or 2D array of x-coordinates
       
       y: 2D array of y-coordinates
       
       figsize (tuple, optional): Size of the figure in inches. Default is (8, 8).
       
       cmap (str, optional): Colormap to use for the plot. Default is 'hot'.
       
       labels (list, optional): Labels for the x, y, and z axes. Default is ['x', 'y', 'z'].
       
       xlim (tuple, optional): Limits for the x-axis. Default is None.
       
       ylim (tuple, optional): Limits for the y-axis. Default is None.
       
       xmajor (float, optional): Major tick interval for the x-axis. Default is None.
       
       xminor (float, optional): Minor tick interval for the x-axis. Default is None.
       
       font_size (int, optional): Font size for the axis labels. Default is 12.
       
       label_size (int, optional): Font size for the tick labels. Default is 12.


   Returns:
       tuple: A tuple containing the figure and axis objects.



.. py:function:: load_2d_json(filename)

   Load reshaped 2D data exported from offline_plotting as a JSON file.

   Args:
       filename (str): Path to the JSON file.

   Returns:
       dict: A dictionary containing the reshaped data.


.. py:function:: export_2d_to_IG(x, y, z, filename)

   Export 2D data to a .dat file in a format that InSpectra Gadget can import.

   Args:
       x (array-like): x-axis values. Shape must match z's or z's first dimension
       y (array-like): y-axis values. Shape must match z's or z's second dimension
       z (2D array-like): z values
       filename (str): name of the file to save the data to, without extension.


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


.. py:function:: load_data(location=None, formatter=None, io=None, include_metadata=True, remove_incomplete=True)

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


.. py:function:: load_data_num(number, datafolder='data', delimiter='_', leadingzeros=3, include_metadata=True, remove_incomplete=True)

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


.. py:function:: load_data_nums(listofnumbers, datafolder='data', delimiter='_', leadingzeros=3, include_metadata=True, remove_incomplete=True)

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

   Set the default format for storing DataSetPPs. See qcodespp.data.location for more information.

   Args:
       fmt (str): A format string for the location of the data, with wildcards determined by the FormatLocation class.
           Another useful format may be 'data/{date}/#{counter}_{name}_{time}'.


.. py:function:: set_data_folder(folder='data')

   Set the default folder for storing DataSetPPs.

   Args:
       folder (str): Folder name relative to the current working directory, e.g. location of the current
           Jupyter notebook. The folder will be created if it does not exist.


.. py:class:: DataSetPP(location=None, arrays=None, formatter=None, io=None, write_period=5, backup_location=None, force_write=False, name=None)

   Bases: :py:obj:`qcodes.utils.DelegateAttributes`


   A container for one complete measurement from qcodespp.Measure or qcodespp.Loop.

   A DataSetPP consists of multiple DataArrays with potentially different 
   sizes and dimensionalities. It is accompanied by metadata containing snapshots 
   of different qcodespp classes, e.g. Instruments and Parameters in the Station.

   A DataSetPP should not be instantiated directly, but constructed by qcodespp.Measure 
   or qcodespp.Loop. A pre-existing DataSetPP can be loaded with qcodespp.load_data, 
   load_data_num, or load_data_nums.

   The default format for storage is (a) text file(s) with GNUPlotFormat, where the 
   DataArrays are converted to numpy arrays. This means that each DataArray must be 
   rectangular, and all elements must be of the same type. Currently, types are limited 
   to float or str; however, almost any type other than str can be converted to a float, 
   and this is done automatically; e.g. boolean --> (0,1). 
   DataArrays which are also Setpoints can only be of type float.

   Args:
       location (str or False): A location in the io manager, or ``False`` for
           an only-in-memory temporary DataSetPP.
           Note that the full path to or physical location of the data is a
           combination of io + location. the default ``DiskIO`` sets the base
           directory, which this location is a relative path inside.

       io (io_manager, optional): base physical location of the ``DataSetPP``.
           Default ``DataSetPP.default_io`` is initially ``DiskIO('.')`` which
           says the root data directory is the current working directory, ie
           where you started the python session.

       arrays (Optional[List[qcodes.DataArray]): arrays to add to the DataSetPP.
               Can be added later with ``self.add_array(array)``.

       formatter (Formatter, optional): sets the file format/structure to
           write (and read) with. Default ``DataSetPP.default_formatter`` which
           is initially ``GNUPlotFormat()``.

       write_period (float or None, optional): Only if ``mode=LOCAL``, seconds
           between saves to disk. If not ``LOCAL``, the ``DataServer`` handles
           this and generally writes more often. Use None to disable writing
           from calls to ``self.store``. Default 5.

   Attributes:
       background_functions (OrderedDict[callable]): Class attribute,
           ``{key: fn}``: ``fn`` is a callable accepting no arguments, and
           ``key`` is a name to identify the function and help you attach and
           remove it.

           In ``DataSetPP.complete`` we call each of these periodically, in the
           order that they were attached.

           Note that because this is a class attribute, the functions will
           apply to every DataSetPP. If you want specific functions for one
           DataSetPP you can override this with an instance attribute.


   .. py:attribute:: delegate_attr_dicts
      :value: ['arrays']


      A list of names (strings) of dictionaries
      which are (or will be) attributes of ``self``, whose keys should
      be treated as attributes of ``self``.



   .. py:attribute:: default_io


   .. py:attribute:: default_formatter


   .. py:attribute:: location_provider


   .. py:attribute:: default_folder
      :value: None



   .. py:attribute:: background_functions
      :type:  Dict[str, Callable]


   .. py:attribute:: backup_used
      :value: False



   .. py:attribute:: writing_skipped
      :value: False



   .. py:attribute:: finalized
      :value: False



   .. py:attribute:: publisher
      :value: None



   .. py:attribute:: name
      :value: None



   .. py:attribute:: formatter


   .. py:attribute:: io


   .. py:attribute:: write_period
      :value: 5



   .. py:attribute:: last_write
      :value: 0



   .. py:attribute:: last_store
      :value: -1



   .. py:attribute:: force_write
      :value: False



   .. py:attribute:: metadata


   .. py:attribute:: uuid
      :value: '00000000000000000000000000000000'



   .. py:attribute:: arrays


   .. py:method:: sync()

      Synchronize this DataSetPP with the DataServer or storage.

      If this DataSetPP is on the server, asks the server for changes.
      If not, reads the entire DataSetPP from disk.

      Returns:
          bool: True if this DataSetPP is live on the server



   .. py:method:: fraction_complete()

      Get the fraction of this DataSetPP which has data in it.

      Returns:
          float: the average of all measured (not setpoint) arrays'
              ``fraction_complete()`` values, independent of the individual
              array sizes. If there are no measured arrays, returns zero.



   .. py:method:: remove_incomplete()

      "
      Returns a DataSetPP minus any incomplete columns.

      DataArrays are initialized with a set shape and filled with NaNs. 
      The NaNs get replaced during the measurements, but if the measurement is
      stopped prematurely, the existence of NaNs can cause problems when plotting.

      Returns:
          DataSetPP: a new DataSetPP with all incomplete columns removed.



   .. py:method:: complete(delay=1.5)

      Periodically sync the DataSetPP and display percent complete status.

      Also, each period, execute functions stored in (class attribute)
      ``self.background_functions``. If a function fails, we log its
      traceback and continue on. If any one function fails twice in
      a row, it gets removed.

      Args:
          delay (float): seconds between iterations. Default 1.5



   .. py:method:: get_changes(synced_indices)

      Find changes since the last sync of this DataSetPP.

      Args:
          synced_indices (dict): ``{array_id: synced_index}`` where
              synced_index is the last flat index which has already
              been synced, for any (usually all) arrays in the DataSetPP.

      Returns:
          Dict[dict]: keys are ``array_id`` for each array with changes,
              values are dicts as returned by ``DataArray.get_changes``
              and required as kwargs to ``DataArray.apply_changes``.
              Note that not all arrays in ``synced_indices`` need be
              present in the return, only those with changes.



   .. py:method:: add_array(data_array)

      Add one DataArray to this DataSetPP, and mark it as part of this DataSetPP.

      Note: DO NOT just set ``data_set.arrays[id] = data_array``, because
      this will not check if we are overwriting another array, nor set the
      reference back to this DataSetPP, nor that the ``array_id`` in the array
      matches how you're storing it here.

      Args:
          data_array (DataArray): the new array to add

      Raises:
          ValueError: if there is already an array with this id here.



   .. py:method:: remove_array(array_id)

      Remove an array from a dataset

      Throws an exception when the array specified is refereced by other
      arrays in the dataset.

      Args:
          array_id (str): array_id of array to be removed



   .. py:method:: store(loop_indices, ids_values)

      Insert data into one or more of our DataArrays.

      Args:
          loop_indices (tuple): the indices within whatever loops we are
              inside. May have fewer dimensions than some of the arrays
              we are inserting into, if the corresponding value makes up
              the remaining dimensionality.
          values (Dict[Union[float, sequence]]): a dict whose keys are
              array_ids, and values are single numbers or entire slices
              to insert into that array.
       



   .. py:method:: default_parameter_name(paramname='amplitude')

      Return name of default parameter for plotting

      The default parameter is determined by looking into
      metdata['default_parameter_name'].  If this variable is not present,
      then the closest match to the argument paramname is tried.

      Args:
          paramname (str): Name to match to parameter name

      Returns:
          name ( Union[str, None] ): name of the default parameter



   .. py:method:: default_parameter_array(paramname='amplitude')

      Return default parameter array

      Args:
          paramname (str): Name to match to parameter name.
               Defaults to 'amplitude'

      Returns:
          array (DataArray): array corresponding to the default parameter

      See also:
          default_parameter_name




   .. py:method:: read(include_metadata=True)

      Read the whole DataSetPP from storage, overwriting the local data.



   .. py:method:: read_metadata()

      Read the metadata from storage, overwriting the local data.



   .. py:method:: write(write_metadata=False, only_complete=True, filename=None, force_rewrite=False)

      Writes updates to the DataSetPP to storage.

      N.B. it is recommended to call data_set.finalize() when a DataSetPP is
      no longer expected to change to ensure files get closed

      Args:
          write_metadata (bool): write the metadata to disk
          only_complete (bool): passed on to the match_save_range inside
              self.formatter.write. Used to ensure that all new data gets
              saved even when some columns are strange.
          filename (Optional[str]): The filename (minus extension) to use.
              The file gets saved in the usual location.



   .. py:method:: write_copy(path=None, io_manager=None, location=None)

      Write a new complete copy of this DataSetPP to storage.

      Args:
          path (str, optional): An absolute path on this system to write to.
              If you specify this, you may not include either ``io_manager``
              or ``location``.

          io_manager (io_manager, optional): A new ``io_manager`` to use with
              either the ``DataSetPP``'s same or a new ``location``.

          location (str, optional): A new ``location`` to write to, using
              either this ``DataSetPP``'s same or a new ``io_manager``.



   .. py:method:: add_metadata(new_metadata)

      Update DataSetPP.metadata with additional data.

      Args:
          new_metadata (dict): new data to be deep updated into
              the existing metadata



   .. py:method:: save_metadata()

      Evaluate and save the DataSetPP's metadata.



   .. py:method:: finalize(filename=None, write_metadata=True, force_rewrite=False)

      Mark the DataSetPP complete and write any remaining modifications.

      Also closes the data file(s), if the ``Formatter`` we're using
      supports that.

      Args:
          filename (Optional[str]): The file name (minus extension) to
              write to. The location of the file is the usual one.
          write_metadata (bool): Whether to save a snapshot. For e.g. dumping
              raw data inside a loop, a snapshot is not wanted.



   .. py:method:: snapshot(update=False)

      JSON state of the DataSetPP.



   .. py:method:: get_array_metadata(array_id)

      Get the metadata for a single contained DataArray.

      Args:
          array_id (str): the array to get metadata for.

      Returns:
          dict: metadata for this array.



   .. py:method:: __repr__()

      Rich information about the DataSetPP and contained arrays.



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



   .. py:attribute:: unit
      :value: ''



   .. py:method:: get_raw()

      Method to get the values of all parameters in the MultiParameter.

      Returns:
          tuple: A tuple containing the values of all parameters in the MultiParameter.



   .. py:method:: set_raw(values)

      Method to set the values of all parameters in the MultiParameter.

      Args:
          values (list, tuple, int, float): The values to set for the parameters.
              If a single value is provided, it will be set for all parameters.
              If a list or tuple is provided, it must match the number of parameters.



   .. py:method:: move(end_values, steps=101, step_time=0.03)

      Move all parameters to new values in a number of steps without taking data.

      Args:
          end_values (list, tuple, int, float): The values to move to.
              If a single value is provided, it will be moved for all parameters.
              If a list or tuple is provided, it must match the number of parameters.
          steps (int, optional): Number of steps to take. Defaults to 101.
          step_time (float, optional): Time in seconds between each step. Defaults to 0.03.



   .. py:method:: sweep(start_vals, stop_vals, num, print_warning=True)

      Create a collection of parameter values to be iterated over for all parameters in the MultiParameter.

      Args:
          start_vals (list, tuple, int, float): The starting values of the sequence.
              If a single value is provided, it will be used for all parameters.
              If a list or tuple is provided, it must match the number of parameters.

          stop_vals (list, tuple, int, float): The end values of the sequence.
              If a single value is provided, it will be used for all parameters.
              If a list or tuple is provided, it must match the number of parameters.

          num (int): Number of values to generate.

          print_warning (bool): Whether to print a warning if the start value is different from the 
              current value. Defaults to True.

      Returns:
          SweepFixedValues or SweepMultiValues: A collection of parameter values to be iterated over which can be passed to a Loop.

      Raises:
          ValueError: If the number of start_vals or stop_vals does not match the number of parameters, 
          or if they are not a single value.



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


.. py:data:: stepper

