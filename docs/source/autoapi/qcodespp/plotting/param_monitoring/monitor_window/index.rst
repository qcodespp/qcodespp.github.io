qcodespp.plotting.param_monitoring.monitor_window
=================================================

.. py:module:: qcodespp.plotting.param_monitoring.monitor_window


Classes
-------

.. autosummary::

   qcodespp.plotting.param_monitoring.monitor_window.MonitorWindow
   qcodespp.plotting.param_monitoring.monitor_window.ParamCache
   qcodespp.plotting.param_monitoring.monitor_window.TimeCache


Module Contents
---------------

.. py:class:: MonitorWindow(*params, interval=0.2, maxlen=500, start=True, ylabel=None, yunit=None, station=None)

   Bases: :py:obj:`PyQt5.QtWidgets.QMainWindow`


   .. py:attribute:: params
      :value: []



   .. py:attribute:: t0


   .. py:attribute:: t0_cache
      :value: 0



   .. py:attribute:: maxlen
      :value: 500



   .. py:attribute:: ylabel
      :value: None



   .. py:attribute:: yunit
      :value: None



   .. py:attribute:: times
      :value: []



   .. py:attribute:: param_dict


   .. py:attribute:: data


   .. py:attribute:: station
      :value: None



   .. py:attribute:: timer


   .. py:method:: closeEvent(event)


.. py:class:: ParamCache(name, window, **kwargs)

   Bases: :py:obj:`qcodespp.MultiParameter`


   MultiParameter to transfer the last mesaured data into a qcpp Measure


   .. py:attribute:: window


   .. py:attribute:: names


   .. py:attribute:: labels


   .. py:attribute:: units


   .. py:attribute:: shapes


   .. py:attribute:: unit
      :value: ''



   .. py:method:: get_raw()

      ``get_raw`` is called to perform the actual data acquisition from the
      instrument. This method should either be overwritten to perform the
      desired operation or alternatively for :class:`.Parameter` a
      suitable method is automatically generated if ``get_cmd`` is supplied
      to the parameter constructor. The method is automatically wrapped to
      provide a ``get`` method on the parameter instance.



.. py:class:: TimeCache(name, window, **kwargs)

   Bases: :py:obj:`qcodespp.Parameter`


   Parameter to transfer the last measured times into a qcpp Measure


   .. py:attribute:: window


   .. py:method:: get_raw()

      ``get_raw`` is called to perform the actual data acquisition from the
      instrument. This method should either be overwritten to perform the
      desired operation or alternatively for :class:`.Parameter` a
      suitable method is automatically generated if ``get_cmd`` is supplied
      to the parameter constructor. The method is automatically wrapped to
      provide a ``get`` method on the parameter instance.



