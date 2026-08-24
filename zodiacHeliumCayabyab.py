#birthyear input and initialization of zodiac list
try:#error handling for non-integer inputs
    birthyear = int(input("Enter your birth year: "))
except ValueError:
    print("Invalid input. Please enter an integer value for the birth year.")
    exit()
zodiacs = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)",
           "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", 
           "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]

#function initialization
    #checkzodiac uses % function to determine the chinnese zodiac of person.
def checkzodiac(year):
    zodiac = (year - 1900) % 12
    return zodiacs[zodiac]
    #validateyear uses conditions to ensure no birthyears are included below 1900 and above current year.
def validateyear(year):
    if year < 1900 or year > 2026:#i added an additional 2026 condition to account for people that input years beyond the current one
        return "Invalid year, it should not be earlier than 1900 nor greater than the current year."
    else:
        return f"Your Chinese Zodiac Sign is: {checkzodiac(year)}"#integrating the checkzodiac function to the validateyear function to make the code more efficient.
    
#run the functions
print(validateyear(birthyear))