qcodespp.instrument_drivers.tektronix.Keithley_2450
===================================================

.. py:module:: qcodespp.instrument_drivers.tektronix.Keithley_2450


Classes
-------

.. autosummary::

   qcodespp.instrument_drivers.tektronix.Keithley_2450.Keithley_2450


Module Contents
---------------

.. py:class:: Keithley_2450(name, address, **kwargs)

   Bases: :py:obj:`qcodes.VisaInstrument`


   qcodes++ driver for the Keithley 2450 voltage source. Behaves similarly to the K2400 series driver.


   .. py:method:: reset()

      Reset the instrument. When the instrument is reset, it performs the
      following actions.

          Returns the SourceMeter to the GPIB default conditions.

          Cancels all pending commands.

          Cancels all previously send `*OPC` and `*OPC?`



