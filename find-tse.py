#!/usr/bin/python

#Get TSE

#Input directory name same as MATLAB scripts for simplicity

##########################
#   Global Variables
##########################

N_min = 10 # Large enough to consider p_B and p_A Gaussian Random Variables
N_max = 100 # Error of 5% for trajectories
alpha = 2 # Necessary to obtain a confidence level of 95% Transition Path Sampling, 2001

import sys
import random
from MDAnalysis import *

##########################
#   Setup Similutions
##########################

# Notes: if I want this to be generalizable

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) != 2:
        print "Usage: find-tse.py rootdir"
        exit()
    if not os.path.isdir(argv[1]):
        # Check that rootdir is a directory 
        print argv[1] + " is not a directory"
    try:
        rootdir = argv[1] + "/"
        Random_inp_num1 = random.randint(100000, 999999)
        Random_inp_num2 = random.randint(100000, 999999)
        # Check that rootdir has correct files:
        
        params_file = open(rootdir + "params.cntl", "r")
        status = "ignore"
        for param_line in params_file:
            if param_line == "[setup]":
                
        # Need params.cntl with parameterfile under [setup]
            # topologyfile under [setup]
            # basin_prod under [tps-setup]
            # stepnum under [find-tse]
            # inpscriptloc under [find-tse] (findtse-submit.inp)
            # If nmin under [find-tse], reset
            # If nmax under [find-tse], reset
            # If alpha under [find-tse], reset
        # Need existance of tps_getv/
        # Need template/startcrd (startcrd under [setup])
        # Need template/startpsf

        psf_read_in_file = 
        # Currently, going to put quantum-region, rxncoor, rxncoor_zero_umbrella,
        # the selection parameters, and basin_prod in the findtse-submit.inp
    except: #Add the type of error
        # If error, return problem
        exit()
    
    num_dirs = len(os.listdir(rootdir + "tps_getv"))
    dcd_list = []
    for root, dirs, files in os.walk(rootdir + "tps_getv"):
        if len(dirs) == 0:
            if "tpsv_trajs.dcd" in files:
                universe = Universe(psf_read_in_file
                
##########################
#   Analyze TSE
##########################

#remove rsum1_test.txt
#remove rsum2_test.txt
