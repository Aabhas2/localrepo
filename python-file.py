# Factorial
def fact(n):
    if n==1 or n==0: 
        return 1
    else:
        return n * fact(n-1)
    

print(fact(5))

# Check Prime
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
def generate_prime(num):
    primes = []
    for num in range(2,n+1):
        if isPrime(num):
            primes.append(num)
    return primes

n = int(input("enter a number: "))
primes = generate_prime(n)
print(f"Primes numbers between 1 and {n} are: {primes}")

# add and average
def add(list):
    sum = 0
    for i in list:
        sum += i 
    print(sum)

def average(list):
    total_sum = sum(list)
    avg = total_sum / len(list)
    print(avg)

numbers = [1,2,3,4,5]
add(numbers)
average(numbers)

# Sets 
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

#Union of sets
union_set = set1.union(set2)
print("Union:", union_set)

inter = set1.intersection(set2)
print("Intersection: ", inter)

diff = set1.difference(set2)
print("set1-set2: ", diff)

diff2 = set2.difference(set1)
print("set2-set1: ", diff2)

# Initial list of numbers
lst = [1, 2, 5, 6, 3, 5, 3, 3, 23, 12, 11, 90, 2, 4, 3, 24, 23, 11]

# Sorting the list
lst.sort()
print("Sorted list:", lst)

# ELEMENT COUNT DICTIONARY
# Counting specific element
count = 0
num = int(input("Enter the element: "))
for i in lst:
    if i == num:
        count += 1
print(f"Count of {num} is ", count)

# Creating a dictionary with element counts
element_count = {}
for i in lst:
    if i in element_count:
        element_count[i] += 1
    else:
        element_count[i] = 1

# Printing the dictionary
print("Element count dictionary:", element_count)

#swap first two and last two letters
def swap_ch(s):
    if len(s) < 4:
        return "string too short"
    new_s = s[-2:] + s[2:-2] + s[:2]
    return new_s

s = "elephant"
result = swap_ch(s)
print(result)

#10 indian cities in file 
ind_cities = ["Delhi","Mumbai","Noida","Bangalore","Chennai","Kolkata","Gurugram","Jaipur","Ahmedabad","Lucknow"]
with open("cities.txt", "w") as file1:
    for city in ind_cities:
        file1.write(city + "\n")

#5 lines about cllg file handling
print("File 'cities.txt' has been created with the names of ten indian cities.")

print("Tell us any five lines about your college!")
list = []
for i in range(1,6):
    para = str(input(f"Enter your line {i} about your college: "))
    list.append(para)
print("Here's the five lines you wrote: ", list)   
with open("college.txt","w") as file:
    for lines in list:
        file.writelines(lines + "\n")

print("File 'college.txt' has been created successfully")


#merge 3 input files 
input_files = ["employees1.txt","employees2.txt","employees3.txt"]
output_file = ["merged_employees.txt"]

with open("output_file","w") as outfile:
    for file_name in input_files:
        with open(file_name , 'r') as infile:
            outfile.writelines(infile.readlines())
            outfile.write("\n")

print(f"Data from {len(input_files)} input files has been merged into '{output_file}'.")

#VOWEL COUNT IN DICTIONARY 
vowel_count = {"a":0,"e":0,"i":0,"o":0,"u":0}

with open("output_file","r") as file:
    text = file.read().lower()
    for char in text:
        if char in vowel_count:
            vowel_count[char] += 1

print("Vowel Counts: ",vowel_count)

with open("vowel_output.txt","w") as outfile:
    outfile.write(str(vowel_count))

print("the vowel counts have been written to 'vowel_output.txt'.")

#csv DICTIONARY CODE
import csv 
students_data = [
    {"RollNo": 1, "Enrollment No": "EN12345", "Name": "Aman Gupta", "Course": "B.Sc Computer Science", "Semester": 3},
    {"RollNo": 2, "Enrollment No": "EN12346", "Name": "Riya Singh", "Course": "B.A Economics", "Semester": 2},
    {"RollNo": 3, "Enrollment No": "EN12347", "Name": "Vikram Kumar", "Course": "B.Com", "Semester": 1},
    {"RollNo": 4, "Enrollment No": "EN12348", "Name": "Sanya Kapoor", "Course": "B.Sc Physics", "Semester": 4},
    {"RollNo": 5, "Enrollment No": "EN12349", "Name": "Rahul Mehta", "Course": "B.A History", "Semester": 3},
]
csv_file = "students.csv"

fieldNames = ["RollNo","Enrollment No","Name","Course","Semester"]

with open(csv_file,"w",newline="") as file:
    writer = csv.DictWriter(file,fieldnames=fieldNames)
    writer.writeheader()
    writer.writerows(students_data)

print(f"The CSV file '{csv_file}' has been created with student data.")


#Write a Python program using tkinter library to create a GUI to enter registration 
#details for an event. 
import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Event Registration Form")
root.geometry("400x350")

# Function to handle form submission
def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    contact = entry_contact.get()
    event = event_var.get()

    if name == "" or email == "" or contact == "" or event == "":
        result_label.config(text="Please fill in all fields.", foreground="red")
    else:
        result_label.config(text=f"Registration successful!\nName: {name}\nEmail: {email}\nContact: {contact}\nEvent: {event}", foreground="green")
        clear_form()

# Function to clear form fields
def clear_form():
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_contact.delete(0, tk.END)
    event_var.set("Select Event")

# Create and place labels, entry fields, and buttons using ttk
ttk.Label(root, text="Event Registration Form", font=('Helvetica', 16)).pack(pady=10)

ttk.Label(root, text="Name").pack()
entry_name = ttk.Entry(root, width=40)
entry_name.pack()

ttk.Label(root, text="Email").pack()
entry_email = ttk.Entry(root, width=40)
entry_email.pack()

ttk.Label(root, text="Contact").pack()
entry_contact = ttk.Entry(root, width=40)
entry_contact.pack()

# Dropdown menu for selecting an event
ttk.Label(root, text="Select Event").pack()
event_var = tk.StringVar()
event_options = ["Workshop", "Seminar", "Conference"]
event_dropdown = ttk.Combobox(root, textvariable=event_var, values=event_options, state="readonly")
event_dropdown.pack()
event_var.set("Select Event")  # Set default option

# Submit and Clear buttons
ttk.Button(root, text="Submit", command=submit_form).pack(pady=10)
ttk.Button(root, text="Clear", command=clear_form).pack()

# Label to display the result
result_label = ttk.Label(root, text="", font=('Helvetica', 12))
result_label.pack(pady=20)

# Run the application
root.mainloop()


import tkinter as tk
from tkinter import ttk
import csv
import os

class LabelInput(tk.Frame):
    '''A widget that pairs a label with an input widget (Entry, Spinbox, etc).'''
    def __init__(self, parent, label, input_class=tk.Entry, **input_args):
        super().__init__(parent)
        
        # Create the label
        self.label = tk.Label(self, text=label)
        self.label.pack(side="left", padx=(0, 10))
        
        # Create the input widget (defaults to Entry)
        self.input = input_class(self, **input_args)
        self.input.pack(side="right", fill="x", expand=True)

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Form App")
        
        # Define the CSV file name
        self.filename = "form_data.csv"
        
        # Create a frame to hold the form
        self.form = tk.Frame(root)
        self.form.pack(padx=10, pady=10)
        
        # Create form inputs using LabelInput Class
        self.name_input = LabelInput(self.form, "Name")
        self.name_input.pack(pady=5)
        
        self.age_input = LabelInput(self.form, "Age", input_class=tk.Spinbox, from_=0, to=100)
        self.age_input.pack(pady=5)
        
        self.gender = LabelInput(self.form, "Gender", input_class=ttk.Combobox, values=["Male", "Female", "Others"], state="readonly")
        self.gender.pack(pady=5)
        
        # Checkbutton for Newsletter Subscription
        self.newsletter_var = tk.BooleanVar()
        self.newsletter_input = LabelInput(self.form, "Subscribe to Newsletter", tk.Checkbutton, variable=self.newsletter_var)
        self.newsletter_input.pack(fill="x", pady=5)
        
        # Education Radio Buttons
        self.val = tk.StringVar()
        self.education_frame = tk.Frame(self.form)
        self.education_frame.pack(pady=5)
        tk.Label(self.education_frame, text="Education:").pack(side="left")
        self.radio1 = tk.Radiobutton(self.education_frame, text="High School", variable=self.val, value="High School")
        self.radio2 = tk.Radiobutton(self.education_frame, text="Undergraduate", variable=self.val, value="Undergraduate")
        self.radio3 = tk.Radiobutton(self.education_frame, text="Graduate", variable=self.val, value="Graduate")
        self.radio1.pack(side="left", padx=5)
        self.radio2.pack(side="left", padx=5)
        self.radio3.pack(side="left", padx=5)
        
        # Create the Submit button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_form)
        self.submit_button.pack(pady=(10, 5), side="left", padx=(10, 5))
        
        # Create the Reset button
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_form)
        self.reset_button.pack(pady=(10, 5), side="right", padx=(5, 10))
        
    def submit_form(self):
        '''Submit form: get values and write them into a CSV file.'''
        name = self.name_input.input.get()
        age = self.age_input.input.get()
        gender = self.gender.input.get()
        subscribe = self.newsletter_var.get()
        education = self.val.get()
        
        if not name or not age or not gender or not education:
            print("Please fill in all fields!")
            return
        
        # Check if the file exists, if not write the header
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Age", "Gender", "Subscribe", "Education"])  # Writing the header
        
        # Append the data to the CSV file
        with open(self.filename, mode='a', newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, age, gender, subscribe, education])
        print(f"Data saved: Name: {name}, Age: {age}, Gender: {gender}, Subscribed to Newsletter: {subscribe}, Education: {education}")
        
        # Optionally reset the form after submission
        self.reset_form()
        
    def reset_form(self):
        '''Reset form: clear all input fields.'''
        self.name_input.input.delete(0, tk.END)
        self.age_input.input.delete(0, tk.END)
        self.gender.input.set("")
        self.newsletter_var.set(False)
        self.val.set("")
        
# Initialize the Tkinter app
root = tk.Tk()
app = MyApp(root)
root.mainloop()


#CALCULATOR CODE TKINTER 
import tkinter as tk
from tkinter import messagebox

# Function to perform the chosen operation
def calculate(operation):
    try:
        # Get the numbers from the input fields
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        # Perform the chosen operation
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2

        # Display the result
        label_result.config(text=f"Result: {result}")

    except ValueError as e:
        messagebox.showerror("Invalid input", f"Error: {e}")

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")

# Input fields and labels
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=10)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=10)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Buttons for operations
tk.Button(root, text="Add", command=lambda: calculate("add")).grid(row=2, column=0, padx=10, pady=10)
tk.Button(root, text="Subtract", command=lambda: calculate("subtract")).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Multiply", command=lambda: calculate("multiply")).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Divide", command=lambda: calculate("divide")).grid(row=3, column=1, padx=10, pady=10)

# Label to display the result
label_result = tk.Label(root, text="Result: ")
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)i

# Run the application
root.mainloop()


# CSV TKINTER 
import tkinter as tk
from tkinter import ttk
import csv

# Function to write student data to CSV
def write_to_csv():
    student_data = {
        "RollNo": entry_rollno.get(),
        "Enrollment No": entry_enrollment.get(),
        "Name": entry_name.get(),
        "Course": entry_course.get(),
        "Semester": entry_semester.get()
    }

    # Check if all fields are filled
    if not all(student_data.values()):
        result_label.config(text="All fields are required!", foreground="red")
        return

    # Write data to CSV
    with open("students.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=student_data.keys())
        # Write header only if file is empty
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(student_data)

    # Clear input fields
    for entry in [entry_rollno, entry_enrollment, entry_name, entry_course, entry_semester]:
        entry.delete(0, tk.END)

    result_label.config(text="Student data saved successfully!", foreground="green")

# Function to read and display data from CSV
def read_from_csv():
    try:
        with open("students.csv", "r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)

            # Clear the display area
            text_display.delete("1.0", tk.END)

            # Display data in the text widget
            for row in rows:
                display_text = f"Roll No: {row['RollNo']}, Enrollment No: {row['Enrollment No']}, "
                display_text += f"Name: {row['Name']}, Course: {row['Course']}, Semester: {row['Semester']}\n"
                text_display.insert(tk.END, display_text)
    except FileNotFoundError:
        text_display.delete("1.0", tk.END)
        text_display.insert(tk.END, "No CSV file found. Add student data first.")

# Create the main application window
root = tk.Tk()
root.title("Student Data Entry")

# Labels and Entry widgets for student details
tk.Label(root, text="Roll No:").pack(padx=10, pady=5)
entry_rollno = ttk.Entry(root, width=30)
entry_rollno.pack(padx=10, pady=5)

tk.Label(root, text="Enrollment No:").pack(padx=10, pady=5)
entry_enrollment = ttk.Entry(root, width=30)
entry_enrollment.pack(padx=10, pady=5)

tk.Label(root, text="Name:").pack(padx=10, pady=5)
entry_name = ttk.Entry(root, width=30)
entry_name.pack(padx=10, pady=5)

tk.Label(root, text="Course:").pack(padx=10, pady=5)
entry_course = ttk.Entry(root, width=30)
entry_course.pack(padx=10, pady=5)

tk.Label(root, text="Semester:").pack(padx=10, pady=5)
entry_semester = ttk.Entry(root, width=30)
entry_semester.pack(padx=10, pady=5)

# Button to save data
btn_save = tk.Button(root, text="Save Data", command=write_to_csv)
btn_save.pack(pady=10)

# Button to read data
btn_read = tk.Button(root, text="Show All Students", command=read_from_csv)
btn_read.pack(pady=10)

# Label to display success/error messages
result_label = tk.Label(root, text="", font=('Helvetica', 10))
result_label.pack(pady=5)

# Text widget to display student data
text_display = tk.Text(root, width=50, height=10)
text_display.pack(padx=10, pady=10)

# Run the application
root.mainloop()


# Age Calculator
import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Function to calculate age
def calculate_age():
    try:
        # Get the DOB from the input field
        dob = entry_dob.get()
        dob_date = datetime.strptime(dob, "%Y-%m-%d")  # Parse DOB in YYYY-MM-DD format
        today = datetime.today()  # Get the current date

        # Calculate age
        age = today.year - dob_date.year
        # Adjust if the birthday hasn't occurred yet this year
        if (today.month, today.day) < (dob_date.month, dob_date.day):
            age -= 1

        # Display the age
        label_result.config(text=f"Your Age: {age} years")

    except ValueError:
        label_result.config(text="Invalid Date Format! Use YYYY-MM-DD")

# Create the main application window
root = tk.Tk()
root.title("Age Calculator")

# Label and entry for DOB
tk.Label(root, text="Enter Date of Birth (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=10)
entry_dob = ttk.Entry(root, width=15)
entry_dob.grid(row=0, column=1, padx=10, pady=10)

# Button to calculate age
tk.Button(root, text="Calculate Age", command=calculate_age).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Label to display the result
label_result = tk.Label(root, text="Your Age: ")
label_result.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()

