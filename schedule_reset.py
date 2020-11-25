import os, time, datetime, warnings, sys, json

warnings.filterwarnings("ignore", category=DeprecationWarning) 
print("Timestamp: " + datetime.datetime.now().strftime("%D  %H:%M:%S"))

schedule_file = open(os.path.dirname(os.path.abspath(__file__))+"/schedule.json")
schedule = json.load(schedule_file)
schedule_file.close()

for data in schedule["CONSTANT"]:
    data["automation_finished"] = False

for data in schedule["ALTERATION"]:
    data["automation_finished"] = False

with open(os.path.dirname(os.path.abspath(__file__))+'/schedule.json', "w") as schedule_file2:
    schedule_file2.write(json.dumps(schedule, indent=4))
    schedule_file2.close()

print("Completed schedule reset\n")