#!/usr/bin/env python

import math
import numpy as np
from crazyflieParser import CrazyflieParser

if __name__ == '__main__':

    index = 3   # for cf1
    initialPosition = [0,-1.5,0] # x,y,z coordinate for this crazyflie
    cfs = CrazyflieParser(index, initialPosition)
    cf = cfs.crazyflies[0]
    time = cfs.timeHelper

    cf.setParam("commander/enHighLevel", 1)
    cf.setParam("stabilizer/estimator", 2) # Use EKF
    cf.setParam("stabilizer/controller", 2) # Use mellinger controller
    #cf.setParam("ring/effect", 7)

    cf.takeoff(targetHeight = 0.5, duration = 3.0)
    time.sleep(3.0)
    # FILL IN YOUR CODE HERE
    # Please try both goTo and cmdPosition
    '''
    cf.goTo([-2, -1.5, 0.5], 0, 12.0)
    time.sleep(12.0)
    cf.goTo([-2, -1.5, 1.5], 0, 6.0)
    time.sleep(6.0)
    cf.goTo([2, -1.5, 1.5], 0, 24.0)
    time.sleep(24.0)
    cf.goTo([2, -1.5, 0.5], 0, 6.0)
    time.sleep(6.0)
    cf.goTo([0, -1.5, 0.5], 0, 12.0)
    time.sleep(12.0)
    '''
    r = 0.5
    '''
    for i in np.arange(0, np.pi/2, np.pi/50):
        x = - r * (1 - math.cos(i))
        y = -1.5 + math.sqrt(r**2 - (x + r)**2)
        cf.cmdPosition([x, y, 0.5], 0)
        time.sleep(0.1)
        print([x, y, 0.5], 1)
    for i in np.arange(0, np.pi/2, np.pi/50):
        x = - r * (1 + math.sin(i))
        y = -1.5 + math.sqrt(r**2 - (x + r)**2)
        cf.cmdPosition([x, y, 0.5], 0)
        time.sleep(0.1)
        print([x, y, 0.5], 2)
    for i in np.arange(0, np.pi/2, np.pi/50):
        x = - r * (1 + math.cos(i))
        y = -1.5 - math.sqrt(r**2 - (x + r)**2)
        cf.cmdPosition([x, y, 0.5], 0)
        time.sleep(0.1)
        print([x, y, 0.5], 3)
    for i in np.arange(0, np.pi/2, np.pi/50):
        x = - r * (1 - math.sin(i))
        y = -1.5 - math.sqrt(r**2 - (x + r)**2)
        cf.cmdPosition([x, y, 0.5], 0)
        time.sleep(0.1)
        print([x, y, 0.5], 4)
    '''
    for i in np.arange(0, np.pi/2, np.pi/50):
        x = - r * (1 - math.cos(i))
        y = -1.5 + math.sqrt(r**2 - (x + r)**2)
        z = 0.5 + 2*i/np.pi/8
        cf.cmdPosition([x, y, z], 0)
        time.sleep(0.1)
        print([x, y, z], 1)
    for i in np.arange(0, np.pi/2, np.pi/50):
        x = - r * (1 + math.sin(i))
        y = -1.5 + math.sqrt(r**2 - (x + r)**2)
        z = 0.625 + 2*i/np.pi/8
        cf.cmdPosition([x, y, z], 0)
        time.sleep(0.1)
        print([x, y, z], 2)
    for i in np.arange(0, np.pi/2, np.pi/50):
        x = - r * (3 - math.cos(i))
        y = -1.5 - math.sqrt(r**2 - (x + 3*r)**2)
        z = 0.75 + 2*i/np.pi/8
        cf.cmdPosition([x, y, z], 0)
        time.sleep(0.1)
        print([x, y, z], 3)
    for i in np.arange(0, np.pi/2, np.pi/50):
        x = - r * (3 + math.sin(i))
        y = -1.5 - math.sqrt(r**2 - (x + 3*r)**2)
        z = 0.875 + 2*i/np.pi/8
        cf.cmdPosition([x, y, z], 0)
        time.sleep(0.1)
        print([x, y, z], 4)
        ##
    for i in np.arange(0, np.pi/2, np.pi/50):
        x = - r * (3 + math.cos(i))
        y = -1.5 + math.sqrt(r**2 - (x + 3*r)**2)
        z = 1.0 - 2*i/np.pi/8
        cf.cmdPosition([x, y, z], 0)
        time.sleep(0.1)
        print([x, y, z], 1)
    for i in np.arange(0, np.pi/2, np.pi/50):
        x = - r * (3 - math.sin(i))
        y = -1.5 + math.sqrt(r**2 - (x + 3*r)**2)
        z = 0.875 - 2*i/np.pi/8
        cf.cmdPosition([x, y, z], 0)
        time.sleep(0.1)
        print([x, y, z], 2)
    for i in np.arange(0, np.pi/2, np.pi/50):
        x = - r * (1 + math.cos(i))
        y = -1.5 - math.sqrt(r**2 - (x + r)**2)
        z = 0.75 - 2*i/np.pi/8
        cf.cmdPosition([x, y, z], 0)
        time.sleep(0.1)
        print([x, y, z], 3)
    for i in np.arange(0, np.pi/2, np.pi/50):
        x = - r * (1 - math.sin(i))
        y = -1.5 - math.sqrt(r**2 - (x + r)**2)
        z = 0.625 - 2*i/np.pi/8
        cf.cmdPosition([x, y, z], 0)
        time.sleep(0.1)
        print([x, y, z], 4)

    cf.land(targetHeight = 0.0, duration = 5.0)
    time.sleep(5.0)
