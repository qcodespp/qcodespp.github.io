qcodespp.plotting.offline.popupwindows
======================================

.. py:module:: qcodespp.plotting.offline.popupwindows


Attributes
----------

.. autosummary::

   qcodespp.plotting.offline.popupwindows.qdarkstyle_imported
   qcodespp.plotting.offline.popupwindows.DARK_THEME


Classes
-------

.. autosummary::

   qcodespp.plotting.offline.popupwindows.LineCutWindow
   qcodespp.plotting.offline.popupwindows.StatsWindow
   qcodespp.plotting.offline.popupwindows.MetadataWindow
   qcodespp.plotting.offline.popupwindows.ErrorWindow
   qcodespp.plotting.offline.popupwindows.ErrorLogWindow
   qcodespp.plotting.offline.popupwindows.AutoRefreshPopup


Module Contents
---------------

.. py:data:: qdarkstyle_imported
   :value: True


.. py:data:: DARK_THEME
   :value: True


.. py:class:: LineCutWindow(parent, orientation, init_cmap='viridis', init_canvas=True, editor_window=None)

   Bases: :py:obj:`PyQt5.QtWidgets.QWidget`


   .. py:attribute:: parent


   .. py:attribute:: editor_window
      :value: None



   .. py:attribute:: running
      :value: True



   .. py:attribute:: orientation


   .. py:attribute:: init_cmap
      :value: 'viridis'



   .. py:method:: init_widgets()


   .. py:method:: init_connections()


   .. py:method:: init_canvas()


   .. py:method:: init_layouts()


   .. py:method:: set_main_layout()


   .. py:method:: init_cuts_table()


   .. py:method:: copy_cuts(which='all')


   .. py:method:: paste_cuts()


   .. py:method:: item_clicked(item)


   .. py:method:: get_checked_items(return_indices=False, cuts_or_fits='cuts')


   .. py:method:: append_cut_to_table(linecut_name)


   .. py:method:: points_dragged(line)


   .. py:method:: cuts_table_edited(item)


   .. py:method:: style_changed(option, value)


   .. py:method:: update_draggable_points(linecut, replot=True)


   .. py:method:: move_diagonal_line(direction)


   .. py:method:: index_changed(row)


   .. py:method:: add_cut_manually(data_index=0, offset=0, linecolor=None, update=True)


   .. py:method:: remove_cut(which='selected')


   .. py:method:: generate_cuts()


   .. py:method:: move_cut(direction)


   .. py:method:: reorder_cuts()


   .. py:method:: apply_colormap()


   .. py:method:: colormap_type_edited()


   .. py:method:: change_all_checkstate(column, checkstate)


   .. py:method:: open_cuts_table_menu(position)


   .. py:method:: limits_edited()


   .. py:method:: reset_limits()


   .. py:method:: update_axscale(which)


   .. py:method:: update_legend()


   .. py:method:: update()


   .. py:method:: fit_class_changed()


   .. py:method:: fit_type_changed()


   .. py:method:: collect_fit_data(x, y)


   .. py:method:: collect_fit_inputs(function_class, function_name)


   .. py:method:: collect_init_guess(function_class, function_name)


   .. py:method:: start_fitting(line='manual', multilinefit=False)


   .. py:method:: fit_checked()


   .. py:method:: print_parameters(line)


   .. py:method:: get_line_data(line)


   .. py:method:: draw_lines(x, y, line)


   .. py:method:: draw_plot()


   .. py:method:: draw_fits(line)


   .. py:method:: autoscale_axes()


   .. py:method:: closeEvent(event)


   .. py:method:: save_data()


   .. py:method:: save_fit_result()


   .. py:method:: save_all_fits()


   .. py:method:: clear_fit(line='manual')


   .. py:method:: clear_all_fits()


   .. py:method:: save_parameters_dependency()


   .. py:method:: save_image()


   .. py:method:: copy_image()


   .. py:method:: copy_cuts_table_to_clipboard()


   .. py:method:: mouse_scroll_canvas(event)


   .. py:method:: mouse_click_canvas(event)


   .. py:method:: save_fit_preset()


   .. py:method:: load_fit_preset()


.. py:class:: StatsWindow(parent)

   Bases: :py:obj:`PyQt5.QtWidgets.QWidget`


   .. py:attribute:: parent


   .. py:attribute:: running
      :value: True



   .. py:attribute:: tree_widget


   .. py:attribute:: main_layout


   .. py:method:: calculate_stats()


   .. py:method:: populate_tree(metadata, parent_item=None)

      Recursively populate the QTreeWidget with nested dictionary data.



.. py:class:: MetadataWindow(parent=None)

   Bases: :py:obj:`PyQt5.QtWidgets.QDialog`


   .. py:attribute:: parent
      :value: None



   .. py:attribute:: layout


   .. py:attribute:: tree_widget


   .. py:method:: populate_tree(metadata, parent_item=None)

      Recursively populate the QTreeWidget with nested dictionary data.



.. py:class:: ErrorWindow(text)

   Bases: :py:obj:`PyQt5.QtWidgets.QDialog`


   .. py:attribute:: layout


   .. py:attribute:: text_edit


   .. py:attribute:: button_layout


   .. py:attribute:: copy_button


   .. py:attribute:: close_button


   .. py:method:: copy_text()


.. py:class:: ErrorLogWindow(error_log)

   Bases: :py:obj:`PyQt5.QtWidgets.QDialog`


   .. py:attribute:: error_log


   .. py:attribute:: layout


   .. py:attribute:: tree_widget


   .. py:attribute:: close_button


   .. py:attribute:: save_button


   .. py:method:: populate_tree(error_log)


   .. py:method:: save_log()


.. py:class:: AutoRefreshPopup(editor_window, from_dropdown=False)

   Bases: :py:obj:`PyQt5.QtWidgets.QDialog`


   .. py:attribute:: editor_window


   .. py:attribute:: from_dropdown
      :value: False



   .. py:attribute:: prev_2d


   .. py:attribute:: prev_1d


   .. py:attribute:: lineedit_2d


   .. py:attribute:: lineedit_1d


   .. py:method:: accept()


