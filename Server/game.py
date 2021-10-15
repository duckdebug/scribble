
from .player import Player
from .board import Board
from .round import Round
class game(object):

    def __init__(self,id ,player):
        """
        init the game! once player threshold is met
        :param id: int
        :param player: Player[]
        """
        self.id= id
        self.player = players
        self.words_used = []
        self.round = None
        self.board = None
        self.player_draw_ind = 0
        self.start_new_round()
    def start_new_round(self):
        """
        Start a new round with a new word
        :return: None
        """
        self.round =Round(self.get_word(), self.players[self.player_draw_ind])
        self.player_draw_ind += 1

        ifself.player_draw_ind >= len(self.player):
        self.end_round()
        self.end_game()

    def player_guess(self, player, guess):
        """
        Makes the player guess the word
        :param player: Player
        :param guess: str
        :return: bool
        """
        pass

    def player_disconnected(self, player):
        """
        Call to clean up objects when player disconnects
        :param player: Player
        :return: Exception()
        """
        pass

    def skip(self):
        """
        Increments the Round  skips, skips are greater than threshold new round.
        :return: None
        """
       if self.round:
           self.round.skips()

    def round_ended(self):
        pass

    def update_board(self):
        pass

    def end_game(self):
        pass

    def get_word(self):
        """
        gives a word that has not yet been used
        :return: str
        """
        # Todo get a list of words fron somewhere
        pass


