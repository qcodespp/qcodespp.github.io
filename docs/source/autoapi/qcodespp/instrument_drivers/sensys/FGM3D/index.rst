qcodespp.instrument_drivers.sensys.FGM3D
========================================

.. py:module:: qcodespp.instrument_drivers.sensys.FGM3D


Attributes
----------

.. autosummary::

   qcodespp.instrument_drivers.sensys.FGM3D.log


Classes
-------

.. autosummary::

   qcodespp.instrument_drivers.sensys.FGM3D.FGM3D
   qcodespp.instrument_drivers.sensys.FGM3D.FGM3D_Parameter


Module Contents
---------------

.. py:data:: log

.. py:class:: FGM3D(name, address, baudrate=400000, unit='T', timeout=2, **kwargs)

   Bases: :py:obj:`qcodes.Instrument`


   QCoDeS driver to capture data stream from a Sensys FGM3D TD digitzer application

   The driver does not communicate directly with the instrument; it is only capable of 
   reading the data stream sent from the 'Live Streaming' section of the GUI. You must
   set up a virtual COM port pair using e.g. com0com. Enable 'use Ports class', 'emulate 
   baud rate', 'enable buffer overrun' and 'enable exclusive mode'. Specify the first 
   port in the GUI, and the second port in this driver.

   The units cannot be read from the instrument; if using Gauss, specify this during init.

   Args:
       name (str): qcodes name for this instrument instance
       address (str): COM port identifier of the virtual COM port pair
       baudrate (int): match the baudrate in the GUI
       unit (str): Units as selected in the GUI
       timeout (float): timeout for collecting a measurement


   .. py:attribute:: ind_dict


   .. py:attribute:: terminator
      :value: Multiline-String

      .. raw:: html

         <details><summary>Show Value</summary>

      .. code-block:: python

         """
         """

      .. raw:: html

         </details>




   .. py:attribute:: address


   .. py:attribute:: unit
      :value: 'T'



   .. py:attribute:: timeout
      :value: 2



   .. py:attribute:: baudrate
      :value: 400000



   .. py:attribute:: ser


   .. py:attribute:: data


   .. py:method:: reset()

      Close and reopen the serial stream



   .. py:method:: close()

      Disconnect and irreversibly tear down the instrument.



   .. py:method:: get_idn()

      Parse a standard VISA ``*IDN?`` response into an ID dict.

      Even though this is the VISA standard, it applies to various other
      types as well, such as IPInstruments, so it is included here in the
      Instrument base class.

      Override this if your instrument does not support ``*IDN?`` or
      returns a nonstandard IDN string. This string is supposed to be a
      comma-separated list of vendor, model, serial, and firmware, but
      semicolon and colon are also common separators so we accept them here
      as well.

      Returns:
          A dict containing vendor, model, serial, and firmware.




   .. py:method:: get_all_data()

      Get all data currently in the serial buffer. Returns a list of tuples (t,x,y,z,r)



.. py:class:: FGM3D_Parameter(name, unit, instrument, **kwargs)

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



   .. py:method:: get_raw()

      ``get_raw`` is called to perform the actual data acquisition from the
      instrument. This method should either be overwritten to perform the
      desired operation or alternatively for :class:`.Parameter` a
      suitable method is automatically generated if ``get_cmd`` is supplied
      to the parameter constructor. The method is automatically wrapped to
      provide a ``get`` method on the parameter instance.



