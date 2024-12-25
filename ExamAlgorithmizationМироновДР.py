import random

class NumberGame:
    def __init__(self):  
        self.score = 0  

    def play_round(self):
        program_numbers = random.sample(range(1, 25), 3)
        user_input = int(input("Введите одно число от 1 до 24: "))

        if user_input in program_numbers:
            self.score += 1  

        print(f"Числа программы: {program_numbers}. Попытка {'успешна' if user_input in program_numbers else 'неуспешна'}.")

    def play_game(self):
        for attempt in range(1, 4):
            print(f"Попытка {attempt}:")
            self.play_round()  

        if self.score >= 2:
            print("Вы выиграли!")
        else:
            print("Вы проиграли.")

def main():
    game = NumberGame() 
    game.play_game() 

if __name__ == "__main__":  
    main()

