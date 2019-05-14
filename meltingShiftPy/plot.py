#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# TODO: fix plotting style
# Update matplotlib rcParameters
#param = mpl.rc_params_from_file("meltingshift_plot_params")
#mpl.rcParams.update(param)

def plot_qs7(df, control, axis_spec, color="red"):
    """
    Plotting function for results from gs7 thermocycler

    :param df:
    :param control:
    :param axis_spec:
    :param color:
    :return:
    """
    # Create iterator of columns for dataframe
    column_iterator = df.iteritems()
    # Create custom figure
    fig = plt.figure(constrained_layout=True)
    fig.set_size_inches(25,25)
    # Create gridplot
    gs = plt.GridSpec(axis_spec, axis_spec, figure = fig)
    # Loop for plotting
    i = 0
    while i < axis_spec:
        for j in range(6):
            # Call next sample replicate
            try:
                sample = next(column_iterator)
            except:
                i = axis_spec
                break
                
            # Create plot
            ax = plt.subplot(gs[j,i])  
            # Sample name  
            name = "_".join(sample[1].name.split("_")[1:])
            # Plotting sample vs control
            ax.set(title=name, xlabel="Temperature", ylabel="Flourescence", xlim=(min(sample[1].index), 70))
            ax.yaxis.set_major_formatter(mpl.ticker.EngFormatter())
            # Plot control vs sample
            ax.scatter(x=control.index, y=sample[1], color=color)
            ax.scatter(x=control.index, y=control)
            
        # Increment placeholder
        i += 1
        
    # Open figure window    
    plt.show()

def plot_cfx(df, control, axis_spec, color="red"):
    """
    Plotting function for results from cfx thermocycler

    :param df:
    :param control:
    :param axis_spec:
    :param color:
    :return:
    """
    # Create custom figure
    fig = plt.figure(constrained_layout=False)
    fig.set_size_inches(36,36)
    # Create gridplot
    gs = plt.GridSpec(axis_spec, axis_spec, figure=fig)
    # Create iterator of columns for dataframe
    column_iterator = df.iteritems()
    # Loop for plotting
    i = 0
    while i < axis_spec:
        for j in range(axis_spec):
            # Call next sample replicate
            try:
                sample = next(column_iterator)
            except:
                i = axis_spec
                break

            # Create plot
            ax = plt.subplot(gs[j, i])
            # Plotting sample vs control
            ax.set(title=sample[1].name, xlabel="Temperature", ylabel="Flourescence", xlim=(min(sample[1].index), 70))
            ax.yaxis.set_major_formatter(mpl.ticker.EngFormatter())
            # Plot control vs sample

            ax.scatter(x=control.index, y=sample[1], color=color)
            ax.scatter(x=control.index, y=control)

        # Increment placeholder
        i += 1

    # Open figure window
    plt.show()
