import os
import sys
dirname = os.path.dirname(__file__)
sys.path.insert(0, f'{dirname}/../')

import matplotlib.pyplot as plt
import numpy as np

from utils.visualization import FilterViz




class ScalerFilter:
    def __init__(self, scale_factor, gain_rate, init_estimate=0, time_step=1.0, debug=True, t_unit='', y_unit=''):
        self.scale_factor  = scale_factor
        self.gain_rate     = gain_rate 
        self.init_estimate = init_estimate
        self.time_step     = time_step
        self.debug         = debug

        self.info         = {
            "t_unit": t_unit,
            "y_unit": y_unit
        }

        self.measurements = []
        self.predictions  = []
        self.estimations  = [init_estimate]



    def propagation(self):
        for measured in self.measurements: 
            # predict new position
            predicted = self.estimations[-1] + self.gain_rate * self.time_step

            # update filter 
            estimated = predicted + self.scale_factor * (measured - predicted)

            # save and log
            self.estimations.append(estimated)
            self.predictions.append(predicted)

            if self.debug:
                print(f'measurement: {1.0*measured:<10.4}, prediction: {1.0*predicted:<10.4}, estimate: {1.0*estimated:<10.4}')




    def add_measurement(self, value):
        '''
        ABOUT:
            Add measurements to the system
        
        ARGUMENTS:
            value : value of measurement
        '''
        self.measurements.append(value)

    def __repr__(self):
        return f"ScalerFilter( scale_factor={self.scale_factor}, gain_rate={self.gain_rate} ) "





if __name__ == '__main__':
    filter = ScalerFilter(scale_factor=0.4, gain_rate=1, init_estimate=100, t_unit='day', y_unit='weights')
    print(filter)
    
    filter.add_measurement(99.0)
    filter.add_measurement(102.0)
    filter.add_measurement(103.0)
    filter.propagation()
    viz = FilterViz(filter)
    viz.plot(save='test.png')