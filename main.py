print("Welcome!")

userName = input("Enter your name: ")
print(userName)

userAge = input("Enter your age: ")
print(userAge)

userCountry = input("Enter your country: ")
print(userCountry)

userFavFood = input("Enter your favourite food: ")
print(userFavFood)

userHobby = input("Enter your hobby: ")
print(userHobby)

prntReceipt = input("Would you like a receipt? (yes, no)")

if prntReceipt == "yes":
    print("-----------------------------")
    print("")
    print("Name: ", userName)
    print("Age: ", userAge)
    print("Country: ", userCountry)
    print("Favourite Food: ", userFavFood)
    print("Hobby: ", userHobby)
    print("")
    print("-----------------------------")
elif prntReceipt == "idk":
    print("idk either ¯\_(ツ)_/¯")
else:
    print("Thank you for using this program.")
