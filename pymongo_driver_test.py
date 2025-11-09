from pymongo import MongoClient 

try:
    # start example code here

    # end example code here
    client = MongoClient('mongodb://127.0.0.1:27017/')
    #client.connect()
    #db = client.enos
    #collection = db.collection


    #client.db.
    client.enos.command("ping")
    print("Connected successfully")

    # other application code

    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)
