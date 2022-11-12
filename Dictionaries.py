# Dictionary

contact_info = {
      "Full Name: ": "Lee Seokmin",
      "Age: ": 25,
      "Address:": "Japan",
      "Contact Number:": "09876543211",
      "Organization/Group:": "Seventeen",
      "Birthday": "February 18, 1997",
      "Fully Vaccinated (Yes or No)": "Yes"
}
print(contact_info)

# Display a menu of options
print("\nMenu: \n"
      "1 -> Add an item\n"
      "2 -> Search \n"
      "3-> Exit (Yes or No)\n\n")

# Allow user to select item in the menu (check if valid)
# Perform the selected option
while True:
      select = input("Select your chosen menu (1-3): ")

      if select == '1':
            name = input("Full name: ")
            contact = int(input("Contact Information: "))
            age = int(input("Age: "))
            address = input("Address: ")
            org = input("Organization: ")

            info = {"Contact Information": contact,
                    "Age": age,
                    "Address": address,
                    "Organization": org
                    }
            information = {
                  "Full name": name,
                  "Personal Info": info
            }
            print(contact_info.update(information))

