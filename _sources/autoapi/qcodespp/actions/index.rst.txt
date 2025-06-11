qcodespp.actions
================

.. py:module:: qcodespp.actions

.. autoapi-nested-parse::

   Actions, mainly to be executed in measurement Loops.



Exceptions
----------

.. autoapisummary::

   qcodespp.actions.UnsafeThreadingException


Classes
-------

.. autoapisummary::

   qcodespp.actions.Task
   qcodespp.actions.Wait
   qcodespp.actions.BreakIf


Module Contents
---------------

.. py:exception:: UnsafeThreadingException

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:class:: Task(func, *args, **kwargs)

   Execute a function within a measurement Loop, e.g. .each(Task(func, *args, **kwargs)).

   The first argument should be a callable function, to which any subsequent
   args and kwargs (which are evaluated before the loop starts) are passed.

   e.g.:
   Define a function to wait for a temperature setpoint to be reached:

   >>> def wait_for_temperature(target_T, measured_T, tolerance):
   >>>     while abs(measured_T - target_T) > tolerance:
   >>>         time.sleep(1)

   Then use it in a Loop, inside each, before measuring.

   >>> loop = Loop(temperature_setpoint.sweep(0,2,101),delay=0.1).each(
   >>>     Task(wait_for_temperature, temperature_setpoint(), temperature(), 0.1),
   >>>     *station.measure())

   If the args and kwargs are also callable, then they are evaluated
   before being passed to the func.

   Args:
       func (callable): Function to executed
       *args: pass to func, after evaluation if callable
       **kwargs: pass to func, after evaluation if callable



   .. py:attribute:: func


   .. py:attribute:: args
      :value: ()



   .. py:attribute:: kwargs


   .. py:method:: __call__(**ignore_kwargs)


   .. py:method:: snapshot(update=False)

      Snapshots  task
      Args:
          update (bool): TODO not in use

      Returns:
          dict: snapshot



.. py:class:: Wait(delay)

   A simple class to tell a Loop to wait <delay> seconds.

   This is transformed into a Task within the Loop, such that
   it can do other things (monitor, check for halt) during the delay.

   But for use outside of a Loop, it is also callable (then it just sleeps)

   Args:
       delay: seconds to delay

   Raises:
       ValueError: if delay is negative


   .. py:attribute:: delay


   .. py:method:: __call__()


   .. py:method:: snapshot(update=False)

      Snapshots  delay
      Args:
          update (bool): TODO not in use

      Returns:
          dict: snapshot



.. py:class:: BreakIf(condition)

   Loop action that breaks out of the loop if a condition is truthy.

   Args:
       condition (callable): a callable taking no arguments.
           Can be a simple function that returns truthy when it's time to quit
   Raises:
       TypeError: if condition is not a callable with no aguments.

   Examples:
           >>> BreakIf(lambda: np.abs(chan1.curr()) >= 3e-9)


   .. py:attribute:: condition


   .. py:method:: __call__(**ignore_kwargs)


   .. py:method:: snapshot(update=False)

      Snapshots breakIf action
      Args:
          update (bool): TODO not in use

      Returns:
          dict: snapshot




