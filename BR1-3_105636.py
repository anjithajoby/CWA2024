#import statements here
import pandas as pd
from statistics import mean
import csv
import serial
from time import sleep

#function to give a remark on my mood based on avg_mood value
def interpret_mood(average_mood):
    if average_mood >= 9:
        return "you're thrilled today. Well done, keep on priotizing getting sufficient rest."
    elif 5 <= average_mood < 9:
        return "you're getting better. That's good, but rememeber sleep and rest is important."
    else:
        return "you're making progress. That's a good start, keep on taking care of yourself by trying to go to sleep early."

#Take them in as integers, as all inputs default to strings
phoneanxiety_wellbeing = int(input("On a scale of 1-10, from none to a lot, how much comfort do you receive from your phone? "))
mental_wellbeing = int(input("On a scale of 1-10 from tired to energetic, how much energy do you have? "))
sleep_wellbeing = int(input("On a scale of 1-10, from bad to good, how do you feel about how much sleep you get ? "))
average_mood = round(mean([phoneanxiety_wellbeing,mental_wellbeing,sleep_wellbeing]),2)
mood_remark = interpret_mood(average_mood)


df = pd.read_csv('BR1-3_105636.csv')
print(df)
# Convert 'Timestamp' column to datetime, is it necessary
#df['time (seconds)'] = pd.to_datetime(df['time (seconds)'], errors='coerce')
light_min = round(df['light'].min(),2)  # Rounds to 2 decimal places, adjust as needed
light_max = round(df['light'].max(), 2)
light_mean = round(df['light'].mean(), 2)
average_mood = round(average_mood, 2) # Assuming avg_mood is already calculated

#VALIDATION OF DATA BR2
if not isinstance(light_min, float):
    light_min = float(light_min)
if not isinstance(light_max, float):
    light_max = float(light_max)
if not isinstance(light_mean, float):
    light_mean = float(light_mean)

f = open("BR1-3_results.csv", "a", newline='')
csver = csv.writer(f)
#csver.writerow(["light_min", "light_max", "light_mean", "average_mood"])
csver.writerow([light_min, light_max, light_mean, phoneanxiety_wellbeing, mental_wellbeing, sleep_wellbeing, average_mood])
print("Light Min is" , light_min)
print("Light Max is" , light_max)
print("Light Mean is" , light_mean)
print("Your mood today is that",mood_remark)

f.close()
