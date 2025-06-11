qcodespp.plotting.offline.fits
==============================

.. py:module:: qcodespp.plotting.offline.fits


Attributes
----------

.. autoapisummary::

   qcodespp.plotting.offline.fits.functions
   qcodespp.plotting.offline.fits.multipeak_description
   qcodespp.plotting.offline.fits.lorgaussform
   qcodespp.plotting.offline.fits.fourparamform
   qcodespp.plotting.offline.fits.fiveparamform
   qcodespp.plotting.offline.fits.thermaldescription
   qcodespp.plotting.offline.fits.stepdescription
   qcodespp.plotting.offline.fits.rectdescription


Functions
---------

.. autoapisummary::

   qcodespp.plotting.offline.fits.linear
   qcodespp.plotting.offline.fits.polynomial
   qcodespp.plotting.offline.fits.fit_powerlaw
   qcodespp.plotting.offline.fits.fit_exponentials
   qcodespp.plotting.offline.fits.fit_lorgausstype
   qcodespp.plotting.offline.fits.fit_voigttype
   qcodespp.plotting.offline.fits.fit_skewedpeaks
   qcodespp.plotting.offline.fits.fit_sines
   qcodespp.plotting.offline.fits.thermal_fit
   qcodespp.plotting.offline.fits.step_fit
   qcodespp.plotting.offline.fits.rectangle_fit
   qcodespp.plotting.offline.fits.expression_fit
   qcodespp.plotting.offline.fits.QD_fit
   qcodespp.plotting.offline.fits.FET_mobility
   qcodespp.plotting.offline.fits.dynes_fit
   qcodespp.plotting.offline.fits.ramsey_fit
   qcodespp.plotting.offline.fits.statistics
   qcodespp.plotting.offline.fits.get_class_names
   qcodespp.plotting.offline.fits.get_function
   qcodespp.plotting.offline.fits.get_names
   qcodespp.plotting.offline.fits.get_parameters
   qcodespp.plotting.offline.fits.get_description
   qcodespp.plotting.offline.fits.fit_data


Module Contents
---------------

.. py:function:: linear(xdata, ydata, p0=None, inputinfo=None)

   Fit a linear model to the data.
   Args:
       xdata: x data to fit
       ydata: y data to fit
       
       Initial guesses and inputinfo not used.
       
   Returns:
       result: lmfit result object.


.. py:function:: polynomial(xdata, ydata, p0=None, inputinfo=2)

   Fit a polynomial model to the data.
   Args:
       xdata: x data to fit
       ydata: y data to fit
       inputinfo (int): degree of the polynomial to fit. Default 2

       Initial guesses (p0) are not used.

   Returns:
       result: lmfit result object.


.. py:function:: fit_powerlaw(xdata, ydata, p0=None, inputinfo=[1, 0])

   Fit a power law model to the data.

   Args:
       xdata: x data to fit
       ydata: y data to fit
       p0 (opt.): initial guesses for the parameters. Should be a list of floats.
       inputinfo: a list containing the number of terms in the power law and whether to include a constant offset.
   Returns:
       result: lmfit result object.


.. py:function:: fit_exponentials(xdata, ydata, p0=None, inputinfo=[1, 0])

   Fit one or more exponential terms to the data, with or without a constant offset.

   Args:
       xdata: x data to fit
       ydata: y data to fit
       p0 (opt.): initial guesses for the parameters. Should be a list of floats.
       inputinfo: a list containing the number of terms in the exponential and whether to include a constant offset.

   Returns:
       result: lmfit result object.


.. py:function:: fit_lorgausstype(modeltype, xdata, ydata, p0=None, inputinfo=[1, 0])

   Fits x,y data with peaks characterised by amplitude, fwhm and position.

   Args:
       modeltype: lmfit model to use for fitting. Options are:
           LorentzianModel, GaussianModel, LognormalModel, StudentsTModel, DampedOscillatorModel
       xdata: x data to fit
       ydata: y data to fit
       p0 (opt.): initial guesses for the parameters. Should be a list of strings.
       inputinfo: a list containing the number of peaks to fit and whether to include a constant offset.
   Returns:
       result: lmfit result object.


.. py:function:: fit_voigttype(modeltype, xdata, ydata, p0=None, inputinfo=[1, 0])

   Fits x,y data with peaks characterised by amplitude, fwhm, position and gamma.

   Args:
       modeltype: lmfit model to use for fitting. Options are:
           VoigtModel, PseudoVoigtModel, BreitWignerModel, SplitLorentzianModel, ExponentialGaussianModel,
           SkewedGaussianModel, MoffatModel, Pearson7Model, DampedHarmonicOscillatorModel, DoniachModel
       xdata: x data to fit
       ydata: y data to fit
       p0 (opt.): initial guesses for the parameters. Should be a list of strings.
       inputinfo: a list containing the number of peaks to fit and whether to include a constant offset.

   Returns:
       result: lmfit result object.


.. py:function:: fit_skewedpeaks(modeltype, xdata, ydata, p0=None, inputinfo=[1, 0])

   Fits x,y data with peaks characterised by amplitude, fwhm, position, gamma and skew.
   Args:
       modeltype: lmfit model to use for fitting. Options are:
           Pearson4Model, SkewedVoigtModel
       xdata: x data to fit
       ydata: y data to fit
       p0 (opt.): initial guesses for the parameters. Should be a list of strings.
       inputinfo: a list containing the number of peaks to fit and whether to include a constant offset.
   Returns:
       result: lmfit result object.


.. py:function:: fit_sines(xdata, ydata, p0=None, inputinfo=[1, 0])

   Fits x,y data with multiple sine waves characterised by amplitude, frequency, phase and position.
   Args:
       xdata: x data to fit
       ydata: y data to fit
       p0 (opt.): initial guesses for the parameters. Should be a list of strings.
       inputinfo: a list containing the number of sine waves to fit and whether to include a constant offset.
   Returns:
       result: lmfit result object.


.. py:function:: thermal_fit(modeltype, xdata, ydata, p0=None, inputinfo=None)

   Fits x,y data with a thermal distribution characterised by temperature and amplitude.
   Args:
       modeltype (str): the type of thermal distribution to fit. Options are:
           maxwell, fermi, bose.
       xdata: x data to fit
       ydata: y data to fit
       p0 (opt.): initial guesses for the parameters. Should be a list of floats.
       inputinfo: not used.
   Returns:
       result: lmfit result object.


.. py:function:: step_fit(modeltype, xdata, ydata, p0=None, inputinfo=None)

   Fits x,y data with a step function characterised by amplitude, center and sigma.
   Args:
       modeltype (str): the type of step function to fit. Options are:
           linear, arctan, erf, logistic

       xdata: x data to fit
       ydata: y data to fit
       p0 (opt.): initial guesses for the parameters. Should be a list of floats.
       inputinfo: not used.

   Returns:
       result: lmfit result object.


.. py:function:: rectangle_fit(modeltype, xdata, ydata, p0=None, inputinfo=None)

   Fits x,y data with a rectangle function characterised by amplitude, center1, center2, sigma1 and sigma2.
   Args:
       modeltype (str): the type of rectangle function to fit. Options are:
        linear, arctan, erf, logistic
       xdata: x data to fit
       ydata: y data to fit
       p0 (opt.): initial guesses for the parameters. Should be a list of floats.
       inputinfo: not used.
   Returns:
       result: lmfit result object.


.. py:function:: expression_fit(xdata, ydata, p0, inputinfo)

   Fits x,y data with an arbitrary expression using lmfit's ExpressionModel.
   Args:
       xdata: x data to fit
       ydata: y data to fit
       p0 (opt.): initial guesses for the parameters. Should be a list of strings.
           Format should be: ['x0=x0_value', 'G0=G0_value', ...]
       inputinfo: The expression to fit, as a string. Should be a valid lmfit expression.
   Returns:
       result: lmfit result object.


.. py:function:: QD_fit(xdata, ydata, p0=None, inputinfo=[1, 0.01])

   Fits one or more Coulomb blockade peaks in the limit of low tunnel coupling: 'G = G_0 * cosh(e*alpha*(Vg - V_0)/(2*k_B*T))**(-2)

   Args:
       xdata: x data to fit
       ydata: y data to fit
       p0 (opt.): initial guesses for the parameters. Should be a list of strings.
           Format should be: ['x0 x0 ... x0','G0 G0 ... G0','T']
       inputinfo: a list containing the number of peaks to fit and the alpha parameter.
           Format should be: [numofpeaks, alpha]
   Returns:
       result: lmfit result object.


.. py:function:: FET_mobility(xdata, ydata, p0=None, inputinfo=None)

   Fits x,y data with a FET mobility model: '1/(R_s + L**2/(C*mu*(x-V_th)))'
   Args:
       xdata: x data to fit
       ydata: y data to fit
       p0 (opt.): List of initial guesses for the parameters.
           Format should be: [mu, V_th, R_s]
       inputinfo: a list containing the capacitance C and device length L.
           Format should be: [C, L]
   Returns:
       result: lmfit result object.


.. py:function:: dynes_fit(xdata, ydata, p0=None, inputinfo=None)

   Fits x,y data with a Dynes model for a superconducting gap: 'G_N * abs((e*x - i*gamma*e)/(sqrt((e*x - i*gamma*e)**2 - (delta*e)**2)))'

   Args:
       xdata: x data to fit
       ydata: y data to fit
       p0 (opt.): initial guesses for the parameters. Should be a list of floats.
           Format should be: [G_N, gamma, delta]
       inputinfo: not used.
   Returns:
       result: lmfit result object.


.. py:function:: ramsey_fit(xdata, ydata, p0, inputinfo)

   Fits x,y data with a Ramsey model for T2 of a qubit: 'A*cos(2*pi*f*x + phi)*exp(-x/T2) + B + C*x'

   Args:
       xdata: x data to fit
       ydata: y data to fit
       p0 (opt.): initial guesses for the parameters. Should be a list of floats.
           Format should be: [A, B, C, f, phi, T2]
       inputinfo: not used.
   Returns:
       result: lmfit result object.


.. py:function:: statistics(xdata, ydata, p0, inputinfo)

.. py:data:: functions

.. py:data:: multipeak_description
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """Fit one or more {} peaks. The inputs are n,c, where n is the number of peaks and c is whether to include a constant offset in the fit. c=0 --> no offset, c=1 --> Offset.
      For exmaple, inputs of 4,0 will fit four peaks without a constant offset.
      By default, the fit assumes equally spaced peaks with heights approximately the max value of the data.
      To change this, provide an initial guess of the form {}
      If providing an intial guess, you must provide all parameters for all peaks."""

   .. raw:: html

      </details>



.. py:data:: lorgaussform
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """w1 ... wn, a1 ... an, x1 ... xn, c where w = peak sigma a = peak amplitude, x = peak position and c = constant offset value (if used). For example:
      0.01 0.014 0.005, 1.1 1.05 1.2, -0.1 0 0.1
      for three peaks with no constant offset, and
      0.01 0.014 0.005, 1.1 1.05 1.2, -0.1 0 0.1,5
      for three peaks with a constant offset of 5.
      """

   .. raw:: html

      </details>



.. py:data:: fourparamform
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """w1 ... wn, a1 ... an, x1 ... xn, g1 ... gn, c where w = peak sigma, a = peak amplitude, x = peak position, g = gamma (see lmfit documentation for meaning in each case) and c = constant offset value (if used). For example:
      0.01 0.014 0.005, 1.1 1.05 1.2, -0.1 0 0.1, 0.001 0.001 0.001
      for three peaks with no constant offset, and
      0.01 0.014 0.005, 1.1 1.05 1.2, -0.1 0 0.1, 0.001 0.001 0.001,5
      for three peaks with a constant offset of 5.
      """

   .. raw:: html

      </details>



.. py:data:: fiveparamform
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """w1 ... wn, a1 ... an, x1 ... xn, g1 ... gn, s1 ... sn, c where w = peak sigma, a = peak amplitude, x = peak position, g = gamma (see lmfit documentation for meaning in each case), s = skew and c = constant offset value (if used). For example:
      0.01 0.014 0.005, 1.1 1.05 1.2, -0.1 0 0.1, 0.001 0.001 0.001, 0.1 0.12 0.14
      for three peaks with no constant offset, and
      0.01 0.014 0.005, 1.1 1.05 1.2, -0.1 0 0.1, 0.001 0.001 0.001, 0.1 0.12 0.14, 5
      for three peaks with a constant offset of 5.
      """

   .. raw:: html

      </details>



.. py:data:: thermaldescription
   :value: 'Fit to a {} distribution: y = {}. kT is considered a single fit parameter. Initial guesses for...


.. py:data:: stepdescription
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """Fit a single step function of type {} (see lmfit documentation for information). 
      The step function starts at 0 and ends with value +/- A. The x-value where y=A/2 is given by x0, and sigma is the characteristic width of the step.
      Use an offset filter on the data in the main panel to ensure your data starts at y=0.
      In addition, the x-data must be ascending; use a filter to multiply by -1, and possibly an add/subtract offset, if necessary.
      """

   .. raw:: html

      </details>



.. py:data:: rectdescription
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """Fit a rectangle function of type {} (see lmfit documentation for information). 
      A rectangle function steps from 0 to +/- A, then back to 0. The x-values where y=A/2 are given by x0_1, x0_2, and sigma_1 and sigma_2 are the characteristic widths of the steps.
      Use an offset filter on the data in the main panel to ensure your data starts at y=0.
      In addition, the x-data must be ascending; use a filter to multiply by -1, and possibly an add/subtract offset, if necessary.
      """

   .. raw:: html

      </details>



.. py:function:: get_class_names()

.. py:function:: get_function(function_class, function_name)

.. py:function:: get_names(fitclass='Polynomials and powers')

.. py:function:: get_parameters(function_class, function_name)

.. py:function:: get_description(function_class, function_name)

.. py:function:: fit_data(function_class, function_name, xdata, ydata, p0=None, inputinfo=None)

