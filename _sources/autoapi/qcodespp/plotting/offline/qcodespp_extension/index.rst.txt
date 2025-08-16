qcodespp.plotting.offline.qcodespp_extension
============================================

.. py:module:: qcodespp.plotting.offline.qcodespp_extension


Classes
-------

.. autosummary::

   qcodespp.plotting.offline.qcodespp_extension.qcodesppData


Module Contents
---------------

.. py:class:: qcodesppData(filepath, canvas, metapath, load_the_data=False)

   Bases: :py:obj:`qcodespp.plotting.offline.datatypes.BaseClassData`


   .. py:attribute:: label
      :value: 'Uninferable'



   .. py:attribute:: independent_parameter_names
      :value: []



   .. py:attribute:: dependent_parameter_names
      :value: []



   .. py:attribute:: all_parameter_names
      :value: []



   .. py:attribute:: channels


   .. py:method:: prepare_dataset()


   .. py:method:: remove_string_arrays(data_dict)

      Removes arrays that have str as data_type, since these cannot be plotted.



   .. py:method:: load_and_reshape_data(reload_data=False, reload_from_file=True, linefrompopup=None)


   .. py:method:: get_column_data(line=None)


   .. py:method:: identify_variables()


   .. py:method:: init_plotted_lines()


   .. py:method:: apply_single_filter(processed_data, filt)


   .. py:method:: add_array_to_data_dict(array, name)


   .. py:method:: filttocol(axis)


   .. py:method:: file_finished()


