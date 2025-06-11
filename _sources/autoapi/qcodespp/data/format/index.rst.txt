qcodespp.data.format
====================

.. py:module:: qcodespp.data.format


Attributes
----------

.. autoapisummary::

   qcodespp.data.format.log


Classes
-------

.. autoapisummary::

   qcodespp.data.format.Formatter


Module Contents
---------------

.. py:data:: log

.. py:class:: Formatter

   Data file formatters

   Formatters translate between DataSetPPs and data files.

   Each Formatter is expected to implement writing methods:

   - ``write``: to write the ``DataArrays``
   - ``write_metadata``: to write the metadata structure

   Optionally, if this Formatter keeps the data file(s) open
   between write calls, it may implement:

   - ``close_file``: to perform any final cleanup and release the
     file and any other resources.

   and reading methods:

   - ``read`` or ``read_one_file`` to reconstruct the ``DataArrays``, either
     all at once (``read``) or one file at a time, supplied by the base class
     ``read`` method that loops over all data files at the correct location.

   - ``read_metadata``: to reload saved metadata. If a subclass overrides
     ``read``, this method should call ``read_metadata``, but keep it also
     as a separate method because it occasionally gets called independently.

   All of these methods accept a ``data_set`` argument, which should be a
   ``DataSetPP`` object. Even if you are loading a new data set from disk, this
   object should already have attributes:

       - io: an IO manager (see qcodes.data.io)
         location: a string, like a file path, that identifies the DataSetPP and
         tells the IO manager where to store it
       - arrays: a dict of ``{array_id:DataArray}`` to read into.

   - read will create entries that don't yet exist.
   - write will write ALL DataArrays in the DataSetPP, using
     last_saved_index and modified_range, as well as whether or not
     it found the specified file, to determine how much to write.


   .. py:class:: ArrayGroup

      Bases: :py:obj:`tuple`


      .. py:attribute:: shape


      .. py:attribute:: set_arrays


      .. py:attribute:: data


      .. py:attribute:: name



   .. py:method:: write(data_set, io_manager, location, write_metadata=True, force_write=False, only_complete=True)
      :abstractmethod:


      Write the DataSetPP to storage.

      Subclasses must override this method.

      It is up to the Formatter to decide when to overwrite completely,
      and when to just append or otherwise update the file(s).

      Args:
          data_set (DataSetPP): the data we are writing.
          io_manager (io_manager): base physical location to write to.
          location (str): the file location within the io_manager.
          write_metadata (bool): if True, then the metadata is written to disk
          force_write (bool): if True, then the data is written to disk
          only_complete (bool): Used only by the gnuplot formatter's
              overridden version of this method



   .. py:method:: read(data_set, include_metadata=True)

      Read the entire ``DataSetPP``.

      Find all files matching ``data_set.location`` (using io_manager.list)
      and call ``read_one_file`` on each. Subclasses may either override
      this method (if they use only one file or want to do their own
      searching) or override ``read_one_file`` to use the search and
      initialization functionality defined here.

      Args:
          data_set (DataSetPP): the data to read into. Should already have
              attributes ``io`` (an io manager), ``location`` (string),
              and ``arrays`` (dict of ``{array_id: array}``, can be empty
              or can already have some or all of the arrays present, they
              expect to be overwritten)



   .. py:method:: write_metadata(data_set, io_manager, location, read_first=True)
      :abstractmethod:


      Write the metadata for this DataSetPP to storage.

      Subclasses must override this method.

      Args:
          data_set (DataSetPP): the data we are writing.
          io_manager (io_manager): base physical location to write to.
          location (str): the file location within the io_manager.
          read_first (bool, optional): whether to first look for previously
              saved metadata that may contain more information than the local
              copy.



   .. py:method:: read_metadata(data_set)
      :abstractmethod:


      Read the metadata from this DataSetPP from storage.

      Subclasses must override this method.

      Args:
          data_set (DataSetPP): the data to read metadata into



   .. py:method:: read_one_file(data_set, f, ids_read)
      :abstractmethod:


      Read data from a single file into a ``DataSetPP``.

      Formatter subclasses that break a DataSetPP into multiple data files may
      choose to override either this method, which handles one file at a
      time, or ``read`` which finds matching files on its own.

      Args:
          data_set (DataSetPP): the data we are reading into.

          f (file-like): a file-like object to read from, as provided by
              ``io_manager.open``.

          ids_read (set): ``array_ids`` that we have already read.
              When you read an array, check that it's not in this set (except
              setpoints, which can be in several files with different inner
              loops) then add it to the set so other files know it should not
              be read again.

      Raises:
          ValueError: if a duplicate array_id of measured data is found



   .. py:method:: match_save_range(group, file_exists, only_complete=True, force_rewrite=False)

      Find the save range that will joins all changes in an array group.

      Matches all full-sized arrays: the data arrays plus the inner loop
      setpoint array.

      Note: if an outer loop has changed values (without the inner
      loop or measured data changing) we won't notice it here. We assume
      that before an iteration of the inner loop starts, the outer loop
      setpoint gets set and then does not change later.

      Args:
          group (Formatter.ArrayGroup): a ``namedtuple`` containing the
              arrays that go together in one file, as tuple ``group.data``.

          file_exists (bool): Does this file already exist? If True, and
              all arrays in the group agree on ``last_saved_index``, we
              assume the file has been written up to this index and we can
              append to it. Otherwise we will set the returned range to start
              from zero (so if the file does exist, it gets completely
              overwritten).

          only_complete (bool): Should we write all available new data,
              or only complete rows? If True, we write only the range of
              array indices which all arrays in the group list as modified,
              so that future writes will be able to do a clean append to
              the data file as more data arrives.
              Default True.

      Returns:
          Tuple(int, int): the first and last raveled indices that should
              be saved. Returns None if:
                  * no data is present
                  * no new data can be found



   .. py:method:: group_arrays(arrays)

      Find the sets of arrays which share all the same setpoint arrays.

      Some Formatters use this grouping to determine which arrays to save
      together in one file.

      Args:
          arrays (Dict[DataArray]): all the arrays in a DataSetPP

      Returns:
          List[Formatter.ArrayGroup]: namedtuples giving:

          - shape (Tuple[int]): dimensions as in numpy
          - set_arrays (Tuple[DataArray]): the setpoints of this group
          - data (Tuple[DataArray]): measured arrays in this group
          - name (str): a unique name of this group, obtained by joining
            the setpoint array ids.



