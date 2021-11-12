from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.j2vkp.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

students = db.get_collection("students")

fred = {
    "student_id": "1007",
    "first_name": "Fred",
    "last_name" : "Gibson"
}

jimmy = {
    "student_id": "1008",
    "first_name": "Jimmy",
    "last_name" : "Johnson"
}

william= {
    "student_id": "1009",
    "first_name": "William",
    "last_name" : "Jones"
}

print("-- INSERT STATEMENTS --")

fred_inserted_id = students.insert_one(fred).inserted_id
print(f"Inserted student record {fred['first_name']} {fred['last_name']} into the students collection with document id {fred_inserted_id}")

jimmy_inserted_id = students.insert_one(jimmy).inserted_id
print(f"Inserted student record {jimmy['first_name']} {jimmy['last_name']} into the students collection with document id {jimmy_inserted_id}")

william_inserted_id = students.insert_one(william).inserted_id
print(f"Inserted student record {william['first_name']} {william['last_name']} into the students collection with document id {william_inserted_id}")
