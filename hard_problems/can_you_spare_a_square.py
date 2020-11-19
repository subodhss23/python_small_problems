''' Try to imagine a world in which you might have to stay home for 14days at any given time. Do you have 
    enough TP to make it through?

    Although the number of squares per roll of TP varies significantly, we'll assume each roll has 500 sheets,
    and the average person use 57 sheets per day.

    Create a function that will receive a dictionary with two key/values:

        - "people" -> Number of people in the household.
        - "tp" -> Number of rolls.

    Return a statement telling the user if they need to buy more TP!'''


def tp_checker(home):
    days = (500 * home['tp']//(home['people'] * 57))
    if days > 14:
        return "Your TP will last " + str(days) + " days, no need to panic!"
    return "Your TP will only last " + str(days) + " days, buy more!"


print(tp_checker({ "people": 4, "tp": 1 }))
print(tp_checker({ "people": 3, "tp": 20 }))
print(tp_checker({ "people": 4, "tp": 12 }))
print(tp_checker({ "people": 2, "tp": 4 }))