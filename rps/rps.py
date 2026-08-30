import random
import sys

class RPS:
    def __init__(self):
        print('Welcome to Rock Paper Scissor!')

        self.moves:dict = {'rock':'🌑' , 'paper': '📄' , 'scissors':'✂'}
        self.valid_moves:list[str] = list(self.moves.keys())

    def play_game(self):
        user_move:str = input('Rock, Paper, Scissors ? ').lower()
        if user_move == 'exit':
            print('Thanks for playing!')
            sys.exit()

        if user_move not in self.valid_moves:
            print('Invalid moves ...')
            return self.play_game()

        ai_move:str = random.choice(self.valid_moves)
        self.display_move(user_move , ai_move)
        self.check_move(user_move , ai_move)

    def display_move(self, user_move:str, ai_move:str):
        print('===')
        print(f'You : {self.moves[user_move]}')
        print(f'AI : {self.moves[ai_move]}')
        print('===')

    def check_move(self , user_move:str, ai_move:str):
        if user_move == ai_move:
            print('It is a tie')
        elif user_move == 'rock' and ai_move == 'scissors':
            print('You win')
        elif user_move == 'scissors' and ai_move == 'paper':
            print('You win')
        elif user_move == 'paper' and ai_move == 'rock':
            print('You win')
        else:
            print('AI win')

