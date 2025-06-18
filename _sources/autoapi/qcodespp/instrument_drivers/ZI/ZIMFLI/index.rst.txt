qcodespp.instrument_drivers.ZI.ZIMFLI
=====================================

.. py:module:: qcodespp.instrument_drivers.ZI.ZIMFLI


Classes
-------

.. autosummary::

   qcodespp.instrument_drivers.ZI.ZIMFLI.ZIMFLI


Module Contents
---------------

.. py:class:: ZIMFLI(name, serial, server='local', digi=False, port=8004, **kwargs)

   Bases: :py:obj:`qcodespp.Instrument`


   This is the driver for the Zurich Instruments MFLI compatible with the older qcodes v0.1.11.
   It has the most important functions for configuring outputs and reading off inputs to qcodes.

   Serial - the device serial number printed on the chassis used for connecting to the device

   TODO: everything



   .. py:attribute:: scoperates


   .. py:attribute:: scopechaninputs


   .. py:method:: print_scope_rates()


   .. py:method:: print_scope_chaninputs()


   .. py:attribute:: LI


   .. py:attribute:: port
      :value: 8004



   .. py:attribute:: serial


   .. py:attribute:: digi
      :value: False



   .. py:attribute:: options


   .. py:attribute:: fwrevision


   .. py:method:: get_idn()

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




