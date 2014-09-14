### pws.py

Alfred workflow to get Weather Underground PWS readings

### NEWS 

- Version 0.1 - initial version

### What's it do?

- Returns lat 5 readings (date/time, temp, barometer, humidity) in Alfred window
- Enables copying of full current day's CSV to clipboard
- URL action goes to PWS readings page

### Requires

* alfred-workflow : https://github.com/deanishe/alfred-workflow (installed to workflow directory)
* the requests library (installed to the workfllow "lib" subdirectory)

### Installation

To build on your own (vs just install the [compiled workflow]()):

* Copy script into an Alfred script filter workflow with 0 args
* If user selects a reading, setup a URL action to open: http://www.wunderground.com/personal-weather-station/dashboard?ID={query}#history 
