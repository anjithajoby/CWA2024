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
                      columns=['light_min', 'light_max', 'light_mean'])
    return model.predict(df)[0]
# Training the model

# Load your dataset
data = pd.read_csv('AR1-3_105636.csv')

# Define your independent variables (features) and dependent variable (target)
X = data[['light_min', 'light_max', 'light_mean']]
Y = data['avg_mood']

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
phoneanxiety_wellbeing = int(input("Enter the amount of blue light you receive from your phone.It can be any integer from 0-300. "))
mental_wellbeing = float(input("Enter how much time you spend to yourself. Can be anything from 0-24 "))
sleep_wellbeing = float(input("Enter how much sleep you get in a day. Can be anything from 0-24 "))

predicted_mood = round(predict_mood(phoneanxiety_wellbeing, mental_wellbeing, sleep_wellbeing)) # Example values
print("\n Your mood score for the values you entered are", predicted_mood)

#WHAT-IF Question 1
# What is will your mood be with low values of all three parameters?
print("-----------------------------------------------------------")
print("What-if Question 1")
print("Let's test how much blue light the user receives from their phone ")
# Low values for all 3 parameters
phonelight = predict_mood(phoneanxiety_wellbeing, mental_wellbeing, sleep_wellbeing)  # Example values
print("\n The amount of blue light the user receives is ", phonelight)
def interpret_mood(bluelight):
    if bluelight >= 9:
        return "This is too much blue light exposure. Put that phone down right now, your snaps can wait."
    elif 5 <= bluelight < 9:
        return "This isn't too bad. Why don't you read a book? You will have less strain on your eyes."
    else:
        return "This is better. Try and go for longer periods without your phone"
phonelight = interpret_mood(phoneanxiety_wellbeing)
# WHAT-IF Question 2
# What is will your mood be with high values of all three parameters?
print("-----------------------------------------------------------")
print("What-if Question 2")
print("Let's test how much time the user spends to theirself")
# High values for all 3 parameters
mentalhealth = predict_mood(phoneanxiety_wellbeing, mental_wellbeing, sleep_wellbeing)  # Example values
print("\n The amount of time the user spends to theirself is ", mentalhealth)
def interpret_mood(mental):
    if mentalhealth >= 9:
        return "This is brilliant. Spending time with yourself can improve your mental health."
    elif 5 <= mentalhealth < 9:
        return "Okay you can do better. Engage in activities that bring you relaxation. It's important to give yourself a break."
    else:
        return "No this is not good. Try and just spend a few minutes to yourself. You will see huge improvements in your mental health."
mentalhealth = interpret_mood(mental_wellbeing)
# WHAT IF QUESTION 3
# What variable is more important
print("-----------------------------------------------------------")
print("What-if Question 3")
print("Let's test how much sleep the user gets in a day")
sleep = predict_mood(phoneanxiety_wellbeing, mental_wellbeing, sleep_wellbeing)  # Example values
print("\n The score mood is", round(sleep))
def interpret_mood(mental):
    if sleep >= 9:
        return "Keep this up. Sleeping is good for you, and you won't have eyebags if you sleep this long."
    elif 5 <= sleep < 9:
        return "Okay this isn't bad. Make sure you go to bed on time and don't be on your phone before you sleep"
    else:
        return "Please tell me your joking. If it's because of the phone you don't sleep well, then leave your phone in another room before you get ready to go to sleep"
sleep = interpret_mood(sleep_wellbeing)



# Baseline 
print("")


#------------------------------------
# AR3 Show Results of WHAT IF on a graph for Questions 1 & 2

# Data: names of the variables and their values
variable_names = ['BlueLight', 'Mental', 'SleepTime']
values = [phoneanxiety_wellbeing, mental_wellbeing, sleep_wellbeing]

# Creating the bar chart
plt.bar(variable_names, values)

# Adding labels and title
plt.xlabel('Wellbeing')
plt.ylabel('Predictions')
plt.title('Bar Chart of What-if Q1, Q2, Q3 Outcomes')

# Show the plot
plt.show()
