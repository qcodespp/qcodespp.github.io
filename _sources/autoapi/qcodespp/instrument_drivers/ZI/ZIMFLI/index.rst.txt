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



   .. py:attribute:: name

      Full name of the instrument

      This is equivalent to :meth:`full_name` for backwards compatibility.



   .. py:attribute:: serial


   .. py:attribute:: digi
      :value: False



   .. py:attribute:: options


   .. py:attribute:: fwrevision


