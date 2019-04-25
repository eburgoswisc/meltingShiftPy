#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

def plot_meltingShift(df, control, axis_spec, color="red"):
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