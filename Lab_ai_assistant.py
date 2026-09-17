import requests
from email_validator import validate_email, EmailNotValidError
import json
from sentence_transformers import SentenceTransformer, util
from ollama import chat

class AI_clinic:
    def __init__(self,query,url="http://localhost:5678/webhook-test/54cb7296-5aeb-4bb0-9c6e-7d0b45c5b4d3",model_name='sentence-transformers/all-MiniLM-L6-v2' , chat_model_name = 'llama3.2'):
        self.query = query
        self.url = url
        self.model = SentenceTransformer(model_name)
        self.chat_model_name = chat_model_name
        self.prompt = f"""
        Classify the patient query into exactly ONE of these intents:

        lab_status
        next_checkup
        clinic_hours
        appointment_booking
        unknown

        Query: "{query}"

        Return ONLY the intent name.
        Do not explain your answer.
        Do not add punctuation.
        Do not add any other words.

        Intent:
        """

    def analyze_query(self):
        messages = [
            {
                "role": "user",
                "content": f"Analyze the following query with the follwing promp:\n{self.prompt}"
            }
        ]
        response = chat(model=self.chat_model_name, messages=messages)
        return response["message"]["content"]
    


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
    print("This is an AI assistant\nI can help with your basic queries")
    query = input("Enter your query : ")
    patient = AI_clinic(query)
    exit = True
    while exit:
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
        while True:
            try:
                response = patient.analyze_query()
                print(repr(response))
            except Exception as e:
                print(f"Error:{e}")
                continue

            if response == "lab_status":
                params = {
                    "id":id,
                    "intent":"lab_status",
                    "mailID":mail_id
                }
                patient.take_query(params)
                print("STATUS:", patient.response.status_code)
                print("RESPONSE:", repr(patient.response.text))
                null_output = patient.response.json()
                print(null_output['message'])
                try:
                    option = input("Enter 'Y' to continue 'Q' to quit: ").lower()
                    if option == 'y':
                        print("\nUnderstood")
                        continue
                    elif option =='q':
                        print("\nExiting...")
                        exit = False
                        break
                    else:
                        raise ValueError("\nTaking it as a yes!!")
                except ValueError:
                    print(ValueError)
                    continue
            elif response == "next_checkup":
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
                        exit = False
                        break
                    else:
                        raise ValueError("\nTaking it as a yes")
                except ValueError:
                    print(ValueError)
                    continue
            elif response == "clinic_hours":
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
                        exit = False
                        break
                    else:
                        raise ValueError("\nTaking it as a yes")
                except ValueError:
                    print(ValueError)
                    continue
            elif response == "appointment_booking":
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
                        exit = False
                        break
                    else:
                        raise ValueError("\nTaking it as a yes")
                except ValueError:
                    print(ValueError)
                    continue
            elif response == "unknown":
                print("This query wll be better handled by consulting the inquiry center!")
                try:
                    option = input("Enter 'Y' to continue 'Q' to quit: ").lower()
                    if option == 'y':
                        print("\nUnderstood..")
                        continue
                    elif option =='q':
                        print("\nExiting...")
                        exit= False
                        break
                    else:
                        raise ValueError("\nTaking it as a yes")
                except ValueError:
                    print(ValueError)
                    continue
            else:
                print("Exiting..!")
                exit = False
                break
        

main()
