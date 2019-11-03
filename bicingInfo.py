# bicingInfo demo script by FerriTheMaker 
# using citybik free service 

from tkinter import *
from tkinter.ttk import *

import requests
import json

def searchStation():
	bicingdata = getinfo()
	stationdata = [e for e in bicingdata if e[0] == combo.get()]
	res = "Free bikes: "+str(stationdata[0][1])+" Empty slots: "+str(stationdata[0][2])
	output.configure(text= res)
    
def getinfo():
	bicingdata = []
	r = requests.get('http://api.citybik.es/v2/networks/bicing')
	bicingJson = r.json()
	for station in bicingJson['network']['stations']:
		bicingdata.append([station['name'],station['free_bikes'],station['empty_slots']])
	return bicingdata

	
bicingdata = getinfo()

window = Tk()
window.title("Bicing Info")
 
window.geometry('600x400')
 
lbl = Label(window, text="Stations:")
lbl.grid(column=1, row=0)

output = Label(window)
output.grid(column=1,row=2)

 
btn = Button(window, text="Search", command=searchStation)
btn.grid(column=2, row=1)
 
 
combo = Combobox(window)

stationNames = []
for element in bicingdata:
	stationNames.append(element[0])

combo['values'] = stationNames
combo['width'] = 40
combo.current(1) #set the selected item
combo.grid(column=1, row=1)


for child in window.winfo_children():
    child.grid_configure(padx=10, pady=10)
    
window.mainloop()
