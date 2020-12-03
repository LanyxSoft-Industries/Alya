import os, time, datetime, warnings, sys, json, subprocess

warnings.filterwarnings("ignore", category=DeprecationWarning) 
print("Timestamp: " + datetime.datetime.now().strftime("%D  %H:%M:%S"))

# nowish = datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
# DT_m = datetime.datetime.now().strftime("%m");DT_d = datetime.datetime.now().strftime("%d");DT_Y = datetime.datetime.now().strftime("%Y");DT_I = datetime.datetime.now().strftime("%I");DT_M = datetime.datetime.now().strftime("%M");DT_S = datetime.datetime.now().strftime("%S");DT_P = datetime.datetime.now().strftime("%p")
# print("Time data:", DT_m, DT_d, DT_Y, DT_I ,DT_M, DT_P, "\n")


# test = '2020-11-23 13:04:00'
# test_DT = datetime.datetime.strptime(test, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %I:%M:%S %p')
# print("test_DT:", test_DT) # print(datetime.datetime.strptime(test, '%Y-%m-%d %H:%M:%S'))
# test_DT_calc_arr = str(test_DT).replace("-", " ").replace(":", " ").split(" ")
# print(test_DT_calc_arr)
# test_nowtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print("test_nowtime:", test_nowtime)
# test_nowtime_arr = str(test_nowtime).replace("-", " ").replace(":", " ").split(" ")
# print(test_nowtime_arr)


schedule_file = open(os.path.dirname(os.path.abspath(__file__))+"/schedule.json")
schedule = json.load(schedule_file)
schedule_file.close()

def process_time(data, IS_CONSTANT=False):
    if data["datetime"] == "":
        print("Data is NULL.\n")
        return
    elif data["automation_finished"] == True:
        print(data["class"], "- Automation already finished.\n")
        return
    else:
        print('data["class"]:', data["class"], "-", data["datetime"], "-", data["code"])
    

    data_DT = datetime.datetime.strptime(data["datetime"], '%Y-%m-%d %H:%M:%S')
    print("data_DT:", data_DT) # print(datetime.datetime.strptime(test, '%Y-%m-%d %H:%M:%S'))
    data_DT_calc_arr = str(data_DT).replace("-", " ").replace(":", " ").split(" ")
    print("data_DT_calc_arr:", data_DT_calc_arr)
    data_nowtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("data_nowtime:", data_nowtime)
    data_nowtime_arr = str(data_nowtime).replace("-", " ").replace(":", " ").split(" ")
    print("data_nowtime_arr:", data_nowtime_arr)

    if len(data_DT_calc_arr) == len(data_nowtime_arr):
        print("check 1 passed", len(data_DT_calc_arr))
        if data_DT_calc_arr[0] == data_nowtime_arr[0]:
            print("check 2 passed", data_DT_calc_arr[0])
            if data_DT_calc_arr[1] == data_nowtime_arr[1]:
                print("check 3 passed", data_DT_calc_arr[1])
                if data_DT_calc_arr[2] == data_nowtime_arr[2]:
                    print("check 4 passed", data_DT_calc_arr[2])
                    if int(data_DT_calc_arr[3]) == int(data_nowtime_arr[3]) or int(data_DT_calc_arr[3]) == int(str(datetime.datetime.now() - datetime.timedelta(hours=1)).replace("-", " ").replace(":", " ").split(" ")[3]) or int(data_DT_calc_arr[3]) == int(str(datetime.datetime.now() + datetime.timedelta(hours=1)).replace("-", " ").replace(":", " ").split(" ")[3]):
                        print("check 5 passed", data_DT_calc_arr[3])
                        # if is bigger -->
                        if int(str(datetime.datetime.now() + datetime.timedelta(minutes=5)).replace("-", " ").replace(":", " ").split(" ")[4]) < int(str(datetime.datetime.now() - datetime.timedelta(minutes=5)).replace("-", " ").replace(":", " ").split(" ")[4]):
                            if int(data_DT_calc_arr[4]) >= int(str(datetime.datetime.now() - datetime.timedelta(minutes=5)).replace("-", " ").replace(":", " ").split(" ")[4]) or int(data_DT_calc_arr[4]) >= 0 and int(data_DT_calc_arr[4]) <= int(str(datetime.datetime.now() + datetime.timedelta(minutes=5)).replace("-", " ").replace(":", " ").split(" ")[4]):
                                print("check 6 passed", data_DT_calc_arr[4])
                                data["automation_finished"] = True
                                if data["code"] != "":
                                    if IS_CONSTANT == True:
                                        if data["type"] == "daily":
                                            data["datetime"] = str(data_DT + datetime.timedelta(days=1))
                                            print("Setting new date [+1 day]")
                                        elif data["type"] == "weekly":
                                            data["datetime"] = str(data_DT + datetime.timedelta(days=7))
                                            print("Setting new date [+1 week]")
                                        elif data["type"] == "non-repetitive":
                                            print("Keeping set datetime")
                                        else:
                                            print("Keeping set datetime")
                                    pipe_file = open(os.path.dirname(os.path.abspath(__file__))+"/meet.log", "a+")
                                    subprocess.Popen(['python3', f"{os.path.dirname(os.path.abspath(__file__))}/meet.py", "-fc", "true", "-c", f'{data["code"]}', "-tk", f'Go to: {data["class"]}'], stdout=pipe_file)
                                    pipe_file.close()
                        # simple block -->
                        elif int(data_DT_calc_arr[3]) != int(data_nowtime_arr[3]):
                            print("check 6 missed")
                        # if is bigger or smaller -->
                        elif int(data_DT_calc_arr[4]) >= int(str(datetime.datetime.now() - datetime.timedelta(minutes=5)).replace("-", " ").replace(":", " ").split(" ")[4]) and int(data_DT_calc_arr[4]) <= int(str(datetime.datetime.now() + datetime.timedelta(minutes=5)).replace("-", " ").replace(":", " ").split(" ")[4]):
                            print("check 6 passed", data_DT_calc_arr[4])
                            data["automation_finished"] = True
                            if data["code"] != "":
                                if IS_CONSTANT == True:
                                    if data["type"] == "daily":
                                        data["datetime"] = str(data_DT + datetime.timedelta(days=1))
                                        print("Setting new date [+1 day]")
                                    elif data["type"] == "weekly":
                                        data["datetime"] = str(data_DT + datetime.timedelta(days=7))
                                        print("Setting new date [+1 week]")
                                    elif data["type"] == "non-repetitive":
                                        print("Keeping set datetime")
                                    else:
                                        print("Keeping set datetime")
                                pipe_file = open(os.path.dirname(os.path.abspath(__file__))+"/meet.log", "a+")
                                subprocess.Popen(['python3', f"{os.path.dirname(os.path.abspath(__file__))}/meet.py", "-fc", "true", "-c", f'{data["code"]}', "-tk", f'Go to: {data["class"]}'], stdout=pipe_file)
                                pipe_file.close()
    print("")

for data in schedule["CONSTANT"]:
    process_time(data, IS_CONSTANT=True)

for data in schedule["ALTERATION"]:
    process_time(data)

with open(os.path.dirname(os.path.abspath(__file__))+'/schedule.json', "w") as schedule_file2:
    schedule_file2.write(json.dumps(schedule, indent=4))
    schedule_file2.close()