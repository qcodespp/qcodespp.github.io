qcodespp.data.gnuplot_format
============================

.. py:module:: qcodespp.data.gnuplot_format


Attributes
----------

.. autosummary::

   qcodespp.data.gnuplot_format.log


Classes
-------

.. autosummary::

   qcodespp.data.gnuplot_format.GNUPlotFormat


Module Contents
---------------

.. py:data:: log

.. py:class:: GNUPlotFormat(extension='dat', terminator='\n', separator='\t', comment='# ', number_format=None, metadata_file=None)

   Bases: :py:obj:`qcodespp.data.format.Formatter`


   Saves data in one or more gnuplot-format files. We make one file for
   each set of matching dependent variables in the loop.

   Args:

       extension (default 'dat'): file extension for data files

       terminator (default '\\n'): newline character(s) to use on write
           not used for reading, we will read any combination of '\\r' and '\\n'

       separator (default '\\t'): field (column) separator, must be whitespace.
           Only used for writing, we will read with any whitespace separation.

       comment (default '# '): lines starting with this are not data
           Comments are written with this full string, and identified on read
           by just the string after stripping whitespace.

       number_format (default 'g'): from the format mini-language, how to
           format numeric data into a string

       always_nest (default True): whether to always make a folder for files
           or just make a single data file if all data has the same setpoints

   These files are basically tab-separated values, but any quantity of
   any whitespace characters is accepted.

   Each row represents one setting of the setpoint variable(s)
   the setpoint variable(s) are in the first column(s)
   measured variable(s) come after.

   The data is preceded by comment lines (starting with #).
   We use three:

   - one for the variable name
   - the (longer) axis label, in quotes so a label can contain whitespace.
   - for each dependent var, the (max) number of points in that dimension
     (this also tells us how many dependent vars we have in this file)

   ::

       # id1   id2     id3...
       # "label1"      "label2"        "label3"...
       # 100   250
       1       2       3...
       2       3       4...

   For data of 2 dependent variables, gnuplot puts each inner loop into one
   block, then increments the outer loop in the next block, separated by a
   blank line.

   We extend this to an arbitrary quantity of dependent variables by using
   one blank line for each loop level that resets. (gnuplot *does* seem to
   use 2 blank lines sometimes, to denote a whole new dataset, which sort
   of corresponds to our situation.)


   .. py:attribute:: metadata_file
      :value: 'snapshot.json'



   .. py:attribute:: extension
      :value: '.'



   .. py:attribute:: terminator
      :value: Multiline-String

      .. raw:: html

         <details><summary>Show Value</summary>

      .. code-block:: python

         """
         """

      .. raw:: html

         </details>




   .. py:attribute:: separator
      :value: '\t'



   .. py:attribute:: comment
      :value: '# '



   .. py:attribute:: comment_chars
      :value: ''



   .. py:attribute:: comment_len


   .. py:method:: read_one_file(data_set, f, ids_read)

      Called by Formatter.read to bring one data file into
      a DataSetPP. Setpoint data may be duplicated across multiple files,
      but each measured DataArray must only map to one file.

      args:
          data_set: the DataSetPP we are reading into
          f: a file-like object to read from
          ids_read: a `set` of array_ids that we have already read.
              when you read an array, check that it's not in this set (except
              setpoints, which can be in several files with different inner loop)
              then add it to the set so other files know not to read it again



   .. py:method:: write(data_set, io_manager, location, force_write=False, write_metadata=True, only_complete=True, filename=None, force_rewrite=False)

      Write updates in this DataSetPP to storage.

      Will choose append if possible, overwrite if not.

      Args:
          data_set (DataSetPP): the data we're storing
          io_manager (io_manager): the base location to write to
          location (str): the file location within io_manager
          only_complete (bool): passed to match_save_range, answers the
              following question: Should we write all available new data,
              or only complete rows? Is used to make sure that everything
              gets written when the DataSetPP is finalised, even if some
              dataarrays are strange (like, full of nans)
          filename (Optional[str]): Filename to save to. Will override
              the usual naming scheme and possibly overwrite files, so
              use with care. The file will be saved in the normal location.



   .. py:method:: write_metadata(data_set, io_manager, location, read_first=True)

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

      Read the metadata from this DataSetPP from storage.

      Subclasses must override this method.

      Args:
          data_set (DataSetPP): the data to read metadata into



