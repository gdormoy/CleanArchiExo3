import sys
import datetime

def main(argv = "World"):
    timeOfTheDay = CheckTimeOfTheDay()
    name = argv[0]
    print("Good", timeOfTheDay, name)


def CheckTimeOfTheDay():
    now = datetime.datetime.now()
    print(now)
    if((now.hour > 12 and now.hour < 20) or (now.hour == 12 and now.minute > 0)):
        return "afternoon"
    elif(now.hour <= 12 and now.hour > 6):
        return "morning"
    else:
        return "night"

if __name__ == "__main__":
    main(sys.argv[1:])