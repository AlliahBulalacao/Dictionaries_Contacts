# Dictionary

name = input("Full name: ")
contact = int(input("Contact Information: "))
age = int(input("Age: "))
address = input("Address: ")
org = input("Organization: ")

info = {"Contact Information": contact,
        "Age" : age,
        "Address" : address,
        "Organization" : org
}
information = {
      "Full name" : name,
      "Personal Info" : info
}
print(info)
print(information)

# Display a menu of options
print("Menu: \n"
      "1 -> Add an item\n"
      "2 -> Search \n"
      "3-> Exit (Yes or No)")

# Allow user to select item in the menu (check if valid)
# Perform the selected option
while True:
      select = input("Select your chosen menu (1-3): ")
      if select == 1:
            add_name = input("Full Name: ")
            add_age = input("Age: ")
            add_address = input("Address: ")
            print(information)
