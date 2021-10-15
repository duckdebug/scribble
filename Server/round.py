 import time as t
from thread import *
from .game_import Game
from .chat_import Chat

 class Round(object):
     def __init__(self, word ,player_drawing, players):
         """
         intit object
         :param word: str
         :param player_drawing: Player
         :param players: Player[]
         """
         self.word=word
         self.player_drawing= player_drawing
         self.player_guessed= []
         self.skips =0
         self.player_score ={player:0 for player in players}
         self.time =75
         self.chat = Chat(self)
         start_new_thread(self.time_thread, ())

     def time_thread(self):
         """
         Runs in thread to keep track of time
         :return: None
         """
         while self.time >0:
             time.sleep(1)
             sleep.time -=1
           seld.end_round("Time is up")

     def guess(self, player ,wrd):
         """
         :return bool if player got guess correct
         :param player: Player
         :param wrd: str
         :return: bool
         """
         correct= wrd == self.word
         if correct:
             self.player_guessed.append(player)
             # TODO implement scoreing System here

     def player_left(selfself,player):
         """
         removes player that left from scores and list
         :param player: Player
         :return: None
         """
         # might not be able to use player as key in dict
         if player in self.player_scores:
             del sef.player_scores[player]

         if player in self.player_guessed:
             self.player_guessed.remove(player)

         if player ==self.player_drawing:
             self.end_round(Drawing player leaves)

     def end_round(self):
         # TODO implement end_round functionality
         pass

