qcodespp.instrument_drivers.Keysight.private.Keysight_344xxA
============================================================

.. py:module:: qcodespp.instrument_drivers.Keysight.private.Keysight_344xxA


Attributes
----------

.. autosummary::

   qcodespp.instrument_drivers.Keysight.private.Keysight_344xxA.log


Classes
-------

.. autosummary::

   qcodespp.instrument_drivers.Keysight.private.Keysight_344xxA.ArrayMeasurement


Module Contents
---------------

.. py:data:: log

.. py:class:: ArrayMeasurement(name, shape=(1, ), *args, **kwargs)

   Bases: :py:obj:`qcodes.parameters.ArrayParameter`


   Class to return several values. Really represents a measurement routine.


   .. py:attribute:: label
      :value: ''



   .. py:attribute:: unit
      :value: ''



   .. py:attribute:: properly_prepared
      :value: False



   .. py:method:: prepare()

      Prepare the measurement, create the setpoints.

      There is some randomness in the measurement times.



   .. py:method:: get_raw()

      ``get_raw`` is called to perform the actual data acquisition from the
      instrument. This method should either be overwritten to perform the
      desired operation or alternatively for :class:`.Parameter` a
      suitable method is automatically generated if ``get_cmd`` is supplied
      to the parameter constructor. The method is automatically wrapped to
      provide a ``get`` method on the parameter instance.



