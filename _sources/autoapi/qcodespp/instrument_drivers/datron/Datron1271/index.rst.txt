qcodespp.instrument_drivers.datron.Datron1271
=============================================

.. py:module:: qcodespp.instrument_drivers.datron.Datron1271


Attributes
----------

.. autosummary::

   qcodespp.instrument_drivers.datron.Datron1271.log


Classes
-------

.. autosummary::

   qcodespp.instrument_drivers.datron.Datron1271.Datron1271


Module Contents
---------------

.. py:data:: log

.. py:class:: Datron1271(name, address, terminator='\n', **kwargs)

   Bases: :py:obj:`qcodes.VisaInstrument`


   QCoDeS driver for the Datron 1271 8.5 digit multimeter

   The Datron 1271 is an old instrument with a few quirks: namely that many of the parameters are not readable. 
   Notable cases are the resolution, range, mode and delay. That means that if you don't set them through software, 
   QCoDeS will not know these values. This matters for the driver in that the parameters 'volt', 'curr' and 'resistance', 
   are only available if the mode is set to read them. You may therefore need to tell the software which mode you are 
   using with soft_mode(mode), where mode is one of 'DCI, ACI, ACV, OHMS, TRUE_OHMS, HI_OHMS'

   Not all functions are implemented or tested. Some functions do not work for unknown reasons.

   Args:
       name (str): qcodes name for this instrument instance
       address (str): VISA address


   .. py:attribute:: volt


   .. py:attribute:: read


   .. py:attribute:: trig_read


   .. py:attribute:: read_buffer


   .. py:attribute:: buffer_size


   .. py:attribute:: max


   .. py:attribute:: min


   .. py:attribute:: resolution


   .. py:attribute:: mode


   .. py:attribute:: range


   .. py:attribute:: filter


   .. py:attribute:: coupling


   .. py:attribute:: offset


   .. py:attribute:: multiplier


   .. py:attribute:: divisor


   .. py:attribute:: delay


   .. py:attribute:: ave_rolling


   .. py:attribute:: averaging


   .. py:attribute:: line_freq


   .. py:attribute:: protected_store


   .. py:attribute:: option_config


   .. py:method:: reset()


   .. py:method:: clear()


   .. py:method:: zero()


   .. py:method:: self_test()


   .. py:method:: fast_test()


   .. py:method:: self_cal()


   .. py:method:: soft_mode(str)


