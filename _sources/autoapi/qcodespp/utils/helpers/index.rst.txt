qcodespp.utils.helpers
======================

.. py:module:: qcodespp.utils.helpers


Attributes
----------

.. autosummary::

   qcodespp.utils.helpers.log


Classes
-------

.. autosummary::

   qcodespp.utils.helpers.NumpyJSONEncoder
   qcodespp.utils.helpers.LogCapture
   qcodespp.utils.helpers.DelegateAttributes


Functions
---------

.. autosummary::

   qcodespp.utils.helpers.tprint
   qcodespp.utils.helpers.is_sequence
   qcodespp.utils.helpers.is_sequence_of
   qcodespp.utils.helpers.is_function
   qcodespp.utils.helpers.full_class
   qcodespp.utils.helpers.named_repr
   qcodespp.utils.helpers.deep_update
   qcodespp.utils.helpers.permissive_range
   qcodespp.utils.helpers.make_sweep
   qcodespp.utils.helpers.wait_secs
   qcodespp.utils.helpers.make_unique
   qcodespp.utils.helpers.strip_attrs
   qcodespp.utils.helpers.compare_dictionaries
   qcodespp.utils.helpers.warn_units
   qcodespp.utils.helpers.foreground_qt_window
   qcodespp.utils.helpers.add_to_spyder_UMR_excludelist
   qcodespp.utils.helpers.attribute_set_to
   qcodespp.utils.helpers.partial_with_docstring


Module Contents
---------------

.. py:data:: log

.. py:class:: NumpyJSONEncoder(*, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)

   Bases: :py:obj:`json.JSONEncoder`


   Return numpy types as standard types.


   .. py:method:: default(obj)

      Implement this method in a subclass such that it returns
      a serializable object for ``o``, or calls the base implementation
      (to raise a ``TypeError``).

      For example, to support arbitrary iterators, you could
      implement default like this::

          def default(self, o):
              try:
                  iterable = iter(o)
              except TypeError:
                  pass
              else:
                  return list(iterable)
              # Let the base class default method raise the TypeError
              return super().default(o)




.. py:function:: tprint(string, dt=1, tag='default')

   Print progress of a loop every dt seconds 


.. py:function:: is_sequence(obj)

   Test if an object is a sequence.

   We do not consider strings or unordered collections like sets to be
   sequences, but we do accept iterators (such as generators)


.. py:function:: is_sequence_of(obj, types=None, depth=None, shape=None)

   Test if object is a sequence of entirely certain class(es).

   Args:
       obj (any): the object to test.

       types (Optional[Union[class, Tuple[class]]]): allowed type(s)
           if omitted, we just test the depth/shape

       depth (Optional[int]): level of nesting, ie if ``depth=2`` we expect
           a sequence of sequences. Default 1 unless ``shape`` is supplied.

       shape (Optional[Tuple[int]]): the shape of the sequence, ie its
           length in each dimension. If ``depth`` is omitted, but ``shape``
           included, we set ``depth = len(shape)``

   Returns:
       bool, True if every item in ``obj`` matches ``types``


.. py:function:: is_function(f, arg_count, coroutine=False)

   Check and require a function that can accept the specified number of
   positional arguments, which either is or is not a coroutine
   type casting "functions" are allowed, but only in the 1-argument form

   Args:
       f (callable): function to check
       arg_count (int): number of argument f should accept
       coroutine (bool): is a coroutine. Default: False

   Return:
       bool: is function and accepts the specified number of arguments



.. py:function:: full_class(obj)

   The full importable path to an object's class.


.. py:function:: named_repr(obj)

   Enhance the standard repr() with the object's name attribute.


.. py:function:: deep_update(dest, update)

   Recursively update one JSON structure with another.

   Only dives into nested dicts; lists get replaced completely.
   If the original value is a dict and the new value is not, or vice versa,
   we also replace the value completely.


.. py:function:: permissive_range(start, stop, step)

   returns range (as a list of values) with floating point step

   inputs:
       start, stop, step

   always starts at start and moves toward stop,
   regardless of the sign of step


.. py:function:: make_sweep(start, stop, step=None, num=None)

   Generate numbers over a specified interval.
   Requires `start` and `stop` and (`step` or `num`)
   The sign of `step` is not relevant.

   Args:
       start (Union[int, float]): The starting value of the sequence.
       
       stop (Union[int, float]): The end value of the sequence.
       
       step (Optional[Union[int, float]]):  Spacing between values.
       
       num (Optional[int]): Number of values to generate.

   Returns:
       numpy.linespace: numbers over a specified interval.

   Examples:
       >>> make_sweep(0, 10, num=5)
       [0.0, 2.5, 5.0, 7.5, 10.0]
       >>> make_sweep(5, 10, step=1)
       [5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
       >>> make_sweep(15, 10.5, step=1.5)
       >[15.0, 13.5, 12.0, 10.5]


.. py:function:: wait_secs(finish_clock)

   calculate the number of seconds until a given clock time
   The clock time should be the result of time.perf_counter()
   Does NOT wait for this time.


.. py:class:: LogCapture(logger=logging.getLogger())

   context manager to grab all log messages, optionally
   from a specific logger

   usage::

       with LogCapture() as logs:
           code_that_makes_logs(...)
       log_str = logs.value



   .. py:attribute:: logger


   .. py:attribute:: stashed_handlers


   .. py:method:: __enter__()


   .. py:method:: __exit__(type, value, tb)


.. py:function:: make_unique(s, existing)

   make string s unique, able to be added to a sequence `existing` of
   existing names without duplication, by appending _<int> to it if needed


.. py:class:: DelegateAttributes

   Mixin class to create attributes of this object by
   delegating them to one or more dicts and/or objects

   Also fixes __dir__ so the delegated attributes will show up
   in dir() and autocomplete


   Attributes:
       delegate_attr_dicts (list): a list of names (strings) of dictionaries
           which are (or will be) attributes of self, whose keys should
           be treated as attributes of self
       delegate_attr_objects (list): a list of names (strings) of objects
           which are (or will be) attributes of self, whose attributes
           should be passed through to self
       omit_delegate_attrs (list): a list of attribute names (strings)
           to *not* delegate to any other dict or object

   any `None` entry is ignored

   attribute resolution order:
       1. real attributes of this object
       2. keys of each dict in delegate_attr_dicts (in order)
       3. attributes of each object in delegate_attr_objects (in order)


   .. py:attribute:: delegate_attr_dicts
      :type:  List[str]
      :value: []



   .. py:attribute:: delegate_attr_objects
      :type:  List[str]
      :value: []



   .. py:attribute:: omit_delegate_attrs
      :type:  List[str]
      :value: []



   .. py:method:: __getattr__(key)


   .. py:method:: __dir__()


.. py:function:: strip_attrs(obj, whitelist=())

   Irreversibly remove all direct instance attributes of obj, to help with
   disposal, breaking circular references.

   Args:
       obj:  object to be stripped
       whitelist (list): list of names that are not stripped from the object


.. py:function:: compare_dictionaries(dict_1, dict_2, dict_1_name='d1', dict_2_name='d2', path='')

   Compare two dictionaries recursively to find non matching elements

   Args:
       dict_1: dictionary 1
       dict_2: dictionary 2
       dict_1_name: optional name used in the differences string
       dict_2_name: ''
   Returns:
       dicts_equal:      Boolean
       dict_differences: formatted string containing the differences



.. py:function:: warn_units(class_name, instance)

.. py:function:: foreground_qt_window(window)

   Try as hard as possible to bring a qt window to the front. This
   will use pywin32 if installed and running on windows as this
   seems to be the only reliable way to foreground a window. The
   build-in qt functions often doesn't work. Note that to use this
   with pyqtgraphs remote process you should use the ref in that module
   as in the example below.

   Args:
       window: handle to qt window to foreground
   Examples:
       >>> Qtplot.qt_helpers.foreground_qt_window(plot.win)


.. py:function:: add_to_spyder_UMR_excludelist(modulename: str)

   Spyder tries to reload any user module. This does not work well for
   qcodes because it overwrites Class variables. QCoDeS uses these to
   store global attributes such as default station, monitor and list of
   instruments. This "feature" can be disabled by the
   gui. Unfortunately this cannot be disabled in a natural way
   programmatically so in this hack we replace the global __umr__ instance
   with a new one containing the module we want to exclude. This will do
   nothing if Spyder is not found.
   TODO is there a better way to detect if we are in spyder?


.. py:function:: attribute_set_to(object_: Any, attribute_name: str, new_value: Any)

   This context manager allows to change a given attribute of a given object
   to a new value, and the original value is reverted upon exit of the context
   manager.

   Args:
       object_
           The object which attribute value is to be changed
       attribute_name
           The name of the attribute that is to be changed
       new_value
           The new value to which the attribute of the object is to be changed


.. py:function:: partial_with_docstring(func, docstring, **kwargs)

   We want to have a partial function which will allow us access the docstring
   through the python built-in help function. This is particularly important
   for client-facing driver methods, whose arguments might not be obvious.

   Consider the follow example why this is needed:

   >>> from functools import partial
   >>> def f():
   >>> ... pass
   >>> g = partial(f)
   >>> g.__doc__ = "bla"
   >>> help(g) # this will print an unhelpful message

   Args:
       func (callable)
       docstring (str)


