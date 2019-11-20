carlist = {
    "car1": {
    "brand": "Honda",
    "model": "civic",
    "year" : "2009",
    "color": "red",
},
"car2": {
     "brand": "tesla",
     "model": "S",
     "year" : "2019",
     "color": "blue",
},
"car3": {
    "brand":"nissan",
    "model":"Murano",
    "year" :"2011",
    "color":"silver",
    }
}

for x in carlist:
    if carlist[x].get("year") == 2009:
        print (carlist[x].get("name"))
