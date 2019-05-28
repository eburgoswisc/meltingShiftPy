#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sys

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
    gs = plt.GridSpec(axis_spec, axis_spec, figure=fig)
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


def plot_cfx(df, control, output, color="red"):
    """
    Plotting function for results from cfx thermocycler

    :param df:
    :param control:
    :param axis_spec:
    :param color:
    :return:
    """

    #plt.ion()
    # Create custom figure
    #fig = plt.figure(constrained_layout=True)
    #fig.set_size_inches(36,36)
    # Create gridplot
    #gs = plt.GridSpec(axis_spec, axis_spec, figure=fig)
    # Create iterator of columns for dataframe
    column_iterator = df.iteritems()
    # Loop for plotting
    i = 1
    while i < len(df.columns):
        fig = plt.figure(constrained_layout=True)
        fig.set_size_inches(40, 40)
        gs = plt.GridSpec(4,4, figure=fig)
        for j in range(4):
            for l in range(4):
                try:
                    # Call next sample replicate
                    sample = next(column_iterator)
                except:
                    plt.show()
                # Create plot
                ax = plt.subplot(gs[l, j], label=sample[1].name)
                # Plotting sample vs control
                ax.set(title=sample[1].name, xlabel="Temperature", ylabel="Flourescence", xlim=(min(sample[1].index), 70))
                ax.yaxis.set_major_formatter(mpl.ticker.EngFormatter())
                # Plot control vs sample
                ax.scatter(x=control.index, y=sample[1], color=color)
                ax.scatter(x=control.index, y=control)

        # Increment placeholder
        i += 12
    print("Done")


def plot_cfx_onegrid(df, control, axis_spec, output, color="red"):
    """
    Plotting function for results from cfx thermocycler

    :param df:
    :param control:
    :param axis_spec:
    :param color:
    :return:
    """
    # Create custom figure
    fig = plt.figure(constrained_layout=True)
    # fig.set_size_inches(36,36)
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
        plt.show()
        # Increment placeholder
        i += 1
    print("Done")
