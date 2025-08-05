qcodespp.plotting.offline.datatypes
===================================

.. py:module:: qcodespp.plotting.offline.datatypes


Classes
-------

.. autosummary::

   qcodespp.plotting.offline.datatypes.DataItem
   qcodespp.plotting.offline.datatypes.BaseClassData
   qcodespp.plotting.offline.datatypes.NumpyData
   qcodespp.plotting.offline.datatypes.InternalData
   qcodespp.plotting.offline.datatypes.MixedInternalData


Module Contents
---------------

.. py:class:: DataItem(data)

   Bases: :py:obj:`PyQt5.QtWidgets.QListWidgetItem`


   .. py:attribute:: data


.. py:class:: BaseClassData(filepath, canvas)

   .. py:attribute:: DEFAULT_PLOT_SETTINGS


   .. py:attribute:: DEFAULT_VIEW_SETTINGS


   .. py:attribute:: DEFAULT_AXLIM_SETTINGS


   .. py:attribute:: filepath


   .. py:attribute:: canvas


   .. py:attribute:: label


   .. py:attribute:: loaded_data
      :value: None



   .. py:attribute:: plot_type
      :value: None



   .. py:attribute:: settings


   .. py:attribute:: view_settings


   .. py:attribute:: axlim_settings


   .. py:attribute:: filters
      :value: []



   .. py:attribute:: labels_changed
      :value: False



   .. py:attribute:: legend
      :value: False



   .. py:method:: prepare_dataset()


   .. py:method:: get_column_data(line=None)


   .. py:method:: get_columns()


   .. py:method:: load_and_reshape_data(reload_data=False, reload_from_file=False, linefrompopup=None)


   .. py:method:: shape_single_array(array)


   .. py:method:: add_array_to_data_dict(array, name)


   .. py:method:: filttocol(axis)


   .. py:method:: copy_raw_to_processed_data(line=None)


   .. py:method:: reshape_for_plot_type(line=None)


   .. py:method:: plot_type_histogram(line)


   .. py:method:: plot_type_fft(line)


   .. py:method:: plot_type_histogram_y()


   .. py:method:: plot_type_histogram_x()


   .. py:method:: plot_type_ffty()


   .. py:method:: plot_type_fftx()


   .. py:method:: plot_type_fftxy()


   .. py:method:: prepare_data_for_plot(reload_data=False, reload_from_file=False, linefrompopup=None, update_color_limits=False, plot_type=None)


   .. py:method:: init_plotted_lines()


   .. py:method:: add_cbar_hist()


   .. py:method:: add_plot(editor_window)


   .. py:method:: apply_default_lables()


   .. py:method:: reset_view_settings(overrule=False)


   .. py:method:: reset_midpoint()


   .. py:method:: apply_plot_settings()


   .. py:method:: apply_view_settings()


   .. py:method:: apply_axlim_settings()


   .. py:method:: apply_axscale_settings()


   .. py:method:: reset_axlim_settings()


   .. py:method:: apply_colormap()


   .. py:method:: apply_single_filter(processed_data, filt)


   .. py:method:: apply_all_filters(update_color_limits=True, filter_box_index=None)


   .. py:method:: extension_setting_edited(editor, setting_name)


   .. py:method:: add_extension_actions(editor, menu)


   .. py:method:: do_extension_actions(editor, menu)


   .. py:method:: file_finished()


   .. py:method:: hide_linecuts()


.. py:class:: NumpyData(filepath, canvas, dataset)

   Bases: :py:obj:`BaseClassData`


   .. py:attribute:: dataset


   .. py:attribute:: label


   .. py:attribute:: filters


   .. py:attribute:: view_settings


   .. py:attribute:: axlim_settings


   .. py:attribute:: raw_data


   .. py:method:: prepare_data_for_plot(reload_data=False)


.. py:class:: InternalData(canvas, dataset, label_name, all_parameter_names, dimension)

   Bases: :py:obj:`BaseClassData`


   .. py:attribute:: loaded_data


   .. py:attribute:: canvas


   .. py:attribute:: all_parameter_names


   .. py:attribute:: data_dict


   .. py:attribute:: label


   .. py:attribute:: dim


   .. py:method:: prepare_dataset()


   .. py:method:: load_and_reshape_data(reload=False, reload_from_file=False, linefrompopup=None)


   .. py:method:: get_column_data(line=None)


.. py:class:: MixedInternalData(canvas, label_name, dataset2d_type, dataset1d_type, dataset2d_filepath=None, dataset1d_filepath=None, dataset1d_loaded_data=None, dataset2d_loaded_data=None, dataset1d_label=None, dataset2d_label=None, dataset1d_all_parameter_names=None, dataset2d_all_parameter_names=None, dataset1d_dim=None, dataset2d_dim=None)

   Bases: :py:obj:`BaseClassData`


   .. py:attribute:: dataset2d_type


   .. py:attribute:: dataset1d_type


   .. py:attribute:: dataset1d_filepath
      :value: None



   .. py:attribute:: dataset2d_filepath
      :value: None



   .. py:attribute:: dataset1d_loaded_data
      :value: None



   .. py:attribute:: dataset2d_loaded_data
      :value: None



   .. py:attribute:: dataset1d_label
      :value: None



   .. py:attribute:: dataset2d_label
      :value: None



   .. py:attribute:: dataset1d_all_parameter_names
      :value: None



   .. py:attribute:: dataset2d_all_parameter_names
      :value: None



   .. py:attribute:: dataset1d_dim
      :value: None



   .. py:attribute:: dataset2d_dim
      :value: None



   .. py:attribute:: filepath
      :value: 'mixed_internal_data'



   .. py:attribute:: canvas


   .. py:attribute:: label


   .. py:attribute:: dim
      :value: 'mixed'



   .. py:attribute:: show_2d_data
      :value: True



   .. py:attribute:: plot_type
      :value: None



   .. py:attribute:: all_parameter_names


   .. py:attribute:: settings_menu_options


   .. py:attribute:: filter_menu_options


   .. py:method:: prepare_data_for_plot(*args, **kwargs)


   .. py:method:: reset_view_settings()


   .. py:method:: add_plot(editor_window)


   .. py:method:: apply_all_filters(update_color_limits=True, filter_box_index=None)


   .. py:method:: add_cbar_hist()


