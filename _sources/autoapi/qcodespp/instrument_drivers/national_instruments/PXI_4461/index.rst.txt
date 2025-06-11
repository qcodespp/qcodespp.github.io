qcodespp.instrument_drivers.national_instruments.PXI_4461
=========================================================

.. py:module:: qcodespp.instrument_drivers.national_instruments.PXI_4461


Attributes
----------

.. autoapisummary::

   qcodespp.instrument_drivers.national_instruments.PXI_4461.p


Classes
-------

.. autoapisummary::

   qcodespp.instrument_drivers.national_instruments.PXI_4461.ParameterArray
   qcodespp.instrument_drivers.national_instruments.PXI_4461.AITask
   qcodespp.instrument_drivers.national_instruments.PXI_4461.AOTask
   qcodespp.instrument_drivers.national_instruments.PXI_4461.PXI_4461


Module Contents
---------------

.. py:class:: ParameterArray(name, instrument, names, get_cmd=None, set_cmd=None, units=None, **kwargs)

   Bases: :py:obj:`qcodes.MultiParameter`


   A gettable parameter that returns multiple values with separate names,
   each of arbitrary shape. Not necessarily part of an instrument.

   Subclasses should define a ``.get_raw`` method, which returns a sequence of
   values. This method is automatically wrapped to provide a ``.get`` method.
   When used in a legacy  method``Loop`` or ``Measure`` operation, each of
   these values will be entered into a different ``DataArray``. The
   constructor args describe what data we expect from each ``.get`` call
   and how it should be handled. ``.get`` should always return the same
   number of items, and most of the constructor arguments should be tuples
   of that same length.

   For now you must specify upfront the array shape of each item returned by
   ``.get_raw``, and this cannot change from one call to the next. Later, we
   intend to require only that you specify the dimension of each item
   returned, and the size of each dimension can vary from call to call.

   Args:
       name: The local name of the whole parameter. Should be a valid
           identifier, ie no spaces or special characters. If this parameter
           is part of an Instrument or Station, this is how it will be
           referenced from that parent, i.e. ``instrument.name`` or
           ``instrument.parameters[name]``.

       names: A name for each item returned by a ``.get``
           call. Will be used as the basis of the ``DataArray`` names
           when this parameter is used to create a ``DataSet``.

       shapes: The shape (as used in numpy arrays) of
           each item. Scalars should be denoted by (), 1D arrays as (n,),
           2D arrays as (n, m), etc.

       instrument: The instrument this parameter
           belongs to, if any.

       labels: A label for each item. Normally used
           as the axis label when a component is graphed, along with the
           matching entry from ``units``.

       units: A unit of measure for each item.
           Use ``''`` or ``None`` for unitless values.

       setpoints: ``array`` can be a DataArray, numpy.ndarray, or sequence.
           The setpoints for each returned array. An N-dimension item should
           have N setpoint arrays, where the first is 1D, the second 2D, etc.
           If omitted for any or all items, defaults to integers from zero in
           each respective direction.
           **Note**: if the setpoints will be different each measurement,
           leave this out and return the setpoints (with extra names) in
           ``.get``.

       setpoint_names: One identifier (like
           ``name``) per setpoint array. Ignored if a setpoint is a
           DataArray, which already has a name.

       setpoint_labels: One label (like
           ``labels``) per setpoint array. Ignored if a setpoint is a
           DataArray, which already has a label.

       setpoint_units: One unit (like
           ``V``) per setpoint array. Ignored if a setpoint is a
           DataArray, which already has a unit.

       docstring: Documentation string for the ``__doc__``
           field of the object. The ``__doc__`` field of the  instance is
           used by some help systems, but not all

       snapshot_get: Prevent any update to the parameter, for example
           if it takes too long to update. Default ``True``.

       snapshot_value: Should the value of the parameter be stored in the
           snapshot. Unlike Parameter this defaults to False as
           MultiParameters are potentially huge.

       snapshot_exclude: True prevents parameter to be
           included in the snapshot. Useful if there are many of the same
           parameter which are clogging up the snapshot.
           Default ``False``.

       metadata: Extra information to include with the
           JSON snapshot of the parameter.



   .. py:attribute:: units
      :value: None



   .. py:method:: get()


   .. py:method:: set(setpoint)


.. py:class:: AITask(device, channels, time_constant=0.05, rate=100000.0)

   Bases: :py:obj:`PyDAQmx.Task`


   .. py:method:: configure()


   .. py:method:: input_range(value=None)


   .. py:method:: time_constant(value=None)


   .. py:method:: sample_rate(value=None)


   .. py:method:: create_ai_chan(chan, vrange=10, mode='diff')


   .. py:method:: read()


.. py:class:: AOTask(device, channels, rate=100000.0)

   Bases: :py:obj:`PyDAQmx.Task`


   .. py:method:: configure()


   .. py:method:: output_range(value=None)


   .. py:method:: sample_rate(value=None)


   .. py:method:: write_ch(ch, data)


   .. py:method:: write(data)


   .. py:method:: read(ch=None)


   .. py:method:: create_ao_chan(chan, vrange)


.. py:class:: PXI_4461(name, device, ai_channels=None, ao_channels=None)

   Bases: :py:obj:`qcodes.Instrument`


   Base class for all QCodes instruments.

   Args:
       name: an identifier for this instrument, particularly for
           attaching it to a Station.
       metadata: additional static metadata to add to this
           instrument's JSON snapshot.
       label: nicely formatted name of the instrument; if None, the
           ``name`` is used.



   .. py:attribute:: rate
      :value: 200000.0



   .. py:method:: __del__()

      Close the instrument and remove its instance record.



.. py:data:: p

