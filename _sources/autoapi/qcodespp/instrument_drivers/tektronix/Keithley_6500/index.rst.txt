qcodespp.instrument_drivers.tektronix.Keithley_6500
===================================================

.. py:module:: qcodespp.instrument_drivers.tektronix.Keithley_6500


Classes
-------

.. autosummary::

   qcodespp.instrument_drivers.tektronix.Keithley_6500.Keithley_Sense
   qcodespp.instrument_drivers.tektronix.Keithley_6500.Keithley_6500


Module Contents
---------------

.. py:class:: Keithley_Sense(parent: qcodes.VisaInstrument, name: str, channel: str)

   Bases: :py:obj:`qcodes.InstrumentChannel`


   This is the class for a measurement channel, i.e. the quantity to be measured (e.g. resistance, voltage).


.. py:class:: Keithley_6500(name: str, address: str, terminator='\n', **kwargs)

   Bases: :py:obj:`qcodes.VisaInstrument`


   This is the qcodes driver for a Keithley DMM6500 digital multimeter.


