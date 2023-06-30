import matplotlib.pyplot as plt
import numpy as np

weights = [158.0, 164.2, 160.3, 159.9, 162.1, 164.6, 
           169.6, 167.4, 166.4, 171.0, 171.2, 172.6]

time_step = 1.0        # day
scale_factor = 0.4 

class ScalerFilter:
    def __init__(self, scale_factor, gain_rate, init_estimate=100, time_step=1.0, debug=True):
        self.scale_factor  = scale_factor
        self.gain_rate     = gain_rate 
        self.init_estimate = init_estimate
        self.time_step     = time_step
        self.debug         = debug

        self.measurements = []
        self.predictions  = []
        self.estimations  = [init_estimate]


    def propagation(self):
        for measured in self.measurements: 
            # predict new position
            predicted = self.estimations[-1] + self.gain_rate * time_step

            # update filter 
            estimated = predicted + scale_factor * (measured - predicted)

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





if __name__ == '__main__':
    filter = ScalerFilter(scale_factor=0.4, gain_rate=1, init_estimate=100)
    filter.add_measurement(99.0)
    filter.add_measurement(102.0)
    filter.add_measurement(103.0)
    filter.propagation()