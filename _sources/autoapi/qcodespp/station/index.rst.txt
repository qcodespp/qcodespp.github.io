qcodespp.station
================

.. py:module:: qcodespp.station

.. autoapi-nested-parse::

   Station objects - collect all the equipment you use to do an experiment.

   The Station class contained herein wraps the QCoDeS Station class and adds some functionality to it.
   It allows for the automatic addition of instruments and parameters to the station,
   and underlies the data acquisition. In qcodesplusplus there is no separate measurement
   context, since all measurements should be done in the context of a station anyway.
   Doing it like this forces the user to only measure parameters in the station,
   without the need for a separate measurement context.



Attributes
----------

.. autosummary::

   qcodespp.station.log


Classes
-------

.. autosummary::

   qcodespp.station.Station


Module Contents
---------------

.. py:data:: log

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



