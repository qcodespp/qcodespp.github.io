Connecting to actual instruments
================================

By far, most instruments communicate via the VISA protocol, whether it's over GPIB, USB, RS232, or Ethernet. Luckily, you don't need to know the details of how VISA works, as qcodes++ takes care of that for you. All you need to do is install the VISA backend, which is usually done by installing the NI-VISA software from the National Instruments website. When that's all working, run:

.. code-block:: python

    import qcodespp as qc
    qc.listVISAinstruments()

and the code will print a list of all the VISA instruments connected to your computer. It should looks something like this:

You can then connect to the instrument by importing the relevant driver and creating an instance of the instrument class. For example, if you have a Keithley 2600 Source Meter, you would do: