import requests
from email_validator import validate_email, EmailNotValidError
import json

class AI_clinic:
    def __init__(self,query,url="http://localhost:5678/webhook-test/54cb7296-5aeb-4bb0-9c6e-7d0b45c5b4d3"):
        self.query = query
        self.url = url


    def take_query(self,params):
        print(f"your query: {self.query} is being processed")
        self.response = requests.post(self.url , json = params)
        if self.response.ok:
            body = self.response.text
            return body
        return None

    def check_email(self, email):
        try:
            email_info = validate_email(email , check_deliverability=True)
            normalized_email = email_info.normalized
            return True , normalized_email
        except EmailNotValidError as e:
            return False , str(e)


def main():
    
    query = input("Enter your query : ")
    patient = AI_clinic(query)
    print("This is an AI assistant\nI can help with your basic queries\nIf your query falls under this category choose that option but before that")
    while True:
        print("To process your queries first enter patient Id and mail_id\n")
        try:
            id = int(input("Enter patient id : "))
            print("\n")
            mail_id = input("Mail Id: ")
            isValid , result = patient.check_email(mail_id)
            if isValid:
                print(f"valid email! Normalized version: {result}")
            else:
                print(f"Invalid email ! Reason: {result}")
                raise ValueError
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
            continue#can be done better by returning none ig

       
        print("1. to know about lab status\n")
        print("2. Next checkup\n")
        print("3. to Know about clinic hours\n")
        print("4. about appointment booking\n")
        print("5.Exit!")
        try:
            choice  = int(input("Enter your choice : "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.? or check the type of input given")
            continue

        if choice == 1:
            params = {
                "id":id,
                "intent":"lab_status",
                "mailID":mail_id
            }
            patient.take_query(params)
            null_output = patient.response.json()
            print(null_output['message'])
            try:
                option = input("Enter 'Y' to continue 'Q' to quit: ").lower()
                if option == 'y':
                    print("\nUnderstood")
                    continue
                elif option =='q':
                    print("\nExiting...")
                    break
                else:
                    raise ValueError("\nTaking it as a yes!!")
            except ValueError:
                print(ValueError)
                continue
        elif choice == 2:
            params = {
                "id":id,
                "intent":"next_checkup",
                "mailID":mail_id
            }
            patient.take_query(params)
            null_output = patient.response.json()
            print(null_output['message'])
            try:
                option = input("Enter 'Y' to continue 'Q' to quit: ").lower()
                if option == 'y':
                    print("\nUnderstood..")
                    continue
                elif option =='q':
                    print("\nExiting...")
                    break
                else:
                    raise ValueError("\nTaking it as a yes")
            except ValueError:
                print(ValueError)
                continue
        elif choice == 3:
            params = {
                "id":id,
                "intent":"clinic_hours",
                "mailID":mail_id
            }
            patient.take_query(params)
            null_output = patient.response.json()
            print(null_output['message'])
            try:
                option = input("Enter 'Y' to continue 'Q' to quit: ").lower()
                if option == 'y':
                    print("\nUnderstood..")
                    continue
                elif option =='q':
                    print("\nExiting...")
                    break
                else:
                    raise ValueError("\nTaking it as a yes")
            except ValueError:
                print(ValueError)
                continue
        elif choice == 4:
            params = {
                "id":id,
                "intent": "appointment_booking",
                "mailID":mail_id
            }
            patient.take_query(params)
            null_output = patient.response.json()
            print(null_output['message'])
            try:
                option = input("Enter 'Y' to continue 'Q' to quit: ").lower()
                if option == 'y':
                    print("\nUnderstood..")
                    continue
                elif option =='q':
                    print("\nExiting...")
                    break
                else:
                    raise ValueError("\nTaking it as a yes")
            except ValueError:
                print(ValueError)
                continue
        elif choice == 5:
            print("Exiting the AI assistant. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
            continue

main()
