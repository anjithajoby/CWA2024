#import statements here
import pandas as pd
from statistics import mean
import csv
import serial
from time import sleep

#function to give a remark on my mood based on avg_mood value
def interpret_mood(avg_mood):
    if avg_mood >= 9:
        return "i'm thrilled today, thankfully."
    elif avg_mood <  5:
        return "i'm doing okay today, thanks for inquiring."
    elif 5 <= avg_mood < 9:
        return "it's getting better, thanks.."
    else:
        return "it's making progress, thanks\n"

#Take them in as integers, as all inputs default to strings
screentime_wellbeing = int(input("On a scale of 1-10, how do you feel about your screentime? "))
mental_wellbeing = int(input("On a scale of 1-10 from tired to energetic, how much energy do you have? "))
sleep_wellbeing = int(input("On a scale of 1-10, how do you feel about how much sleep you get ? "))
avg_mood = round(mean([screentime_wellbeing,mental_wellbeing,sleep_wellbeing]),2)
mood_remark = interpret_mood(avg_mood)
print("My average mood today is that",mood_remark, " ", avg_mood)

df = pd.read_csv('BR1-3_105636.csv')
print(df)
# Convert 'Timestamp' column to datetime, is it necessary
#df['time (seconds)'] = pd.to_datetime(df['time (seconds)'], errors='coerce')
light_min = round(df['light'].min(), 2)  # Rounds to 2 decimal places, adjust as needed
light_max = round(df['light'].max(), 2)
light_mean = round(df['light'].mean(), 2)
avg_mood = round(avg_mood, 2)  # Assuming avg_mood is already calculated

print(light_min, light_max, light_mean, avg_mood)

f = open("BR1-3_results.csv", "a", newline='')
csver = csv.writer(f)
#csver.writerow(["light_min", "light_max", "light_mean", "avg_mood"])
csver.writerow([light_min, light_max, light_mean, avg_mood])
f.close()

#VALIDATION OF DATA BR2
if not isinstance(light_min, float):
    light_min = float(light_min)
if not isinstance(light_max, float):
    light_max = float(light_max)
if not isinstance(light_mean, float):
    light_mean = float(light_mean)

