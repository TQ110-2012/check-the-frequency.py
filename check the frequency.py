test_dict = {'Codingal' : 3, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
print("Test Dictionary:", test_dict)

user_input = input("Enter the value you want to check the frequency of: ")

try:
    search_value = int(user_input)
except ValueError:
    search_value = user_input

frequency = list(test_dict.values()).count(search_value)

print(f"Frequency of {search_value} is: {frequency}")
