qcodespp.instrument_drivers.Hioki.Hioki_DM7275
==============================================

.. py:module:: qcodespp.instrument_drivers.Hioki.Hioki_DM7275


Classes
-------

.. autosummary::

   qcodespp.instrument_drivers.Hioki.Hioki_DM7275.HiokiDM7275


Module Contents
---------------

.. py:class:: HiokiDM7275(name, address, **kwargs)

   Bases: :py:obj:`qcodes.VisaInstrument`


   QCoDeS driver for the Hioki DC7275 Precision DC voltmeter

   Args:
       name (str): qcodes name for this instrument instance
       address (str): VISA address


   .. py:attribute:: volt


   .. py:attribute:: volt_triggered


   .. py:attribute:: read_buffer


   .. py:attribute:: num_buffer_readings


   .. py:attribute:: nplc


   .. py:attribute:: integrationtime


   .. py:attribute:: autorange


   .. py:attribute:: range


   .. py:attribute:: digits


   .. py:attribute:: offset


   .. py:attribute:: offset_enabled


   .. py:attribute:: trigger_source


   .. py:attribute:: trigger_continuous


   .. py:attribute:: trigger_count


   .. py:attribute:: trigger_delay


   .. py:attribute:: trigger_autodelay


   .. py:method:: auto_offset(meas_num=10)

      Measure the input voltage and apply this value as the offset (null)

      Args:
          meas_num: Number of measurements to average over to obtain the offset value.



   .. py:method:: trigger_now(trigger_count=None, wait=True, return_buffer=False)

      Manually trigger measurement(s). 

      Clears the buffer and stores the number of measurements specified by trigger_count, spaced by integrationtime.

      Args:
          trigger_count (int): Number of measurements to perform. If None, self.trigger_count used
          wait (bool): Whether to sleep until all measurements stored in buffer
          return_buffer (bool): Whether to return the buffer values after measurement.
                              Default False since reading the buffer clears it.



   .. py:method:: clear_buffer()


   .. py:method:: reset()

      Resets instrument



