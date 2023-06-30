import os

import numpy as np
import matplotlib.pyplot as plt


class FilterViz:
    def __init__(self, filter, style='pepso_dark') :
        self.filter       = filter
        self.measurements = filter.measurements
        self.predictions  = filter.predictions
        self.estimations  = filter.estimations


        if os.path.exists("assets/mpl_styles"):
            if style=='pepso_dark':
                pepso_dark_style   = r"assets\mpl_styles\pepso_dark.mplstyle"
                plt.style.use(pepso_dark_style)

            elif style=='pepso_light':
                pepso_light_style = r"assets\mpl_styles\pepso_light.mplstyle"
                plt.style.use(pepso_light_style)

            else:
                plt.style.use("fivethirtyeight")

    def plot(self, figsize=(16,9), title=None, legend=True, grid=True, save=None):
        fig = plt.figure(figsize=figsize)
        plt.plot(self.estimations[1:], color='blue' , marker='o', label='Estimated')
        plt.plot(self.predictions    , color='red'  , marker='s', label='Predicted')
        plt.plot(self.measurements   , color='green', marker='x', label='Measured')

        plt.ylabel(f"{self.filter.info['y_unit']}")
        plt.xlabel(f"{self.filter.info['t_unit']}")
        if title==None: plt.title(f"{self.filter}")
        if legend: plt.legend()
        if grid:   plt.grid(True)

        if save!=None: fig.savefig(f"outputs/{save}") 
        plt.show()


