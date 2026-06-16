qcodespp.plotting.RemoteQtPlotWidgets
=====================================

.. py:module:: qcodespp.plotting.RemoteQtPlotWidgets

.. autoapi-nested-parse::

   Back-end functions used in live plotting. Not intended to be used directly.



Attributes
----------

.. autosummary::

   qcodespp.plotting.RemoteQtPlotWidgets.qtapp
   qcodespp.plotting.RemoteQtPlotWidgets.plot


Classes
-------

.. autosummary::

   qcodespp.plotting.RemoteQtPlotWidgets.PlotTrace
   qcodespp.plotting.RemoteQtPlotWidgets.PlotImage
   qcodespp.plotting.RemoteQtPlotWidgets.PlotDock
   qcodespp.plotting.RemoteQtPlotWidgets.QtPlot


Functions
---------

.. autosummary::

   qcodespp.plotting.RemoteQtPlotWidgets.make_rgba
   qcodespp.plotting.RemoteQtPlotWidgets.one_rgba


Module Contents
---------------

.. py:function:: make_rgba(colorscale)

.. py:function:: one_rgba(c)

   convert a single color value to (r, g, b, a)
   input can be an rgb string 'rgb(r,g,b)', '#rrggbb'
   if we decide we want more we can make more, but for now this is just
   to convert plotly colorscales to pyqtgraph tuples


.. py:data:: qtapp

.. py:class:: PlotTrace(*args, **kwargs)

   Bases: :py:obj:`pyqtgraph.PlotDataItem`


   PlotDataItem with benefits

   delete()
   update()
   - check if data has been updated
   - call set_data() with the updated data





   .. py:method:: setData(*args, **kwargs)

      Clear any data displayed by this item and display new data.

      Parameters
      ----------
      *args : tuple
          See :class:`PlotDataItem` description for supported arguments.
      **kwargs : dict
          See :class:`PlotDataItem` description for supported arguments.

      Raises
      ------
      TypeError
          Raised when an invalid type was passed in for `x` or `y` data.

      See Also
      --------
      :class:`PlotDataItem`
          The arguments accepted by :meth:`setData` are the same used during 
          initialization, and are listed in the opening section.
      :func:`~pyqtgraph.arrayToQPath`
          Explains the constructions of the draw paths.



   .. py:method:: update_data()


.. py:class:: PlotImage(*args, **kwargs)

   Bases: :py:obj:`pyqtgraph.ImageItem`


   ImageItem with benefits

   delete()
   update()
   - check if data has been updated
   - call set_data() with the updated data


   .. py:attribute:: x_data
      :value: None



   .. py:attribute:: y_data
      :value: None



   .. py:attribute:: z_data
      :value: None



   .. py:method:: setImage(*args, **kwargs)

      Update the image displayed by this ImageItem.

      All keywords supported by :meth:`setOpts` are also allowed here.

      Parameters
      ----------
      image : np.ndarray or None, default None
          Image data given as NumPy array with an integer or floating point dtype of
          any bit depth. A 2-dimensional array describes single-valued
          (monochromatic) data. A 3-dimensional array is used to give individual
          color components. The third dimension must be of length 3 (RGB) or 4
          (RGBA). ``np.nan`` values are treated as transparent pixels.
      autoLevels : bool or None, default None
          If ``True``, ImageItem will automatically select levels based on the maximum
          and minimum values encountered in the data. For performance reasons, this
          search sub-samples the images and may miss individual bright or dark points
          in the data set. If ``False``, the search will be omitted. If ``None``, the
          value set by :func:`~pyqtgraph.ImageItem.setOpts` is used, unless a ``levels``
          keyword argument is given, which implies `False`.
      levelSamples : int, default 65536
          Only used when ``autoLevels is None``.  When determining minimum and
          maximum values, ImageItem only inspects a subset of pixels no larger than
          this number. Setting this larger than the total number of pixels considers
          all values. See `quickMinMax`.
      **kwargs : dict, optional
          Extra arguments that are passed to `setOpts`.

      See Also
      --------
      quickMinMax
          See this method for how levelSamples value is utilized.
      :func:`pyqtgraph.functions.makeARGB`
          See this function for how image data is modified prior to rendering.

      Notes
      -----
      For backward compatibility, image data is assumed to be in column-major order
      (column, row) by default. However, most data is stored in row-major order
      (row, column). It can either be transposed before assignment

      .. code-block:: python

          imageitem.setImage(imagedata.T)

      or the interpretation of the data can be changed locally through the
      `axisOrder` keyword or by changing the `imageAxisOrder`
      :ref:`global configuration option <apiref_config>`.



   .. py:method:: update_data()


.. py:class:: PlotDock(*args, **kwargs)

   Bases: :py:obj:`pyqtgraph.dockarea.Dock`


   Dock with benefits

   - contains a list of traces

   - turns on and of Hist item

   setGeometry()
   clear()
   save()
   to_matplolib()


   .. py:attribute:: theme
      :value: ((60, 60, 60), 'w')



   .. py:attribute:: grid
      :value: 20



   .. py:attribute:: dock_widget


   .. py:attribute:: hist_item


   .. py:attribute:: plot_item


   .. py:attribute:: legend


   .. py:method:: set_cmap(cmap=None, traces=None)


   .. py:method:: add_item(*args, pen=False, **kwargs)

      Shortcut to .plot_item.addItem() which also figures out 1D or 2D etc.



   .. py:method:: set_labels(config=None)


   .. py:method:: close()

      Remove this dock from the DockArea it lives inside.



   .. py:method:: clear()


.. py:class:: QtPlot(*args, title=None, figsize=(1000, 600), figposition=None, window_title=None, theme=((60, 60, 60), 'w'), parent=None, cmap='viridis', **kwargs)

   Bases: :py:obj:`PyQt5.QtWidgets.QWidget`


   .. py:attribute:: theme
      :value: ((60, 60, 60), 'w')



   .. py:attribute:: area


   .. py:method:: clear()


   .. py:method:: closeEvent(event)

      Make sure all dock-widgets are deleted upon closing or during garbage-
      collection. Otherwise references keep plots alive forever.



   .. py:method:: add_dock(title=None, position='right', relativeto=None)

      Add a new dock to the current window.

      Args:
          title (str):
              Title of the dock

          position (str):
              'bottom', 'top', 'left', 'right', 'above', or 'below'

          relativeto (DockWidget, int):
              If relativeto is None, then the new Dock is added to fill an
              entire edge of the window. If relativeto is another Dock, then
              the new Dock is placed adjacent to it (or in a tabbed
              configuration for 'above' and 'below').



   .. py:method:: add(*args, subplot=0, **kwargs)


.. py:data:: plot

