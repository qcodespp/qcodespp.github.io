qcodespp.plotting.offline.main
==============================

.. py:module:: qcodespp.plotting.offline.main


Attributes
----------

.. autosummary::

   qcodespp.plotting.offline.main.DARK_THEME
   qcodespp.plotting.offline.main.qdarkstyle_imported


Functions
---------

.. autosummary::

   qcodespp.plotting.offline.main.offline_plotting
   qcodespp.plotting.offline.main.main


Module Contents
---------------

.. py:data:: DARK_THEME
   :value: True


.. py:data:: qdarkstyle_imported
   :value: True


.. py:function:: offline_plotting(folder=None, link_to_default=True, use_thread=True)

   Entry point for qcodespp offline plotting. Call qcodespp.offline_plotting() to start the application.

   Args:
       folder (str): Path (inc relative) to a folder containing the data files to be plotted.
       link_to_default (bool): Link to the qcodespp default folder specified by qc.set_data_folder().
           Ignored if another folder is specified by folder.
       use_thread (bool): Runs the application in a separate thread or not. Default is True.
           Threading may cause problems on some systems, e.g. macOS.


.. py:function:: main(folder=None, link_to_default=True)

   Initializes the offline_plotting Qt application and opens the editor window.


