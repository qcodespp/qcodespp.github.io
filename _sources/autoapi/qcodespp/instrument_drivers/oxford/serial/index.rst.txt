qcodespp.instrument_drivers.oxford.serial
=========================================

.. py:module:: qcodespp.instrument_drivers.oxford.serial

.. autoapi-nested-parse::

   Serial instrument driver based on pyserial.


   Exists in qcodes++ solely to support an old Oxford MercuryiPS. All new drivers should be based on VisaInstrument or just Instrument.



Classes
-------

.. autosummary::

   qcodespp.instrument_drivers.oxford.serial.SerialInstrument


Module Contents
---------------

.. py:class:: SerialInstrument(name, address=None, baudrate=9600, timeout=5, stopbits=1, terminator='', **kwargs)

   Bases: :py:obj:`qcodes.Instrument`


   Base class for all QCodes instruments.

   Args:
       name: an identifier for this instrument, particularly for
           attaching it to a Station.
       metadata: additional static metadata to add to this
           instrument's JSON snapshot.
       label: nicely formatted name of the instrument; if None, the
           ``name`` is used.



   .. py:method:: default_server_name(**kwargs)
      :classmethod:



   .. py:method:: set_address(address)

      Change the address for this instrument.

      Args:
          address: The visa resource name to use to connect.
              Optionally includes '@<backend>' at the end. For example,
              'ASRL2' will open COM2 with the default NI backend, but
              'ASRL2@py' will open COM2 using pyvisa-py. Note that qcodes
              does not install (or even require) ANY backends, it is up to
              the user to do that.
              see eg: http://pyvisa.readthedocs.org/en/stable/names.html



   .. py:method:: set_timeout(timeout=None)

      Change the read timeout for the socket.

      Args:
          timeout (number): Seconds to allow for responses.



   .. py:method:: set_terminator(terminator)

              Change the read terminator to use.

              Args:
                  terminator (str): Character(s) to look for at the end of a read.
                      eg. '
      '.
              



   .. py:method:: close()

      Disconnect and irreversibly tear down the instrument.



   .. py:method:: write(cmd)

      Write a command string with NO response to the hardware.

      Subclasses that transform ``cmd`` should override this method, and in
      it call ``super().write(new_cmd)``. Subclasses that define a new
      hardware communication should instead override ``write_raw``.

      Args:
          cmd (str): the string to send to the instrument

      Raises:
          Exception: wraps any underlying exception with extra context,
              including the command and the instrument.



   .. py:method:: write_raw(cmd)

      Low-level interface to ``serial_handle.write``.

      Args:
          cmd (str): The command to send to the instrument.



   .. py:method:: read_raw(size=200)


   .. py:method:: read()


   .. py:method:: read_until(retry=True)


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




   .. py:method:: ask_raw(cmd)

      Low-level interface to ``serial_handle.ask``.

      Args:
          cmd (str): The command to send to the instrument.

      Returns:
          str: The instrument's response.



   .. py:method:: snapshot_base(update=False)

      State of the instrument as a JSON-compatible dict.

      Args:
          update (bool): If True, update the state by querying the
              instrument. If False, just use the latest values in memory.

      Returns:
          dict: base snapshot



