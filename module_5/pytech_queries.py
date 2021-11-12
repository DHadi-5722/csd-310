from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.j2vkp.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

students = db.get_collection("students")

foundstudents = students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for foundstudent in foundstudents:
    print(f"Student ID: {foundstudent['student_id']}")
    print(f"First Name: {foundstudent['first_name']}")
    print(f"Last Name: {foundstudent['last_name']}")
    print("")

foundonestudent = students.find_one({"student_id": "1007"})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY --")
print(f"Student ID: {foundonestudent['student_id']}")
print(f"First Name: {foundonestudent['first_name']}")
print(f"Last Name: {foundonestudent['last_name']}")