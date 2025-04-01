#Updated 1 Feb 2025
#Watch the video here: https://www.youtube.com/watch?v=YKxvDL3JxEA or follow the instructor led demo
#Implement all the code shown in the video.
#Modify the code so the checks from 12 and under for the $8 price tag
#and 62 and older for the $12 price tag.

# Input age
age = int(input("Please enter your age: "))

# Determine price based on age
if age <= 12:
    price = 8
elif age >= 62:
    price = 12
else:
    price = 15  # Default price for others

# Display the result
print(f"The ticket price for age {age} is ${price}.")
