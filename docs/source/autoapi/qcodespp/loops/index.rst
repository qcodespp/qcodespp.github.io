qcodespp.loops
==============

.. py:module:: qcodespp.loops

.. autoapi-nested-parse::

   Data acquisition loops.

   The general scheme is:

   1. create a (potentially nested) ``Loop``, which defines the sweep setpoints and
   delays

   2. activate the loop (which changes it to an ``ActiveLoop`` object),
   by attaching one or more actions to it, using the ``.each`` method.
   Actions can be: parameters to measure, tasks to run, waits, or other loops.

   3. Associate the ``ActiveLoop`` with a ``DataSetPP``, which will hold the data collected,
   using the ``.get_data_set`` method.

   4. Run the ``ActiveLoop`` with the ``.run`` method, which additionally can be passed
   parameters to be plotted using ``live_plot``.

   Supported commands to ``.each`` are:

   - ``Parameter``: anything with a ``.get`` method and ``.name`` or ``.names``
   - ``ActiveLoop`` (or ``Loop``, will be activated with default measurement)
   - ``Task``: any callable that does not generate data, e.g. a function
   - ``BreakIf``: a condition that will break the loop if True, e.g. ``BreakIf(lambda: param1()>10)``
   - ``Wait``: a delay

   Some examples:

   - 1D sweep, specifying parameters to measure and plot

   >>> loop=Loop(sweep_parameter.sweep(0,1,num=101), delay=0.1).each(measure_param1, measure_param2)
   >>> data=loop.get_data_set(name='My 1D sweep')
   >>> loop.run([measure_param1, measure_param2])

   - 2D sweep, using station.set_measurement to set the default measurement

   >>> station.set_measurement(measure_param1, measure_param2)
   >>> loop=Loop(parameter1.sweep(0,1,num=11), delay=0.1).loop(parameter2.sweep(-1,0,num=101), delay=0.1).each(*station.measure())
   >>> data=loop.get_data_set(name='My 2D sweep')
   >>> loop.run([measure_param1, measure_param2])

   However, these simple examples are covered by the convenience functions
   ``loop1d`` and ``loop2d``, which also take care of data set definition and naming and live plotting.
   An example of a 2D loop would be:

   >>> loop = loop2d(
       parameter1, 0, 1, 11, 0.1,
       parameter2, -1, 0, 101, 0.1,
       device_info='My device',
       instrument_info='My setup',
       measure=[measure_param1, measure_param2],
       plot=[measure_param1, measure_param2])
   >>> loop.run()



Attributes
----------

.. autosummary::

   qcodespp.loops.log


Classes
-------

.. autosummary::

   qcodespp.loops.Loop
   qcodespp.loops.ActiveLoop


Functions
---------

.. autosummary::

   qcodespp.loops.loop1d
   qcodespp.loops.loop2d
   qcodespp.loops.loop2dUD


Module Contents
---------------

.. py:data:: log

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


.. py:class:: Loop(sweep_values, delay=0, snake=False, station=None, progress_interval=None, progress_bar=True)

   Bases: :py:obj:`qcodes.metadatable.Metadatable`


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



.. py:class:: ActiveLoop(sweep_values, delay, *actions, then_actions=(), station=None, progress_interval=None, bg_task=None, bg_final_task=None, bg_min_delay=None, progress_bar=True, snake=False)

   Bases: :py:obj:`qcodes.metadatable.Metadatable`


   Automatically generated object returned when attaching ``actions`` to a ``Loop`` using e.g. `.each()`.

   When calling ActiveLoop.get_data_set(), the ActiveLoop will determine which ``DataArrays`` it 
   will need to hold the  data it collects, and it creates a ``DataSetPP`` holding these ``DataArrays``.
   Thus: a ``Loop`` returns an ``ActiveLoop`` when actions are attached to it, and an ``ActiveLoop`` 
   returns a ``DataSetPP`` from ActiveLoop.get_data_set().

   Example:
       loop = Loop(sweep_parameter.sweep(0, 1, num=101), delay=0.1).each(*station.measure())
       data = loop.get_data_set(name='My 1D sweep')

   The ActiveLoop.run() then runs the loop to perform the experiment.

   Args:
       Should only be accessed automatically by the ``Loop`` class.


   .. py:attribute:: active_loop
      :value: None



   .. py:attribute:: sweep_values


   .. py:attribute:: delay


   .. py:attribute:: actions
      :value: []



   .. py:attribute:: progress_interval
      :value: None



   .. py:attribute:: then_actions
      :value: ()



   .. py:attribute:: station
      :value: None



   .. py:attribute:: bg_task
      :value: None



   .. py:attribute:: bg_final_task
      :value: None



   .. py:attribute:: bg_min_delay
      :value: None



   .. py:attribute:: data_set
      :value: None



   .. py:attribute:: progress_bar
      :value: True



   .. py:attribute:: was_broken
      :value: False



   .. py:attribute:: snake
      :value: False



   .. py:attribute:: flip
      :value: False



   .. py:method:: __getitem__(item)

      Retrieves action with index `item`

      Args:
          item: actions index

      Returns:
          loop.actions[item]



   .. py:method:: then(*actions, overwrite=False)

      Attach actions to be performed after the loop completes.

      These can only be ``Task`` and ``Wait`` actions, as they may not
      generate any data.

      returns a new ActiveLoop object - the original is untouched



      Args:
          *actions: ``Task`` and ``Wait`` objects to execute in order

          overwrite: (default False) whether subsequent .then() calls (including
              calls in an ActiveLoop after .then() has already been called on
              the Loop) will add to each other or overwrite the earlier ones.



   .. py:method:: with_bg_task(task, bg_final_task=None, min_delay=0.01)

      Attaches a background task to this loop.

      Args:
          task: A callable object with no parameters. This object will be
              invoked periodically during the measurement loop.

          bg_final_task: A callable object with no parameters. This object will be
              invoked to clean up after or otherwise finish the background
              task work.

          min_delay (default 1): The minimum number of seconds to wait
              between task invocations. Note that the actual time between
              task invocations may be much longer than this, as the task is
              only run between passes through the loop.



   .. py:method:: snapshot_base(update=False)

      Snapshot of this ActiveLoop's definition.



   .. py:method:: containers()

      Finds the data arrays that will be created by the actions in this
      loop, and nests them inside this level of the loop.

      Recursively calls `.containers` on any enclosed actions.



   .. py:method:: set_common_attrs(data_set, use_threads)

      Set a couple of common attributes that the main and nested loops

      all need to have:
      - the DataSetPP collecting all our measurements
      - a queue for communicating with the main process



   .. py:method:: get_data_set(*args, **kwargs)

      Return the data set for this loop.

      If no data set has been created yet, a new one will be created and
      returned. Note that all arguments can only be provided when the
      `DataSetPP` is first created; giving these during `run` when
      `get_data_set` has already been called on its own is an error.

      Args:
          data_manager: a DataManager instance (omit to use default,
              False to store locally)

      kwargs are passed along to data_set.new_data. The key ones are:

      Args:
          location: the location of the DataSetPP, a string whose meaning
              depends on formatter and io, or False to only keep in memory.
              May be a callable to provide automatic locations. If omitted, will
              use the default DataSetPP.location_provider
          name: if location is default or another provider function, name is
              a string to add to location to make it more readable/meaningful
              to users
          formatter: knows how to read and write the file format
              default can be set in DataSetPP.default_formatter
          io: knows how to connect to the storage (disk vs cloud etc)

          write_period: how often to save to storage during the loop.
              default 5 sec, use None to write only at the end. 
              
      Returns:
          a DataSetPP object that we can use to plot



   .. py:method:: time_estimate(station=None, extra_delay=[0, 0])

      Estimates the time it will take to run this loop. Currently only works for 1D or 2D loops, including 2D loops with multiple subloops.

      Args:
          station: a Station instance for snapshots (omit to use a previously
              provided Station, or the default Station)
          extra_delay: an array with extra delay per action in the loop.
              The first element is the extra delay for the outer loop, the second
              element is the extra delay for the inner loop(s). If there are more
              inner loops, they will all have the same extra delay as the second
              element. If there are no inner loops, this will be ignored.

      Returns:
          A string with the estimated time in seconds, minutes and hours, and the
          estimated time of completion.



   .. py:method:: run_temp(**kwargs)

      wrapper to run this loop in the foreground as a temporary data set,
      especially for use in composite parameters that need to run a Loop
      as part of their get method



   .. py:method:: run(plot=None, use_threads=False, quiet=False, station=None, progress_interval=False, set_active=True, publisher=None, progress_bar=True, check_written_data=True, *args, **kwargs)

      Execute this loop.

      Args:
          plot: a list of parameters to plot at each point in the loop.
              Can either be the DataArray objects, or the parameters themselves.

          use_threads: (default False): whenever there are multiple `get` calls
              back-to-back, execute them in separate threads so they run in
              parallel (as long as they don't block each other)

          quiet: (default False): set True to not print anything except errors

          station: a Station instance for snapshots (omit to use a previously
              provided Station, or the default Station)

          progress_interval (default None): show progress of the loop every x
              seconds. If provided here, will override any interval provided
              with the Loop definition. Default false, since the next item is better...

          progress_bar (default True): show a progress bar during the loop using tqdm

          check_written_data: At loop completion, check that the data written to file
              matches the data in memory. If not, write a copy of the data in memory
              and warn the user.
          

      kwargs are passed along to data_set.new_data. These can only be
      provided when the `DataSetPP` is first created; giving these during `run`
      when `get_data_set` has already been called on its own is an error.
      The key ones are:

      Args:
          location: the location of the DataSetPP, a string whose meaning
              depends on formatter and io, or False to only keep in memory.
              May be a callable to provide automatic locations. If omitted, will
              use the default DataSetPP.location_provider

          name: if location is default or another provider function, name is
              a string to add to location to make it more readable/meaningful
              to users

          formatter: knows how to read and write the file format
              default can be set in DataSetPP.default_formatter

          io: knows how to connect to the storage (disk vs cloud etc)
              write_period: how often to save to storage during the loop.
              default 5 sec, use None to write only at the end


      returns:
          a DataSetPP object that we can use to plot



