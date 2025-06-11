qcodespp.plotting.offline.qcodes_pp_extension
=============================================

.. py:module:: qcodespp.plotting.offline.qcodes_pp_extension


Classes
-------

.. autoapisummary::

   qcodespp.plotting.offline.qcodes_pp_extension.qcodesppData


Module Contents
---------------

.. py:class:: qcodesppData(filepath, canvas, metapath, load_the_data=True)

   Bases: :py:obj:`qcodespp.plotting.offline.datatypes.BaseClassData`


   .. py:attribute:: filepath


   .. py:attribute:: label
      :value: 'Uninferable'



   .. py:attribute:: independent_parameters
      :value: []



   .. py:attribute:: independent_parameter_names
      :value: []



   .. py:attribute:: dependent_parameters
      :value: []



   .. py:attribute:: dependent_parameter_names
      :value: []



   .. py:attribute:: all_parameters
      :value: []



   .. py:attribute:: all_parameter_names
      :value: []



   .. py:attribute:: channels


   .. py:attribute:: plot_type
      :value: None



   .. py:attribute:: index_x
      :value: 0



   .. py:attribute:: index_y
      :value: 1



   .. py:attribute:: dataset_id


   .. py:method:: prepare_dataset()


   .. py:method:: isFinished()


   .. py:method:: finished_dimensions()


   .. py:method:: get_column_data(line=None)


   .. py:method:: load_and_reshape_data(reload_data=False, reload_from_file=True, linefrompopup=None)


   .. py:method:: identify_independent_vars()


   .. py:method:: init_plotted_lines()


   .. py:method:: apply_single_filter(processed_data, filt)


   .. py:method:: filttocol(axis)


