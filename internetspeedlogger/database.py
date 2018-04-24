from pymongo import MongoClient


def connect_db():
	# connects to MongoDB on localhost
    client = MongoClient('mongodb://localhost:27017')
    return client


def insert_results(client, results):
	db = client.InternetSpeedLog
	res = db.insert_one(results)
	client.close()
	print res
