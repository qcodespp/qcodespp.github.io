qcodespp.instrument_drivers.Keysight.Keysight_E5080B
====================================================

.. py:module:: qcodespp.instrument_drivers.Keysight.Keysight_E5080B


Classes
-------

.. autosummary::

   qcodespp.instrument_drivers.Keysight.Keysight_E5080B.Keysight_E5080B


Module Contents
---------------

.. py:class:: Keysight_E5080B(name: str, address: str, **kwargs: Any)

   Bases: :py:obj:`qcodes.VisaInstrument`


   Qcodes driver for the Keysight E5080B Vector Network Analyzer


   .. py:attribute:: start_freq
      :type:  qcodes.parameters.Parameter

      Parameter start_freq



   .. py:attribute:: stop_freq
      :type:  qcodes.parameters.Parameter

      Parameter stop_freq



   .. py:attribute:: center_freq
      :type:  qcodes.parameters.Parameter

      Parameter center_freq



   .. py:attribute:: span
      :type:  qcodes.parameters.Parameter

      Parameter span



   .. py:attribute:: cw
      :type:  qcodes.parameters.Parameter

      Parameter Continuous wave



   .. py:attribute:: points
      :type:  qcodes.parameters.Parameter

      Parameter points



   .. py:attribute:: source_power
      :type:  qcodes.parameters.Parameter

      Parameter source_power



   .. py:attribute:: if_bandwidth
      :type:  qcodes.parameters.Parameter

      Parameter if_bandwidth



   .. py:attribute:: sweep_type
      :type:  qcodes.parameters.Parameter

      Parameter sweep_type



   .. py:attribute:: sweep_mode
      :type:  qcodes.parameters.Parameter

      Parameter sweep_mode



   .. py:attribute:: sweep_group_count
      :type:  qcodes.parameters.Parameter

      Parameter sweep_group_count



   .. py:attribute:: trigger_source
      :type:  qcodes.parameters.Parameter

      Trigger Source



   .. py:attribute:: trigger_type
      :type:  qcodes.parameters.Parameter

      Trigger Type



   .. py:attribute:: trigger_slope
      :type:  qcodes.parameters.Parameter

      Trigger Slope



   .. py:attribute:: accept_trigger_before_armed
      :type:  qcodes.parameters.Parameter

      Accept Trigger Before Armed



   .. py:attribute:: sweep_time
      :type:  qcodes.parameters.Parameter

      Parameter sweep_time



   .. py:attribute:: sweep_time_auto
      :type:  qcodes.parameters.Parameter

      Parameter sweep_time_auto



   .. py:attribute:: scattering_parameter
      :type:  qcodes.parameters.Parameter

      Parameter scattering_parameter



   .. py:attribute:: averages_enabled
      :type:  qcodes.parameters.Parameter

      Parameter averages_enabled



   .. py:attribute:: averages_count
      :type:  qcodes.parameters.Parameter

      Parameter averages count



   .. py:attribute:: averages_mode
      :type:  qcodes.parameters.Parameter

      Parameter averages mode



   .. py:attribute:: format_data
      :type:  qcodes.parameters.Parameter

      Parameter averages mode



   .. py:attribute:: rf_on
      :type:  qcodes.parameters.Parameter

      Parameter RF Power Source



   .. py:attribute:: format_border
      :type:  qcodes.parameters.Parameter

      Parameter Format Border



   .. py:attribute:: operation_status
      :type:  qcodes.parameters.Parameter

      Status Operation



   .. py:method:: get_data(sparam=None)

      Retrieve the complex measurement data



   .. py:method:: get_frequencies()

      return freqpoints



   .. py:method:: get_snp(n=2)

      return all S-parameters for n ports



