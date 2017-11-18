#
#	Simple cleanup function
#		- The variable source contains the folder to be cleaned
#		- All items within source are consolidated to a date named folder
#
#	Created by Nathan Green

import shutil
import os
import datetime

#store the date via datetime function
now = datetime.datetime.now()

#modify this variable to determine which folder is consolidated
source = 'C:/Users/Nathan/Desktop/'

#generate aussie date structure for folder
destination = source + str(now.day) + '-' + str(now.month) + '-' + str(now.year)

#create directory with current date if not exists
if not os.path.exists(destination):
	os.makedirs(destination)

#create list of filenames
files = os.listdir(source)

#Iterate through items and pass them to the destination
for item in files:
	shutil.move(source+item, destination)