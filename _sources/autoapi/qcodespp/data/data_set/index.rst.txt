qcodespp.data.data_set
======================

.. py:module:: qcodespp.data.data_set

.. autoapi-nested-parse::

   DataSetPP class and factory functions.



Attributes
----------

.. autosummary::

   qcodespp.data.data_set.log


Classes
-------

.. autosummary::

   qcodespp.data.data_set.DataSetPP


Functions
---------

.. autosummary::

   qcodespp.data.data_set.new_data
   qcodespp.data.data_set.load_data
   qcodespp.data.data_set.load_data_num
   qcodespp.data.data_set.load_data_nums
   qcodespp.data.data_set.set_data_format
   qcodespp.data.data_set.set_data_folder


Module Contents
---------------

.. py:data:: log

.. py:function:: new_data(location=None, loc_record=None, name=None, overwrite=False, io=None, backup_location=None, force_write=False, **kwargs)

   Create a new DataSetPP, the text-based data set of qcodespp.

   Args:
       location (str or callable or False, optional): If you provide a string,
           it must be an unused location in the io manager. Can also be:

           - a callable ``location provider`` with one required parameter
             (the io manager), and one optional (``record`` dict),
             which returns a location string when called
           - ``False`` - denotes an only-in-memory temporary DataSetPP.

           Note that the full path to or physical location of the data is a
           combination of io + location. the default ``DiskIO`` sets the base
           directory, which this location is a relative path inside.
           Default ``DataSetPP.location_provider`` which is initially
           ``FormatLocation()``

       loc_record (dict, optional): If location is a callable, this will be
           passed to it as ``record``

       name (str, optional): overrides the ``name`` key in the ``loc_record``.

       overwrite (bool): Are we allowed to overwrite an existing location?
           Default False.

       io (io_manager, optional): base physical location of the ``DataSetPP``.
           Default ``DataSetPP.default_io`` is initially ``DiskIO('.')`` which
           says the root data directory is the current working directory, ie
           where you started the python session.

       arrays (Optional[List[qcodes.DataArray]): arrays to add to the DataSetPP.
               Can be added later with ``self.add_array(array)``.

       formatter (Formatter, optional): sets the file format/structure to
           write (and read) with. Default ``DataSetPP.default_formatter`` which
           is initially ``GNUPlotFormat()``.

       write_period (float or None, optional):seconds
           between saves to disk.
   Returns:
       A new ``DataSetPP`` object ready for storing new data in.


.. py:function:: load_data(location=None, formatter=None, io=None, include_metadata=True)

   Load an existing DataSetPP.

   Args:
       location (str, optional): the location to load from. Default is the
           current live DataSetPP.
           Note that the full path to or physical location of the data is a
           combination of io + location. the default ``DiskIO`` sets the base
           directory, which this location is a relative path inside.

       formatter (Formatter, optional): sets the file format/structure to
           read with. Default ``DataSetPP.default_formatter`` which
           is initially ``GNUPlotFormat()``.

       io (io_manager, optional): base physical location of the ``DataSetPP``.
           Default ``DataSetPP.default_io`` is initially ``DiskIO('.')`` which
           says the root data directory is the current working directory, ie
           where you started the python session.

   Returns:
       A new ``DataSetPP`` object loaded with pre-existing data.


.. py:function:: load_data_num(number, datafolder='data', delimiter='_', leadingzeros=3, include_metadata=True)

   Load a qcodespp DataSetPP using the counter as identifier.

   Typically qcodespp DataSetPPs are forced to use the format counter_name_date_time,
   where the counter is a zero-padded integer. This function will search for
   a folder with the given counter number, and load the data from it.

   Args:
       number (str or int): the dataset's counter number
       datafolder (str, optional): the folder to load from. Default is the
           current live DataSetPP.
           Note that the full path to or physical location of the data is a
           combination of io + location. the default ``DiskIO`` sets the base
           directory, which this location is a relative path inside.
       delimiter (str, optional): The character after the number. Almost always
           underscore but may be specified if necessary.

   Returns:
       A new ``DataSetPP`` object loaded with pre-existing data.


.. py:function:: load_data_nums(listofnumbers, datafolder='data', delimiter='_', leadingzeros=3, include_metadata=True)

   Loads numerous DataSetPPs from the specified folder by counter number.

   Args:
       litsofnumbers (list of strings or ints): list of desired dataset numbers.
       datafolder (str, optional): the folder to load from. Default is the
           current live DataSetPP.
           Note that the full path to or physical location of the data is a
           combination of io + location. the default ``DiskIO`` sets the base
           directory, which this location is a relative path inside.
       delimiter (str, optional): The character after the number. Almost always
           underscore but may be specified if necessary.

   Returns:
       An array containing ``DataSetPP`` objects loaded with pre-existing data.


.. py:function:: set_data_format(fmt='data/#{counter}_{name}_{date}_{time}')

   Set the default format for storing DataSetPPs. It is not recommended to alter this: instead use set_data_folder.

   Args:
       fmt (str): A format string for the location of the data, with wildcards determined by the FormatLocation class.


.. py:function:: set_data_folder(folder='data')

   Set the default folder for storing DataSetPPs.

   Args:
       folder (str): Folder name relative to the current working directory, e.g. location of the current
           Jupyter notebook. The folder will be created if it does not exist.


.. py:class:: DataSetPP(location=None, arrays=None, formatter=None, io=None, write_period=5, backup_location=None, force_write=False, name=None)

   Bases: :py:obj:`qcodes.utils.helpers.DelegateAttributes`


   A container for one complete measurement from qcodespp.Measure or qcodespp.Loop.

   A DataSetPP consists of multiple DataArrays with potentially different 
   sizes and dimensionalities. It is accompanied by metadata containing snapshots 
   of different qcodespp classes, e.g. Instruments and Parameters in the Station.

   A DataSetPP should not be instantiated directly, but constructed by qcodespp.Measure 
   or qcodespp.Loop. A pre-existing DataSetPP can be loaded with qcodespp.load_data, 
   load_data_num, or load_data_nums.

   The default format for storage is (a) text file(s) with GNUPlotFormat, where the 
   DataArrays are converted to numpy arrays. This means that each DataArray must be 
   rectangular, and all elements must be of the same type. Currently, types are limited 
   to float or str; however, almost any type other than str can be converted to a float, 
   and this is done automatically; e.g. boolean --> (0,1). 
   DataArrays which are also Setpoints can only be of type float.

   Args:
       location (str or False): A location in the io manager, or ``False`` for
           an only-in-memory temporary DataSetPP.
           Note that the full path to or physical location of the data is a
           combination of io + location. the default ``DiskIO`` sets the base
           directory, which this location is a relative path inside.

       io (io_manager, optional): base physical location of the ``DataSetPP``.
           Default ``DataSetPP.default_io`` is initially ``DiskIO('.')`` which
           says the root data directory is the current working directory, ie
           where you started the python session.

       arrays (Optional[List[qcodes.DataArray]): arrays to add to the DataSetPP.
               Can be added later with ``self.add_array(array)``.

       formatter (Formatter, optional): sets the file format/structure to
           write (and read) with. Default ``DataSetPP.default_formatter`` which
           is initially ``GNUPlotFormat()``.

       write_period (float or None, optional): Only if ``mode=LOCAL``, seconds
           between saves to disk. If not ``LOCAL``, the ``DataServer`` handles
           this and generally writes more often. Use None to disable writing
           from calls to ``self.store``. Default 5.

   Attributes:
       background_functions (OrderedDict[callable]): Class attribute,
           ``{key: fn}``: ``fn`` is a callable accepting no arguments, and
           ``key`` is a name to identify the function and help you attach and
           remove it.

           In ``DataSetPP.complete`` we call each of these periodically, in the
           order that they were attached.

           Note that because this is a class attribute, the functions will
           apply to every DataSetPP. If you want specific functions for one
           DataSetPP you can override this with an instance attribute.


   .. py:attribute:: delegate_attr_dicts
      :value: ['arrays']


      A list of names (strings) of dictionaries
      which are (or will be) attributes of ``self``, whose keys should
      be treated as attributes of ``self``.



   .. py:attribute:: default_io


   .. py:attribute:: default_formatter


   .. py:attribute:: location_provider


   .. py:attribute:: background_functions
      :type:  Dict[str, Callable]


   .. py:attribute:: backup_used
      :value: False



   .. py:attribute:: writing_skipped
      :value: False



   .. py:attribute:: finalized
      :value: False



   .. py:attribute:: publisher
      :value: None



   .. py:attribute:: name
      :value: None



   .. py:attribute:: formatter


   .. py:attribute:: io


   .. py:attribute:: write_period
      :value: 5



   .. py:attribute:: last_write
      :value: 0



   .. py:attribute:: last_store
      :value: -1



   .. py:attribute:: force_write
      :value: False



   .. py:attribute:: metadata


   .. py:attribute:: uuid
      :value: '00000000000000000000000000000000'



   .. py:attribute:: arrays


   .. py:method:: sync()

      Synchronize this DataSetPP with the DataServer or storage.

      If this DataSetPP is on the server, asks the server for changes.
      If not, reads the entire DataSetPP from disk.

      Returns:
          bool: True if this DataSetPP is live on the server



   .. py:method:: fraction_complete()

      Get the fraction of this DataSetPP which has data in it.

      Returns:
          float: the average of all measured (not setpoint) arrays'
              ``fraction_complete()`` values, independent of the individual
              array sizes. If there are no measured arrays, returns zero.



   .. py:method:: complete(delay=1.5)

      Periodically sync the DataSetPP and display percent complete status.

      Also, each period, execute functions stored in (class attribute)
      ``self.background_functions``. If a function fails, we log its
      traceback and continue on. If any one function fails twice in
      a row, it gets removed.

      Args:
          delay (float): seconds between iterations. Default 1.5



   .. py:method:: get_changes(synced_indices)

      Find changes since the last sync of this DataSetPP.

      Args:
          synced_indices (dict): ``{array_id: synced_index}`` where
              synced_index is the last flat index which has already
              been synced, for any (usually all) arrays in the DataSetPP.

      Returns:
          Dict[dict]: keys are ``array_id`` for each array with changes,
              values are dicts as returned by ``DataArray.get_changes``
              and required as kwargs to ``DataArray.apply_changes``.
              Note that not all arrays in ``synced_indices`` need be
              present in the return, only those with changes.



   .. py:method:: add_array(data_array)

      Add one DataArray to this DataSetPP, and mark it as part of this DataSetPP.

      Note: DO NOT just set ``data_set.arrays[id] = data_array``, because
      this will not check if we are overwriting another array, nor set the
      reference back to this DataSetPP, nor that the ``array_id`` in the array
      matches how you're storing it here.

      Args:
          data_array (DataArray): the new array to add

      Raises:
          ValueError: if there is already an array with this id here.



   .. py:method:: remove_array(array_id)

      Remove an array from a dataset

      Throws an exception when the array specified is refereced by other
      arrays in the dataset.

      Args:
          array_id (str): array_id of array to be removed



   .. py:method:: store(loop_indices, ids_values)

      Insert data into one or more of our DataArrays.

      Args:
          loop_indices (tuple): the indices within whatever loops we are
              inside. May have fewer dimensions than some of the arrays
              we are inserting into, if the corresponding value makes up
              the remaining dimensionality.
          values (Dict[Union[float, sequence]]): a dict whose keys are
              array_ids, and values are single numbers or entire slices
              to insert into that array.
       



   .. py:method:: default_parameter_name(paramname='amplitude')

      Return name of default parameter for plotting

      The default parameter is determined by looking into
      metdata['default_parameter_name'].  If this variable is not present,
      then the closest match to the argument paramname is tried.

      Args:
          paramname (str): Name to match to parameter name

      Returns:
          name ( Union[str, None] ): name of the default parameter



   .. py:method:: default_parameter_array(paramname='amplitude')

      Return default parameter array

      Args:
          paramname (str): Name to match to parameter name.
               Defaults to 'amplitude'

      Returns:
          array (DataArray): array corresponding to the default parameter

      See also:
          default_parameter_name




   .. py:method:: read(include_metadata=True)

      Read the whole DataSetPP from storage, overwriting the local data.



   .. py:method:: read_metadata()

      Read the metadata from storage, overwriting the local data.



   .. py:method:: write(write_metadata=False, only_complete=True, filename=None, force_rewrite=False)

      Writes updates to the DataSetPP to storage.

      N.B. it is recommended to call data_set.finalize() when a DataSetPP is
      no longer expected to change to ensure files get closed

      Args:
          write_metadata (bool): write the metadata to disk
          only_complete (bool): passed on to the match_save_range inside
              self.formatter.write. Used to ensure that all new data gets
              saved even when some columns are strange.
          filename (Optional[str]): The filename (minus extension) to use.
              The file gets saved in the usual location.



   .. py:method:: write_copy(path=None, io_manager=None, location=None)

      Write a new complete copy of this DataSetPP to storage.

      Args:
          path (str, optional): An absolute path on this system to write to.
              If you specify this, you may not include either ``io_manager``
              or ``location``.

          io_manager (io_manager, optional): A new ``io_manager`` to use with
              either the ``DataSetPP``'s same or a new ``location``.

          location (str, optional): A new ``location`` to write to, using
              either this ``DataSetPP``'s same or a new ``io_manager``.



   .. py:method:: add_metadata(new_metadata)

      Update DataSetPP.metadata with additional data.

      Args:
          new_metadata (dict): new data to be deep updated into
              the existing metadata



   .. py:method:: save_metadata()

      Evaluate and save the DataSetPP's metadata.



   .. py:method:: finalize(filename=None, write_metadata=True, force_rewrite=False)

      Mark the DataSetPP complete and write any remaining modifications.

      Also closes the data file(s), if the ``Formatter`` we're using
      supports that.

      Args:
          filename (Optional[str]): The file name (minus extension) to
              write to. The location of the file is the usual one.
          write_metadata (bool): Whether to save a snapshot. For e.g. dumping
              raw data inside a loop, a snapshot is not wanted.



   .. py:method:: snapshot(update=False)

      JSON state of the DataSetPP.



   .. py:method:: get_array_metadata(array_id)

      Get the metadata for a single contained DataArray.

      Args:
          array_id (str): the array to get metadata for.

      Returns:
          dict: metadata for this array.



   .. py:method:: __repr__()

      Rich information about the DataSetPP and contained arrays.



