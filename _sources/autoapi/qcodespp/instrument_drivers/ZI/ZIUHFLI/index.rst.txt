qcodespp.instrument_drivers.ZI.ZIUHFLI
======================================

.. py:module:: qcodespp.instrument_drivers.ZI.ZIUHFLI


Attributes
----------

.. autoapisummary::

   qcodespp.instrument_drivers.ZI.ZIUHFLI.log


Classes
-------

.. autoapisummary::

   qcodespp.instrument_drivers.ZI.ZIUHFLI.AUXOutputChannel
   qcodespp.instrument_drivers.ZI.ZIUHFLI.Sweep
   qcodespp.instrument_drivers.ZI.ZIUHFLI.Scope
   qcodespp.instrument_drivers.ZI.ZIUHFLI.ZIUHFLI


Module Contents
---------------

.. py:data:: log

.. py:class:: AUXOutputChannel(parent: ZIUHFLI, name: str, channum: int)

   Bases: :py:obj:`qcodes.InstrumentChannel`


   Base class for a module in an instrument.
   This could be in the form of a channel (e.g. something that
   the instrument has multiple instances of) or another logical grouping
   of parameters that you wish to group together separate from the rest of the
   instrument.

   Args:
       parent: The instrument to which this module should be
         attached.
       name: The name of this module.
       **kwargs: Forwarded to the base class.



.. py:class:: Sweep(name, instrument, **kwargs)

   Bases: :py:obj:`qcodes.MultiParameter`


   Parameter class for the ZIUHFLI instrument class for the sweeper.

   The get method returns a tuple of arrays, where each array contains the
   values of a signal added to the sweep (e.g. demodulator 4 phase).

   Attributes:
       names (tuple): Tuple of strings containing the names of the sweep
         signals (to be measured)
       units (tuple): Tuple of strings containg the units of the signals
       shapes (tuple): Tuple of tuples each containing the Length of a
         signal.
       setpoints (tuple): Tuple of N copies of the sweep x-axis points,
         where N is he number of measured signals
       setpoint_names (tuple): Tuple of N identical strings with the name
         of the sweep x-axis.



   .. py:method:: build_sweep()

      Build a sweep with the current sweep settings. Must be called
      before the sweep can be executed.

      For developers:
      This is a general function for updating the sweeper.
      Every time a parameter of the sweeper is changed, this function
      must be called to update the sweeper. Although such behaviour is only
      strictly necessary for parameters that affect the setpoints of the
      Sweep parameter, having to call this function for any parameter is
      deemed more user friendly (easier to remember; when? -always).

      The function sets all (user specified) settings on the sweeper and
      additionally sets names, units, and setpoints for the Sweep
      parameter.




   .. py:method:: get_raw()

      Execute the sweeper and return the data corresponding to the
      subscribed signals.

      Returns:

          tuple: Tuple containg N numpy arrays where N is the number
            of signals added to the sweep.

      Raises:
          ValueError: If no signals have been added to the sweep
          ValueError: If a sweep setting has been modified since
            the last sweep, but Sweep.build_sweep has not been run



.. py:class:: Scope(name, instrument, **kwargs)

   Bases: :py:obj:`qcodes.MultiParameter`


   Parameter class for the ZI UHF-LI Scope Channel 1

   The .get method launches an acquisition and returns a tuple of two
   np.arrays
   FFT mode is NOT supported.

   Attributes:
       names (tuple): Tuple of strings containing the names of the sweep
         signals (to be measured)
       units (tuple): Tuple of strings containg the units of the signals
       shapes (tuple): Tuple of tuples each containing the Length of a
         signal.
       setpoints (tuple): Tuple of N copies of the sweep x-axis points,
         where N is he number of measured signals
       setpoint_names (tuple): Tuple of N identical strings with the name
         of the sweep x-axis.


   .. py:method:: add_post_trigger_action(action: Callable) -> None

      Add an action to be performed immediately after the trigger
      has been armed. The action must be a callable taking zero
      arguments



   .. py:property:: post_trigger_actions
      :type: List[Callable]



   .. py:method:: prepare_scope()

      Prepare the scope for a measurement. Must immediately preceed a
      measurement.



   .. py:method:: get_raw()

      Acquire data from the scope.

      Returns:
          tuple: Tuple of two n X m arrays where n is the number of segments
              and m is the number of points in the scope trace.

      Raises:
          ValueError: If the scope has not been prepared by running the
              prepare_scope function.



.. py:class:: ZIUHFLI(name: str, device_ID: str, **kwargs)

   Bases: :py:obj:`qcodes.Instrument`


   QCoDeS driver for ZI UHF-LI.

   Currently implementing demodulator settings and the sweeper functionality.

   Requires ZI Lab One software to be installed on the computer running QCoDeS.
   Furthermore, the Data Server and Web Server must be running and a connection
   between the two must be made.

   TODOs:
       * Add zoom-FFT


   .. py:attribute:: api_level
      :value: 5



   .. py:attribute:: sweeper


   .. py:attribute:: scope


   .. py:method:: NEPBW_to_timeconstant(NEPBW, order)
      :staticmethod:


      Helper function to translate a NEP BW and a filter order
      to a filter time constant. Meant to be used when calculating
      sweeper sweep times.

      Note: precise only to within a few percent.

      Args:
          NEPBW (float): The NEP bandwidth in Hz
          order (int): The filter order

      Returns:
          float: The filter time constant in s.



   .. py:method:: add_signal_to_sweeper(demodulator, attribute)

      Add a signal to the output of the sweeper. When the sweeper sweeps,
      the signals added to the sweeper are returned.

      Args:
          demodulator (int): A number from 1-8 choosing the demodulator.
            The same demodulator can be chosen several times for
            different attributes, e.g. demod1 X, demod1 phase
          attribute (str): The attribute to record, e.g. phase or Y

      Raises:
          ValueError: if a demodulator outside the allowed range is
            selected
          ValueError: if an attribute not in the list of allowed attributes
            is selected



   .. py:method:: remove_signal_from_sweeper(demodulator, attribute)

      Remove a signal from the output of the sweeper. If the signal
      has not previously been added, a warning is logged.

      Args:
          demodulator (int): A number from 1-8 choosing the demodulator.
            The same demodulator can be chosen several times for
            different attributes, e.g. demod1 X, demod1 phase
          attribute (str): The attribute to record, e.g. phase or Y



   .. py:method:: print_sweeper_settings()

      Pretty-print the current settings of the sweeper.
      If Sweep.build_sweep and Sweep.get are called, the sweep described
      here will be performed.



   .. py:method:: close()

      Override of the base class' close function



