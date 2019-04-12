import csv
import datetime
import os
import utilities

if __name__ == "__main__":

    if not os.path.exists("output/welcome_letters"):
        os.makedirs("output/welcome_letters")

    with open ("output/teams.txt", "w") as file:
        file.write("")

    # Divide players into groups
    teams = {
        "trolls": {
            "team_name": "TROLLS",
            "roster": [],
            "practice_info": datetime.datetime(2019, 4, 20, 13)},

        "monkeys": {

        }

    }