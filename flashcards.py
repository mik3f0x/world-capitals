from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model
from main import Country
import random

def capitals_game():

    countries = []

    for country in Country.select():
        country_dict = {
            'name': country.name,
            'capital': country.capital,
            # Add other attributes as needed
        }
        countries.append(country_dict)

    correct = 0
    incorrect = 0

    random.shuffle(countries)

    print("Guess the capitals of each country and test your knowledge!")

    for i in range(0, len(countries)):
        guess = input(f"What is the capital of {countries[i]['name']}: ")

        answer = countries[i]["capital"]

        while guess != answer:
            incorrect += 1
            guess = input(f"WRONG!\nCorrect: {correct} Incorrect: {incorrect}\nWhat is the capital of {countries[i]['name']}: ")

        correct += 1
        print(f"RIGHT!\nCorrect: {correct} Incorrect: {incorrect}")

    print(f"Your final score is {correct - incorrect}!")
    new_game = input('Would you like to play again? Yes (y) or No (n): ')

    if new_game == 'y':
        capitals_game()
    else:
        print("Thank you for playing my game! Goodbye!")

capitals_game()