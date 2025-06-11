qcodespp.plotting.RemotePlot
============================

.. py:module:: qcodespp.plotting.RemotePlot


Classes
-------

.. autoapisummary::

   qcodespp.plotting.RemotePlot.ControlListener
   qcodespp.plotting.RemotePlot.Plot


Functions
---------

.. autoapisummary::

   qcodespp.plotting.RemotePlot.live_plot


Module Contents
---------------

.. py:function:: live_plot(data_set=None, data_items=None)

   Entry point for live plotting of qcodespp data.

   Args:
       data_set (``DataSetPP``, optional): The ``DataSetPP`` to link to the live plot.
           If not provided, it will try to use the default dataset.
           If no data_set, one can add items to the plot, but the data will not be tracked.
       *data_items (Sequence[``DataArray``, ``Parameter``], optional): List of ``DataArray``
           or ``Parameter`` objects to plot. If not provided, nothing will be plotted initially,
           the user can use ``Plot.add()`` later.

   Returns:
       The ``Plot`` instance.


.. py:class:: ControlListener(client_ready_event=None, port=8876)

   Bases: :py:obj:`threading.Thread`


   ListenToClientTask


   .. py:attribute:: client_ready_event
      :value: None



   .. py:attribute:: context


   .. py:attribute:: socket


   .. py:attribute:: port


   .. py:attribute:: poller


   .. py:attribute:: running
      :value: True



   .. py:method:: run()

      Method representing the thread's activity.

      You may override this method in a subclass. The standard run() method
      invokes the callable object passed to the object's constructor as the
      target argument, if any, with sequential and keyword arguments taken
      from the args and kwargs arguments, respectively.




.. py:class:: Plot(title=None, name=None)

   Main class for remote plotting.

   Most methods of this class should not be called directly; only add(), add_multiple(), clear() and close()
   should be used by the user.

   Args:
       title (str, optional): Title of the plot window.
       name (str, optional): Name of the plot instance. If not provided, a random UUID will be used.


   .. py:attribute:: context


   .. py:attribute:: socket


   .. py:attribute:: port
      :value: 8876



   .. py:attribute:: encoding
      :value: 'utf-8'



   .. py:attribute:: topic
      :value: 'qcodes.plot.00000000000000000000000000000000'



   .. py:attribute:: metadata


   .. py:attribute:: data_uuid
      :value: '00000000000000000000000000000000'



   .. py:attribute:: client_ready_event


   .. py:attribute:: control_task


   .. py:attribute:: control_port


   .. py:method:: publish(data, uuid=None)


   .. py:method:: publish_data(data, uuid, meta, arrays)


   .. py:method:: add_metadata(new_metadata, uuid=None)


   .. py:method:: store(loop_indices, ids_values, uuid)


   .. py:method:: save_metadata(metadata, uuid=None)


   .. py:method:: finalize(uuid=None)


   .. py:method:: new_client(name=None)


   .. py:method:: clear()


   .. py:method:: add_multiple(*z_params)


   .. py:method:: add(*args, x=None, y=None, z=None, subplot=0, name=None, title=None, position=None, relativeto=None, xlabel=None, ylabel=None, zlabel=None, xunit=None, yunit=None, zunit=None, silent=True, linecuts=False, symbol=None, size=None, **kwargs)

      Add a trace to the plot.

      Args:
          *args (DataArray): positional arguments, can be:
              - ``y`` or ``z``: specify just the 1D or 2D data independent parameter, with the setpoint
                  axis or axes implied from the DataSetPP setpoints.
              - ``x, y`` or ``x, y, z``: specify all axes of the data.
          x (DataArray, optional): x-axis data.
          y (DataArray, optional): y-axis data.
          z (DataArray, optional): z-axis data.
          subplot (int, optional): Subplot index to add the trace to. Defaults to 0.
          name (str, optional): Name of the trace. If not provided, the name of the DataArray will be used.
          title (str, optional): Title of the trace. If not provided, the name of the DataArray will be used.
          position (str): Position of the subplot in the plot window. Options are 'bottom', 'top', 'left', 'right', 'above', or 'below'.
          relativeto (str, optional): Position relative to which the subplot should be placed.
          xlabel (str, optional): Label for the x-axis. If not provided, the label of the DataArray will be used.
          ylabel (str, optional): Label for the y-axis. If not provided, the label of the DataArray will be used.
          zlabel (str, optional): Label for the z-axis. If not provided, the label of the DataArray will be used.
          xunit (str, optional): Unit for the x-axis. If not provided, the unit of the DataArray will be used.
          yunit (str, optional): Unit for the y-axis. If not provided, the unit of the DataArray will be used.
          zunit (str, optional): Unit for the z-axis. If not provided, the unit of the DataArray will be used.
          silent (bool, optional): If True, do not wait for the client to be ready. Defaults to True.
          linecuts (bool, optional): If True, plot line cuts instead of a 2D image. Defaults to False.
          symbol (str, optional): Symbol to use for the trace. Defaults to None.
          size (int, optional): Size of the symbol. Defaults to None.



   .. py:method:: expand_trace(args, kwargs)

      Complete the x, y (and possibly z) data definition for a trace.

      Also modifies kwargs in place so that all the data needed to fully specify the
      trace is present (ie either x and y or x and y and z)

      Both ``__init__`` (for the first trace) and the ``add`` method support multiple
      ways to specify the data in the trace:

      As args:
          - ``add(y)`` or ``add(z)`` specify just the main 1D or 2D data, with the setpoint
            axis or axes implied.
          - ``add(x, y)`` or ``add(x, y, z)`` specify all axes of the data.
      And as kwargs:
          - ``add(x=x, y=y, z=z)`` you specify exactly the data you want on each axis.
            Any but the last (y or z) can be omitted, which allows for all of the same
            forms as with args, plus x and z or y and z, with just one axis implied from
            the setpoints of the z data.

      This method takes any of those forms and converts them into a complete set of
      kwargs, containing all of the explicit or implied data to be used in plotting this trace.

      Args:
          args (Tuple[DataArray]): positional args, as passed to either ``__init__`` or ``add``
          kwargs (Dict(DataArray]): keyword args, as passed to either ``__init__`` or ``add``.
              kwargs may contain non-data items in keys other than x, y, and z.

      Raises:
         ValueError: if the shape of the data does not match that of args
         ValueError: if the data is provided twice



   .. py:method:: set_title(title)


   .. py:method:: set_cmap(cmap)


   .. py:method:: save(filename=None, subplot=None)


   .. py:method:: set_xlabel(label, subplot=0)


   .. py:method:: set_ylabel(label, subplot=0)


   .. py:method:: set_geometry(height, width, x0, y0)


   .. py:method:: close()


