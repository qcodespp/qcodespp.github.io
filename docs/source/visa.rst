Connecting to actual instruments
================================

The vast majority of scientific instruments communicate via the VISA protocol, whether it's over GPIB, USB, RS232, or Ethernet. Assuming you've installed a National Instruments or Keysight backend to handle VISA, qcodes++ deals with connecting to VISA instruments in a very uniform way. To find out which VISA instruments are attached to your computer, use:

.. code-block:: python

    import qcodespp as qc
    qc.listVISAinstruments()

The output should look something like this::

    Instrument IDN: KEITHLEY INSTRUMENTS,MODEL 2450,04613345,1.7.12b
    VISA Address: TCPIP0::169.254.100.202::inst0::INSTR

    Instrument IDN: KEITHLEY INSTRUMENTS,MODEL 2450,02613340,1.7.12b
    VISA Address: GPIB0::12::INSTR

    Instrument IDN: QDevil, QDAC-II, 159, 13-1.57
    VISA Address: ASRL9::INSTR 

There are three instruments attached to the computer: two Keithley 2450 Source Meters, one over TCP/IP and one over GPIB, and a QDevil QDAC-II over USB/serial (ASRL). To connect to these instruments in our notebook, we first, import the relevant drivers, then create instrument objects from the drivers, using the addresses printed by ``listVISAinstruments()``.

.. code-block:: python

    from qcodespp.instrument_drivers.QDevil.QDAC2 import QDac2
    from qcodespp.instrument_drivers.tektronix.Keithley_2450 import Keithley_2450

    k1 = Keithley_2450('k1','TCPIP0::169.254.100.202::inst0::INSTR')
    k2 = Keithley_2450('k2','GPIB0::16::INSTR')
    qdac = QDac2('qdac','ASRL9::INSTR')

The process is the same no matter the instrument, or connection type, as long as it's a VISA instrument. There are some instruments that don't use VISA. Naturally, they will not show up when using ``listVISAinstruments()``, and may require a different syntax to connect to them. Check out the relevant documentation or source code.

Where are the drivers?
----------------------

There are three possible sources for pre-existing instrument drivers; `qcodes++ <https://qcodespp.github.io/autoapi/qcodespp/instrument_drivers/index.html>`__, `QCoDeS <https://microsoft.github.io/Qcodes/drivers_api/index.html>`__ and `qcodes_contrib_drivers <https://qcodes.github.io/Qcodes_contrib_drivers/index.html>`__. Look through the instruments available at those links to find the one you're looking for. If you don't have the qcodes_contrib_drivers package installed, you can install it with::

    pip install qcodes_contrib_drivers

Then import the driver you need:

.. code-block:: python

    from qcodespp.instrument_drivers.QDevil.QDAC2 import QDac2
    from qcodes.instrument_drivers.Keithley import Keithley2400
    from qcodes_contrib_drivers.drivers.Tektronix.AWG520 import Tektronix_AWG520

All these drivers will work perfectly fine with qcodes++ despite coming from different sources.

How do I know which features an instrument has?
-----------------------------------------------

There are many ways! If you kind of know what you're looking for, hit the tab key after typing the instrument name, e.g. ``k2600.`` and it will show you all the available functions of the instrument. Many of those functions will either be Parameters or Submodules. Submodules are typically used to represent the channels of an instrument. For example, the Keithley 2600 Source Meters have two channels. In the qcodes driver, these are named ``smua`` and ``smub``. Each of these submodules have various parameters, including ``volt``, ``curr``, etc. Therefore reading the voltage on Channel A is done with ``k2600.smua.volt()``

You can list the Parameters of the instrument by running:

.. code-block:: python

    instrument.parameters

and the SubModules by running:

.. code-block:: python

    instrument.submodules

and of course the Parameters of any submodule by:

.. code-block:: python

    instrument.channel01.parameters

To get the entire 'picture' of the current state of the instrument, you can use the ``instrument.snapshot()`` function.

However, eventually you will be better off either reading the API for the driver or the source code, likely in combination with the instrument's manual. It's painful, I know, but it's still better than writing your own driver ;)

Writing your own driver
-----------------------

If you can't find a driver for your instrument from any of the above sources, you will need to write your own, following the instructions at `qcodes_contrib_drivers <https://qcodes.github.io/Qcodes_contrib_drivers/index.html>`__. 