# Dictionary
contact_dict = {
            "Lee":{
            "Full Name": "Lee Seokmin",
            "Age": 25,
            "Address": "Japan",
            "Contact Number": "09876543211",
            "Organization/Group": "Seventeen",
            "Birthday": "February 18, 1997",
            "Fully Vaccinated (Yes or No)": "Yes"
}}

print(contact_dict)

# Display a menu of options
print("\nMenu: \n"
      "1 -> Add an item\n"
      "2 -> Search \n"
      "3-> Exit (Yes or No)\n\n")

# Allow user to select item in the menu (check if valid)
# Perform the selected option
while True:
      select = input("Select your chosen menu (1-3): ")

#Option 1: Ask personal data for contact tracing(Listed are sample only, add more).
# Use dictionary to store the info. Use the full name as key. The value is another dictionary
# of personal information.

      if select == '1':
            print("=====CONTACT TRACING INFORMATION=====")
            name = input("Full name: ")
            contact = int(input("Contact Number: "))
            age = int(input("Age: "))
            address = input("Address: ")
            org = input("Organization: ")
            bday = input("Birthday: ")
            vacci_status = input("Fully Vaccinated (Yes or No): ")

            new_info_dict = {"Full Name": name,
                  "Contact Number": contact,
                  "Age": age,
                  "Address": address,
                  "Organization": org,
                  "Birthday": bday,
                  "Vaccination Status": vacci_status
            }
            print(new_info_dict)
            contact_dict.update(new_info_dict)
            print("Contact Information:", contact_dict)

# Option 2: Search, ask full name then display the record

      elif select == '2':
            print("=====CONTACT TRACING INFORMATION=====")
            search = input("Whose record do you want to find? ")
            for search in contact_dict:
                  print(search, contact_dict[search])

# Option 3: Ask the user if want to exit or retry.

      elif select == "3":
            print("Thank you! Keep safe!")
            break

      else:
            print("Try again!")
            continue
