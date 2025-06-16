qcodespp.instrument_drivers.tektronix.Keithley_2700
===================================================

.. py:module:: qcodespp.instrument_drivers.tektronix.Keithley_2700


Exceptions
----------

.. autosummary::

   qcodespp.instrument_drivers.tektronix.Keithley_2700.K2700Exception


Classes
-------

.. autosummary::

   qcodespp.instrument_drivers.tektronix.Keithley_2700.Keithley_2700


Functions
---------

.. autosummary::

   qcodespp.instrument_drivers.tektronix.Keithley_2700.bool_to_str
   qcodespp.instrument_drivers.tektronix.Keithley_2700.parseint
   qcodespp.instrument_drivers.tektronix.Keithley_2700.parsebool
   qcodespp.instrument_drivers.tektronix.Keithley_2700.parsestr


Module Contents
---------------

.. py:exception:: K2700Exception

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:function:: bool_to_str(val)

   Function to convert boolean to 'ON' or 'OFF'


.. py:function:: parseint(v)

.. py:function:: parsebool(v)

.. py:function:: parsestr(v)

.. py:class:: Keithley_2700(name, address, reset=False, use_defaults=False, **kwargs)

   Bases: :py:obj:`qcodes.VisaInstrument`


   This is the qcodes driver for the Keithley_2700 Multimeter

   Usage: Initialize with::

       <name> =  = Keithley_2700(<name>, address='<GPIB address>', reset=<bool>,
           change_display=<bool>, change_autozero=<bool>)

   This driver does not yet contain all commands available, but supports reading
   voltage, current, resistance, temperature and frequency. Each of these parameters
   is only available when mode() is set to the corresponding value.



   .. py:method:: get_all()

      Reads all relevant parameters from instrument

      Input:
          None

      Output:
          None



   .. py:method:: set_defaults()

      Set to driver defaults:
      Output=data only
      Mode=Volt:DC
      Digits=7
      Trigger=Continous
      Range=10 V
      NPLC=1
      Averaging=off



   .. py:method:: reset()

      Resets instrument to default values

      Input:
          None

      Output:
          None



