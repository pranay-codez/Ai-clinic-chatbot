import requests
import json

class AI_clinic:
    def __init__(self,query,url):
        self.query = query
        self.url = url


    def take_query(self,params):
        print(f"your query: {self.query} is being processed")
        response = requests.post(self.url , json = params)

def main():
    
    query = input("Enter your query.")
    patient = AI_clinic(query)
    print("This is an AI assistant.\nI can help with your basic queries,\n If your query falls under this category choose that option but before that")
    while True:
        print("To process your queries first enter patient Id!!")
        try:
            id = int(input("Enter patient id : "))
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
            continue#can be done better by returning none ig

        print("Patient Id and phone number accepted.")
        print("1. Patient Room no.")
        print("2. Discharge date.")
        print("3. to check Status for lab results")
        print("4. Next checkup date.")
        print("5.Exit!")
        try:
            choice  = int(input("Enter your choice : "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.? or check the type of input given")
            continue

        if choice == 1:
            params = {
                "value":1
            }
        elif choice == 2:
            params = {
                "value":2
            }
        elif choice == 3:
            params = {
                "value":3
            }
        elif choice == 4:
            params = {
                "value":4
            }
        elif choice == 5:
            print("Exiting the AI assistant. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
            continue

main()
