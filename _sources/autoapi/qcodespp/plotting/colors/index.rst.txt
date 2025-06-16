qcodespp.plotting.colors
========================

.. py:module:: qcodespp.plotting.colors


Attributes
----------

.. autosummary::

   qcodespp.plotting.colors.color_cycle
   qcodespp.plotting.colors.colorscales_raw
   qcodespp.plotting.colors.colorscales


Functions
---------

.. autosummary::

   qcodespp.plotting.colors.make_rgba
   qcodespp.plotting.colors.one_rgba


Module Contents
---------------

.. py:data:: color_cycle
   :value: ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',...


.. py:data:: colorscales_raw

.. py:function:: make_rgba(colorscale)

.. py:function:: one_rgba(c)

   convert a single color value to (r, g, b, a)
   input can be an rgb string 'rgb(r,g,b)', '#rrggbb'
   if we decide we want more we can make more, but for now this is just
   to convert plotly colorscales to pyqtgraph tuples


.. py:data:: colorscales

