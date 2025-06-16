qcodespp.instrument_drivers.oxford.triton
=========================================

.. py:module:: qcodespp.instrument_drivers.oxford.triton


Classes
-------

.. autosummary::

   qcodespp.instrument_drivers.oxford.triton.Triton


Module Contents
---------------

.. py:class:: Triton(name, address=None, port=None, terminator='\r\n', tmpfile=None, timeout=20, **kwargs)

   Bases: :py:obj:`qcodes.IPInstrument`


   Triton Driver

   Args:
       tmpfile: Optional: an exported windows registry file from the registry
           path:
           `[HKEY_CURRENT_USER\Software\Oxford Instruments\Triton System Control\Thermometry]`
           and is used to extract the available temperature channels.


   Status: beta-version.
       TODO:
       fetch registry directly from fridge-computer


   .. py:attribute:: chan_alias


   .. py:attribute:: chan_temp_names


   .. py:method:: set_B(x, y, z, s)


   .. py:method:: get_idn()

      Return the Instrument Identifier Message 



