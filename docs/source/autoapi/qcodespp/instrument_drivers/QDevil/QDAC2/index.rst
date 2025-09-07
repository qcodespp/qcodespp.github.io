qcodespp.instrument_drivers.QDevil.QDAC2
========================================

.. py:module:: qcodespp.instrument_drivers.QDevil.QDAC2


Attributes
----------

.. autosummary::

   qcodespp.instrument_drivers.QDevil.QDAC2.error_ambiguous_wave
   qcodespp.instrument_drivers.QDevil.QDAC2.ExternalInput


Classes
-------

.. autosummary::

   qcodespp.instrument_drivers.QDevil.QDAC2.QDac2Trigger_Context
   qcodespp.instrument_drivers.QDevil.QDAC2.QDac2ExternalTrigger
   qcodespp.instrument_drivers.QDevil.QDAC2.Sweep_Context
   qcodespp.instrument_drivers.QDevil.QDAC2.List_Context
   qcodespp.instrument_drivers.QDevil.QDAC2.Square_Context
   qcodespp.instrument_drivers.QDevil.QDAC2.Sine_Context
   qcodespp.instrument_drivers.QDevil.QDAC2.Triangle_Context
   qcodespp.instrument_drivers.QDevil.QDAC2.Awg_Context
   qcodespp.instrument_drivers.QDevil.QDAC2.Measurement_Context
   qcodespp.instrument_drivers.QDevil.QDAC2.QDac2Channel
   qcodespp.instrument_drivers.QDevil.QDAC2.Trace_Context
   qcodespp.instrument_drivers.QDevil.QDAC2.Virtual_Sweep_Context
   qcodespp.instrument_drivers.QDevil.QDAC2.Arrangement_Context
   qcodespp.instrument_drivers.QDevil.QDAC2.MultiCurrents_Context
   qcodespp.instrument_drivers.QDevil.QDAC2.QDac2


Functions
---------

.. autosummary::

   qcodespp.instrument_drivers.QDevil.QDAC2.ints_to_comma_separated_list
   qcodespp.instrument_drivers.QDevil.QDAC2.floats_to_comma_separated_list
   qcodespp.instrument_drivers.QDevil.QDAC2.comma_sequence_to_list
   qcodespp.instrument_drivers.QDevil.QDAC2.comma_sequence_to_list_of_floats
   qcodespp.instrument_drivers.QDevil.QDAC2.comma_sequence_to_single_float
   qcodespp.instrument_drivers.QDevil.QDAC2.diff_matrix
   qcodespp.instrument_drivers.QDevil.QDAC2.split_version_string_into_components
   qcodespp.instrument_drivers.QDevil.QDAC2.forward_and_back


Module Contents
---------------

.. py:data:: error_ambiguous_wave
   :value: 'Only one of frequency_Hz or period_s can be specified for a wave form'


.. py:function:: ints_to_comma_separated_list(array: Sequence[int]) -> str

.. py:function:: floats_to_comma_separated_list(array: Sequence[float]) -> str

.. py:function:: comma_sequence_to_list(sequence: str) -> Sequence[str]

.. py:function:: comma_sequence_to_list_of_floats(sequence: str) -> Sequence[float]

.. py:function:: comma_sequence_to_single_float(sequence: str) -> float

.. py:function:: diff_matrix(initial: Sequence[float], measurements: Sequence[Sequence[float]]) -> numpy.ndarray

   Subtract an array of measurements by an initial measurement
       


.. py:function:: split_version_string_into_components(version: str) -> List[str]

.. py:data:: ExternalInput

.. py:class:: QDac2Trigger_Context(parent: QDac2, value: int)

   Internal Triggers with automatic deallocation

   This context manager wraps an already-allocated internal trigger number so
   that the trigger can be automatically reclaimed when the context exits.


   .. py:method:: __enter__()


   .. py:method:: __exit__(exc_type, exc_val, exc_tb)


   .. py:property:: value
      :type: int


      internal SCPI trigger number



.. py:class:: QDac2ExternalTrigger(parent: QDac2, name: str, external: int)

   Bases: :py:obj:`qcodes.InstrumentChannel`


   External output trigger

   There are three 5V isolated triggers on the front (1, 2, 3) and two
   non-isolated 3V3 on the back (4, 5).


.. py:class:: Sweep_Context(channel: QDac2Channel, start_V: float, stop_V: float, points: int, repetitions: int, dwell_s: float, delay_s: float, backwards: bool, stepped: bool)

   Bases: :py:obj:`_Dc_Context`


   .. py:method:: start() -> None

      Start the DC sweep
              



   .. py:method:: points() -> int

      Returns:
          int: Number of steps in the DC sweep



   .. py:method:: cycles_remaining() -> int

      Returns:
          int: Number of cycles remaining in the DC sweep



   .. py:method:: time_s() -> float

      Returns:
          float: Seconds that it will take to do the sweep



   .. py:method:: start_V() -> float

      Returns:
          float: Starting voltage



   .. py:method:: stop_V() -> float

      Returns:
          float: Ending voltage



   .. py:method:: values_V() -> Sequence[float]

      Returns:
          Sequence[float]: List of voltages



.. py:class:: List_Context(channel: QDac2Channel, voltages: Sequence[float], repetitions: int, dwell_s: float, delay_s: float, backwards: bool, stepped: bool)

   Bases: :py:obj:`_Dc_Context`


   .. py:method:: start() -> None

      Start the DC list generator
              



   .. py:method:: append(voltages: Sequence[float]) -> None

      Append voltages to the existing list

      Arguments:
          voltages (Sequence[float]): Sequence of voltages



   .. py:method:: points() -> int

      Returns:
          int: Number of steps in the DC list



   .. py:method:: cycles_remaining() -> int

      Returns:
          int: Number of cycles remaining in the DC list



   .. py:method:: values_V() -> Sequence[float]

      Returns:
          Sequence[float]: List of voltages



.. py:class:: Square_Context(channel: QDac2Channel, frequency_Hz: Optional[float], repetitions: int, period_s: Optional[float], duty_cycle_percent: float, kind: str, inverted: bool, span_V: float, offset_V: float, delay_s: float, slew_V_s: Optional[float])

   Bases: :py:obj:`_Waveform_Context`


   .. py:method:: start() -> None

      Start the square wave generator
              



   .. py:method:: abort() -> None

      Abort any running square wave generator
              



   .. py:method:: cycles_remaining() -> int

      Returns:
          int: Number of cycles remaining in the square wave



   .. py:method:: end_marker() -> QDac2Trigger_Context

      Internal trigger that will mark the end of the square wave

      A new internal trigger is allocated if necessary.

      Returns:
          QDac2Trigger_Context: trigger that will mark the end



   .. py:method:: start_marker() -> QDac2Trigger_Context

      Internal trigger that will mark the beginning of the square wave

      A new internal trigger is allocated if necessary.

      Returns:
          QDac2Trigger_Context: trigger that will mark the beginning



   .. py:method:: period_end_marker() -> QDac2Trigger_Context

      Internal trigger that will mark the end of each period

      A new internal trigger is allocated if necessary.

      Returns:
          QDac2Trigger_Context: trigger that will mark the end of each period



   .. py:method:: period_start_marker() -> QDac2Trigger_Context

      Internal trigger that will mark the beginning of each period

      A new internal trigger is allocated if necessary.

      Returns:
          QDac2Trigger_Context: trigger that will mark the beginning of each period



   .. py:method:: start_on(trigger: QDac2Trigger_Context) -> None

      Attach internal trigger to start the square wave generator

      Args:
          trigger (QDac2Trigger_Context): trigger that will start square wave



   .. py:method:: start_on_external(trigger: ExternalInput) -> None

      Attach external trigger to start the square wave generator

      Args:
          trigger (ExternalInput): external trigger that will start square wave



.. py:class:: Sine_Context(channel: QDac2Channel, frequency_Hz: Optional[float], repetitions: int, period_s: Optional[float], inverted: bool, span_V: float, offset_V: float, delay_s: float, slew_V_s: Optional[float])

   Bases: :py:obj:`_Waveform_Context`


   .. py:method:: start() -> None

      Start the sine wave generator
              



   .. py:method:: abort() -> None

      Abort any running sine wave generator
              



   .. py:method:: cycles_remaining() -> int

      Returns:
          int: Number of cycles remaining in the sine wave



   .. py:method:: end_marker() -> QDac2Trigger_Context

      Internal trigger that will mark the end of the sine wave

      A new internal trigger is allocated if necessary.

      Returns:
          QDac2Trigger_Context: trigger that will mark the end



   .. py:method:: start_marker() -> QDac2Trigger_Context

      Internal trigger that will mark the beginning of the sine wave

      A new internal trigger is allocated if necessary.

      Returns:
          QDac2Trigger_Context: trigger that will mark the beginning



   .. py:method:: period_end_marker() -> QDac2Trigger_Context

      Internal trigger that will mark the end of each period

      A new internal trigger is allocated if necessary.

      Returns:
          QDac2Trigger_Context: trigger that will mark the end of each period



   .. py:method:: period_start_marker() -> QDac2Trigger_Context

      Internal trigger that will mark the beginning of each period

      A new internal trigger is allocated if necessary.

      Returns:
          QDac2Trigger_Context: trigger that will mark the beginning of each period



   .. py:method:: start_on(trigger: QDac2Trigger_Context) -> None

      Attach internal trigger to start the sine wave generator

      Args:
          trigger (QDac2Trigger_Context): trigger that will start sine wave



   .. py:method:: start_on_external(trigger: ExternalInput) -> None

      Attach external trigger to start the sine wave generator

      Args:
          trigger (ExternalInput): external trigger that will start sine wave



.. py:class:: Triangle_Context(channel: QDac2Channel, frequency_Hz: Optional[float], repetitions: int, period_s: Optional[float], duty_cycle_percent: float, inverted: bool, span_V: float, offset_V: float, delay_s: float, slew_V_s: Optional[float])

   Bases: :py:obj:`_Waveform_Context`


   .. py:method:: start() -> None

      Start the triangle wave generator
              



   .. py:method:: abort() -> None

      Abort any running triangle wave generator
              



   .. py:method:: cycles_remaining() -> int

      Returns:
          int: Number of cycles remaining in the triangle wave



   .. py:method:: end_marker() -> QDac2Trigger_Context

      Internal trigger that will mark the end of the triangle wave

      A new internal trigger is allocated if necessary.

      Returns:
          QDac2Trigger_Context: trigger that will mark the end



   .. py:method:: start_marker() -> QDac2Trigger_Context

      Internal trigger that will mark the beginning of the triangle wave

      A new internal trigger is allocated if necessary.

      Returns:
          QDac2Trigger_Context: trigger that will mark the beginning



   .. py:method:: period_end_marker() -> QDac2Trigger_Context

      Internal trigger that will mark the end of each period

      A new internal trigger is allocated if necessary.

      Returns:
          QDac2Trigger_Context: trigger that will mark the end of each period



   .. py:method:: period_start_marker() -> QDac2Trigger_Context

      Internal trigger that will mark the beginning of each period

      A new internal trigger is allocated if necessary.

      Returns:
          QDac2Trigger_Context: trigger that will mark the beginning of each period



   .. py:method:: start_on(trigger: QDac2Trigger_Context) -> None

      Attach internal trigger to start the triangle wave generator

      Args:
          trigger (QDac2Trigger_Context): trigger that will start triangle



   .. py:method:: start_on_external(trigger: ExternalInput) -> None

      Attach external trigger to start the triangle wave generator

      Args:
          trigger (ExternalInput): external trigger that will start triangle



.. py:class:: Awg_Context(channel: QDac2Channel, trace_name: str, repetitions: int, scale: float, offset_V: float, slew_V_s: Optional[float])

   Bases: :py:obj:`_Waveform_Context`


   .. py:method:: start() -> None

      Start the AWG
              



   .. py:method:: abort() -> None

      Abort any running AWG
              



   .. py:method:: cycles_remaining() -> int

      Returns:
          int: Number of cycles remaining in the AWG



   .. py:method:: end_marker() -> QDac2Trigger_Context

      Internal trigger that will mark the end of the AWG

      A new internal trigger is allocated if necessary.

      Returns:
          QDac2Trigger_Context: trigger that will mark the end



   .. py:method:: start_marker() -> QDac2Trigger_Context

      Internal trigger that will mark the beginning of the AWG

      A new internal trigger is allocated if necessary.

      Returns:
          QDac2Trigger_Context: trigger that will mark the beginning



   .. py:method:: period_end_marker() -> QDac2Trigger_Context

      Internal trigger that will mark the end of each period

      A new internal trigger is allocated if necessary.

      Returns:
          QDac2Trigger_Context: trigger that will mark the end of each period



   .. py:method:: period_start_marker() -> QDac2Trigger_Context

      Internal trigger that will mark the beginning of each period

      A new internal trigger is allocated if necessary.

      Returns:
          QDac2Trigger_Context: trigger that will mark the beginning of each period



   .. py:method:: start_on(trigger: QDac2Trigger_Context) -> None

      Attach internal trigger to start the AWG

      Args:
          trigger (QDac2Trigger_Context): trigger that will start AWG



   .. py:method:: start_on_external(trigger: ExternalInput) -> None

      Attach external trigger to start the AWG

      Args:
          trigger (ExternalInput): external trigger that will start AWG



.. py:class:: Measurement_Context(channel: QDac2Channel, delay_s: float, repetitions: int, current_range: str, aperture_s: Optional[float], nplc: Optional[int])

   Bases: :py:obj:`_Channel_Context`


   .. py:method:: start() -> None

      Start a current measurement
              



   .. py:method:: start_on(trigger: QDac2Trigger_Context) -> None

      Attach internal trigger to start the current measurement

      Args:
          trigger (QDac2Trigger_Context): trigger that will start measurement



   .. py:method:: start_on_external(trigger: ExternalInput) -> None

      Attach external trigger to start the current measurement

      Args:
          trigger (ExternalInput): trigger that will start measurement



   .. py:method:: abort() -> None

      Abort current measurement
              



   .. py:method:: n_cycles_remaining() -> int

      Returns:
          int: Number of measurements remaining



   .. py:method:: n_available() -> int

      Returns:
          int: Number of measurements available



   .. py:method:: available_A() -> Sequence[float]

      Retrieve current measurements

      The available measurements will be removed from measurement queue.

      Returns:
          Sequence[float]: list of available current measurements



   .. py:method:: peek_A() -> float

      Peek at the first available current measurement

      Returns:
          float: current in Amperes



.. py:class:: QDac2Channel(parent: QDac2, name: str, channum: int)

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



   .. py:attribute:: loc_folder


   .. py:property:: number
      :type: int


      Channel number



   .. py:method:: clear_measurements() -> Sequence[float]

      Retrieve current measurements

      The available measurements will be removed from measurement queue.

      Returns:
          Sequence[float]: list of available current measurements



   .. py:method:: measurement(delay_s: float = 0.0, repetitions: int = 1, current_range: str = 'high', aperture_s: Optional[float] = None, nplc: Optional[int] = None) -> Measurement_Context

      Set up a sequence of current measurements

      Args:
          delay_s (float, optional): Seconds to delay the actual measurement after trigger (default 0)
          repetitions (int, optional): Number of consecutive measurements (default 1)
          current_range (str, optional): high (10mA, default) or low (200nA)
          nplc (None, optional): Integration time in power-line cycles (default 1)
          aperture_s (None, optional): Seconds of integration time instead of NPLC

      Returns:
          Measurement_Context: context manager

      Raises:
          ValueError: configuration error



   .. py:method:: output_mode(range: str = 'HIGH', filter: str = 'HIGH') -> None

      Set the output voltage

      Args:
          range (str, optional): Low or high (default) current range
          filter (str, optional): DC (10Hz), medium (10kHz) or high (300kHz, default) voltage filter



   .. py:method:: dc_list(voltages: Sequence[float], repetitions: int = 1, dwell_s: float = 0.001, delay_s: float = 0, backwards: bool = False, stepped: bool = False) -> List_Context

      Set up a DC-list generator

      Args:
          voltages (Sequence[float]): Voltages in list
          repetitions (int, optional): Number of repetitions of the list (default 1)
          dwell_s (float, optional): Seconds between each voltage (default 1ms)
          delay_s (float, optional): Seconds of delay after receiving a trigger (default 0)
          backwards (bool, optional): Use list in reverse (default is forward)
          stepped (bool, optional): True means that each step needs to be triggered (default False)

      Returns:
          List_Context: context manager



   .. py:method:: dc_sweep(start_V: float, stop_V: float, points: int, repetitions: int = 1, dwell_s: float = 0.001, delay_s: float = 0, backwards=False, stepped=True) -> Sweep_Context

      Set up a DC sweep

      Args:
          start_V (float): Start voltage
          stop_V (float): Send voltage
          points (int): Number of steps
          repetitions (int, optional): Number of repetition (default 1)
          dwell_s (float, optional): Seconds between each voltage (default 1ms)
          delay_s (float, optional): Seconds of delay after receiving a trigger (default 0)
          backwards (bool, optional): Sweep in reverse (default is forward)
          stepped (bool, optional): True means that each step needs to be triggered (default False)

      Returns:
          Sweep_Context: context manager



   .. py:method:: square_wave(frequency_Hz: Optional[float] = None, period_s: Optional[float] = None, repetitions: int = -1, duty_cycle_percent: float = 50.0, kind: str = 'symmetric', inverted: bool = False, span_V: float = 0.2, offset_V: float = 0.0, delay_s: float = 0, slew_V_s: Optional[float] = None) -> Square_Context

      Set up a square-wave generator

      Args:
          frequency_Hz (float, optional): Frequency
          period_s (float, optional): Period length (instead of frequency)
          repetitions (int, optional): Number of repetition (default infinite)
          duty_cycle_percent (float, optional): Percentage on-time (default 50%)
          kind (str, optional): Positive, negative or symmetric (default) around the offset
          inverted (bool, optional): True means flipped (default False)
          span_V (float, optional): Voltage span (default 200mV)
          offset_V (float, optional): Offset (default 0V)
          delay_s (float, optional): Seconds of delay after receiving a trigger (default 0)
          slew_V_s (float, optional): Max slew rate in V/s (default None)

      Returns:
          Square_Context: context manager

      Raises:
          ValueError: configuration error



   .. py:method:: sine_wave(frequency_Hz: Optional[float] = None, period_s: Optional[float] = None, repetitions: int = -1, inverted: bool = False, span_V: float = 0.2, offset_V: float = 0.0, delay_s: float = 0, slew_V_s: Optional[float] = None) -> Sine_Context

      Set up a sine-wave generator

      Args:
          frequency_Hz (float, optional): Frequency
          period_s (float, optional): Period length (instead of frequency)
          repetitions (int, optional): Number of repetition (default infinite)
          inverted (bool, optional): True means flipped (default False)
          span_V (float, optional): Voltage span (default 200mV)
          offset_V (float, optional): Offset (default 0V)
          delay_s (float, optional): Seconds of delay after receiving a trigger (default 0)
          slew_V_s (None, optional): Max slew rate in V/s (default None)

      Returns:
          Sine_Context: context manager

      Raises:
          ValueError: configuration error



   .. py:method:: triangle_wave(frequency_Hz: Optional[float] = None, period_s: Optional[float] = None, repetitions: int = -1, duty_cycle_percent: float = 50.0, inverted: bool = False, span_V: float = 0.2, offset_V: float = 0.0, delay_s: float = 0, slew_V_s: Optional[float] = None) -> Triangle_Context

      Set up a triangle-wave generator

      Args:
          frequency_Hz (float, optional): Frequency
          period_s (float, optional): Period length (instead of frequency)
          repetitions (int, optional): Number of repetition (default infinite)
          duty_cycle_percent (float, optional): Percentage on-time (default 50%)
          inverted (bool, optional): True means flipped (default False)
          span_V (float, optional): Voltage span (default 200mV)
          offset_V (float, optional): Offset (default 0V)
          delay_s (float, optional): Seconds of delay after receiving a trigger (default 0)
          slew_V_s (float, optional): Max slew rate in V/s (default None)

      Returns:
          Triangle_Context: context manager

      Raises:
          ValueError: configuration error



   .. py:method:: arbitrary_wave(trace_name: str, repetitions: int = 1, scale: float = 1.0, offset_V: float = 0.0, slew_V_s: Optional[float] = None) -> Awg_Context

      Set up an arbitrary-wave generator

      Args:
          trace_name (str): Use data from this named trace
          repetitions (int, optional): Number of repetition (default 1)
          scale (float, optional): Scaling factor of voltages (default 1)
          offset_V (float, optional): Offset (default 0V)
          slew_V_s (None, optional): Max slew rate in V/s (default None)

      Returns:
          Awg_Context: context manager



   .. py:method:: ask_channel(cmd: str) -> str

      Inject channel number into SCPI query

      Arguments:
          cmd (str): Must contain a '{0}' placeholder for the channel number

      Returns:
          str: SCPI answer



   .. py:method:: write_channel(cmd: str) -> None

      Inject channel number into SCPI command

      Arguments:
          cmd (str): Must contain a '{0}' placeholder for the channel number



   .. py:method:: write_channel_floats(cmd: str, values: Sequence[float]) -> None

      Inject channel number and a list of values into SCPI command

      The values are appended to the end of the command.

      Arguments:
          cmd (str): Must contain a '{0}' placeholder for channel number
          values (Sequence[float]): Sequence of numbers



   .. py:method:: write(cmd: str) -> None

      Send a SCPI command

      Args:
          cmd (str): SCPI command



.. py:class:: Trace_Context(parent, name: str, size: int)

   .. py:method:: __len__()


   .. py:property:: size
      :type: int


      Number of values in trace



   .. py:property:: name
      :type: str


      Name of trace



   .. py:method:: waveform(values: Sequence[float]) -> None

      Fill values into trace

      Args:
          values (Sequence[float]): Sequence of values

      Raises:
          ValueError: size mismatch



.. py:class:: Virtual_Sweep_Context(arrangement: Arrangement_Context, sweep: numpy.ndarray, start_trigger: Optional[str], step_time_s: float, step_trigger: Optional[str], repetitions: Optional[int])

   .. py:method:: __enter__()


   .. py:method:: __exit__(exc_type, exc_val, exc_tb)


   .. py:method:: actual_values_V(contact: str) -> numpy.ndarray

      The corrected values that would actually be sent to the contact

      Args:
          contact (str): Name of contact

      Returns:
          np.ndarray: Corrected voltages



   .. py:method:: start() -> None

      Start the 2D sweep
              



.. py:class:: Arrangement_Context(qdac: QDac2, contacts: Dict[str, int], output_triggers: Optional[Dict[str, int]], internal_triggers: Optional[Sequence[str]])

   .. py:attribute:: loc_folder


   .. py:attribute:: curr_fit_params_high


   .. py:attribute:: curr_fit_params_low


   .. py:attribute:: init_voltages


   .. py:attribute:: init_curr_ranges


   .. py:method:: __enter__()


   .. py:method:: __exit__(exc_type, exc_val, exc_tb)


   .. py:property:: shape
      :type: int


      Number of contacts in the arrangement



   .. py:property:: correction_matrix
      :type: numpy.ndarray


      Correction matrix



   .. py:property:: contact_names
      :type: Sequence[str]


      Returns:
          Sequence[str]: Contact names in the same order as channel_numbers



   .. py:method:: initiate_correction(contact: str, factors: Sequence[float]) -> None

      Override how much a particular contact influences the other contacts

      Args:
          contact (str): Name of contact
          factors (Sequence[float]): factors between -1.0 and 1.0



   .. py:method:: set_virtual_voltage(contact: str, voltage: float) -> None

      Set virtual voltage on specific contact

      The actual voltage that the contact will receive depends on the
      correction matrix.

      Args:
          contact (str): Name of contact
          voltage (float): Voltage corresponding to no correction



   .. py:method:: set_virtual_voltages(contacts_to_voltages: Dict[str, float]) -> None

      Set virtual voltages on specific contacts in one go

      The actual voltage that each contact will receive depends on the
      correction matrix.

      Args:
          contact_to_voltages (Dict[str,float]): contact to voltage map



   .. py:method:: add_correction(contact: str, factors: Sequence[float]) -> None

      Update how much a particular contact influences the other contacts

      This is mostly useful in arrangements where each contact has significant
      effect only on nearby contacts, and thus can be added incrementally.

      The factors are extended by the identity matrix and multiplied to the
      correction matrix.

      Args:
          contact (str): Name of contact
          factors (Sequence[float]): factors usually between -1.0 and 1.0



   .. py:property:: channel_numbers
      :type: Sequence[int]


      Returns:
          Sequence[int]: Channels numbers in the same order as contact_names



   .. py:method:: channel(name: str) -> QDac2Channel


   .. py:method:: virtual_voltage(contact: str) -> float

      Args:
          contact (str): Name of contact

      Returns:
          float: Voltage before correction



   .. py:method:: actual_voltages() -> Sequence[float]

      Returns:
          Sequence[float]: Corrected voltages for all contacts



   .. py:method:: get_trigger_by_name(name: str) -> QDac2Trigger_Context

      Args:
          name (str): Name of trigger

      Returns:
          QDac2Trigger_Context: Trigger context manager



   .. py:method:: currents_A() -> Sequence[float]

      Measure currents on all contacts using calibration. Note: Assumes nplc and curr_range set properly previously.

              



   .. py:method:: currents_A_ucal(nplc: int = 1, current_range: str = 'low') -> Sequence[float]

      Measure currents on all contacts. Note: uncalibrated current! Large error if high resistive load

      Args:
          nplc (int, optional): Number of powerline cycles to average over
          current_range (str, optional): Current range (default low)



   .. py:method:: virtual_sweep(contact: str, voltages: Sequence[float], start_sweep_trigger: Optional[str] = None, step_time_s: float = 1e-05, step_trigger: Optional[str] = None, repetitions: int = 1) -> Virtual_Sweep_Context

      Sweep a contact to create a 1D sweep

      Args:
          contact (str): Name of sweeping contact
          voltages (Sequence[float]): Virtual sweep voltages
          outer_contact (str): Name of slow-changing (outer) contact
          start_sweep_trigger (None, optional): Trigger that starts sweep
          step_time_s (float, optional): Delay between voltage changes
          step_trigger (None, optional): Trigger that marks each step
          repetitions (int, Optional): Number of back-and-forth sweeps, or -1 for infinite

      Returns:
          Virtual_Sweep_Context: context manager



   .. py:method:: virtual_sweep2d(inner_contact: str, inner_voltages: Sequence[float], outer_contact: str, outer_voltages: Sequence[float], start_sweep_trigger: Optional[str] = None, inner_step_time_s: float = 1e-05, inner_step_trigger: Optional[str] = None, repetitions: int = 1) -> Virtual_Sweep_Context

      Sweep two contacts to create a 2D sweep

      Args:
          inner_contact (str): Name of fast-changing (inner) contact
          inner_voltages (Sequence[float]): Inner contact virtual voltages
          outer_contact (str): Name of slow-changing (outer) contact
          outer_voltages (Sequence[float]): Outer contact virtual voltages
          start_sweep_trigger (None, optional): Trigger that starts sweep
          inner_step_time_s (float, optional): Delay between voltage changes
          inner_step_trigger (None, optional): Trigger that marks each step
          repetitions (int, Optional): Number of back-and-forth sweeps, or -1 for infinite

      Returns:
          Virtual_Sweep_Context: context manager



   .. py:method:: virtual_detune(contacts: Sequence[str], start_V: Sequence[float], end_V: Sequence[float], steps: int, start_trigger: Optional[str] = None, step_time_s: float = 1e-05, step_trigger: Optional[str] = None, repetitions: int = 1) -> Virtual_Sweep_Context

      Sweep any number of contacts linearly from one set of values to another set of values

      Args:
          contacts (Sequence[str]): contacts involved in sweep
          start_V (Sequence[float]): First-extreme values
          end_V (Sequence[float]): Second-extreme values
          steps (int): Number of steps between extremes
          start_trigger (None, optional): Trigger that starts sweep
          step_time_s (float, Optional): Seconds between each step
          step_trigger (None, optional): Trigger that marks each step
          repetitions (int, Optional): Number of back-and-forth sweeps, or -1 for infinite



   .. py:method:: leakage(modulation_V: float, nplc: int = 2) -> numpy.ndarray

      Run a simple leakage test between the contacts

      Each contact is changed in turn and the resulting change in current from
      steady-state is recorded.  The resulting resistance matrix is calculated
      as modulation_voltage divided by current_change.

      Args:
          modulation_V (float): Virtual voltage added to each contact
          nplc (int, Optional): Powerline cycles to wait for each measurement

      Returns:
          ndarray: contact-to-contact resistance in Ohms



.. py:class:: MultiCurrents_Context(qdac: QDac2, chans, name='qdac_currents')

   Bases: :py:obj:`qcodes.MultiParameter`


   A gettable parameter that returns multiple values with separate names,
   each of arbitrary shape. Not necessarily part of an instrument.

   Subclasses should define a ``.get_raw`` method, which returns a sequence of
   values. This method is automatically wrapped to provide a ``.get`` method.
   When used in a legacy  method``Loop`` or ``Measure`` operation, each of
   these values will be entered into a different ``DataArray``. The
   constructor args describe what data we expect from each ``.get`` call
   and how it should be handled. ``.get`` should always return the same
   number of items, and most of the constructor arguments should be tuples
   of that same length.

   For now you must specify upfront the array shape of each item returned by
   ``.get_raw``, and this cannot change from one call to the next. Later, we
   intend to require only that you specify the dimension of each item
   returned, and the size of each dimension can vary from call to call.

   Args:
       name: The local name of the whole parameter. Should be a valid
           identifier, ie no spaces or special characters. If this parameter
           is part of an Instrument or Station, this is how it will be
           referenced from that parent, i.e. ``instrument.name`` or
           ``instrument.parameters[name]``.

       names: A name for each item returned by a ``.get``
           call. Will be used as the basis of the ``DataArray`` names
           when this parameter is used to create a ``DataSet``.

       shapes: The shape (as used in numpy arrays) of
           each item. Scalars should be denoted by (), 1D arrays as (n,),
           2D arrays as (n, m), etc.

       instrument: The instrument this parameter
           belongs to, if any.

       labels: A label for each item. Normally used
           as the axis label when a component is graphed, along with the
           matching entry from ``units``.

       units: A unit of measure for each item.
           Use ``''`` or ``None`` for unitless values.

       setpoints: ``array`` can be a DataArray, numpy.ndarray, or sequence.
           The setpoints for each returned array. An N-dimension item should
           have N setpoint arrays, where the first is 1D, the second 2D, etc.
           If omitted for any or all items, defaults to integers from zero in
           each respective direction.
           **Note**: if the setpoints will be different each measurement,
           leave this out and return the setpoints (with extra names) in
           ``.get``.

       setpoint_names: One identifier (like
           ``name``) per setpoint array. Ignored if a setpoint is a
           DataArray, which already has a name.

       setpoint_labels: One label (like
           ``labels``) per setpoint array. Ignored if a setpoint is a
           DataArray, which already has a label.

       setpoint_units: One unit (like
           ``V``) per setpoint array. Ignored if a setpoint is a
           DataArray, which already has a unit.

       docstring: Documentation string for the ``__doc__``
           field of the object. The ``__doc__`` field of the  instance is
           used by some help systems, but not all

       snapshot_get: Prevent any update to the parameter, for example
           if it takes too long to update. Default ``True``.

       snapshot_value: Should the value of the parameter be stored in the
           snapshot. Unlike Parameter this defaults to False as
           MultiParameters are potentially huge.

       snapshot_exclude: True prevents parameter to be
           included in the snapshot. Useful if there are many of the same
           parameter which are clogging up the snapshot.
           Default ``False``.

       metadata: Extra information to include with the
           JSON snapshot of the parameter.



   .. py:attribute:: arrangement


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



.. py:function:: forward_and_back(start: float, end: float, steps: int)

.. py:class:: QDac2(name: str, address: str, **kwargs)

   Bases: :py:obj:`qcodes.VisaInstrument`


   Base class for all instruments using visa connections.

   Args:
       name: What this instrument is called locally.
       address: The visa resource name to use to connect.
       timeout: seconds to allow for responses.  If "unset" will read the value from
          `self.default_timeout`. None means wait forever. Default 5.
       terminator: Read and write termination character(s).
           If unset will use `self.default_terminator`.
           If None the terminator will not be set and we
           rely on the defaults from PyVisa. Default None.
       device_clear: Perform a device clear. Default True.
       visalib: Visa backend to use when connecting to this instrument.
           This should be in the form of a string '<pathtofile>@<backend>'.
           Both parts can be omitted and pyvisa will try to infer the
           path to the visa backend file.
           By default the IVI backend is used if found, but '@py' will use the
           ``pyvisa-py`` backend. Note that QCoDeS does not install (or even require)
           ANY backends, it is up to the user to do that. see eg:
           http://pyvisa.readthedocs.org/en/stable/names.html
       metadata: additional static metadata to add to this
           instrument's JSON snapshot.
       pyvisa_sim_file: Name of a pyvisa-sim yaml file used to simulate the instrument.
           The file is expected to be loaded from a python module.
           The file can be given either as only the file name in which case it is loaded
           from ``qcodes.instruments.sims`` or in the format ``module:filename`` e.g.
           ``qcodes.instruments.sims:AimTTi_PL601P.yaml`` in which case it is loaded
           from the supplied module. Note that it is an error to pass both
           ``pyvisa_sim_file`` and ``visalib``.
       **kwargs: Other kwargs are forwarded to the baseclass.

   See help for :class:`.Instrument` for additional information on writing
   instrument subclasses.



   .. py:attribute:: serial


   .. py:method:: n_channels() -> int

      Returns:
          int: Number of channels



   .. py:method:: channel(ch: int) -> QDac2Channel

      Args:
          ch (int): Channel number

      Returns:
          QDac2Channel: Visa representation of the channel



   .. py:method:: n_triggers() -> int
      :staticmethod:


      Returns:
          int: Number of internal triggers



   .. py:method:: n_external_inputs() -> int
      :staticmethod:


      Returns:
          int: Number of external input triggers



   .. py:method:: n_external_outputs() -> int

      Returns:
          int: Number of external output triggers



   .. py:method:: allocate_trigger() -> QDac2Trigger_Context

      Allocate an internal trigger

      Does not have any effect on the instrument, only the driver.

      Returns:
          QDac2Trigger_Context: Context manager

      Raises:
          ValueError: no free triggers



   .. py:method:: free_trigger(trigger: QDac2Trigger_Context) -> None

      Free an internal trigger

      Does not have any effect on the instrument, only the driver.

      Args:
          trigger (QDac2Trigger_Context): trigger to free



   .. py:method:: free_all_triggers() -> None

      Free all an internal triggers

      Does not have any effect on the instrument, only the driver.



   .. py:method:: connect_external_trigger(port: int, trigger: QDac2Trigger_Context, width_s: float = 1e-06) -> None

      Route internal trigger to external trigger

      Args:
          port (int): External output trigger number
          trigger (QDac2Trigger_Context): Internal trigger
          width_s (float, optional): Output trigger width in seconds (default 1ms)



   .. py:method:: reset() -> None


   .. py:method:: errors() -> str

      Retrieve and clear all previous errors

      Returns:
          str: Comma separated list of errors or '0, "No error"'



   .. py:method:: error() -> str

      Retrieve next error

      Returns:
          str: The next error or '0, "No error"'



   .. py:method:: n_errors() -> int

      Peek at number of previous errors

      Returns:
          int: Number of errors



   .. py:method:: start_all() -> None

      Trigger the global SCPI bus (``*TRG``)

      All generators, that have not been explicitly set to trigger on an
      internal or external trigger, will be started.



   .. py:method:: remove_traces() -> None

      Delete all trace definitions from the instrument

      This means that all AWGs loose their data.



   .. py:method:: traces() -> Sequence[str]

      List all defined traces

      Returns:
          Sequence[str]: trace names



   .. py:method:: allocate_trace(name: str, size: int) -> Trace_Context

      Reserve memory for a new trace

      Args:
          name (str): Name of new trace
          size (int): Number of voltage values in the trace

      Returns:
          Trace_Context: context manager



   .. py:method:: mac() -> str

      Returns:
          str: Media Access Control (MAC) address of the instrument



   .. py:method:: arrange(contacts: Dict[str, int], output_triggers: Optional[Dict[str, int]] = None, internal_triggers: Optional[Sequence[str]] = None) -> Arrangement_Context

      An arrangement of contacts and triggers for virtual gates

      Each contact corresponds to a particular output channel.  Each
      output_trigger corresponds to a particular external output trigger.
      Each internal_trigger will be allocated from the pool of internal
      triggers, and can later be used for synchronisation.  After
      initialisation of the arrangement, contacts and triggers can only be
      referred to by name.

      The voltages that will appear on each contact depends not only on the
      specified virtual voltage, but also on a correction matrix.  Initially,
      the contacts are assumed to not influence each other, which means that
      the correction matrix is the identity matrix, ie. the row for
      each contact has a value of [0, ..., 0, 1, 0, ..., 0].

      Args:
          contacts (Dict[str, int]): Name/channel pairs
          output_triggers (Sequence[Tuple[str,int]], optional): Name/number pairs of output triggers
          internal_triggers (Sequence[str], optional): List of names of internal triggers to allocate

      Returns:
          Arrangement_Context: context manager



   .. py:method:: multi_currents(channel_list=[i + 1 for i in range(24)], name='qdac_currents')


   .. py:method:: start_recording_scpi() -> None

      Record all SCPI commands sent to the instrument

      Any previous recordings are removed.  To inspect the SCPI commands sent
      to the instrument, call get_recorded_scpi_commands().



   .. py:method:: get_recorded_scpi_commands() -> List[str]

      Returns:
          Sequence[str]: SCPI commands sent to the instrument



   .. py:method:: clear() -> None

      Reset the VISA message queue of the instrument
              



   .. py:method:: clear_read_queue() -> Sequence[str]

      Flush the VISA message queue of the instrument

      Takes at least _message_flush_timeout_ms to carry out.

      Returns:
          Sequence[str]: Messages lingering in queue



   .. py:method:: write(cmd: str) -> None

      Send SCPI command to instrument

      Args:
          cmd (str): SCPI command



   .. py:method:: ask(cmd: str) -> str

      Send SCPI query to instrument

      Args:
          cmd (str): SCPI query

      Returns:
          str: SCPI answer



   .. py:method:: write_floats(cmd: str, values: Sequence[float]) -> None

      Append a list of values to a SCPI command

      By default, the values are IEEE binary encoded.

      Remember to include separating space in command if needed.



   .. py:method:: print_all_voltages()


   .. py:method:: print_all_currents()


   .. py:method:: set_multiple_voltages(voltage, channel_list=[i + 1 for i in range(24)], steps=1, step_time=0.03)


   .. py:method:: set_multiple_channels(parameter, value, channel_list=[i + 1 for i in range(24)])


   .. py:method:: get_multiple_channels(parameter, channel_list=[i + 1 for i in range(24)])


   .. py:method:: calibrate_currents(channel_list=0, lowcurrent=True, highcurrent=True, nplc=2, numdatapoints=1001, fitindex=10, update_latest=True, datafolder=0)


   .. py:method:: openControlPanel()


