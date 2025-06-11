qcodespp.instrument_drivers.multiplexer_instrument
==================================================

.. py:module:: qcodespp.instrument_drivers.multiplexer_instrument


Classes
-------

.. autoapisummary::

   qcodespp.instrument_drivers.multiplexer_instrument.MultiplexerChannel
   qcodespp.instrument_drivers.multiplexer_instrument.Multiplexer


Module Contents
---------------

.. py:class:: MultiplexerChannel(parent: Multiplexer, name: str, volt=0, curr=0)

   Bases: :py:obj:`qcodes.instrument.channel.InstrumentChannel`


   Used to automatically add gates/channels in a Multiplexer to itself


.. py:class:: Multiplexer(name='MPX', volt_source_list=0, curr_list=0, open_volt=1, close_volt=-1, stepnum=101, **kwargs)

   Bases: :py:obj:`qcodes.instrument.base.Instrument`


   Base class for all QCodes instruments.

   Args:
       name: an identifier for this instrument, particularly for
           attaching it to a Station.
       metadata: additional static metadata to add to this
           instrument's JSON snapshot.
       label: nicely formatted name of the instrument; if None, the
           ``name`` is used.



   .. py:attribute:: lvls


   .. py:attribute:: gates


   .. py:method:: mpx_element(element, lvl)


   .. py:method:: print_all_voltages()


   .. py:method:: print_all_currents()


   .. py:method:: set_multiple_gates(voltage, gate_list=0, stepnum=101)


   .. py:method:: GrayCode()


