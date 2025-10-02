qcodespp.instrument_drivers.instrument_mocks
============================================

.. py:module:: qcodespp.instrument_drivers.instrument_mocks


Attributes
----------

.. autosummary::

   qcodespp.instrument_drivers.instrument_mocks.log


Classes
-------

.. autosummary::

   qcodespp.instrument_drivers.instrument_mocks.MockParabola
   qcodespp.instrument_drivers.instrument_mocks.MockMetaParabola
   qcodespp.instrument_drivers.instrument_mocks.DummyInstrument
   qcodespp.instrument_drivers.instrument_mocks.DummyMeasurementInstrument
   qcodespp.instrument_drivers.instrument_mocks.DummyChannel
   qcodespp.instrument_drivers.instrument_mocks.DummyChannelInstrument
   qcodespp.instrument_drivers.instrument_mocks.MultiGetter
   qcodespp.instrument_drivers.instrument_mocks.MultiSetPointParam
   qcodespp.instrument_drivers.instrument_mocks.Multi2DSetPointParam
   qcodespp.instrument_drivers.instrument_mocks.MultiScalarParam
   qcodespp.instrument_drivers.instrument_mocks.ArraySetPointParam


Functions
---------

.. autosummary::

   qcodespp.instrument_drivers.instrument_mocks.setpoint_generator


Module Contents
---------------

.. py:data:: log

.. py:class:: MockParabola(name, **kw)

   Bases: :py:obj:`qcodes.Instrument`


   Holds dummy parameters which are get and set able as well as provides
   some basic functions that depends on these parameters for testing
   purposes.

   This instrument is intended to be simpler than the mock model in that it
   does not emulate communications.

   It has 3 main parameters (x, y, z) in order to allow for testing of 3D
   sweeps. The function (parabola with optional noise) is chosen to allow
   testing of numerical optimizations.


.. py:class:: MockMetaParabola(name, mock_parabola_inst, **kw)

   Bases: :py:obj:`qcodes.Instrument`


   Test for a meta instrument, has a tunable gain knob


   .. py:attribute:: mock_parabola_inst


.. py:class:: DummyInstrument(name='dummy', gates=['dac1', 'dac2'], **kwargs)

   Bases: :py:obj:`qcodes.Instrument`


   Base class for all QCodes instruments.

   Args:
       name: an identifier for this instrument, particularly for
           attaching it to a Station.
       metadata: additional static metadata to add to this
           instrument's JSON snapshot.
       label: nicely formatted name of the instrument; if None, the
           ``name`` is used.



.. py:class:: DummyMeasurementInstrument(name: str, **kwargs)

   Bases: :py:obj:`qcodes.Instrument`


   Base class for all QCodes instruments.

   Args:
       name: an identifier for this instrument, particularly for
           attaching it to a Station.
       metadata: additional static metadata to add to this
           instrument's JSON snapshot.
       label: nicely formatted name of the instrument; if None, the
           ``name`` is used.



   .. py:method:: get_linear()


   .. py:method:: get_para()


   .. py:method:: ask(cmd)

      Write a command string to the hardware and return a response.

      Subclasses that transform ``cmd`` should override this method, and in
      it call ``super().ask(new_cmd)``. Subclasses that define a new
      hardware communication should instead override ``ask_raw``.

      Args:
          cmd: The string to send to the instrument.

      Returns:
          response

      Raises:
          Exception: Wraps any underlying exception with extra context,
              including the command and the instrument.




.. py:class:: DummyChannel(parent, name, channel)

   Bases: :py:obj:`qcodes.instrument.InstrumentChannel`


   A single dummy channel implementation


.. py:class:: DummyChannelInstrument(name, **kwargs)

   Bases: :py:obj:`qcodes.Instrument`


   Dummy instrument with channels


.. py:class:: MultiGetter(**kwargs)

   Bases: :py:obj:`qcodes.parameters.MultiParameter`


   Test parameters with complicated return values
   instantiate with kwargs::

       MultiGetter(name1=return_val1, name2=return_val2)

   to set the names and (constant) return values of the
   pieces returned. Each return_val can be any array-like
   object
   eg::

       MultiGetter(one=1, onetwo=(1, 2))



   .. py:method:: get_raw()

      ``get_raw`` is called to perform the actual data acquisition from the
      instrument. This method should either be overwritten to perform the
      desired operation or alternatively for :class:`.Parameter` a
      suitable method is automatically generated if ``get_cmd`` is supplied
      to the parameter constructor. The method is automatically wrapped to
      provide a ``get`` method on the parameter instance.



.. py:class:: MultiSetPointParam(instrument=None, name='testparameter')

   Bases: :py:obj:`qcodes.parameters.MultiParameter`


   Multiparameter which only purpose it to test that units, setpoints
   and so on are copied correctly to the individual arrays in the datarray.


   .. py:method:: get_raw()

      ``get_raw`` is called to perform the actual data acquisition from the
      instrument. This method should either be overwritten to perform the
      desired operation or alternatively for :class:`.Parameter` a
      suitable method is automatically generated if ``get_cmd`` is supplied
      to the parameter constructor. The method is automatically wrapped to
      provide a ``get`` method on the parameter instance.



.. py:class:: Multi2DSetPointParam(instrument=None, name='testparameter')

   Bases: :py:obj:`qcodes.parameters.MultiParameter`


   Multiparameter which only purpose it to test that units, setpoints
   and so on are copied correctly to the individual arrays in the datarray.


   .. py:method:: get_raw()

      ``get_raw`` is called to perform the actual data acquisition from the
      instrument. This method should either be overwritten to perform the
      desired operation or alternatively for :class:`.Parameter` a
      suitable method is automatically generated if ``get_cmd`` is supplied
      to the parameter constructor. The method is automatically wrapped to
      provide a ``get`` method on the parameter instance.



.. py:class:: MultiScalarParam(instrument=None, name='multiscalarparameter')

   Bases: :py:obj:`qcodes.parameters.MultiParameter`


   Multiparameter whos elements are scalars i.e. similar to
   Parameter with no setpoints etc.


   .. py:method:: get_raw()

      ``get_raw`` is called to perform the actual data acquisition from the
      instrument. This method should either be overwritten to perform the
      desired operation or alternatively for :class:`.Parameter` a
      suitable method is automatically generated if ``get_cmd`` is supplied
      to the parameter constructor. The method is automatically wrapped to
      provide a ``get`` method on the parameter instance.



.. py:class:: ArraySetPointParam(instrument=None, name='testparameter')

   Bases: :py:obj:`qcodes.parameters.ArrayParameter`


   Arrayparameter which only purpose it to test that units, setpoints
   and so on are copied correctly to the individual arrays in the datarray.


   .. py:method:: get_raw()

      ``get_raw`` is called to perform the actual data acquisition from the
      instrument. This method should either be overwritten to perform the
      desired operation or alternatively for :class:`.Parameter` a
      suitable method is automatically generated if ``get_cmd`` is supplied
      to the parameter constructor. The method is automatically wrapped to
      provide a ``get`` method on the parameter instance.



.. py:function:: setpoint_generator(*sp_bases)

   Helper function to generate setpoints in the format that ArrayParameter
   (and MultiParameter) expects

   Args:
       *sp_bases:

   Returns:



