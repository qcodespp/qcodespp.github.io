Getting started with qcodes++
=============================

Qcodes++ is a python-based package for collecting data covering the core aspects
generally required to run an experiment:

1)	Drivers for setting and reading parameters from instruments
2)	A framework for the storage and organization of data
3)  Loops, i.e. step-wise increment an independent parameter (e.g. a voltage)

This means that one can vary an independent parameter, measure all dependent parameters, and store these
data in a well-organised format. This is pretty much all one ever does in science. Live plotting of the
data is included, as well as offline analysis and plotting capabilities.

The below graphic gives a rough conceptualisation of qcodes++ structure. The Station contains Instruments,
which each contain various Parameters that can be measured and/or set. Parameters can be scaled, combined
in any way and defined without instruments (e.g. time). The Data Set defines the independent parameter’s
setpoints as a Loop, and collects measurements of the desired dependent parameters from Station. Station
also sends important metadata to the DataSet. Two options for plotting are available: live plotting, which is
very fast and allows you to see the data as it is being collected, and offline plotting, which allows you to
view the data after it has been collected, and to perform more complex analysis.

In addition to the Loop, qcodes++ also has a Measure function, which simply measures a set of parameters
at a single point in time, without looping.

The features of qcodes++ are mostly either directly inherited from the latest version of QCoDeS, or are 
improved versions of features that were present in QCoDeS prior to version 0.11. In particular, qcodes++
uses the text-based DataSetPP, which although much less flexible than the QCoDeS DataSet, is much more
user-friendly, especially when combined with the Loop and Measure functions. And indeed the limitations
imposed by the DataSetPP enables the really excellent plotting capabilities developed by Merlin von Soosten,
Joeri de Bruijke, Dags Olsteins and others.

In short; if you want a user-friendly way to collect and plot data, use qcodes++. If you need something
highly customisable, use QCoDeS. The good news; installing qcodes++ does not interfere with a QCoDeS
installation, and in fact requires it; this means you can use the best of both worlds!