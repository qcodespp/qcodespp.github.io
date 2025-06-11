qcodespp.data.io
================

.. py:module:: qcodespp.data.io

.. autoapi-nested-parse::

   IO managers for QCodespp.

   IO managers wrap whatever physical storage layer the user wants to use
   in an interface mimicking the built-in <open> context manager, with
   some restrictions to minimize the overhead in creating new IO managers.

   The main thing these managers need to implement is the open context manager:

   - Only the context manager needs to be implemented, not separate
     open function and close methods.

   - open takes the standard parameters:

       - filename: (string)
       - mode: (string) only 'r' (read), 'w' (write), and 'a' (append) are
         expected to be implemented. As with normal file objects, the only
         difference between write and append is that write empties the file
         before adding new data, and append leaves the existing contents in
         place but starts writing at the end.
       - encoding: If a special output encoding is desired. i.e. 'utf8

   - the file-like object returned should implement a minimal set of operations.

     In read mode:
       - read([size]): read to the end or at most size bytes into a string
       - readline([size]): read until a newline or up to size bytes, into a string
       - iter(): usually return self, but can be any iterator over lines
       - next(): assuming iter() returns self, this yields the next line.

     In write or append mode:
       - write(s): add string s to the end of the file.
       - writelines(seq): add a sequence of strings

   IO managers should also implement:

   - a join method, ala ``os.path.join(*args)``.
   - a list method, that returns all objects matching location
   - a remove method, ala os.remove(path) except that it will remove directories
     as well as files, since we're allowing "locations" to be directories
     or files.



Attributes
----------

.. autoapisummary::

   qcodespp.data.io.ALLOWED_OPEN_MODES


Classes
-------

.. autoapisummary::

   qcodespp.data.io.DiskIO


Module Contents
---------------

.. py:data:: ALLOWED_OPEN_MODES
   :value: ('r', 'w', 'a')


.. py:class:: DiskIO(base_location)

   Simple IO object to wrap disk operations with a custom base location.

   Also accepts both forward and backward slashes at any point, and
   normalizes both to the OS we are currently on.

   Args:
       base_location (str): a path to the root data folder.
           Converted to an absolute path immediately, so even if you supply a
           relative path, later changes to the OS working directory will not
           affect data paths.


   .. py:method:: open(filename, mode, encoding=None)

      Mimic the interface of the built in open context manager.

      Args:
          filename (str): path relative to base_location.

          mode (str): 'r' (read), 'w' (write), or 'a' (append).
              Other open modes are not supported because we don't want
              to force all IO managers to support others.

      Returns:
          context manager yielding the open file



   .. py:method:: to_path(location)

      Convert a location string into a path on the local file system.

      For DiskIO this just fixes slashes and prepends the base location,
      doing nothing active with the file. But for other io managers that
      refer to remote storage, this method may actually fetch the file and
      put it at a temporary local path.

      Args:
          location (str): A location string for a complete dataset or
              a file within it.

      Returns:
          path (str): The path on disk to which this location maps.



   .. py:method:: to_location(path)

      Convert a local filesystem path into a location string.

      Args:
          path (str): a path on the local file system.

      Returns:
          location (str): the location string corresponding to this path.



   .. py:method:: __repr__()

      Show the base location in the repr.



   .. py:method:: join(*args)

      Context-dependent os.path.join for this io manager.



   .. py:method:: isfile(location)

      Check whether this location matches a file.



   .. py:method:: list(location, maxdepth=1, include_dirs=False)

      Return all files that match location.

      This is either files whose names match up to an arbitrary extension,
      or any files within an exactly matching directory name.

      Args:
          location (str): the location to match.
              May contain the usual path wildcards * and ?

          maxdepth (int, optional): maximum levels of directory nesting to
              recurse into looking for files. Default 1.

          include_dirs (bool, optional): whether to allow directories in
              the results or just files. Default False.

      Returns:
          A list of matching files and/or directories, as locations
          relative to our base_location.



   .. py:method:: remove(filename)

      Delete a file or folder and prune the directory tree.



   .. py:method:: remove_all(location)

      Delete all files/directories in the dataset at this location.

      Afterward prunes the directory tree.



