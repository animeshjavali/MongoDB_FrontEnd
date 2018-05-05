from pymongo import MongoClient
from flask import Flask 
client=MongoClient()
collection=client['my_db']['collect']
app=Flask(__name__)
@app.route('/insert/<name>/<value1>/<value2>')
def insert(name,value1,value2):
	collection.insert({'name':name,'age':value1,'weight':value2})
	doc=collection.find({})
	for x in doc:
		x.pop("_id",None)
		print x
	return "Inserted a doccument "+name+"."

@app.route('/remove/<name>')
def remove(name):
	collection.remove({'name':name})
	return "Removed the document "+name+"."

@app.route('/update/<name1>/<name2>')
def update(name1,name2):
	collection.update({'name':name1},{'$set':{'name':name2}})
	return "Updated the doccument name from "+name1+" to "+name2+"."
#collection.update({"name":"joe"},{'$set':{"name":"Animesh J","age":19,"weight":40}})
#collection.update({'name':"Sensor data"},{'$set':{'value':data}},{'upsert':True})
#collection.remove({'name':"Sensor data"},{'justone':1})
#collection.update({'name':"Animesh J"},{'$set':{'name':'roman'}})

if __name__=='__main__':
	app.run()