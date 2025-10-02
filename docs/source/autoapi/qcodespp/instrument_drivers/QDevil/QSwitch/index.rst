qcodespp.instrument_drivers.QDevil.QSwitch
==========================================

.. py:module:: qcodespp.instrument_drivers.QDevil.QSwitch


Attributes
----------

.. autosummary::

   qcodespp.instrument_drivers.QDevil.QSwitch.State
   qcodespp.instrument_drivers.QDevil.QSwitch.OneOrMore
   qcodespp.instrument_drivers.QDevil.QSwitch.relay_lines
   qcodespp.instrument_drivers.QDevil.QSwitch.relays_per_line


Classes
-------

.. autosummary::

   qcodespp.instrument_drivers.QDevil.QSwitch.QSwitch
   qcodespp.instrument_drivers.QDevil.QSwitch.QSwitches


Functions
---------

.. autosummary::

   qcodespp.instrument_drivers.QDevil.QSwitch.channel_list_to_state
   qcodespp.instrument_drivers.QDevil.QSwitch.state_to_expanded_list
   qcodespp.instrument_drivers.QDevil.QSwitch.state_to_compressed_list
   qcodespp.instrument_drivers.QDevil.QSwitch.expand_channel_list
   qcodespp.instrument_drivers.QDevil.QSwitch.compress_channel_list


Module Contents
---------------

.. py:data:: State

.. py:data:: OneOrMore

.. py:function:: channel_list_to_state(channel_list: str) -> State

.. py:function:: state_to_expanded_list(state: State) -> str

.. py:function:: state_to_compressed_list(state: State) -> str

.. py:function:: expand_channel_list(channel_list: str) -> str

.. py:function:: compress_channel_list(channel_list: str) -> str

.. py:data:: relay_lines
   :value: 24


.. py:data:: relays_per_line
   :value: 10


.. py:class:: QSwitch(name: str, address: str, **kwargs: Unpack[InstrumentBaseKWArgs])

   Bases: :py:obj:`qcodes.instrument.visa.Instrument`


   Base class for all QCodes instruments.

   Args:
       name: an identifier for this instrument, particularly for
           attaching it to a Station.
       metadata: additional static metadata to add to this
           instrument's JSON snapshot.
       label: nicely formatted name of the instrument; if None, the
           ``name`` is used.



   .. py:attribute:: locked_relays
      :value: []



   .. py:method:: reset() -> None


   .. py:method:: soft_reset(force=False) -> None

      Resets the relays to the default state excluding the relays in self.locked_relays
          The check for locked relays prevents accidentally reseting e.g. a gate in the case that
          the kernel is restarted but the locked_relays parameter is not updated.
      Args:
          force (bool): If True, all relays are reset to the default state. Bypasses the check for locked relays.



   .. py:method:: errors() -> str

      Retrieve and clear all previous errors

      Returns:
          str: Comma separated list of errors or '0, "No error"'



   .. py:method:: error() -> str

      Retrieve next error

      Returns:
          str: The next error or '0, "No error"'



   .. py:method:: state_force_update() -> None


   .. py:method:: save_state(name: str, unique=False, overwrite=False) -> None

      Save the current state of the relays

      Args:
          name (str): Name of the saved state
          unique (bool): If True, save the state in a file with the serial number of the qswitch as an identifier



   .. py:method:: load_state(name: str, unique=False) -> None

      Load a saved state of the relays

      Args:
          name (str): Name of the saved state
          unique (bool): If True, load the state from a file with the serial number of the qswitch as an identifier



   .. py:method:: saved_states(unique=False) -> Dict[str, str]

      Get a dictionary of saved states

      Args:
          unique (bool): If True, load the state from a file with the serial number of the qswitch as an identifier

      Returns:
          Dict[str, str]: Dictionary of saved states



   .. py:method:: close_relays(relays: State) -> None

      Close multiple relays at once.

      Args:
          relays: A list of tuples (line, tap) specifying the each relay to close.
              e.g. [(1, 0), (2, 1)]



   .. py:method:: close_relay(line: int, tap: int) -> None

      Close a relay at the specified line and tap.

      Args:
          line: The line number (1 to N*24)
          tap: The tap number (0 for ground, 1-8 for breakouts, 9 for connect)



   .. py:method:: open_relays(relays: State) -> None

      Open multiple relays at once.

      Args:
          relays: A list of tuples (line, tap) specifying the relays to open.
              e.g. [(1, 0), (2, 1)]



   .. py:method:: open_relay(line: int, tap: int) -> None

      Open a relay at the specified line and tap.

      Args:
          line: The line number (1 to N*24)
          tap: The tap number (0 for ground, 1-8 for breakouts, 9 for connect)



   .. py:method:: ground(lines: OneOrMore) -> None

      Connect one or more lines to ground (tap 0).

      Args:
          lines: A line name, number, or list of names/numbers.



   .. py:method:: connect(lines: OneOrMore) -> None

      Connect the specified lines directly through to the output (i.e. connect tap 9)

      Args:
          lines: The line(s) to connect to the output. Specify a single line through its integer value
              or its name, or multiple lines through a list of integers or names.



   .. py:method:: connect_all() -> None

      Connect all lines on all QSwitches through to their outputs, i.e. close tap 9 for all lines.



   .. py:method:: breakout(line: Union[str, int], tap: Union[str, int]) -> None

      Connect the specified line to the specified tap and disconnect ground.

      Args:
          line: The line to connect to the breakout. Specify either its integer value or its name.
          tap: The tap to connect the line to. Specify either its integer value or its name



   .. py:method:: line_float(lines: OneOrMore) -> None

      Open all relays on one or more lines such that the line is floating.

      Args:
          lines: The line(s) to float. Specify a single line through its integer value
              or its name, or multiple lines through a list of integers or names.



   .. py:method:: arrange(breakouts: Optional[Dict[str, int]] = None, lines: Optional[Dict[str, int]] = None) -> None

      An arrangement of names for lines and breakouts

      Args:
          breakouts (Dict[str, int]): Name/breakout pairs
          lines (Dict[str, int]): Name/line pairs



   .. py:method:: start_recording_scpi() -> None

      Record all SCPI commands sent to the instrument

      Any previous recordings are removed.  To inspect the SCPI commands sent
      to the instrument, call get_recorded_scpi_commands().



   .. py:method:: get_recorded_scpi_commands() -> List[str]

      Returns:
          Sequence[str]: SCPI commands sent to the instrument



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



.. py:class:: QSwitches(qsws, linked_BNCs=None, name='qsws', **kwargs)

   Bases: :py:obj:`qcodes.instrument.visa.Instrument`


   Treat multiple QSwitches as a single instrument.

   Lines are numbered 1 to N*24 where N is the number of QSwitches
   BNC taps are numbered 1-8, 11-18, 21-28, etc.
   Special taps 'ground'  and 'connect' remain marked as 0 and 9.

   linked_BNCs supports the case of externally linking the front BNCs such that e.g. a single
   instrument input/output can be connected to any of the N*24 lines. The user can then use the
   lowest value defined by the link. e.g. if linked_BNCs=[[1,11],[2,12]] then
   qsws.close_relay(28,1) is equivalent to
   qsws.close_relay(28,11), and so on.
   It is assumed maximum one link per QSwitch, since otherwise links can be made internally.

   Args:
       qsws (sequence[QSwitches]): list of already initialized/connected qswitches OR
           list of addresses (str) of qswitches to be initialized/connected.
       linked_BNCs (list[list]): list of linked BNCs, e.g. [[1,11],[2,12],[4,31]].
       name (str): QCodes name. Default = 'qsws'

   Usage:
       qsw1 = QSwitch(...)
       qsw2 = QSwitch(...)
       qsws = QSwitches([qsw1, qsw2])


   .. py:attribute:: qsws
      :value: []



   .. py:attribute:: linked_BNCs
      :value: None



   .. py:attribute:: state


   .. py:attribute:: closed_relays


   .. py:attribute:: overview


   .. py:attribute:: auto_save


   .. py:attribute:: locked_relays
      :value: []



   .. py:method:: get_idn()

      Parse a standard VISA ``*IDN?`` response into an ID dict.

      Even though this is the VISA standard, it applies to various other
      types as well, such as IPInstruments, so it is included here in the
      Instrument base class.

      Override this if your instrument does not support ``*IDN?`` or
      returns a nonstandard IDN string. This string is supposed to be a
      comma-separated list of vendor, model, serial, and firmware, but
      semicolon and colon are also common separators so we accept them here
      as well.

      Returns:
          A dict containing vendor, model, serial, and firmware.




   .. py:method:: reset()

      Reset all QSwitches to their default state, i.e. connected to ground through 1MOhm.



   .. py:method:: soft_reset(force=False) -> None

      Soft reset all QSwitches, i.e. connect all lines through 1MOhm to ground unless locked via self.locked_relays.



   .. py:method:: errors() -> str


   .. py:method:: error() -> str


   .. py:method:: state_force_update() -> None


   .. py:method:: abort() -> None


   .. py:method:: save_state(name: str, overwrite=False) -> None


   .. py:method:: load_state(name: str) -> None


   .. py:method:: saved_states() -> Dict[str, str]


   .. py:method:: open_relay(line: int, tap: int) -> None

      Open a relay at the specified line and tap.

      Args:
          line: The line number (1 to N*24)
          tap: The tap number (0 for ground, 1-8 for breakouts, 9 for connect)



   .. py:method:: close_relay(line: int, tap: int) -> None

      Close a relay at the specified line and tap.

      Args:
          line: The line number (1 to N*24)
          tap: The tap number (0 for ground, 1-8 for breakouts, 9 for connect)



   .. py:method:: close_relays(relays: State) -> None

      Close multiple relays at once.

      Args:
          relays: A list of tuples specifying the (line, tap) of each relay to close.
              e.g. [(1, 0), (2, 1)]



   .. py:method:: open_relays(relays: State) -> None

      Open multiple relays at once.

      Args:
          relays: A list of tuples specifying the (line, tap) of each relay to open.
              e.g. [(1, 0), (2, 1)]



   .. py:method:: ground(lines: OneOrMore) -> None

      Connect the specified lines to ground through 1MOhm resistors.

      Args:
          lines: The line(s) to connect to ground. Specify a single line through its integer value
              or its name, or multiple lines through a list of integers or names.



   .. py:method:: connect(lines: OneOrMore) -> None

      Connect the specified lines directly through to the output (i.e. connect tap 9)

      Args:
          lines: The line(s) to connect to the output. Specify a single line through its integer value
              or its name, or multiple lines through a list of integers or names.



   .. py:method:: connect_all() -> None

      Connect all lines on all QSwitches through to their outputs, i.e. close tap 9 for all lines.



   .. py:method:: breakout(line: Union[str, int], tap: Union[str, int]) -> None

      Connect the specified line to the specified tap AND disconnect ground.

      Args:
          line: The line to connect to the breakout. Specify either its integer value or its name.
          tap: The tap to connect the line to. Specify either its integer value or its name



   .. py:method:: line_float(lines: OneOrMore) -> None

      Open _all_ relays on one or more lines such that the line is floating.

      Args:
          lines: The line(s) to float. Specify a single line through its integer value
              or its name, or multiple lines through a list of integers or names.



   .. py:method:: arrange(breakouts: Optional[Dict[str, int]] = None, lines: Optional[Dict[str, int]] = None) -> None

      An arrangement of names for lines and breakouts

      Args:
          breakouts (Dict[str, int]): Name/breakout pairs
          lines (Dict[str, int]): Name/line pairs



