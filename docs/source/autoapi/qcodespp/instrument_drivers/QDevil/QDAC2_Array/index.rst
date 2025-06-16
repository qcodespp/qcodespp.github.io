qcodespp.instrument_drivers.QDevil.QDAC2_Array
==============================================

.. py:module:: qcodespp.instrument_drivers.QDevil.QDAC2_Array


Classes
-------

.. autosummary::

   qcodespp.instrument_drivers.QDevil.QDAC2_Array.Array_Arrangement_Context
   qcodespp.instrument_drivers.QDevil.QDAC2_Array.QDac2_Array


Module Contents
---------------

.. py:class:: Array_Arrangement_Context(qdacs: QDac2_Array, contacts: Dict[str, Dict[str, int]], output_triggers: Optional[Dict[str, Dict[str, int]]] = None, internal_triggers: Optional[Sequence[str]] = None)

   .. py:method:: __enter__()


   .. py:method:: __exit__(exc_type, exc_val, exc_tb)


   .. py:property:: contact_names
      :type: Sequence[str]


      Returns:
         Sequence[str]: Channel names



   .. py:method:: channel(contact: str) -> qcodespp.instrument_drivers.QDevil.QDAC2.QDac2Channel

      Args:
          contact (str): Name

      Returns:
         QDac2Channel: Instrument channel



   .. py:method:: qdac_names() -> Sequence[str]


   .. py:method:: virtual_voltage(contact: str) -> float

      Args:
          contact (str): Name of contact

      Returns:
          float: Voltage before correction



   .. py:method:: set_virtual_voltages(contacts_to_voltages: Dict[str, float]) -> None


   .. py:method:: currents_A(nplc: int = 1, current_range: str = 'low') -> Sequence[float]

      Measure currents on all contacts

      The order is that of contacts()

      Args:
          nplc (int, optional): Number of powerline cycles to average over
          current_range (str, optional): Current range (default low)



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



.. py:class:: QDac2_Array(controller: qcodespp.instrument_drivers.QDevil.QDAC2.QDac2, listeners: Sequence[qcodespp.instrument_drivers.QDevil.QDAC2.QDac2])

   A collection of interconnected QDAC-IIs

   The instruments are required to be connected as described in section 5.5
   'Synchronization of multiple QDAC-II units' in the manual.  The sync
   cables must be left in place after sync, so that the clock is
   continuously distributed, and the Controller can trigger all Listerners
   by sending pulses from Ext Out 4 to all Ext In 3 simultaneously.


   .. py:property:: trigger_out
      :type: int



   .. py:property:: common_trigger_in
      :type: qcodespp.instrument_drivers.QDevil.QDAC2.ExternalInput



   .. py:property:: controller
      :type: str


      Returns:
         str: Name of Controller



   .. py:property:: names
      :type: FrozenSet[str]


      Returns:
         FrozenSet[str]: Names of all QDAC-IIs in the array



   .. py:method:: allocate_trigger() -> qcodespp.instrument_drivers.QDevil.QDAC2.QDac2Trigger_Context

      Allocate internal trigger on the Controller

      Returns:
          QDac2Trigger_Context: context manager



   .. py:method:: connect_external_trigger(port: int, trigger: qcodespp.instrument_drivers.QDevil.QDAC2.QDac2Trigger_Context, width_s: float = 1e-06) -> None

      Route internal trigger to external trigger

      Args:
          port (int): External output trigger number
          trigger (QDac2Trigger_Context): Internal trigger
          width_s (float, optional): Output trigger width in seconds (default 1ms)



   .. py:method:: trigger(internal_trigger: qcodespp.instrument_drivers.QDevil.QDAC2.QDac2Trigger_Context)

      Fire an internal trigger on the Controller

      Args:
          QDac2Trigger_Context: internal trigger



   .. py:method:: sync() -> None

      Synchronizes the array of QDAC-IIs

      The Listeners will stop using their own clock and start using the
      Controller's clock.



   .. py:method:: arrange(contacts: Dict[str, Dict[str, int]], output_triggers: Optional[Dict[str, Dict[str, int]]] = None, internal_triggers: Optional[Sequence[str]] = None) -> Array_Arrangement_Context

      An arrangement of contacts across several QDAC-II instruments

      The arrangement is a collection of QDac2.arrangement, one for each
      instrument but with a dedicated controller.

      See QDac2.arrangement() for further documentation.  Note that an
      array arrangement does not (yet) support corrections between contacts
      (which the indiviual arrangements on each instrument does).

      Args:
          contacts (Dict[str,Dict[str, int]]): Instrument name to contact-name/channel pairs
          output_triggers (Dict[str,Dict[str, int]], optional): Instrument name to name/output-trigger pairs
          internal_triggers (Sequence[str], optional): List of names of internal triggers to allocate on the controller

      Returns:
          Array_Arrangement_Context: context manager



