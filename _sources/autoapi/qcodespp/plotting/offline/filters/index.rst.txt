qcodespp.plotting.offline.filters
=================================

.. py:module:: qcodespp.plotting.offline.filters

.. autoapi-nested-parse::

   Created on Thu Nov 9 20:05:23 2017

   @author: Joeri de Bruijckere, Damon Carrad



Classes
-------

.. autosummary::

   qcodespp.plotting.offline.filters.Filter


Functions
---------

.. autosummary::

   qcodespp.plotting.offline.filters.derivative
   qcodespp.plotting.offline.filters.cumulative_sum
   qcodespp.plotting.offline.filters.integrate_rectangle
   qcodespp.plotting.offline.filters.integrate_trapezoid
   qcodespp.plotting.offline.filters.integrate_simpson
   qcodespp.plotting.offline.filters.integrate
   qcodespp.plotting.offline.filters.smooth
   qcodespp.plotting.offline.filters.sav_gol
   qcodespp.plotting.offline.filters.crop_x
   qcodespp.plotting.offline.filters.crop_y
   qcodespp.plotting.offline.filters.roll_x
   qcodespp.plotting.offline.filters.roll_y
   qcodespp.plotting.offline.filters.cut_x
   qcodespp.plotting.offline.filters.cut_y
   qcodespp.plotting.offline.filters.swap_xy
   qcodespp.plotting.offline.filters.flip
   qcodespp.plotting.offline.filters.normalize
   qcodespp.plotting.offline.filters.subtract_average
   qcodespp.plotting.offline.filters.offset_line_by_line
   qcodespp.plotting.offline.filters.subtract_ave_line_by_line
   qcodespp.plotting.offline.filters.offset
   qcodespp.plotting.offline.filters.absolute
   qcodespp.plotting.offline.filters.multiply
   qcodespp.plotting.offline.filters.divide
   qcodespp.plotting.offline.filters.logarithm
   qcodespp.plotting.offline.filters.power
   qcodespp.plotting.offline.filters.root
   qcodespp.plotting.offline.filters.interp2d
   qcodespp.plotting.offline.filters.interpolate
   qcodespp.plotting.offline.filters.sort
   qcodespp.plotting.offline.filters.add_slope
   qcodespp.plotting.offline.filters.subtract_trace
   qcodespp.plotting.offline.filters.invert


Module Contents
---------------

.. py:function:: derivative(data, method, times_x, times_y)

.. py:function:: cumulative_sum(data, method, times_x, times_y)

.. py:function:: integrate_rectangle(x, y)

   Numerically integrate y with respect to x. Should be the same as cumulative sum for regularly spaced x.


.. py:function:: integrate_trapezoid(x, y)

   Numerically integrate y with respect to x using the trapezoidal rule.


.. py:function:: integrate_simpson(x, y)

   Numerically integrate y with respect to x using Simpson's rule.


.. py:function:: integrate(data, method, times_x, times_y)

.. py:function:: smooth(data, method, width_x, width_y)

.. py:function:: sav_gol(data, method, window_length, polyorder)

.. py:function:: crop_x(data, method, left, right)

.. py:function:: crop_y(data, method, bottom, top)

.. py:function:: roll_x(data, method, position, amount)

.. py:function:: roll_y(data, method, position, amount)

.. py:function:: cut_x(data, method, left, width)

.. py:function:: cut_y(data, method, bottom, width)

.. py:function:: swap_xy(data, method=None, setting1=None, setting2=None)

.. py:function:: flip(data, method, setting1, setting2)

.. py:function:: normalize(data, method, point_x, point_y)

.. py:function:: subtract_average(data, method, setting1=None, setting2=None)

.. py:function:: offset_line_by_line(data, method, index, setting2=None)

.. py:function:: subtract_ave_line_by_line(data, method, setting1=None, setting2=None)

.. py:function:: offset(data, method, setting1, setting2, array=None)

.. py:function:: absolute(data, method, setting1, setting2)

.. py:function:: multiply(data, method, setting1, setting2=None, array=None)

.. py:function:: divide(data, method, setting1, setting2=None, array=None)

.. py:function:: logarithm(data, method, setting1=10, setting2=None)

.. py:function:: power(data, method, setting1, setting2=None)

.. py:function:: root(data, method, setting1, setting2=None)

.. py:function:: interp2d(x, y, z, kind='linear')

   Re-do the job that scipy used to do


.. py:function:: interpolate(data, method, n_x, n_y)

.. py:function:: sort(data, method, setting1=None, setting2=None)

.. py:function:: add_slope(data, method, a_x, a_y)

.. py:function:: subtract_trace(data, method, index, setting2=None)

.. py:function:: invert(data, method, setting1=None, setting2=None)

.. py:class:: Filter(name, method=None, settings=None, checkstate=None, dimension=2)

   .. py:attribute:: DEFAULT_SETTINGS


   .. py:attribute:: name


   .. py:attribute:: method_list


   .. py:attribute:: function


   .. py:attribute:: description


