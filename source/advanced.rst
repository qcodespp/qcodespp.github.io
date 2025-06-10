Advanced use of Loop, DataSetPP and live_plot
=============================================

Throughout, we have used the ``loop1d`` and ``loop2d`` functions to create loops for 1D and 2D measurements. However, you can also create loops manually using the `Loop` class, which gives you more control over the measurement process.

live_plot
---------
The first thing you may want to do is customise live_plots. Instead of 

What does loop1d actually do?
-----------------------------
The `loop1d` function is a convenience function that relies on several classes inside qcodes++, namely ``Loop``, ``ActiveLoop``, ``DataSetPP`` and ``Plot``. Here is the source code:

.. code-block:: python

    def loop1d(sweep_parameter,
                start, stop, num, delay,
                device_info='', instrument_info='',
                params_to_measure=None,
                params_to_plot=None,
                run=False):

        if params_to_measure is None:
            params_to_measure = Station.default.measure()

        loop=Loop(sweep_parameter.sweep(start,stop,num=num), delay).each(*params_to_measure)

        name=f'{device_info} {sweep_parameter.name}({start:.6g} {stop:.6g}){sweep_parameter.unit} with {instrument_info}'

        data=loop.get_data_set(name=name)

        if params_to_plot:
            pp=live_plot(data,params_to_plot)
        
        print(data,'\n'+loop.time_estimate())

        if run:
            loop.run()

        return loop

