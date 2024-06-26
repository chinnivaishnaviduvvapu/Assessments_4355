# -*- coding: utf-8 -*-
"""LVADSUSR147_DUVVAPU CHINNI VAISHNAVI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WXQMjEZ0pR22UWphi4g-TRPVdqBdPN4Y
"""

#1
def cal_area(length,width):
  return length*width
def cat(area):
  if area<1000:
    return "Small property"
  elif area<2000:
    return "Medium property"
  else:
    return "Large property"
length=float(input("enter length inmeters"))
width=float(input("enter the width in meters"))
area=cal_area(length,width)
category=cat(area)
print("Area in meters is :",area)
print("Catergory type is :",category)



#2
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight.Eat more healthy foods"
    elif bmi < 25:
        return "Normal weight.Continue your diet plan"
    elif bmi < 30:
        return "Overweight.Reduce food quantity especially fats"
    else:
        return "Obese.Reduce food quantity especially fats and do excercuises regularly"
if __name__ == "__main__":
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    interpretation = interpret_bmi(bmi)

    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Interpretation: {interpretation}")

#3
report = {}
def add_update_student_record(student_id, student_name, grades):
    report[student_id] = {'name': student_name, 'grades': grades}
def retrieve_student_record(student_id):
    return report.get(student_id)
def print_student_report(student_id):
    student_record = retrieve_student_record(student_id)
    if student_record:
        print(f"Student ID: {student_id}")
        print(f"Name: {student_record['name']}")
        print("Grades:")
        for subject, grade in student_record['grades'].items():
            print(f"{subject}: {grade}")
    else:
        print("Student record not found.")
add_update_student_record(1, 'Alice', {'Math': 90, 'Science': 85, 'History': 88})
add_update_student_record(2, 'Bob', {'Math': 78, 'Science': 92, 'History': 85})

print_student_report(1)
print("\n")
print_student_report(2)

#4
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
df = pd.read_csv('movies.csv')
df['content_rating'] = df['content_rating'].apply(lambda x: content_rating_dict[x])
df['age_category'] = df['age_category'].apply(lambda x: age_category_dict[x])

vectorizer = TfidfVectorizer()
movie_vectors = vectorizer.fit_transform(df['description'])

similarity_matrix = cosine_similarity(movie_vectors)

def recommend_movies(movie_title, age_category):
    movie_index = df[df['title'] == movie_title].index[0]
    similarity_scores = list(enumerate(similarity_matrix[movie_index]))
    sorted_similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    recommended_movies = []
    for movie in sorted_similarity_scores:
        if df.iloc[movie[0]]['age_category'] <= age_category and df.iloc[movie[0]]['content_rating'] <= age_category:
            recommended_movies.append(df.iloc[movie[0]]['title'])
        if len(recommended_movies) >= 10:
            break
    return recommended_movies

#5
def even_subid(subids):
  a=[]
  for i in subids:
    if i%2==0:
      a.append(i)
  return a
subids=list(map(int,input("enter subscriber ids").split(",")))
target_audience=even_subid(subids)
print("Targeted even number subscriber ids are:",target_audience)

#6
class SecuritySystem:
  def __init__(self,password):
    self.password=password

  def passkey(self,a):
    if a==self.password:
      return True
password="vaishnavi"
obj=SecuritySystem(password)
while True:
  a=input("enter passkey")
  obj.passkey(a)
  if obj.passkey(a)==True:
    print("Password matched.Access granted")
    break
  print("Access denied.Check your password again and enter it")

#7
def avg_score(x):
  return sum(x)/len(x)
def feedback(averagescore):
  if averagescore<30:
    return "Very dissatisfied.Services need to be improved highly"
  elif averagescore<50:
    return "dissatisfied.Services need to be improved"
  elif averagescore<70:
    return "Good.No improvement needed"
  else:
    return "excellent.Keep it up"
x=[]
while True:
    feedbackscore=int(input("enter your feedback score:"))
    if feedbackscore==0000:
      print("feedback survey ended")
      break
    x.append(feedbackscore)
averagescore  =avg_score(x)
feed=feedback(averagescore)
print("Average score is:",averagescore)
print("Insights for improvement are:",feed)

#8
def filter_comments(s):
  count=0
  for i in s:
    for j in i:
      if j in ["a","e","i","o","u","A","E","I","O","U"]:
        count +=1
  return count

def remove_comments(counter):
  quality_comments=[]
  for i in s:
    if counter>2:
      quality_comments.append(s[i])
    return quality_comments
s=list((input("enter your comment").split(",")))
counter=filter_comments(s)
good_comments=remove_comments(counter)
print("quality comments left are:\n")
print(quality_comments)

#9
import datetime
import time
events = {
    "event1": {
        "name": "Birthday Party",
        "date": datetime.datetime(2024, 5, 1, 15, 0, 0),
        "alert": "Don't forget to bring a gift!"
    },
    "event2": {
        "name": "Project Deadline",
        "date": datetime.datetime(2024, 4, 30, 23, 59, 59),
        "alert": "Don't forget to submit your project!"
    }
}
def send_alert(event):
    print(f"Alert for {event['name']}: {event['alert']}")
for event_name, event_info in events.items():
    event_time = event_info["date"]
    schedule.every().day.at(event_time.time()).do(send_alert, event_info)

while True:
    schedule.run_pending()
    time.sleep(1)

#10
def calculate_loan_repayment(principal, annual_interest_rate, num_periods):
    try:
        monthly_interest_rate = annual_interest_rate / 12 / 100
        monthly_payment = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** num_periods) / ((1 + monthly_interest_rate) ** num_periods - 1)
        return round(monthly_payment, 2)
    except Exception as e:
        print(f"Error: {e}")
        return None

principal = 10000
annual_interest_rate = 5
num_periods = 60

monthly_payment = calculate_loan_repayment(principal, annual_interest_rate, num_periods)
if monthly_payment is not None:
    print(f"Monthly payment: {monthly_payment}")

#11
def validate_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid input. Please try again.")
valid_options = ["yes", "no"]
user_input = validate_input("Do you want to participate in the poll? (yes/no): ", valid_options)

if user_input == "yes":
    poll_question = "What is your favorite color?"
    valid_options = ["red", "green", "blue"]
    poll_vote = validate_input(f"{poll_question} (choose from {', '.join(valid_options)}): ", valid_options)
    print(f"Thank you for voting! Your vote for {poll_vote} has been recorded.")
else:
    print("Okay, no problem. Thanks for stopping by!")

#12
def scientific_calculator():
    while True:
        try:
            print("Scientific Data Processing Tool")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exit")

            choice = int(input("Enter your choice (1-5): "))

            if choice == 5:
                print("Exiting the program...")
                break

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == 1:
                result = num1 + num2
                print(f"Result: {result}")
            elif choice == 2:
                result = num1 - num2
                print(f"Result: {result}")
            elif choice == 3:
                result = num1 * num2
                print(f"Result: {result}")
            elif choice == 4:
                try:
                    result = num1 / num2
                    print(f"Result: {result}")
                except ZeroDivisionError:
                    print("Error: Division by zero is not allowed.")
            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")
scientific_calculator()

#13
import datetime
import logging
logging.basicConfig(filename='server_status_report.log', level=logging.INFO, format='%(asctime)s - %(message)s')
server_uptime=22
current_date = datetime.date.today()
#assume the uptime is a variable named `server_uptime`
status_report = f"Server Status Report - {current_date}\n\nServer uptime: {server_uptime}"

logging.info(status_report)

print("Status report has been generated and written to server_status_report.log.")

#14

with open('log_file.log', 'r') as f:
    # Read the contents of the file
print(log_contents)

#15