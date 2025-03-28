# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
      
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        # your code for determining the winner goes here
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2
        else:
            return 0
   
class MostVowels(WordGame):
    def __init__(self,rounds):
        super().__init__(rounds)
        self.vowels = ["a","e","i","o","u"]
    
    def round_winner(self, player1_word: str, player2_word: str):
        # your code for determining the winner goes here
        word_1 = []
        word_2 = []

        for player_char in player1_word:
            if player_char in self.vowels:
                word_1.append(player_char)
        
        for player_char in player2_word:
            if player_char in self.vowels:
                word_2.append(player_char)
                         
        if len(word_1) > len(word_2):
            return 1
        elif len(word_2) > len(word_1):
            return 2
        else:
            return 0
        
class RockPaperScissors(WordGame):

    def __init__(self, rounds):
        super().__init__(rounds)
        
    def round_winner(self, player1_word: str, player2_word: str):
        allowed_words = ["rock","paper","scissors"]

        if (player1_word not in allowed_words) and (player2_word not in allowed_words):
            return 
        
        if player1_word not in allowed_words: return 2
        if player2_word not in allowed_words: return 1

        if player1_word == "rock" and player2_word == "scissors":
            return 1
        elif player1_word == "paper" and player2_word == "rock":
            return 1
        elif player1_word =="scissors" and player2_word == "paper":
            return 1
        else:
            if player1_word == player2_word:
                return 
            else:
                return 2 

