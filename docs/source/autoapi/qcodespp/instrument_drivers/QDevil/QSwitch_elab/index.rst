qcodespp.instrument_drivers.QDevil.QSwitch_elab
===============================================

.. py:module:: qcodespp.instrument_drivers.QDevil.QSwitch_elab


Attributes
----------

.. autosummary::

   qcodespp.instrument_drivers.QDevil.QSwitch_elab.State
   qcodespp.instrument_drivers.QDevil.QSwitch_elab.relay_lines
   qcodespp.instrument_drivers.QDevil.QSwitch_elab.relays_per_line


Classes
-------

.. autosummary::

   qcodespp.instrument_drivers.QDevil.QSwitch_elab.QSwitch


Functions
---------

.. autosummary::

   qcodespp.instrument_drivers.QDevil.QSwitch_elab.channel_list_to_state
   qcodespp.instrument_drivers.QDevil.QSwitch_elab.state_to_expanded_list
   qcodespp.instrument_drivers.QDevil.QSwitch_elab.state_to_compressed_list
   qcodespp.instrument_drivers.QDevil.QSwitch_elab.expand_channel_list
   qcodespp.instrument_drivers.QDevil.QSwitch_elab.compress_channel_list


Module Contents
---------------

.. py:data:: State

.. py:function:: channel_list_to_state(channel_list: str) -> State

.. py:function:: state_to_expanded_list(state: State) -> str

.. py:function:: state_to_compressed_list(state: State) -> str

.. py:function:: expand_channel_list(channel_list: str) -> str

.. py:function:: compress_channel_list(channel_list: str) -> str

.. py:data:: relay_lines
   :value: 24


.. py:data:: relays_per_line
   :value: 9


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

      Resets the relays to the default state excluding the relays in self.lokced_relays
          The check for locked relays prevents accidentally reseting e.g. a gate in the case that the kernel is restarted but the locked_relays parameter is not updated.
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


   .. py:method:: save_state(name: str, unique=False) -> None

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


   .. py:method:: close_relay(line: int, tap: int) -> None


   .. py:method:: open_relays(relays: State) -> None


   .. py:method:: open_relay(line: int, tap: int) -> None


   .. py:attribute:: OneOrMore


   .. py:method:: ground(lines: OneOrMore) -> None


   .. py:method:: connect(lines: OneOrMore) -> None


   .. py:method:: breakout(line: str, tap: str) -> None


   .. py:method:: lineFloat(lines: OneOrMore) -> None


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



