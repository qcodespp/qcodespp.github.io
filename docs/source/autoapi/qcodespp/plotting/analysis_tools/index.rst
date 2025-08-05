qcodespp.plotting.analysis_tools
================================

.. py:module:: qcodespp.plotting.analysis_tools

.. autoapi-nested-parse::

   Useful functions for plotting in Jupyter notebooks using matplotlib.



Functions
---------

.. autosummary::

   qcodespp.plotting.analysis_tools.colorplot
   qcodespp.plotting.analysis_tools.colored_traces
   qcodespp.plotting.analysis_tools.sort_lists
   qcodespp.plotting.analysis_tools.load_2d_json


Module Contents
---------------

.. py:function:: colorplot(x, y, z, figsize=0, cmap=0, labels=0, xlim=0, ylim=0, zlim=0, xmajor=0, xminor=0, ymajor=0, yminor=0, font_size=0, label_size=0, check_shapes=False)

   Make a nice colourplot from a three-dimensional data array using matplotlib. 

   Args:
       
       x: 1D or 2D array of x-coordinates
       
       y: 1D or 2D array of y-coordinates
       
       z: 2D array of z-values corresponding to the x and y coordinates.
       
       figsize (tuple, optional): Size of the figure in inches. Default is (8, 8).
       
       cmap (str, optional): Colormap to use for the plot. Default is 'hot'.
       
       labels (list, optional): Labels for the x, y, and z axes. Default is ['x', 'y', 'z'].
       
       xlim (tuple, optional): Limits for the x-axis. Default is None.
       
       ylim (tuple, optional): Limits for the y-axis. Default is None.
       
       zlim (tuple, optional): Limits for the z-axis (color scale). Default is None.
       
       xmajor (float, optional): Major tick interval for the x-axis. Default is None.
       
       xminor (float, optional): Minor tick interval for the x-axis. Default is None.
       
       ymajor (float, optional): Major tick interval for the y-axis. Default is None.
       
       yminor (float, optional): Minor tick interval for the y-axis. Default is None.
       
       font_size (int, optional): Font size for the axis labels. Default is 12.
       
       label_size (int, optional): Font size for the tick labels. Default is 12.

       check_shapes (bool, optional): If True, checks the shapes of x, y, and z arrays and transposes if necessary. Default is False.

   Returns:
       tuple: A tuple containing the figure, axis, and colorbar axis objects.



.. py:function:: colored_traces(x, y, offset=0, figsize=0, cmap=0, labels=0, xlim=0, ylim=0, xmajor=0, xminor=0, ymajor=0, yminor=0, font_size=0, label_size=0)

   Plot a series of 1D traces where the lines are colored according to a matplotlib colormap.

   Args:
       
       x: 1D or 2D array of x-coordinates
       
       y: 2D array of y-coordinates
       
       figsize (tuple, optional): Size of the figure in inches. Default is (8, 8).
       
       cmap (str, optional): Colormap to use for the plot. Default is 'hot'.
       
       labels (list, optional): Labels for the x, y, and z axes. Default is ['x', 'y', 'z'].
       
       xlim (tuple, optional): Limits for the x-axis. Default is None.
       
       ylim (tuple, optional): Limits for the y-axis. Default is None.
       
       xmajor (float, optional): Major tick interval for the x-axis. Default is None.
       
       xminor (float, optional): Minor tick interval for the x-axis. Default is None.
       
       font_size (int, optional): Font size for the axis labels. Default is 12.
       
       label_size (int, optional): Font size for the tick labels. Default is 12.


   Returns:
       tuple: A tuple containing the figure and axis objects.



.. py:function:: sort_lists(X, Y)

   Sort two lists according to the ascending order of the first list.

   Args:
       X: List whose elements will be sorted in ascending order
       Y: List whose elements will be sorted according to the new order of X

   Returns
       (X,Y): The sorted lists


.. py:function:: load_2d_json(filename)

   Load reshaped 2D data exported from offline_plotting as a JSON file.

   Args:
       filename (str): Path to the JSON file.

   Returns:
       dict: A dictionary containing the reshaped data.


