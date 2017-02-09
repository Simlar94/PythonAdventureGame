import time
import sys
from enemies import *
from weapons import *
from attack import *


def tobecontinued():
    print("To be continued...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    sys.exit()


def staffstory():
    playerobj.damage = playerobj.damage + staff.damage

    print("")
    time.sleep(1)
    print("Jeff: It's time for you to move on... In the name of The Great Tree, I send you to The Ancient Forest!")
    print("")
    time.sleep(5)
    print("A vampire approaches you!")
    print("")
    time.sleep(1)
    print("Name: " + vampireeasy.name
          + "\n"
          + "HP: " + str(vampireeasy.hp)
          + "\n"
          + "Difficulty: " + vampireeasy.difficulty)

    while playerobj.hp and vampireeasy.hp > 0:
        print("")
        time.sleep(1)
        print("A: Attack\nB: Heal")
        print("")
        time.sleep(1)
        choice = input("Choice: ")

        while choice != "A" and choice != "B":
            choice = input("Invalid choice, please type A or B: ")

        if choice == "A":
                attackenemy(vampireeasy)
                print("")
                print("Smash! -" + str(playerobj.damage))
                time.sleep(1)
                print(vampireeasy.name + " has " + str(vampireeasy.hp) + " HP left.")
                print("")
                time.sleep(1)
                if vampireeasy.hp < 1:
                    Attack.checklife(vampireeasy)
                    print("")
                    time.sleep(1)
                    tobecontinued()
                else:
                    attackplayer(vampireeasy)
                    print("Swush!")
                    time.sleep(1)
                    print(vampireeasy.name + " attacked you! -" + str(vampireeasy.damage))
                    time.sleep(1)
                    print("You have " + str(playerobj.hp) + " HP left.")
        elif choice == "B":
            attackplayer(vampireeasy)
            Player.healplayer(playerobj)
            print("")
            print("You've regained " + str(playerobj.healingability) + " HP.")
            time.sleep(1)
            print(vampireeasy.name + " attacked you! -" + str(vampireeasy.damage))
            time.sleep(1)
            print("You have " + str(playerobj.hp) + " HP left.")

    if playerobj.hp < 1:
        Attack.checklife(playerobj)
        print("")
        time.sleep(1)
        tobecontinued()


def daggerstory():
    playerobj.damage = playerobj.damage + dagger.damage
    print("")
    print("Jeff: It's time for you to move on... In the name of The Great Tree, I send you to The Tomb of Kings!")


def swordstory():
    playerobj.damage = playerobj.damage + sword.damage

    print("")
    print("Jeff: It's time for you to move on... In the name of The Great Tree, I send you to The Vampire Manor!")


def part1():
    print("Welcome to The Elders' World, my name is Jeff.")
    print("")
    time.sleep(1)
    playerobj.name = input("What's your name?: ")
    print("")
    time.sleep(1)
    print("Welcome, " + playerobj.name + "!")
    print("")
    time.sleep(1)
    print("Your characteristics are:\nDamage: "
          + str(playerobj.damage)
          + "\nHP: " + str(playerobj.hp)
          + "\nAbility: Regain " + str(playerobj.healingability) + " HP")
    print("")
    time.sleep(5)
    print("Choose your weapon...")
    time.sleep(1)
    print("")
    print("A: " + staff.name + "\n" + staff.description)
    print("")
    print("B: " + dagger.name + "\n" + dagger.description)
    print("")
    print("C: " + sword.name + "\n" + sword.description)
    print("")

    playerchose = input("Choice: ")

    while playerchose != "A" and playerchose != "B" and playerchose != "C":
        playerchose = input("Invalid choice, please type A, B or C: ")

    if playerchose == "A":
        print("")
        time.sleep(1)
        print("You've chosen the " + staff.name + "!")
        staffstory()
    elif playerchose == "B":
        # print("")
        # time.sleep(1)
        # print("You've chosen the " + dagger.name + "!")
        print("")
        time.sleep(1)
        tobecontinued()
        # daggerstory()
    elif playerchose == "C":
        # print("")
        # time.sleep(1)
        # print("You've chosen the " + sword.name + "!")
        print("")
        time.sleep(1)
        tobecontinued()
        # swordstory()

part1()