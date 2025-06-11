qcodespp.instrument_drivers.ZI.ZIHF2LI
======================================

.. py:module:: qcodespp.instrument_drivers.ZI.ZIHF2LI


Classes
-------

.. autoapisummary::

   qcodespp.instrument_drivers.ZI.ZIHF2LI.ZIHF2LI


Module Contents
---------------

.. py:class:: ZIHF2LI(name, serial, **kwargs)

   Bases: :py:obj:`qcodespp.Instrument`


   This is the driver for the Zurich Instruments HF2LI compatible with the older qcodes v0.1.11.
   It has the most important functions for configuring outputs and reading off inputs to qcodes.

   Serial - the device serial number printed on the chassis used for connecting to the device

   TODO add remaining parameters, perhaps change the output amplitudes to Vrms for easier setup.
   Add validators to parameters that don't have them yet.


   .. py:attribute:: LI


   .. py:attribute:: daq


   .. py:attribute:: serial


   .. py:attribute:: hwrevision


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




   .. py:method:: setAmplitude(path, val)

      The lock-in sets amplitude as fraction of output range, the command here converts it such that you can input actual voltage as a normal person.
      It also converts from the rms value that should be given to qcodes into the pk-pk value accepted at the LI



   .. py:method:: getAmplitude(path)


   .. py:method:: getX(path)


   .. py:method:: getY(path)


   .. py:method:: getR(path)


   .. py:method:: getP(path)


