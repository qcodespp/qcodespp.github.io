qcodespp.instrument_drivers.tektronix.Keithley_2182a
====================================================

.. py:module:: qcodespp.instrument_drivers.tektronix.Keithley_2182a


Classes
-------

.. autoapisummary::

   qcodespp.instrument_drivers.tektronix.Keithley_2182a.Keithley_2182a


Functions
---------

.. autoapisummary::

   qcodespp.instrument_drivers.tektronix.Keithley_2182a.parse_output_string
   qcodespp.instrument_drivers.tektronix.Keithley_2182a.parse_output_bool


Module Contents
---------------

.. py:function:: parse_output_string(s)

   Parses and cleans string outputs of the Keithley 


.. py:function:: parse_output_bool(value)

.. py:class:: Keithley_2182a(name, address, reset=False, **kwargs)

   Bases: :py:obj:`qcodes.VisaInstrument`


   Driver for the Keithley 2182a nanovoltmeter.
   Currently written to support VOLTAGE MEASUREMENTS ONLY
   Temperature may be supported at a later date.


   .. py:method:: trigger()


