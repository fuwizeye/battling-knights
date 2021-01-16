class Battle:

    @staticmethod
    def fight(attacker, defender):
        """Determines the outcome of the battle between two knights

        Args:
            attacker (Knight): Knight that moves to the tile of of another knight
            defender (Knight): Knight that is already on the tile
        """
        attacker.attack_score += 0.5
