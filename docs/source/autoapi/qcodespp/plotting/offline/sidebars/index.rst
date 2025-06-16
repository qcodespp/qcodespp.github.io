qcodespp.plotting.offline.sidebars
==================================

.. py:module:: qcodespp.plotting.offline.sidebars


Classes
-------

.. autosummary::

   qcodespp.plotting.offline.sidebars.Sidebar1D


Module Contents
---------------

.. py:class:: Sidebar1D(parent, editor_window=None)

   Bases: :py:obj:`PyQt5.QtWidgets.QWidget`


   .. py:attribute:: init_cmap
      :value: 'viridis'



   .. py:attribute:: parent


   .. py:attribute:: running
      :value: True



   .. py:method:: init_widgets()


   .. py:method:: init_connections()


   .. py:method:: init_layouts()


   .. py:method:: set_main_layout()


   .. py:method:: init_trace_table()


   .. py:method:: plot_type_changed()


   .. py:method:: item_clicked(item)


   .. py:method:: get_checked_items(return_indices=False, traces_or_fits='traces')


   .. py:method:: duplicate_trace()


   .. py:method:: add_trace_manually()


   .. py:method:: append_trace_to_table(index)


   .. py:method:: trace_table_edited(item)


   .. py:method:: remove_trace(which='selected')


   .. py:method:: move_trace(direction)


   .. py:method:: apply_colormap()


   .. py:method:: colormap_type_edited()


   .. py:method:: open_trace_table_menu(position)


   .. py:method:: change_all_checkstate(column, checkstate)


   .. py:method:: replace_table_entry(signal)


   .. py:method:: limits_edited()


   .. py:method:: reset_limits()


   .. py:method:: update(clearplot=True)


   .. py:method:: fit_class_changed()


   .. py:method:: fit_type_changed()


   .. py:method:: collect_fit_data(x, y)


   .. py:method:: collect_fit_inputs(function_class, function_name)


   .. py:method:: collect_init_guess(function_class, function_name)


   .. py:method:: start_fitting(line='manual', multilinefit=False)


   .. py:method:: fit_checked()


   .. py:method:: print_parameters(line)


   .. py:method:: get_line_data(line)


   .. py:method:: plot_Yerr(x, y, error, line)


   .. py:method:: plot_Xerr(x, y, error, line)


   .. py:method:: process_uncertainties(line, x, y)


   .. py:method:: draw_plot(clearplot=True)


   .. py:method:: draw_fits(line)


   .. py:method:: save_fit_result()


   .. py:method:: save_all_fits()


   .. py:method:: clear_fit(line='manual')


   .. py:method:: clear_all_fits()


   .. py:method:: save_fit_preset()


   .. py:method:: load_fit_preset()


   .. py:method:: closeEvent(event)


