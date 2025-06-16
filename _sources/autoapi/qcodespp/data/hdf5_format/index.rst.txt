qcodespp.data.hdf5_format
=========================

.. py:module:: qcodespp.data.hdf5_format


Classes
-------

.. autosummary::

   qcodespp.data.hdf5_format.HDF5Format
   qcodespp.data.hdf5_format.HDF5FormatMetadata


Functions
---------

.. autosummary::

   qcodespp.data.hdf5_format.str_to_bool


Module Contents
---------------

.. py:class:: HDF5Format

   Bases: :py:obj:`qcodespp.data.format.Formatter`


   HDF5 formatter for saving qcodespp datasets.

   Capable of storing (write) and recovering (read) qcodes datasets.



   .. py:method:: close_file(data_set)

      Closes the hdf5 file open in the dataset.

      Args:
          data_set (DataSetPP): DataSetPP object



   .. py:method:: read(data_set, location=None)

      Reads an hdf5 file specified by location into a data_set object.
      If no data_set is provided will create an empty data_set to read into.


      Args:
          data_set (DataSetPP): the data to read into. Should already have
              attributes ``io`` (an io manager), ``location`` (string),
              and ``arrays`` (dict of ``{array_id: array}``, can be empty
              or can already have some or all of the arrays present, they
              expect to be overwritten)
          location (None or str): Location to write the data. If no location 
              is provided will use the location specified in the dataset.



   .. py:method:: write(data_set, io_manager=None, location=None, force_write=False, flush=True, write_metadata=True, only_complete=False)

      Writes a data_set to an hdf5 file.

      Args:
          data_set: qcodes data_set to write to hdf5 file
          io_manager: io_manger used for providing path
          location: location can be used to specify custom location
          force_write (bool): if True creates a new file to write to
          flush (bool) : whether to flush after writing, can be disabled
              for testing or performance reasons
          write_metadata (bool): If True write the dataset metadata to disk
          only_complete (bool): Not used by this formatter, but must be
              included in the call signature to avoid an "unexpected
              keyword argument" TypeError.

      N.B. It is recommended to close the file after writing, this can be
      done by calling ``HDF5Format.close_file(data_set)`` or
      ``data_set.finalize()`` if the data_set formatter is set to an
      hdf5 formatter.  Note that this is not required if the dataset
      is created from a Loop as this includes a data_set.finalize()
      statement.

      The write function consists of two parts, writing DataArrays and
      writing metadata.

          - The main part of write consists of writing and resizing arrays,
            the resizing providing support for incremental writes.

          - write_metadata is called at the end of write and dumps a
            dictionary to an hdf5 file. If there already is metadata it will
            delete this and overwrite it with current metadata.




   .. py:method:: write_metadata(data_set, io_manager=None, location=None, read_first=True)

      Writes metadata of dataset to file using write_dict_to_hdf5 method

      Note that io and location are arguments that are only here because
      of backwards compatibility with the loop.
      This formatter uses io and location as specified for the main
      dataset.
      The read_first argument is ignored.



   .. py:method:: write_dict_to_hdf5(data_dict, entry_point)

      Write a (nested) dictionary to HDF5 

      Args:
          data_dict (dict): Dicionary to be written
          entry_point (object): Object to write to



   .. py:method:: read_metadata(data_set)

      Reads in the metadata, this is also called at the end of a read
      statement so there should be no need to call this explicitly.

      Args:
          data_set (DataSetPP): Dataset object to read the metadata into



   .. py:method:: read_dict_from_hdf5(data_dict, h5_group)

      Read a dictionary from HDF5 

      Args:
          data_dict (dict): Dataset to read from
          h5_group (object): HDF5 object to read from



.. py:function:: str_to_bool(s)

.. py:class:: HDF5FormatMetadata

   Bases: :py:obj:`HDF5Format`


   HDF5 formatter for saving qcodespp datasets.

   Capable of storing (write) and recovering (read) qcodes datasets.



   .. py:attribute:: metadata_file
      :value: 'snapshot.json'



   .. py:method:: write_metadata(data_set, io_manager=None, location=None, read_first=False)

      Write all metadata in this DataSetPP to storage.

      Args:
          data_set (DataSetPP): the data we're storing

          io_manager (io_manager): the base location to write to

          location (str): the file location within io_manager

          read_first (bool, optional): read previously saved metadata before
              writing? The current metadata will still be the used if
              there are changes, but if the saved metadata has information
              not present in the current metadata, it will be retained.
              Default True.



   .. py:method:: read_metadata(data_set)

      Reads in the metadata, this is also called at the end of a read
      statement so there should be no need to call this explicitly.

      Args:
          data_set (DataSetPP): Dataset object to read the metadata into



