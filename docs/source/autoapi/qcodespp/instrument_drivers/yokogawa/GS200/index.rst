qcodespp.instrument_drivers.yokogawa.GS200
==========================================

.. py:module:: qcodespp.instrument_drivers.yokogawa.GS200


Exceptions
----------

.. autoapisummary::

   qcodespp.instrument_drivers.yokogawa.GS200.GS200Exception


Classes
-------

.. autoapisummary::

   qcodespp.instrument_drivers.yokogawa.GS200.GS200_Monitor
   qcodespp.instrument_drivers.yokogawa.GS200.GS200


Functions
---------

.. autoapisummary::

   qcodespp.instrument_drivers.yokogawa.GS200.float_round


Module Contents
---------------

.. py:function:: float_round(val)

   Rounds a floating number

   Args:
       val: number to be rounded

   Returns:
       Rounded integer


.. py:exception:: GS200Exception

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:class:: GS200_Monitor(parent: GS200, name: str, present: bool)

   Bases: :py:obj:`qcodes.InstrumentChannel`


   Monitor part of the GS200. This is only enabled if it is
   installed in the GS200 (it is an optional extra).

   The units will be automatically updated as required.

   To measure:
   `GS200.measure.measure()`

   Args:
       parent (GS200)
       name (str): instrument name
       present (bool):


   .. py:attribute:: present


   .. py:method:: off()

      Turn measurement off



   .. py:method:: on()

      Turn measurement on



   .. py:method:: state()

      Check measurement state



   .. py:method:: update_measurement_enabled(unit: str, output_range: float)

      Args:
          unit (str)
          output_range (float)



.. py:class:: GS200(name: str, address: str, terminator: str = '\n', **kwargs)

   Bases: :py:obj:`qcodes.VisaInstrument`


   This is the qcodes driver for the Yokogawa GS200 voltage and current source

   Args:
     name (str): What this instrument is called locally.
     address (str): The GPIB address of this instrument
     kwargs (dict): kwargs to be passed to VisaInstrument class
     terminator (str): read terminator for reads/writes to the instrument.


   .. py:attribute:: range


   .. py:attribute:: output_level


   .. py:method:: on()

      Turn output on



   .. py:method:: off()

      Turn output off



   .. py:method:: state()

      Check state



   .. py:method:: ramp_voltage(ramp_to: float, step: float, delay: float) -> None

      Ramp the voltage from the current level to the specified output

      Args:
          ramp_to (float): The ramp target in Volt
          step (float): The ramp steps in Volt
          delay (float): The time between finishing one step and starting another in seconds.



   .. py:method:: ramp_current(ramp_to: float, step: float, delay: float) -> None

      Ramp the current from the current level to the specified output

      Args:
          ramp_to (float): The ramp target in Ampere
          step (float): The ramp steps in Ampere
          delay (float): The time between finishing one step and starting another in seconds.



