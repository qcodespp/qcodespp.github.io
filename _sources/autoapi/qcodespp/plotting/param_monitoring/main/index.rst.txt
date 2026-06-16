qcodespp.plotting.param_monitoring.main
=======================================

.. py:module:: qcodespp.plotting.param_monitoring.main


Functions
---------

.. autosummary::

   qcodespp.plotting.param_monitoring.main.param_monitor
   qcodespp.plotting.param_monitoring.main.main


Module Contents
---------------

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


.. py:function:: main(*params, interval=0.2, maxlen=500, ylabel=None, yunit=None)

   Initializes the monitor_window Qt application and opens the monitor window.


