import json
import pickle
import os

print("2.1")
print("*"*100+"\n")

with open("contributors_sample.json", "r") as file:
    data = json.load(file)

jobsDict = dict()
for contributor in data:
    username = contributor['username']
    jobs = contributor.get('jobs', [])

    for job in jobs:
        if job not in jobsDict: jobsDict[job] = []
        jobsDict[job].append(username)

print(list(jobsDict.items())[:2])

print()
print("2.2")
print("*"*100+"\n")

with open('job_people.pickle', 'wb') as pickle_file:
    pickle.dump(jobsDict, pickle_file)

with open('job_people.json', 'w', encoding='utf-8') as json_file:
    json.dump(jobsDict, json_file, indent=4, ensure_ascii=False)

pickle_size = os.path.getsize('job_people.pickle')
json_size = os.path.getsize('job_people.json')

print(f"Размер job_people.pickle: {pickle_size} байт")
print(f"Размер job_people.json: {json_size} байт")

if pickle_size < json_size:
    print("Файл в формате pickle меньше.")
else:
    print("Файл в формате JSON меньше или одинаковый по размеру.")

print()
print("2.3")
print("*"*100+"\n")

with open('job_people.pickle', 'rb') as pickle_file:
    loaded_data = pickle.load(pickle_file)

print(list(loaded_data.items())[:2])