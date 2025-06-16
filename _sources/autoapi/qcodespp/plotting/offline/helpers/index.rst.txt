qcodespp.plotting.offline.helpers
=================================

.. py:module:: qcodespp.plotting.offline.helpers


Attributes
----------

.. autosummary::

   qcodespp.plotting.offline.helpers.cmaps
   qcodespp.plotting.offline.helpers.DARK_COLOR
   qcodespp.plotting.offline.helpers.GREY_COLOR
   qcodespp.plotting.offline.helpers.LIGHT_COLOR


Classes
-------

.. autosummary::

   qcodespp.plotting.offline.helpers.MidpointNormalize
   qcodespp.plotting.offline.helpers.NavigationToolbarMod
   qcodespp.plotting.offline.helpers.NoScrollQComboBox
   qcodespp.plotting.offline.helpers.DraggablePoint


Functions
---------

.. autosummary::

   qcodespp.plotting.offline.helpers.rcParams_to_dark_theme
   qcodespp.plotting.offline.helpers.rcParams_to_light_theme


Module Contents
---------------

.. py:data:: cmaps

.. py:class:: MidpointNormalize(vmin=None, vmax=None, midpoint=None, clip=False)

   Bases: :py:obj:`matplotlib.colors.Normalize`


   A class which, when called, maps values within the interval
   ``[vmin, vmax]`` linearly to the interval ``[0.0, 1.0]``. The mapping of
   values outside ``[vmin, vmax]`` depends on *clip*.

   Examples
   --------
   ::

       x = [-2, -1, 0, 1, 2]

       norm = mpl.colors.Normalize(vmin=-1, vmax=1, clip=False)
       norm(x)  # [-0.5, 0., 0.5, 1., 1.5]
       norm = mpl.colors.Normalize(vmin=-1, vmax=1, clip=True)
       norm(x)  # [0., 0., 0.5, 1., 1.]

   See Also
   --------
   :ref:`colormapnorms`


   .. py:attribute:: midpoint
      :value: None



   .. py:method:: __call__(value, clip=None)

      Normalize the data and return the normalized data.

      Parameters
      ----------
      value
          Data to normalize.
      clip : bool, optional
          See the description of the parameter *clip* in `.Normalize`.

          If ``None``, defaults to ``self.clip`` (which defaults to
          ``False``).

      Notes
      -----
      If not already initialized, ``self.vmin`` and ``self.vmax`` are
      initialized using ``self.autoscale_None(value)``.



.. py:class:: NavigationToolbarMod(canvas, parent=None, coordinates=True)

   Bases: :py:obj:`matplotlib.backends.backend_qt5.NavigationToolbar2QT`


   Base class for the navigation cursor, version 2.

   Backends must implement a canvas that handles connections for
   'button_press_event' and 'button_release_event'.  See
   :meth:`FigureCanvasBase.mpl_connect` for more information.

   They must also define

   :meth:`save_figure`
       Save the current figure.

   :meth:`draw_rubberband` (optional)
       Draw the zoom to rect "rubberband" rectangle.

   :meth:`set_message` (optional)
       Display message.

   :meth:`set_history_buttons` (optional)
       You can change the history back / forward buttons to indicate disabled / enabled
       state.

   and override ``__init__`` to set up the toolbar -- without forgetting to
   call the base-class init.  Typically, ``__init__`` needs to set up toolbar
   buttons connected to the `home`, `back`, `forward`, `pan`, `zoom`, and
   `save_figure` methods and using standard icons in the "images" subdirectory
   of the data path.

   That's it, we'll do the rest!


.. py:data:: DARK_COLOR
   :value: '#19232D'


.. py:data:: GREY_COLOR
   :value: '#505F69'


.. py:data:: LIGHT_COLOR
   :value: '#F0F0F0'


.. py:function:: rcParams_to_dark_theme()

.. py:function:: rcParams_to_light_theme()

.. py:class:: NoScrollQComboBox(*args, **kwargs)

   Bases: :py:obj:`PyQt5.QtWidgets.QComboBox`


   .. py:method:: wheelEvent(*args, **kwargs)


.. py:class:: DraggablePoint(parent, x, y, linecut, orientation, draw_line=False, draw_circle=False)

   .. py:attribute:: lock
      :value: None



   .. py:method:: connect()


   .. py:method:: on_press(event)


   .. py:method:: on_motion(event)


   .. py:method:: on_release(event)


   .. py:method:: disconnect()


