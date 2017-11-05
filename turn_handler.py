class Turn_Handler:
    def __init__(self, players):
        self.active_player, self.inactive_player = players

    def switch_turns(self):
        self.active_player, self.inactive_player = self.inactive_player, self.active_player
