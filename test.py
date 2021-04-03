import datetime


classes = {"1": {"start": datetime.time(8, 30), "end": datetime.time(8, 50)},
           "2": {"start": datetime.time(9, 5), "end": datetime.time(9, 25)},
           "3": {"start": datetime.time(4, 30), "end": datetime.time(10, 0)},
           "4": {"start": datetime.time(10, 30), "end": datetime.time(10, 50)},
           "5": {"start": datetime.time(11, 5), "end": datetime.time(11, 25)},
           "6": {"start": datetime.time(11, 40), "end": datetime.time(12, 00)},
           "1 afternoon": {"start": datetime.time(13, 30), "end": datetime.time(13, 50)},
           "2 afternoon": {"start": datetime.time(14, 5), "end": datetime.time(14, 25)},
           "3 afternoon": {"start": datetime.time(14, 40), "end": datetime.time(15, 0)},
           "4 afternoon": {"start": datetime.time(15, 15), "end": datetime.time(15, 35)},
           "5 afternoon": {"start": datetime.time(15, 50), "end": datetime.time(16, 10)}
            }

current_time = datetime.datetime.now()
class_break = False

for current in classes:
    if classes[current]["start"] <= current_time.time() <= classes[current]["end"]:
        print(f"{current} {classes[current]['start']} - {classes[current]['end']}")
        continue
    datetime.timedelta
    #  if classes[current]["start"]
    print("Break")




