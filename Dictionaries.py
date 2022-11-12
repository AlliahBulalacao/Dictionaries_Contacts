# Display a menu of options
print("Menu:"
      "1 -> Add an item"
      "2 -> Search "
      "3-> Exit (Yes or No")

# Allow user to select item in the menu (check if valid)
select = input("Select your chosen menu (1-3): ")

# Perform the selected option

if select == 1:
      name = input("Full name: ")
      age = input("Age: ")
      org = input("Organization: ")
      contact = input("Contact Number:")
      address = input("Address: ")
      personal_info = {contact : address, age : org}
      information = {name : personal_info}