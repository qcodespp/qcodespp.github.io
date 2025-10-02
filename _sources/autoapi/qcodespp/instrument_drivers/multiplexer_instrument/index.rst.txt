qcodespp.instrument_drivers.multiplexer_instrument
==================================================

.. py:module:: qcodespp.instrument_drivers.multiplexer_instrument


Classes
-------

.. autosummary::

   qcodespp.instrument_drivers.multiplexer_instrument.MultiplexerChannel
   qcodespp.instrument_drivers.multiplexer_instrument.Multiplexer


Module Contents
---------------

.. py:class:: MultiplexerChannel(parent: Multiplexer, name: str, volt=0, curr=0)

   Bases: :py:obj:`qcodes.InstrumentChannel`


   Used to automatically add gates/channels in a Multiplexer to itself


.. py:class:: Multiplexer(name='MPX', volt_source_list=0, curr_list=0, open_volt=1, close_volt=-1, stepnum=101, **kwargs)

   Bases: :py:obj:`qcodes.Instrument`


   Treat an on-chip analog multiplexer as a qcodes instrument. 

   The driver assumes a multiplexer of the form in https://arxiv.org/abs/2304.12765.
   That is, it consists of a number of levels (lvls) each with two sets of transistors 
   that can be either open/on or closed/off. Level 1 has two transistors, level 2 has four 
   transistors, level 3 had eight and so on. The number of gates is twice the number of levels. 
   Since the voltages to these gates needs to be applied by a 'real' instrument(s), you need to 
   tell this instrument what those parameters are via volt_source_list. volt_source_list should 
   be a list of the full parameter used to connect the multiplexer, 
   e.g. [qdac.ch01.volt,qdac.ch02.volt,qdac.ch03.volt....]
   You can easily generate it by using e.g. [qdac.channel(i+1).volt for i in range(16)]
   If your instrument has current-measuring capability you can also pass these parameters via 
   curr_list in a similar manner to volt_source_list.
   You can provide the open_volt, close_volt and stepnum (the number of steps each gate takes 
   between the close_volt and open_volt) during initialisation, or later by addressing them 
   as any other qcodes parameter.
   IMPORTANT! Note that this is for only ONE multiplexer! If you have e.g. a multiplexer and 
   de-multiplexer on the source and drain side, respectively, you need two of these instruments.


   .. py:attribute:: lvls


   .. py:attribute:: gates


   .. py:method:: mpx_element(element, lvl)


   .. py:method:: print_all_voltages()


   .. py:method:: print_all_currents()


   .. py:method:: set_multiple_gates(voltage, gate_list=0, stepnum=101)


   .. py:method:: GrayCode()


