qcodespp.data.data_array
========================

.. py:module:: qcodespp.data.data_array


Classes
-------

.. autosummary::

   qcodespp.data.data_array.DataArray


Module Contents
---------------

.. py:class:: DataArray(parameter=None, name=None, full_name=None, label=None, snapshot=None, array_id=None, set_arrays=(), shape=None, action_indices=(), unit=None, is_setpoint=False, preset_data=None, data_type=None)

   Bases: :py:obj:`qcodes.utils.DelegateAttributes`


   A container for one parameter's data in a qcodespp DataSetPP

   A DataArray can either be a setpoint array or a measured parameter.
   If this is a measured parameter, this object doesn't contain
   the data of the setpoints it was measured at, but it references
   the DataArray objects of these parameters. Those objects only have
   the dimensionality at which they were set - ie the inner loop setpoint
   the same dimensionality as the measured parameter, but the outer
   loop setpoint(s) have lower dimensionality

   When it's first created, a DataArray has no dimensionality,
   .nest must be called for each dimension.

   If preset_data is provided it is used to initialize the data, and the array
   can still be nested around it (making many copies of the data).
   Otherwise it is an error to nest an array that already has data.

   Once the array is initialized, a DataArray acts a lot like a numpy array,
   because we delegate attributes through to the numpy array

   Args:
       parameter (Optional[Parameter]): The parameter whose values will
           populate this array, if any. Will copy ``name``, ``full_name``,
           ``label``, ``unit``, and ``snapshot`` from here unless you
           provide them explicitly.

       name (Optional[str]): The short name of this array.
           TODO: use full_name as name, and get rid of short name

       full_name (Optional[str]): The complete name of this array. If the
           array is based on a parameter linked to an instrument, this is
           typically '<instrument_name>_<param_name>'

       label (Optional[str]): A description of the values in this array to
           use for axis and colorbar labels on plots.

       snapshot (Optional[dict]): Metadata snapshot to save with this array.

       array_id (Optional[str]): A name for this array that's unique within
           its ``DataSetPP``. Typically the full_name, but when the ``DataSetPP``
           is constructed we will append '_<i>' (``i`` is an integer starting
           from 1) if necessary to differentiate arrays with the same id.
           TODO: this only happens for arrays provided to the DataSetPP
           constructor, not those added with add_array. Fix this!
           Also, do we really need array_id *and* full_name (let alone name
           but I've already said we should remove this)?

       set_arrays (Optional[Tuple[DataArray]]): If this array is being
           created with shape already, you can provide one setpoint array
           per dimension. The first should have one dimension, the second
           two dimensions, etc.

       shape (Optional[Tuple[int]]): The shape (as in numpy) of the array.
           Will be prepended with new dimensions by any calls to ``nest``.

       action_indices (Optional[Tuple[int]]): If used within a ``Loop``,
           these are the indices at each level of nesting within the
           ``Loop`` of the loop action that's populating this array.
           TODO: this shouldn't be in DataArray at all, the loop should
           handle converting this to array_id internally (maybe it
           already does?)

       unit (Optional[str]): The unit of the values stored in this array.

       units (Optional[str]): DEPRECATED, redirects to ``unit``.

       is_setpoint (bool): True if this is a setpoint array, False if it
           is measured. Default False.

       preset_data (Optional[Union[ndarray, sequence]]): Contents of the
           array, if already known (for example if this is a setpoint
           array). ``shape`` will be inferred from this array instead of
           from the ``shape`` argument.

       data_type (Optional[Type] default = float): numpy array entries 
           must be of the same type. Float covers most instances, otherwise
           string is best. 


   .. py:attribute:: SNAP_ATTRS
      :value: ('array_id', 'name', 'shape', 'unit', 'label', 'action_indices', 'is_setpoint', 'set_array_ids',...



   .. py:attribute:: COPY_ATTRS_FROM_INPUT
      :value: ('name', 'label', 'unit', 'data_type')



   .. py:attribute:: SNAP_OMIT_KEYS
      :value: ('ts', 'value', '__class__', 'shape', 'array_id', 'set_arraysaction_indices')



   .. py:attribute:: name
      :value: None



   .. py:attribute:: full_name
      :value: None



   .. py:attribute:: label
      :value: None



   .. py:attribute:: shape
      :value: None



   .. py:attribute:: unit
      :value: None



   .. py:attribute:: array_id
      :value: None



   .. py:attribute:: is_setpoint
      :value: False



   .. py:attribute:: action_indices
      :value: ()



   .. py:attribute:: set_arrays
      :value: ()



   .. py:attribute:: data_type
      :value: None



   .. py:attribute:: last_saved_index
      :value: None



   .. py:attribute:: modified_range
      :value: None



   .. py:attribute:: ndarray
      :value: None



   .. py:property:: data_set

      The DataSetPP this array belongs to.

      A DataArray can belong to at most one DataSetPP.
      TODO: make this a weakref



   .. py:property:: set_array_ids


   .. py:method:: nest(size, action_index=None, set_array=None)

      Nest this array inside a new outer loop.

      You cannot call ``nest`` after ``init_data`` unless this is a
      setpoint array.
      TODO: is this restriction really useful? And should we maintain
      a distinction between _preset and is_setpoint, or can wejust use
      is_setpoint?

      Args:
          size (int): Length of the new loop.

          action_index (Optional[int]): Within the outer loop at this
              nesting level, which action does this array derive from?

          set_array (Optional[DataArray]): The setpoints of the new outer
              loop. If this DataArray *is* a setpoint array, you should
              omit both ``action_index`` and ``set_array``, and it will
              reference itself as the inner setpoint array.

      Returns:
          DataArray: self, in case you want to construct the array with
              chained method calls.



   .. py:method:: init_data(data=None)

      Create the actual numpy array to hold data.

      The array will be sized based on either ``self.shape`` or
      data provided here.

      Idempotent: will do nothing if the array already exists.

      If data is provided, this array is marked as a preset
      meaning it can still be nested around this data.
      TODO: per above, perhaps remove this distinction entirely?

      Args:
          data (Optional[Union[ndarray, sequence]]): If provided,
              we fill the array with this data. Otherwise the new
              array will be filled with NaN.

      Raises:
          ValueError: if ``self.shape`` does not match ``data.shape``
          ValueError: if the array was already initialized with a
              different shape than we're about to create



   .. py:method:: clear()

      Fill the (already existing) data array with nan.

      Numpy ndarrays have to be filled with something. Zero (or any number) is a bad choice, 
      so we use NaN for floats and 'nan' for strings. These are the only 
      data types supported, but Boolean, Int, etc can be cast to float, and 
      complex numbers can either be broken into two floats, or stored as string.



   .. py:method:: __setitem__(loop_indices, value)

      Set data values.

      Follows numpy syntax, allowing indices of lower dimensionality than
      the array, if value makes up the extra dimension(s)

      Also update the record of modifications to the array. If you don't
      want this overhead, you can access ``self.ndarray`` directly.



   .. py:method:: __getitem__(loop_indices)


   .. py:attribute:: delegate_attr_objects
      :value: ['ndarray']


      A list of names (strings) of objects
      which are (or will be) attributes of ``self``, whose attributes
      should be passed through to ``self``.



   .. py:method:: __len__()

      Array length.

      Must be explicitly delegated, because len() will look for this
      attribute to already exist.



   .. py:method:: flat_index(indices, index_fill=None)

      Generate the raveled index for the given indices.

      This is the index you would have if the array is reshaped to 1D,
      looping over the indices from inner to outer.

      Args:
          indices (sequence): indices of an element or slice of this array.

          index_fill (sequence, optional): extra indices to use if
              ``indices`` has less dimensions than the array, ie it points
              to a slice rather than a single element. Use zeros to get the
              beginning of this slice, and [d - 1 for d in shape] to get the
              end of the slice.

      Returns:
          int: the resulting flat index.



   .. py:method:: mark_saved(last_saved_index)

      Mark certain outstanding modifications as saved.

      Args:
          last_saved_index (int): The flat index of the last point
              saved. If ``modified_range`` extends beyond this, the
              data past ``last_saved_index`` will still be marked
              modified, otherwise ``modified_range`` is cleared
              entirely.



   .. py:method:: clear_save()

      Make previously saved parts of this array look unsaved (modified).

      This can be used to force overwrite or rewrite, like if we're
      moving or copying the ``DataSetPP``.



   .. py:method:: get_synced_index()

      Get the last index which has been synced from the server.

      Will also initialize the array if this hasn't happened already.
      TODO: seems hacky to init_data here.

      Returns:
          int: the last flat index which has been synced from the server,
              or -1 if no data has been synced.



   .. py:method:: get_changes(synced_index)

      Find changes since the last sync of this array.

      Args:
          synced_index (int): The last flat index which has already
              been synced.

      Returns:
          Union[dict, None]: None if there is no new data. If there is,
              returns a dict with keys:
                  start (int): the flat index of the first returned value.
                  stop (int): the flat index of the last returned value.
                  vals (List[float]): the new values



   .. py:method:: apply_changes(start, stop, vals)

      Insert new synced values into the array.

      To be be called in a ``PULL_FROM_SERVER`` ``DataSetPP`` using results
      returned by ``get_changes`` from the ``DataServer``.

      TODO: check that vals has the right length?

      Args:
          start (int): the flat index of the first new value.
          stop (int): the flat index of the last new value.
          vals (List[float]): the new values



   .. py:method:: __repr__()


   .. py:method:: snapshot(update=False)

      JSON representation of this DataArray.



   .. py:method:: fraction_complete()

      Get the fraction of this array which has data in it.

      Or more specifically, the fraction of the latest point in the array
      where we have touched it.

      Returns:
          float: fraction of array which is complete, from 0.0 to 1.0



   .. py:method:: subset(indices)

      Return a subset of this DataArray.

      Args:
          indices (sequence): Indices to select from the array.
              If this is a single index, it will return a scalar.
              If this is a sequence, it will return a new DataArray
              with the same metadata as this one, but with the
              selected data.

      Returns:
          DataArray or scalar: The selected data.



   .. py:method:: __add__(val)


   .. py:method:: __radd__(val)


   .. py:method:: __sub__(val)


   .. py:method:: __rsub__(val)


   .. py:method:: __mul__(val)


   .. py:method:: __rmul__(val)


   .. py:method:: __truediv__(val)


   .. py:method:: __rtruediv__(val)


   .. py:method:: __floordiv__(val)


   .. py:method:: __rfloordiv__(val)


   .. py:method:: __mod__(val)


   .. py:method:: __rmod__(val)


   .. py:method:: __pow__(val)


   .. py:method:: __rpow__(val)


   .. py:method:: __neg__()


   .. py:method:: __pos__()


   .. py:method:: __abs__()


   .. py:method:: __lt__(val)


   .. py:method:: __le__(val)


   .. py:method:: __gt__(val)


   .. py:method:: __ge__(val)


