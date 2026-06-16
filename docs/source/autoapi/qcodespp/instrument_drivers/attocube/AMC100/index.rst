qcodespp.instrument_drivers.attocube.AMC100
===========================================

.. py:module:: qcodespp.instrument_drivers.attocube.AMC100

.. autoapi-nested-parse::

   qcodespp driver for Attodube AMC1XX instruments.
   In contrast to the qcodes_contrib_drivers driver, it assumes 
   the user has installed the attocube AMC-APIs as a package.



Classes
-------

.. autosummary::

   qcodespp.instrument_drivers.attocube.AMC100.MultiAxisPosition
   qcodespp.instrument_drivers.attocube.AMC100.MultiAxisPositionParameter
   qcodespp.instrument_drivers.attocube.AMC100.AMC100Axis
   qcodespp.instrument_drivers.attocube.AMC100.AttocubeAMC100


Module Contents
---------------

.. py:class:: MultiAxisPosition

   Bases: :py:obj:`collections.abc.Sequence`\ [\ :py:obj:`float`\ ]


   A tuple-like representation of (a subset of) axis positions.

   Use this class to set any number of positions simultaneously using
   :attr:`AttocubeAMC100.multi_axis_position`.


   .. py:attribute:: axis_1
      :type:  float


   .. py:attribute:: axis_2
      :type:  float


   .. py:attribute:: axis_3
      :type:  float


   .. py:method:: __getitem__(index: int, /) -> float
                  __getitem__(index: slice, /) -> collections.abc.Sequence[float]


   .. py:method:: __len__() -> int


.. py:class:: MultiAxisPositionParameter(name: str, *args: Any, names: collections.abc.Sequence[str] = _NAMES_UNSET, shapes: collections.abc.Sequence[collections.abc.Sequence[int]] = _SHAPES_UNSET, instrument: qcodes.parameters.parameter_base.InstrumentTypeVar_co = None, labels: collections.abc.Sequence[str] | None = None, units: collections.abc.Sequence[str] | None = None, setpoints: collections.abc.Sequence[collections.abc.Sequence[Any]] | None = None, setpoint_names: collections.abc.Sequence[collections.abc.Sequence[str]] | None = None, setpoint_labels: collections.abc.Sequence[collections.abc.Sequence[str]] | None = None, setpoint_units: collections.abc.Sequence[collections.abc.Sequence[str]] | None = None, docstring: str | None = None, snapshot_get: bool = True, snapshot_value: bool = False, snapshot_exclude: bool = False, metadata: collections.abc.Mapping[Any, Any] | None = None, **kwargs: Any)

   Bases: :py:obj:`qcodes.parameters.MultiParameter`


   A parameter that simulatenously sets multiple axis positions.

   Always returns all three axes, but accepts a variable number for
   setting. The following are allowed for the single value argument:

    - an instance of :class:`MultiAxisPosition`
    - a mapping with possible keys ``axis_1``, ``axis_2``, ``axis_3``
      and float values
    - a sequence of floats which will be interpreted as
      `(axis_1, axis_2, ...)`



   .. py:method:: get_raw() -> qcodes.parameters.ParamRawDataType

      ``get_raw`` is called to perform the actual data acquisition from the
      instrument. This method should either be overwritten to perform the
      desired operation or alternatively for :class:`.Parameter` a
      suitable method is automatically generated if ``get_cmd`` is supplied
      to the parameter constructor. The method is automatically wrapped to
      provide a ``get`` method on the parameter instance.



   .. py:method:: set_raw(value: qcodes.parameters.ParamRawDataType) -> None

      ``set_raw`` is called to perform the actual setting of a parameter on
      the instrument. This method should either be overwritten to perform the
      desired operation or alternatively for :class:`.Parameter` a
      suitable method is automatically generated if ``set_cmd`` is supplied
      to the parameter constructor. The method is automatically wrapped to
      provide a ``set`` method on the parameter instance.



.. py:class:: AMC100Axis(parent: AttocubeAMC100, name: str, axis: int, label: str | None = None, **kwargs: Any)

   Bases: :py:obj:`qcodes.instrument.InstrumentChannel`


   Base class for a module in an instrument.
   This could be in the form of a channel (e.g. something that
   the instrument has multiple instances of) or another logical grouping
   of parameters that you wish to group together separate from the rest of the
   instrument.

   Args:
       parent: The instrument to which this module should be
         attached.
       name: The name of this module.
       **kwargs: Forwarded to the base class.



   .. py:attribute:: actor_type


   .. py:attribute:: open_loop_status


   .. py:attribute:: reference_position_valid


   .. py:attribute:: reference_position


   .. py:attribute:: position


   .. py:attribute:: frequency


   .. py:attribute:: amplitude


   .. py:attribute:: output


   .. py:method:: move_to_reference_position()

      This function starts an approach to the reference position.

      A running motion command is aborted; closed loop moving is
      switched on. Requires a valid reference position.



   .. py:method:: single_step(backward: bool)

      This function triggers one step on the selected axis in
      desired direction.

      Parameters
      ----------
      backward : Selects the desired direction. False triggers a
          forward step, true a backward step.



.. py:class:: AttocubeAMC100(name: str, address: str | None = None, axis_labels: collections.abc.Sequence[str] = (), **kwargs: Any)

   Bases: :py:obj:`qcodes.instrument.Instrument`


   Driver for the AMC100 position controller.


   .. py:attribute:: device


   .. py:method:: all_on() -> None


   .. py:method:: all_off() -> None


   .. py:property:: exception_type
      :type: Exception



   .. py:method:: close()

      Irreversibly stop this instrument and free its resources.

      Subclasses should override this if they have other specific
      resources to close.



   .. py:method:: get_idn() -> dict[str, str | None]

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




