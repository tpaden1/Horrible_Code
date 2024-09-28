import random
def bad_fortune_teller():
    print("I WILL TELL YOUR FORTUNE!")
    #I am adding this comment to change things for the commit
    inpoot = input("TYPE YOUR NAME: ")
    print("HELLO " + inpoot + "! I WILL TELL YOUR FORTUNE!")
    # Below is a bad name for the list, violates clean code
    rick_and_morty_season_6_5 = [
        "YOU WILL BE LUCKY!",
        "YOU WILL BE NEARLY LUCKY!",
        "YOU WILL BE UNLUCKY!",
        "YOU WILL LOSE $20!",
        "YOU WILL WRITE A LETTER TO YOUR BOSS!",
        "YOU WILL GET A PROMOTION!",
        "YOU WILL GET A BONUS!",
        "YOU WILL LOSE YOUR JOB!",
        "YOU WILL GET AN INTERNSHIP!",
        "YOU WILL GET A JOB!",
        "YOU WILL FAIL 3155 BECAUSE OF LATE WORK!",
        "YOU WILL SLEEP THROUGH ALL ALARMS!",
        "YOU WILL GET A BACHELOR'S DEGREE!",
        "YOU WILL GET A MASTER'S DEGREE!",
        "YOUR PARTNER WILL LEAVE YOU!",
        "YOU WILL MEET YOUR FUTURE SPOUSE IN A LINE!"
    ]
    # Above is some fortunes to give to the user
    extra_feature_unused = input("TYPE A FORTUNE YOU WANT: ")
    days_since_fortune = 12 / 365
    # Above is some useless code

    if int(input("TYPE YOUR AGE: ")) > 18:
        print("I see that you are of legal age. I will guess your future now. GOOD LUCK!")
        print(random.choice(rick_and_morty_season_6_5))
        print("THANKS FOR TRYING MY PROGRAM!" + inpoot + "GOOD LUCK >:)")
        johhny_boy = input("TYPE YES TO REPEAT: ")
        # Above is bad variable name (violates clean code)
        if johhny_boy == "YES":
            bad_fortune_teller()
        else:
            exit(0)


    else:
        print("YOU ARE NOT OF LEGAL AGE! YOUR FUTURE IS NOT PREDICTABLE YET!\n YOU ARE BANISHED FROM THE PROGRAM!")
        exit(0)


bad_fortune_teller()
