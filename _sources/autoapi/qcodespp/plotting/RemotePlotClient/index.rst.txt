qcodespp.plotting.RemotePlotClient
==================================

.. py:module:: qcodespp.plotting.RemotePlotClient

.. autoapi-nested-parse::

   Back-end functions used in live plotting. Not intended to be used directly.



Attributes
----------

.. autoapisummary::

   qcodespp.plotting.RemotePlotClient.qtapp
   qcodespp.plotting.RemotePlotClient.app_icon
   qcodespp.plotting.RemotePlotClient.control_port


Classes
-------

.. autoapisummary::

   qcodespp.plotting.RemotePlotClient.DataSet
   qcodespp.plotting.RemotePlotClient.ZeroMQ_Listener
   qcodespp.plotting.RemotePlotClient.QtPlotWindow


Module Contents
---------------

.. py:data:: qtapp

.. py:data:: app_icon

.. py:class:: DataSet(dataset_id)

   .. py:attribute:: id


   .. py:attribute:: arrays


   .. py:attribute:: metadata


   .. py:method:: add_metadata(metadata)


   .. py:method:: get_array(array_id, shape=100)


   .. py:method:: new_array(array_id, shape)


   .. py:method:: store(array_id, indices, values)


.. py:class:: ZeroMQ_Listener(topic, port)

   Bases: :py:obj:`PyQt5.QtCore.QObject`


   .. py:attribute:: message


   .. py:attribute:: socket


   .. py:attribute:: poller


   .. py:attribute:: running
      :value: True



   .. py:method:: loop()


.. py:class:: QtPlotWindow(topic, port, control_port=None, parent=None, theme=((60, 60, 60), 'w'))

   Bases: :py:obj:`PyQt5.QtWidgets.QWidget`


   .. py:attribute:: control_port
      :value: None



   .. py:attribute:: stores


   .. py:attribute:: plots
      :value: []



   .. py:attribute:: theme
      :value: ((60, 60, 60), 'w')



   .. py:attribute:: title_parts
      :value: []



   .. py:attribute:: plot


   .. py:attribute:: thread


   .. py:attribute:: zeromq_listener


   .. py:attribute:: update_interval
      :value: 1



   .. py:attribute:: update_timer


   .. py:method:: auto_update()


   .. py:method:: control_send(data)


   .. py:method:: get_default_title()


   .. py:method:: set_title(title=None)


   .. py:method:: signal_received(topic, uuid, message)


   .. py:method:: update_labels()


   .. py:method:: save(filename=None, subplot=None)

      Save current plot to filename, by default
      to the location corresponding to the default
      title.

      Args:
          filename (Optional[str]): Location of the file



   .. py:method:: closeEvent(event)


.. py:data:: control_port
   :value: None


