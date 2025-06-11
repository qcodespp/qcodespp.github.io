qcodespp.instrument_drivers.Lakeshore.Model_340
===============================================

.. py:module:: qcodespp.instrument_drivers.Lakeshore.Model_340


Classes
-------

.. autoapisummary::

   qcodespp.instrument_drivers.Lakeshore.Model_340.Model_340_Curve
   qcodespp.instrument_drivers.Lakeshore.Model_340.Model_340_Sensor
   qcodespp.instrument_drivers.Lakeshore.Model_340.Model_340_Heater
   qcodespp.instrument_drivers.Lakeshore.Model_340.Model_340


Module Contents
---------------

.. py:class:: Model_340_Curve(parent: Model_340, index: int)

   Bases: :py:obj:`qcodes.InstrumentChannel`


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



   .. py:attribute:: valid_sensor_units
      :value: ['mV', 'V', 'Ohm', 'log Ohm']



   .. py:attribute:: temperature_key
      :value: 'Temperature (K)'



   .. py:method:: get_data() -> dict


   .. py:method:: validate_datadict(data_dict: dict) -> str
      :classmethod:


      A data dict has two keys, one of which is 'Temperature (K)'. The other
      contains the units in which the curve is defined and must be one of:
      'mV', 'V', 'Ohm' or 'log Ohm'

      This method validates this and returns the sensor unit encountered in
      the data dict



   .. py:method:: set_data(data_dict: dict, sensor_unit: str = None) -> None

      Set the curve data according to the values found the the dictionary.

      Args:
          data_dict (dict): See `validate_datadict` to see the format of this
                              dictionary
          sensor_unit (str): If None, the data dict is validated and the
                              units are extracted.



.. py:class:: Model_340_Sensor(parent: Model_340, name: str, inp: str)

   Bases: :py:obj:`qcodes.InstrumentChannel`


   A single sensor of a  Lakeshore 340.

   Args:
       parent (Model_340): The instrument this heater belongs to
       name (str)
       inp (str): One of 'A', 'B', 'C1','C2','C3','C4','D1','D2'


   .. py:attribute:: sensor_status_codes


   .. py:method:: decode_sensor_status(sum_of_codes: int) -> str

      The sensor status is one of the status codes, or a sum thereof. Multiple
      status are possible as they are not necessarily mutually exclusive.

      args:
          sum_of_codes (int)



   .. py:property:: curve
      :type: Model_340_Curve



.. py:class:: Model_340_Heater(parent: Model_340, name: str, loop: int)

   Bases: :py:obj:`qcodes.InstrumentChannel`


   Heater control for the Lakeshore 340.

   Args:
       parent (Model_340): The instrument this heater belongs to
       name (str)
       loop (int): Either 1 or 2


.. py:class:: Model_340(name: str, address: str, channel_names=['A', 'B', 'C1', 'C2', 'C3', 'C4', 'D1', 'D2'], **kwargs)

   Bases: :py:obj:`qcodes.VisaInstrument`


   Lakeshore Model 340 Temperature Controller Driver


   .. py:method:: upload_curve(index: int, name: str, serial_number: str, data_dict: dict) -> None

      Upload a curve to the given index

      Args:
           index (int): The index to upload the curve to. We can only use
                          indices reserved for user defined curves, 21-35
           name (str)
           serial_number (str)
           data_dict (dict): A dictionary containing the curve data



