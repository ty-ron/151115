# 151115_q1.py

# Import necessary libraries
import json

# Function to add a new patient
def add_patient(patients):
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    illness = input("Enter patient's illness: ")
    patient = {"name": name, "age": age, "illness": illness}
    patients.append(patient)
    print("Patient added successfully!")

# Function to display all patients
def display_patients(patients):
    if not patients:
        print("No patients found.")
    else:
        for patient in patients:
            print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")

# Function to search for a patient by name
def search_patient(patients, name):
    for patient in patients:
        if patient["name"].lower() == name.lower():
            print(f"Found patient - Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
            return
    print("Patient not found.")

# Function to remove a patient by name
def remove_patient(patients, name):
    for patient in patients:
        if patient["name"].lower() == name.lower():
            patients.remove(patient)
            print(f"Removed patient {name}")
            return
    print("Patient not found.")

# Function to load patients from a JSON file
def load_patients(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save patients to a JSON file
def save_patients(filename, patients):
    with open(filename, 'w') as file:
        json.dump(patients, file)

def main():
    filename = 'patients.json'
    patients = load_patients(filename)
    
    while True:
        print("\nHospital Patient Management System")
        print("1. Add a new patient")
        print("2. Display all patients")
        print("3. Search for a patient by name")
        print("4. Remove a patient by name")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_patient(patients)
        elif choice == '2':
            display_patients(patients)
        elif choice == '3':
            name = input("Enter patient's name to search: ")
            search_patient(patients, name)
        elif choice == '4':
            name = input("Enter patient's name to remove: ")
            remove_patient(patients, name)
        elif choice == '5':
            save_patients(filename, patients)
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
