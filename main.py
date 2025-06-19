import random
from multiprocessing.connection import answer_challenge


def random_number(min_num, max_num):
    return random.randint(a = min_num, b = max_num)

def input_number(it):
    num = int(input(f"{it}. Введите число от 1 до 100!: "))
    return num



def play_game():
    secret_num = random_number(0, 100)
    it = 0
    while True:
        it+=1
        people_num = input_number(it)

        if secret_num < people_num:
            print("Мен каткан сан кичине! ")
        elif secret_num > people_num:
            print("Мен каткан сан чон! ")
        elif secret_num == people_num:
            answer =  input(f"Мен каткан санды {it} аракет менен таптыныз! "
                  "\nКайра ойносузбу (о, ж)>>>>")
            if answer == "о":
                print("\n\n0=0=0 Новая Игра 0=0=0\n")
                play_game()
            elif answer == "ж":
                print("\n\nСпасибо за игру))\n")
                break
            else:
                print("Туура эмес команда жаздыныз. Кайра башынан баштаныз!!!")

def main():
    play_game()

main()


