class Game_Handler:
    """Handles Turns in the game.

    :param players: The players in the game.
    """

    def __init__(self, players):
        self.players = players
        self.active_player, self.inactive_player = self.players
        self.winner = None

    def switch_turns(self):
        """When a player's actions are done, switch which player is the active player.
        """
        self.active_player, self.inactive_player = self.inactive_player, self.active_player
        return self.active_player
    def game_over(self):
        """Checks to see if a player is no longer alive.
        """
        for num, player in enumerate(self.players, 1):
            if not player.alive():
                self.winner = 'Winner: Player ' + str(num)
                return True


# def check_players():
#     for i in range(len(players)):
#         if not players[i].alive():
#             font = pg.font.Font(os.path.join('font', 'kindergarten.ttf'), 48)
#             text = font.render(
#                 'Winner: Player ' + ('1' if i == 1 else '2'), False, pg.Color('black'))
#             display.blit(text, text.get_rect(center=(width / 2, height / 2)))
