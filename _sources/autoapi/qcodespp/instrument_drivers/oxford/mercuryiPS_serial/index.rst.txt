qcodespp.instrument_drivers.oxford.mercuryiPS_serial
====================================================

.. py:module:: qcodespp.instrument_drivers.oxford.mercuryiPS_serial

.. autoapi-nested-parse::

   Driver that supports very old mercuryiPS instruments still communicating via serial.

   Most newer iPS's will use the standard QCoDeS driver



Classes
-------

.. autosummary::

   qcodespp.instrument_drivers.oxford.mercuryiPS_serial.MercuryiPSArray
   qcodespp.instrument_drivers.oxford.mercuryiPS_serial.MercuryiPS_120


Module Contents
---------------

.. py:class:: MercuryiPSArray(name, instrument, names, get_cmd, set_cmd, units=None, **kwargs)

   Bases: :py:obj:`qcodes.MultiParameter`


   This parameter holds the MercuryiPS's 3 dimensional parameters


   .. py:attribute:: units
      :value: None



   .. py:method:: get_raw()

      ``get_raw`` is called to perform the actual data acquisition from the
      instrument. This method should either be overwritten to perform the
      desired operation or alternatively for :class:`.Parameter` a
      suitable method is automatically generated if ``get_cmd`` is supplied
      to the parameter constructor. The method is automatically wrapped to
      provide a ``get`` method on the parameter instance.



   .. py:method:: set_raw(setpoint)

      ``set_raw`` is called to perform the actual setting of a parameter on
      the instrument. This method should either be overwritten to perform the
      desired operation or alternatively for :class:`.Parameter` a
      suitable method is automatically generated if ``set_cmd`` is supplied
      to the parameter constructor. The method is automatically wrapped to
      provide a ``set`` method on the parameter instance.



.. py:class:: MercuryiPS_120(name, address, **kwargs)

   Bases: :py:obj:`qcodespp.instrument_drivers.oxford.serial.SerialInstrument`


   This is the qcodes driver for the Oxford MercuryiPS magnet power supply.

   Args:
       name (str): name of the instrument
       address (str): The IP address or domain name of this instrument
       port (int): the IP port to communicate on (TODO: what port is normal?)

       axes (List[str], Optional): axes to support, as a list of uppercase
           characters, eg ``['X', 'Y', 'Z']``. If omitted, will ask the
           instrument what axes it supports.

   Status: beta-version.

   .. todo::

       - SAFETY!! we need to make sure the magnet is only ramped at certain
         conditions!
       - make ATOB a parameter, and move all possible to use
         _read_cmd, _write_cmd
       - this findall stuff in _get_cmd, is that smart?

   The driver is written as an IPInstrument, but it can likely be converted to
   ``VisaInstrument`` by removing the ``port`` arg and defining methods:

       - ``def _send(self, msg): self.visa_handle.write(msg)``
       - ``def _recv(self): return self.visa_handle.read()``



   .. py:attribute:: axes
      :value: 'xyz'



   .. py:attribute:: axes_map


   .. py:attribute:: amps_per_tesla


   .. py:method:: clear_buffer()


   .. py:method:: ask(cmd)

      Write a command string to the hardware and return a response.

      Subclasses that transform ``cmd`` should override this method, and in
      it call ``super().ask(new_cmd)``. Subclasses that define a new
      hardware communication should instead override ``ask_raw``.

      Args:
          cmd: The string to send to the instrument.

      Returns:
          response

      Raises:
          Exception: Wraps any underlying exception with extra context,
              including the command and the instrument.




   .. py:method:: read()


   .. py:method:: write(cmd)

      Write a command string with NO response to the hardware.

      Subclasses that transform ``cmd`` should override this method, and in
      it call ``super().write(new_cmd)``. Subclasses that define a new
      hardware communication should instead override ``write_raw``.

      Args:
          cmd (str): the string to send to the instrument

      Raises:
          Exception: wraps any underlying exception with extra context,
              including the command and the instrument.



   .. py:method:: hold()


   .. py:method:: rtos()


   .. py:method:: rtoz()


   .. py:method:: get_idn(axes=None)

      Parse a standard VISA ``*IDN?`` response into an ID dict.

      Even though this is the VISA standard, it applies to various other
      types as well, such as IPInstruments, so it is included here in the
      Instrument base class.

      Override this if your instrument does not support ``*IDN?`` or
      returns a nonstandard IDN string. This string is supposed to be a
      comma-separated list of vendor, model, serial, and firmware, but
      semicolon and colon are also common separators so we accept them here
      as well.

      Returns:
          A dict containing vendor, model, serial, and firmware.




