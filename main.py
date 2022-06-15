import csv
trains_list = []
stations_list = []
good_list = []
min_price = float()
min_price = 9999
sred = 0;
i = 1
with open('test_task_data.csv', newline='') as csvfile:
    strtStation = "1921"
    finishStation = "1999"
    reader = csv.DictReader(csvfile, delimiter=";")
    print("Train number:\tOtpravlenie:\tPribitie\tCost:")
    for row in reader:
        #print(i, row['trNum'], row['otprSt'],row['stPrib'], row['cost'])
        if row['otprSt'] == strtStation and row['stPrib'] == finishStation:
            if float(row['cost']) < min_price:
                min_price = float(row['cost'])
            else:
                pass
            good_list.append(row['trNum'])
            print(f"{row['trNum']}\t\t{row['otprSt']}\t\t{row['stPrib']}\t\t{row['cost']}")
        trains_list.append(row['trNum'])
        i += 1
        sred += float(row['cost'])
        try:
            if row['otprSt'] in stations_list:
                raise Exception()
            stations_list.append(row['otprSt'])
        except:
            pass

sredc = sred/float(len(trains_list))
if min_price == 9999:
    print("Minimal cost: 0")
else:
    print(f"Minimal cost: {min_price}")
#print(trains_list)
print(f"Total amount of trains: {len(trains_list)}")
print(stations_list)
print(f"Total amount of stations: {len(stations_list)}")
print(f"Average cost if: {sredc}({sred},{len(trains_list)})")
