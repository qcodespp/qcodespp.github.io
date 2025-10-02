qcodespp.plotting.offline.editor
================================

.. py:module:: qcodespp.plotting.offline.editor

.. autoapi-nested-parse::

   Inspectra-Gadget

   Author: Joeri de Bruijckere

   Adapted for qcodes++ by: Dags Olsteins and Damon Carrad



Attributes
----------

.. autosummary::

   qcodespp.plotting.offline.editor.qdarkstyle_imported
   qcodespp.plotting.offline.editor.DARK_THEME
   qcodespp.plotting.offline.editor.PRESETS
   qcodespp.plotting.offline.editor.DARK_COLOR
   qcodespp.plotting.offline.editor.FONT_SIZES
   qcodespp.plotting.offline.editor.SETTINGS_MENU_OPTIONS
   qcodespp.plotting.offline.editor.AXIS_SCALING_OPTIONS


Classes
-------

.. autosummary::

   qcodespp.plotting.offline.editor.Editor


Module Contents
---------------

.. py:data:: qdarkstyle_imported
   :value: True


.. py:data:: DARK_THEME
   :value: True


.. py:data:: PRESETS

.. py:data:: DARK_COLOR
   :value: '#19232D'


.. py:data:: FONT_SIZES
   :value: ['8', '9', '10', '12', '14', '16', '18', '24']


.. py:data:: SETTINGS_MENU_OPTIONS

.. py:data:: AXIS_SCALING_OPTIONS
   :value: ['linear', 'log', 'symlog', 'logit']


.. py:class:: Editor(folder=None, link_to_default=True)

   Bases: :py:obj:`PyQt5.QtWidgets.QMainWindow`, :py:obj:`qcodespp.plotting.offline.design.Ui_MainWindow`


   .. py:attribute:: window_title_auto_refresh
      :value: ''



   .. py:attribute:: linked_folder
      :value: None



   .. py:attribute:: linked_files
      :value: []



   .. py:attribute:: refresh_2d
      :value: 30



   .. py:attribute:: refresh_1d
      :value: 5



   .. py:attribute:: ask_autorefresh
      :value: True



   .. py:attribute:: live_tracking
      :value: False



   .. py:attribute:: show_linecut_markers
      :value: True



   .. py:attribute:: global_text_size
      :value: '12'



   .. py:attribute:: error_log


   .. py:method:: init_plot_settings()


   .. py:method:: init_view_settings()


   .. py:method:: init_axis_scaling()


   .. py:method:: init_filters()


   .. py:method:: init_connections()


   .. py:method:: init_canvas()


   .. py:method:: set_window_title(extra_info='')


   .. py:method:: load_data_item(filepath)


   .. py:method:: open_files(filepaths=None, attr_dicts=None, overrideautocheck=False)


   .. py:method:: reload_plotted_lines(data, item)


   .. py:method:: reload_linecuts(data, item_checkState)


   .. py:method:: add_internal_data(item, check_item=True, uncheck_others=True)


   .. py:method:: remove_files(which='current')


   .. py:method:: move_file(direction)


   .. py:method:: open_files_from_folder(rootdir=None)


   .. py:method:: check_already_loaded(subdir, filepaths)


   .. py:method:: update_link_to_folder(new_folder=True, folder=None)


   .. py:method:: unlink_folder()


   .. py:method:: refresh_files()


   .. py:method:: save_session(save_as=False)


   .. py:method:: remove_linecutwindows_and_fits(d, exclude_key='linecut_window', exclude_key2='fit_result', exclude_key3='draggable_points')


   .. py:method:: remove_temp_files(dirpath, attempts=5)


   .. py:method:: single_remove_attempt(dirpath)


   .. py:method:: load_session(filepath=None)


   .. py:method:: resolve_missing_files(filenames)


   .. py:method:: export_processed_data(which='all')


   .. py:method:: file_checked(item)


   .. py:method:: file_double_clicked(item)


   .. py:method:: file_clicked()


   .. py:method:: plot_type_changed()


   .. py:method:: bins_changed(which='X')


   .. py:method:: show_2d_data_checkbox_changed()


   .. py:method:: legend_checkbox_changed()


   .. py:method:: show_or_hide_view_settings()


   .. py:method:: show_or_hide_mixeddata_widgets()


   .. py:method:: clear_sidebar1D()


   .. py:method:: initial_data_load(item)


   .. py:method:: update_plots(item=None, update_data=True, update_color_limits=False)


   .. py:method:: update_pick_radii()


   .. py:method:: get_checked_items(return_indices=False)


   .. py:method:: get_unchecked_items(return_indices=False)


   .. py:method:: get_all_items(return_indices=False)


   .. py:method:: set_refresh_intervals(from_dropdown=False)


   .. py:method:: start_stop_tracking()


   .. py:method:: start_auto_refresh(time_interval, wait_for_file=False)


   .. py:method:: wait_for_file_call()


   .. py:method:: auto_refresh_call()


   .. py:method:: stop_auto_refresh()


   .. py:method:: show_current_all()


   .. py:method:: show_data_shape()


   .. py:method:: populate_new_plot_settings()


   .. py:method:: show_current_plot_settings()


   .. py:method:: show_current_view_settings()


   .. py:method:: show_current_axlim_settings()


   .. py:method:: show_current_axscale_settings()


   .. py:method:: show_current_filters()


   .. py:method:: global_text_changed()


   .. py:method:: plot_setting_edited(setting_item=None, setting_name=None)


   .. py:method:: axlim_setting_edited(edited_setting)


   .. py:method:: reset_axlim_settings()


   .. py:method:: axis_scaling_changed()


   .. py:method:: view_setting_edited(edited_setting)


   .. py:method:: fill_colormap_box()


   .. py:method:: colormap_type_edited()


   .. py:method:: colormap_edited()


   .. py:method:: reset_color_limits()


   .. py:method:: copy_plot_settings()


   .. py:method:: copy_filters()


   .. py:method:: copy_view_settings()


   .. py:method:: copy_axlim_settings()


   .. py:method:: paste_plot_settings(which='copied')


   .. py:method:: paste_filters(which='copied')


   .. py:method:: paste_view_settings(which='copied')


   .. py:method:: paste_axlim_settings(which='copied')


   .. py:method:: open_item_menu()


   .. py:method:: do_item_action(signal)


   .. py:method:: duplicate_item(new_plot_button=False)


   .. py:method:: combine_plots()


   .. py:method:: open_plot_settings_menu()


   .. py:method:: replace_plot_setting(signal)


   .. py:method:: which_filters(item, filters=None, filt=None)


   .. py:method:: filters_table_edited(item)


   .. py:method:: open_filter_settings_menu()


   .. py:method:: replace_filter_setting(signal)


   .. py:method:: check_all_filters(signal, manual_signal=None)


   .. py:method:: filters_box_changed()


   .. py:method:: mixeddata_filterbox_changed()


   .. py:method:: reset_filters_combobox(dim=None)


   .. py:method:: append_filter_to_table()


   .. py:method:: remove_filters(which='current')


   .. py:method:: move_filter(to)


   .. py:method:: save_filters()


   .. py:method:: load_filters()


   .. py:method:: filttocol_clicked(axis)


   .. py:method:: init_linecuts(data)


   .. py:method:: make_linecut_window(orientation, data=None, show=True)


   .. py:method:: show_linecut_window(orientation, data)


   .. py:method:: copy_linecuts(orientation, item=None, lines=None)


   .. py:method:: paste_single_linecut_orientation(orientation, data, lines)


   .. py:method:: paste_linecuts(item=None)


   .. py:method:: show_hide_linecuts_changed()


   .. py:method:: reinstate_markers(item, orientation)


   .. py:method:: draggable_point_selected(x, y, data)


   .. py:method:: mouse_click_canvas(event)


   .. py:method:: on_motion(event)


   .. py:method:: on_release(event)


   .. py:method:: on_pick(event)


   .. py:method:: popup_canvas(signal)


   .. py:method:: enter_move_tester(urls)


   .. py:method:: drop_files_tester(urls)


   .. py:method:: drop_folders_tester(urls)


   .. py:method:: dragEnterEvent(event)


   .. py:method:: dragMoveEvent(event)


   .. py:method:: dropEvent(event)


   .. py:method:: show_metadata()


   .. py:method:: show_stats()


   .. py:method:: get_axis_in_focus(event)


   .. py:method:: zoom_plot(event, axis, item)


   .. py:method:: mouse_scroll_canvas(event)


   .. py:method:: keyPressEvent(event)


   .. py:method:: save_preset()


   .. py:method:: load_preset()


   .. py:method:: copy_canvas_to_clipboard()


   .. py:method:: save_image()


   .. py:method:: save_images_as(extension='.png')


   .. py:method:: tight_layout()


   .. py:method:: log_error(error_message, show_popup=False)


   .. py:method:: open_error_log()


   .. py:method:: closeEvent(event)


