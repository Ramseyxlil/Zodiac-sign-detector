import datetime

# Ask the user for their birth year and convert it to an integer
birth_year = int(input("What year were you born in? "))

# Calculate the user's age
current_year = datetime.datetime.now().year
age = current_year - birth_year

# Print the user's age
print("You are approximately", age, "years old.")

# Ask the user for their birth month and day and convert them to integers
birth_month = int(input("What month were you born in (number between 1-12)? "))
birth_day = int(input("What day of the month were you born on? "))

# Create a dictionary of zodiac signs and their corresponding date ranges
zodiac_signs = {
    "Aquarius": (1, 20, 2, 18),
    "Pisces": (2, 19, 3, 20),
    "Aries": (3, 21, 4, 19),
    "Taurus": (4, 20, 5, 20),
    "Gemini": (5, 21, 6, 20),
    "Cancer": (6, 21, 7, 22),
    "Leo": (7, 23, 8, 22),
    "Virgo": (8, 23, 9, 22),
    "Libra": (9, 23, 10, 22),
    "Scorpio": (10, 23, 11, 21),
    "Sagittarius": (11, 22, 12, 21),
    "Capricorn": (12, 22, 1, 19)
}

# Determine the user's zodiac sign based on their birthdate
for sign, (start_month, start_day, end_month, end_day) in zodiac_signs.items():
    if (birth_month == start_month and birth_day >= start_day) or (birth_month == end_month and birth_day <= end_day):
        zodiac_sign = sign
        break

# Print the user's zodiac sign
print("Your zodiac sign is", zodiac_sign + ".")
