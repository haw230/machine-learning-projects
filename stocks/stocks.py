# -*- coding: utf-8 -*-
import pandas as pd
import os
import time
from datetime import datetime

path = '/cshome/ha10/Downloads/intraQuarter/'

def Key_Stats(gather='Total Debt/Equity (mrq)'): #gather is data we're gathering
    statspath = path + '/_KeyStats' #path to key stats
    stock_list = [x[0] for x in os.walk(statspath)] #list of all stock directory names
    #print(stock_list)
    
    for each_dir in stock_list[1:]: #first element is root directory
        each_file = os.listdir(each_dir) #gets file names for each directory
        if(len(each_file) > 0): #if directory isn't empty
            for file in each_file: #for each file in the directory
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html') #extracts date as that format (2008-12-04 09:42:09)
                unix_time = time.mktime(date_stamp.timetuple()) #unix time, seconds since Jan 1st 1970 (1228408929.0)
                print(date_stamp, unix_time)

Key_Stats()
