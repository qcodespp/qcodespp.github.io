qcodespp.data.location
======================

.. py:module:: qcodespp.data.location

.. autoapi-nested-parse::

   Standard location_provider class(es) for creating DataSetPP locations.



Classes
-------

.. autosummary::

   qcodespp.data.location.SafeFormatter
   qcodespp.data.location.FormatLocation


Module Contents
---------------

.. py:class:: SafeFormatter

   Bases: :py:obj:`string.Formatter`


   Modified string formatter that doesn't complain about missing keys.


   .. py:method:: get_value(key, args, kwargs)

      Missing keys just get left as they were: '{key}'.



.. py:class:: FormatLocation(fmt=None, fmt_date=None, fmt_time=None, fmt_counter=None, record=None)

   This is the default DataSetPP Location provider.

   It provides a callable that returns a new (not used by another DataSetPP)
   location string, based on a format string ``fmt`` and a dict ``record`` of
   information to pass to ``fmt``.

   Default record items are ``date``, ``time``, and ``counter``
   Record item priority from lowest to highest (double items will be
   overwritten):

   - current ``date``, and ``time``
   - record dict from ``__init__``
   - record dict from ``__call__``
   - automatic ``counter``

   For example if any record dict contains a `date` keyword, it will no longer
   be auto-generated.

   Uses ``io.list`` to search for existing data at a matching location.

   ``counter`` must NOT be provided in the record. If ``fmt`` contains
   '{counter}', we look for existing files matching everything BEFORE this,
   then find the highest counter (integer) among those files and use the next
   value.

   If the format string does not contain ``{counter}`` but the location we
   would return is occupied, we add ``'_{counter}'`` to the end.

   Usage::

       loc_provider = FormatLocation(
           fmt='{date}/#{counter}_{time}_{name}_{label}')
       loc = loc_provider(DiskIO('.'),
                          record={'name': 'Rainbow', 'label': 'test'})
       loc
       > '2016-04-30/#001_13-28-15_Rainbow_test'

   Args:
       fmt (str, optional): a format string that all the other info will be
           inserted into. Default '{date}/{time}', or '{date}/{time}_{name}'
           if there is a ``name`` in the record.

       fmt_date (str, optional): a ``datetime.strftime`` format string,
           should only use the date part. The result will be inserted in
           '{date}' in ``fmt``. Default '%Y-%m-%d'.

       fmt_time (str, optional): a ``datetime.strftime`` format string,
           should only use the time part. The result will be inserted in
           '{time}' in ``fmt``. Default '%H-%M-%S'.

       fmt_counter (str, optional): a format string for the counter (integer)
           which is automatically generated from existing DataSetPPs that the
           io manager can see. Default '{03}'.

       record (dict, optional): A dict of default values to provide when
           calling the location_provider. Values provided later will
           override these values.

   Note:
       Do not include date/time or number formatting in ``fmt`` itself, such
       as '{date:%Y-%m-%d}' or '{counter:03}'


   .. py:attribute:: default_fmt


   .. py:attribute:: fmt


   .. py:attribute:: fmt_date
      :value: '%Y-%m-%d'



   .. py:attribute:: fmt_time
      :value: '%H-%M-%S'



   .. py:attribute:: fmt_counter
      :value: '{:03}'



   .. py:attribute:: base_record
      :value: None



   .. py:attribute:: formatter


   .. py:attribute:: counter
      :value: 0



   .. py:method:: __call__(io, record=None)

      Call the location provider to get a new location.

      Args:
          io (io manager): where we intend to put the new DataSetPP.

          record (dict, optional): information to insert in the format string
              Any key provided here will override the default record



