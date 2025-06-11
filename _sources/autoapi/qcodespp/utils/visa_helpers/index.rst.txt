qcodespp.utils.visa_helpers
===========================

.. py:module:: qcodespp.utils.visa_helpers


Functions
---------

.. autoapisummary::

   qcodespp.utils.visa_helpers.listVISAinstruments


Module Contents
---------------

.. py:function:: listVISAinstruments(baudrates='qdac')

   List the VISA instruments connected to the computer. Deault baudrates checked are 9600 and 921600.

   Args:
       baudrates (int, str, list): The baudrate(s) to check for the instruments.
           - If an integer, it will check only that baudrate.
           - If a string, it can be 'qdac', 'standard', or 'all' to use predefined baudrate lists.
           - If a list, it should contain integers representing the baudrates to check.
   Returns:
       None: Prints the list of instruments and their identification strings.

   Details:
       If you are expecting instrument(s), e.g. QDAC, to communicate with a baudrate other than 9600,
       you can include the possible baudrates when calling the function. By default it also checks for the
       baudrate used by the qdac. If you want to check other baudrates, include them explicitly as a list,
       or use predefined lists 'standard' or 'all', with baudrates defined according the National Instruments standards.


