# Function to get user data
def get_user_data():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    city = input("Enter your city: ")

    return name, age, city


# Function to print user data
def print_user_data(name, age, city):
    print("\n----- User Details -----")
    print("Name :", name)
    print("Age  :", age)
    print("City :", city)


# Main function
def main():
    name, age, city = get_user_data()
    print_user_data(name, age, city)


# Run the program
main()