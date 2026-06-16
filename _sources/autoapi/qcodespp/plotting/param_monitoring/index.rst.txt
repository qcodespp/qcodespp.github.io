qcodespp.plotting.param_monitoring
==================================

.. py:module:: qcodespp.plotting.param_monitoring


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/qcodespp/plotting/param_monitoring/main/index
   /autoapi/qcodespp/plotting/param_monitoring/monitor_window/index


Classes
-------

.. autosummary::

   qcodespp.plotting.param_monitoring.MonitorWindow


Functions
---------

.. autosummary::

   qcodespp.plotting.param_monitoring.param_monitor


Package Contents
----------------

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


.. py:function:: param_monitor(*params, interval=0.2, maxlen=500, use_thread=True, ylabel=None, yunit=None)

   Entry point for qcodespp parameter monitoring. 
   Args:
       params (list): List of QCoDeS parameters to monitor.
       interval (int): Update interval in seconds.
       maxlen (int): Number of points to keep in the rolling window.
       use_thread (bool): Runs the application in a separate thread or not. Default is False.
           Threading may cause problems on some systems, e.g. macOS.
       ylabel (str): Label for the y-axis. Default is None, which will use 'Param value(s) (arb units)'.
       yunit (str): Unit for the y-axis. Default is None


