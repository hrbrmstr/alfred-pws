#
# pws.py
# 
# Version 0.1 - initial version
#
# Alfred workflow to get Weather Underground PWS readings
#
# - Returns lat 5 readings (date/time, temp, barometer, humidity) in Alfred window
# - Enables copying of full current day's CSV to clipboard
# - URL action goes to PWS readings page
#
# Requires:
#
# * alfred-workflow : https://github.com/deanishe/alfred-workflow (installed to workflow directory)
# * the requests library (installed to the workfllow "lib" subdirectory)
# 
#
# To build on your own (vs just install the compiled workflow):
#
# * Copy script into an Alfred script filter workflow with 0 args
# * Setup a URL action to open:
#
#     http://www.wunderground.com/personal-weather-station/dashboard?ID={query}#history
#
#   if user selects a reading
#

import re
import csv
import sys
import datetime
from lib import requests
from workflow import Workflow, web
from StringIO import StringIO

# retrieve today's history for station "X"

def get_wx_data(station):

  tdy = datetime.datetime.today()
    
  # construct the URL for "today"
  url = 'http://www.wunderground.com/weatherstation/WXDailyHistory.asp?ID=%s&day=%d&month=%d&year=%d&graphspan=day&format=1' % (station, tdy.day, tdy.month, tdy.year)
    
  r = web.get(url) # get the data
     
  r.raise_for_status() # report any errors
    
  return(re.sub("\n\n", "\n", re.sub("^\n|<br>", "", r.text))) # clean up the output & pass it back to main control


# main workflow control

def main(wf):

  station = "KMEBERWI7" # change to use your own/favorite station

  resp = get_wx_data(station)

  # only want last 5 readings, change this to whatever you want
  max = 5

  i=0
  for row in reversed(list(csv.reader(StringIO(resp)))):
    wf.add_item(title=row[0] + " | " + row[1] + "F | " + row[3] + "in | " + row[8] + "%", 
                subtitle=station, # so you know where you're getting data from
                arg=station, # passed as query to URL action - http://www.wunderground.com/personal-weather-station/dashboard?ID={query}#history
                valid=True, # it can be opened in the browser
                icon="/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/ToolbarInfo.icns", # info icon
                copytext=resp) # get the whole CSV file in a copy
    if (i==max): break
    i += 1

  # output to alfred

  wf.send_feedback()

if __name__ == u"__main__":
  wf = Workflow()
  sys.exit(wf.run(main))