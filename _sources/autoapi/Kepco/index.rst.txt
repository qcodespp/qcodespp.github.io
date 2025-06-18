Kepco
=====

.. py:module:: Kepco


Classes
-------

.. autosummary::

   Kepco.KepcoMagnet


Module Contents
---------------

.. py:class:: KepcoMagnet(name, parameter, max_field, volt_to_amp, field_to_amp, axis, rate=0.15, **kwargs)

   Bases: :py:obj:`qcodes.Instrument`


   Base class for all QCodes instruments.

   Args:
       name: an identifier for this instrument, particularly for
           attaching it to a Station.
       metadata: additional static metadata to add to this
           instrument's JSON snapshot.
       label: nicely formatted name of the instrument; if None, the
           ``name`` is used.



   .. py:attribute:: MAX_AMP
      :value: 20


      This is the qcodes driver for controlling the magnetic field through the Kepco BOP 20-20M.
      It will control an external voltage source, in order to convert it into a current, used to control the Mercury magnet.

      Args
          name (str) =  the name of the instruemnt.
          
          parameter = a settable parameter controlling the voltage source.
          
          max_field = maximum magnetic field allowed
          
          volt_to_amp = conversion factor from Volt to Ampere.

          field_to_amp = converion factor from Tesla to Ampere.
          
          axis (str) = controlled magnetic axis.
          
          rate = maximum sweeping rate allowed (in Tesla)
          
          MAX_AMP = maximum current that Kepco can hndle in Ampere (model dependent).
          
      This is a virtual driver only and will not talk to your instrument.
       



   .. py:attribute:: v1


   .. py:attribute:: max_field


   .. py:attribute:: volt_to_amp


   .. py:attribute:: field_to_amp


   .. py:attribute:: axis


   .. py:attribute:: rate
      :value: 0.15



   .. py:method:: set_field(value: Union[int, float]) -> None

      Independently from the voltage power supply, the set_val will sweep this instrument and will not jump.



   .. py:method:: get_field() -> Union[int, float]

      Returns:
          number: value at which was set at the sample



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




