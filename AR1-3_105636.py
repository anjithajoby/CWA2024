# This program takes three values from a CSV file and compares them to predict a fourth value
# This is given the fancy name "Multiple Linear Regression".
# It's like a bunch of linear trendlines mashed up together to allow a few more extra variables.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


def predict_mood(bluelight_min, bluelight_max, bluelight_mean):
    df = pd.DataFrame([[bluelight_min, bluelight_max, bluelight_mean]],
                      columns=['bluelight_min', 'bluelight_max', 'bluelight_mean'])
    return model.predict(df)[0]
# Training the model

# Load your dataset
data = pd.read_csv('AR1-3_105636.csv')

# Define your independent variables (features) and dependent variable (target)
X = data[['bluelight_min', 'bluelight_max', 'bluelight_mean']]
Y = data['avg_bluelight']

# Splitting the dataset into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Creating the Linear Regression model
model = LinearRegression()

# Fitting the model with the training data
model.fit(X_train, Y_train)

# Predicting mood scores for the test set
Y_pred = model.predict(X_test)


print("Multiple Linear Regression Model Complete!")

# Checking how well it worked
mse = mean_squared_error(Y_test, Y_pred)

 # Let the user enter their own 3 parameters
print("")
print("User will be asked three questions!")
bluelight = int(input("Enter the amount of blue light you receive from your phone.It can be any integer from 0-300. "))
mental = float(input("Enter how much time you spend to yourself. Can be anything from 0-24 "))
sleeptime = float(input("Enter how much sleep you get in a day. Can be anything from 0-24 "))

predicted_mood = predict_mood(bluelight, mental, sleeptime)  # Example values
print("\n The Predicted Mood Score for the values entered is", predicted_mood)


#WHAT-IF Question 1
# What is will your mood be with low values of all three parameters?
print("-----------------------------------------------------------")
print("What-if Question 1")
print("Let's test how much blue light the user receives from their phone ")
# Low values for all 3 parameters

mood_if_littleSun = predict_mood(bluelight, mental, sleeptime)  # Example values
print("\n The amount of blue light the user receives is ", mood_if_littleSun)

# WHAT-IF Question 2
# What is will your mood be with high values of all three parameters?
print("-----------------------------------------------------------")
print("What-if Question 2")
print("Let's test how much time the user spends to theirself")
# High values for all 3 parameters




mood_if_LoadsaSun = predict_mood(bluelight, mental, sleeptime)  # Example values
print("\n The amount of time the user spends to theirself is ", mood_if_LoadsaSun)

# WHAT IF QUESTION 3
# What variable is more important
print("-----------------------------------------------------------")
print("What-if Question 3")
print("Let's test how much sleep the user gets in a day")
print("We will keep the hours (A) the same and double the others (B) and (C) one at a time")
print("")
print("Let's get a baseline from fairly average values...")

# Baseline 


baseline_mood = predict_mood(bluelight, mental, sleeptime)  # Example values
print("\n The baseline Score mood is", baseline_mood)
print("")


#------------------------------------
# AR3 Show Results of WHAT IF on a graph for Questions 1 & 2

# Data: names of the variables and their values
variable_names = ['BlueLight', 'Mental', 'SleepTime']
values = [bluelight, mental, sleeptime]

# Creating the bar chart
plt.bar(variable_names, values)

# Adding labels and title
plt.xlabel('Amount of blue light')
plt.ylabel('Users Moods')
plt.title('Bar Chart of What-if Q1, Q2, Q3 Outcomes')

# Show the plot
plt.show()

