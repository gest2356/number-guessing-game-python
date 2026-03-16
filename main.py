import random



def main():
    users_difficulty_input = 0
    number_to_gess = 10 # random.randint(1,100)
    number_guessed = False
    number_of_goes = 1
    while True:
        if number_to_gess == 1:
            print("Welcome to the Number Guessing Game!")
            print("I'm thinking of a number between 1 and 100.")
            print("Please select the difficulty level:")
            print("1. Easy (10 chances)")
            print("2. Medium (5 chances)")
            print("3. Hard (3 chances)")
            print("4. impossible (1 chance)")

            users_difficulty_input = input("Please enter a your choice:")
        elif number_to_gess == 2:
            print("I see, your first go didn't work out")
            print("dont worry, you can give it a shot agin, the number is still the same")
            print("Please select the difficulty level:")
            print("1. Easy (10 chances)")
            print("2. Medium (5 chances)")
            print("3. Hard (3 chances)")
            print("4. impossible (1 chance)")

            users_difficulty_input = input("Please enter a your choice:")
        elif number_to_gess > 2:
            print("It didn't work out again. That sucks.")
            print("go again you can do it :)")
            print("Please select the difficulty level:")
            print("1. Easy (10 chances)")
            print("2. Medium (5 chances)")
            print("3. Hard (3 chances)")
            print("4. impossible (1 chance)")

            users_difficulty_input = input("Please enter a your choice:")

        if users_difficulty_input == "1":
            for i in range(0, 10):
                user_gess = int(input("go on. Have a gess:"))
                if user_gess == number_to_gess:
                    print("You win!")
                    number_guessed = True
                    break

            if not number_guessed:
                print("You lost")
                number_of_goes += 1

        if users_difficulty_input == "2":
            for i in range(0, 5):
                user_gess = input("go on. Have a gess:")
                if user_gess == number_to_gess:
                    print("You win!")
                    number_guessed = True
                    break

            if not number_guessed:
                print("You lost")
                number_of_goes += 1


        if users_difficulty_input == "3":
            for i in range(0, 3):
                user_gess = input("go on. Have a gess:")
                if user_gess == number_to_gess:
                    print("You win!")
                    number_guessed = True
                    break

            if not number_guessed:
                print("You lost")
                number_of_goes += 1

        if users_difficulty_input == "4":
            for i in range(0, 1):
                user_gess = input("go on. Have a gess:")
                if user_gess == number_to_gess:
                    print("You win!")
                    number_guessed = True
                    break

            if not number_guessed:
                print("You lost")
                number_of_goes += 1



if __name__ == '__main__':
    main()