#! /usr/bin/python3
# For exercise 1-2, p11
#
# chap01ex_my.py
# Reads 2002FemResp.dat.gz and...
# 1. prints value counts for the pregnum variable (compare with published results in NSFG codebook
# 2. makes a dictionary, using nsfg.MakePregMap, that maps each caseid to
#    a list of indices into the pregnancy DataFrame

from collections import defaultdict
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import sys

import thinkstats2

# modified version of function ReadFemPreg from nsfg.py; chaged names and
#   removed call to data cleaning function
def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz'):
    """Reads the NSFG respondent data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    return df

FemResp = ReadFemResp()
print("The value counts: #{FemResp.pregnum.value_counts())}")
FemRespDict = nsfg.MakePregMap(FemResp)
print(FemRespDict)
