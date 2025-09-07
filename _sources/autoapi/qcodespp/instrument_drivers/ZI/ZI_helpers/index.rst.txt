qcodespp.instrument_drivers.ZI.ZI_helpers
=========================================

.. py:module:: qcodespp.instrument_drivers.ZI.ZI_helpers


Classes
-------

.. autosummary::

   qcodespp.instrument_drivers.ZI.ZI_helpers.ZISampleParam
   qcodespp.instrument_drivers.ZI.ZI_helpers.R4ptParam


Module Contents
---------------

.. py:class:: ZISampleParam(name, sample, unit='V', ai1unit='V', ai2unit='V', components=['x', 'y', 'r', 'phase'], gain=1.0, ai0gain=1.0, ai1gain=1.0)

   Bases: :py:obj:`qcodespp.MultiParameter`


   MultiParameter containing various parts of a ZI lockin sample reading.

   ZI lockins enable making a single reading for X, Y, R, phase, etc. 
   Leverage that to make a single reading and return as many pieces as the user wishes.
   The advantage is that the communication time scales linearly with the number of times 
   the lockin is called; i.e. individually reading X, Y, R, and phase would take four times 
   longer than using this approach.

   Should work for any ZI lockin, using either the zhinst-qcodes or qcodespp drivers.

   Args:
       name (str): The name of the parameter.
       sample (callable): The .sample method of the ZI lock-in amplifier.
       unit (Opt, str): The unit for the demodulator input. Default is 'V'.
       ai1unit (Opt, str): The unit for auxin0 readings (default is 'V').
       ai2unit (Opt, str): The unit for auxin1 readings (default is 'V').
       components (Opt, list of strings): The components to include in the reading. 
           Accepts any of the values returned by the sample (default is 'x', 'y', 'r', 'phase').
       gain (Opt, float): Scaling factor to apply to X, Y, R (default is 1).
       ai0gain (Opt, float): Scaling factor to apply to auxin0 (default is 1).
       ai1gain (Opt, float): Scaling factor to apply to auxin1 (default is 1).

   Usage:
       Current = ZISampleParam('Current', 
                               li_a.demod0_sample, 
                               unit='A', 
                               components=['r', 'phase'],
                               gain=1e-6
                               )
       station.set_measurement(Current)


   .. py:attribute:: gain
      :value: 1.0



   .. py:attribute:: ai0gain
      :value: 1.0



   .. py:attribute:: ai1gain
      :value: 1.0



   .. py:method:: get_raw()

      ``get_raw`` is called to perform the actual data acquisition from the
      instrument. This method should either be overwritten to perform the
      desired operation or alternatively for :class:`.Parameter` a
      suitable method is automatically generated if ``get_cmd`` is supplied
      to the parameter constructor. The method is automatically wrapped to
      provide a ``get`` method on the parameter instance.



.. py:class:: R4ptParam(li_a_sample, li_b_sample, current_gain=1e-06, voltage_gain=0.001, include_R=True, include_phase=True, name='R4pt')

   Bases: :py:obj:`qcodespp.MultiParameter`


   MultiParameter to return current, voltage and resistance based on two ZI lockin readings.

   ZI lockins enable making a single reading for X, Y, R, phase. 
   Leverage that to make a single reading for each of two lockins to return all relevant parameters: 
   Currents X Y R P, Voltages X Y R P, and computed resistances X Y R. 
   Basically requires only two communication instances instead of 14. 
   Phase not returned for resistance since it's not obvious what that means. 
   If currents are exactly zero, resistance returns NaN.

   Should work for any ZI lockin, using either the zhinst-qcodes or qcodespp drivers.

   Args:
       li_a_sample (callable): The .sample method of the current-reading lock-in amplifier.
       li_b_sample (callable): The .sample method of the voltage-reading lock-in amplifier.
       current_gain (float): Gain on the current preamplifier (default is 1e-6).
       voltage_gain (float): Gain on the voltage preamplifier (default is 1e-3).
       include_R (bool): Whether to include amplitude values in the output (default is True).
       include_phase (bool): Whether to include phase values in the output (default is True).
       name (str): The name of the parameter (default is 'R4pt').

   Usage:
       R4pt = R4ptParam(li_a.demod0_sample, li_b.demod0_sample,1e-6,1e-3)
       station.set_measurement(R4pt)


   .. py:method:: get_raw()

      ``get_raw`` is called to perform the actual data acquisition from the
      instrument. This method should either be overwritten to perform the
      desired operation or alternatively for :class:`.Parameter` a
      suitable method is automatically generated if ``get_cmd`` is supplied
      to the parameter constructor. The method is automatically wrapped to
      provide a ``get`` method on the parameter instance.



