qcodespp.data.hdf5_format_hickle
================================

.. py:module:: qcodespp.data.hdf5_format_hickle


Attributes
----------

.. autosummary::

   qcodespp.data.hdf5_format_hickle.log


Classes
-------

.. autosummary::

   qcodespp.data.hdf5_format_hickle.HDF5FormatHickle


Module Contents
---------------

.. py:data:: log

.. py:class:: HDF5FormatHickle

   Bases: :py:obj:`qcodespp.data.hdf5_format.HDF5Format`


   HDF5 formatter for saving qcodespp datasets.

   Capable of storing (write) and recovering (read) qcodes datasets.



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

      Reads in the metadata

      Args:
          data_set (DataSetPP): Dataset object to read the metadata into



