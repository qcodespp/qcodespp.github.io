qcodespp.instrument_drivers.cryogenic.CryogenicSMS120C
======================================================

.. py:module:: qcodespp.instrument_drivers.cryogenic.CryogenicSMS120C

.. autoapi-nested-parse::

   # Please refer to Cryogenic's Magnet Power Supply SMS120C manual for further details and functionality.
   # This magnet PS model is not SCPI compliant.
   # Note: Some commands return more than one line in the output,
           some are unidirectional, with no return (eg. 'write' rathern than 'ask').

   This magnet PS driver has been tested with:
       FTDI chip drivers (USB to serial), D2XX version installed.



Attributes
----------

.. autosummary::

   qcodespp.instrument_drivers.cryogenic.CryogenicSMS120C.log


Classes
-------

.. autosummary::

   qcodespp.instrument_drivers.cryogenic.CryogenicSMS120C.CryogenicSMS120C


Module Contents
---------------

.. py:data:: log

.. py:class:: CryogenicSMS120C(name, address, coil_constant=0.113375, current_rating=105.84, current_ramp_limit=0.0506, reset=False, querytime=0.5, timeout=5, log_timeouts=False, terminator='\r\n', **kwargs)

   Bases: :py:obj:`qcodes.VisaInstrument`


   The following hard-coded, default values for Cryogenic magnets are safety limits
   and should not be modified.
   - these values should be set using the corresponding arguments when the class is called.


   .. py:attribute:: default_current_ramp_limit
      :value: 0.0506



   .. py:attribute:: default_max_current_ramp_limit
      :value: 0.12


      Driver for the Cryogenic SMS120C magnet power supply.
      This class controls a single magnet PSU.
      Magnet and magnet PSU limits : max B=12T, I=105.84A, V=3.5V

      Args:
          name (string): a name for the instrument
          address (string): (serial to USB) COM number of the power supply
          coil_constant (float): coil constant in Tesla per ampere, fixed at 0.113375T/A
          current_rating (float): maximum current rating in ampere, fixed at 105.84A
          current_ramp_limit (float): current ramp limit in ampere per second,
              for 50mK operation 0.0506A/s (5.737E-3 T/s, 0.34422T/min) - usually used
              for 4K operation 0.12A/s (0.013605 T/s, 0.8163 T/min) - not recommended

      Note about timing : SMS120C needs a minimum of 200ms delay between commands being sent.
      The controller will send bad commands if asked too often. This driver tries to circumvent that.
      If the controller sends a bad command, the code will wait for the 'timeout' time (default 5s)
      before asking for the parameter again, and will keep asking until the controller sends something sensible.
      The problem mainly occurs when getting parameters.
      However, the problem is most prevalent when _setting_ the field, since the code has to continually/regularly
      ask the controller whether the field has been reached. To get around this, you can set an appropriate 
      querytime>0.2s (default 0.5s). However this limits the sweeprate to at least this value.
      Alternatively, you can use one of the other rampModes (see description in parameter)



   .. py:method:: get_idn()

      Overwrites the get_idn function using constants as the hardware
      does not have a proper \*IDN function.



   .. py:method:: query(msg)

      Message outputs do not follow the standard SCPI format,
      separate regexp to parse unique/variable instrument message structures.

      Returns:
          key : unused
          value : parsed value extracted from output message



