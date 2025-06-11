qcodespp.instrument_drivers.tektronix.Keithley_2400
===================================================

.. py:module:: qcodespp.instrument_drivers.tektronix.Keithley_2400


Classes
-------

.. autoapisummary::

   qcodespp.instrument_drivers.tektronix.Keithley_2400.Keithley_2400


Module Contents
---------------

.. py:class:: Keithley_2400(name, address, **kwargs)

   Bases: :py:obj:`qcodes.VisaInstrument`


   QCoDeS driver for the Keithley 2400 voltage source.


   .. py:method:: reset()

      Reset the instrument. When the instrument is reset, it performs the
      following actions.

          Returns the SourceMeter to the GPIB default conditions.

          Cancels all pending commands.

          Cancels all previously send `*OPC` and `*OPC?`



