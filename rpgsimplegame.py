# Choose your own adventure mini Python game
# This is the best way to start learning python 
# Python is pretty easy to learn

print("Welcome to your mini side quest!")
your_name = input("What is your name?: ")
your_age = int(input("What is your age?: "))
print("Hey,", your_name, "You say you are", your_age, "years old. I think you're lying to me.")
# is_older = your_age >= 18
# print(is_older)
if your_age >= 10:
    print("You are wayyy to young, where are your parents???")

if your_age >= 18:
    print("You are old enough to play.")

wants_to_play = input("Do you want to play tho? ").lower()
if wants_to_play == "yes":
    print("Sucka! You're soul is mine now!")

health = 15
print("You are starting with", health, " health. Good luck!")



# weapon = input("Pick a weapon(sword/gun/stick/rock):")
#    if weapon == "sword"

left_or_right = input("First Choice: Left or Right(left/right)?")
if left_or_right == "left":
    ans = input("Nice, you follow the path and reach a rock. You sit on it. Do you want to go around or swim across the lake in front of you? (across/around)? ")
    if ans == "across":
        print("You went across the lake but you got bit by a snake. You lost 10 health.")
        health -=10
    elif ans == "around":
        print("You decided to go take a walk but a snake bit you too! You lost 5 health. Sorry, nature doesn't like you for some strange reason.")
        health -= 5
    ans = input("You notice a small cabin and a river. Which do you to (river/house)? ")
    if ans == "house":
        print("You go to the house and are greeted by the owner. He doesn't like you and you lose 5 health.")
        health -= 5
        if health <= 0:
            print("You now have 0 health and you lose the game...")
    else:
        print("You fell in the river and lost...")
#    else:
#        print("You Lost!")




