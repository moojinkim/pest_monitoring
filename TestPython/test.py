from readcsv import readData
from readcsv import saveData
from getColor import getColor2
from combined_code import classifyMoth
from finalcode import combined_code
from finalcode import combined_code_id
import csv
import itertools
import matplotlib.pyplot as plt
import matplotlib as mpl 

import numpy as np

a,b,c,d=combined_code(id="anwls328",data="/Users/master/Desktop/test.jpg",sizethreshold=300,distance_threshold=10,imageShow=False,BugName=["a","b","c","d"])
a,b,c,d=combined_code(id="anwls328",data="/Users/master/Desktop/test.jpg",sizethreshold=300,distance_threshold=10,imageShow=False,BugName=["a","b","c","d"])
# # a,b,c=combined_code_url(data_url="http://211.179.225.31:25000/?action=snapshot",sizethreshold=300,imageShow=True)

# a,b,c,d=combined_code_id(id="anwls3281",sizethreshold=300,distance_threshold=10,imageShow=False)
# a,b,c=combined_code_id(data_url="http://211.179.225.31:25000/?action=snapshot",sizethreshold=300,imageShow=True)

  