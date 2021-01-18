class Battle:

    @staticmethod
    def fight(attacker, defender):
        """
        Determines the outcome of the battle between two knights

        Args:
            attacker (Knight): Knight that moves to the tile of of another knight
            defender (Knight): Knight that is already on the tile

        Returns:
            tuple: tuple of knights(winner, loser)
        """

        surprise_score = 0.5
        attacker.attack_score += surprise_score

        if attacker.item:
            attacker.attacker_score += attacker.item.attack

        if defender.item:
            defender.defence_score += defender.item.defence

        return (
            (attacker, defender)
            if attacker.attacker_score > defender.defence_score
            else (defender, attacker)
        )

    @staticmethod
    def kill_knight(knight, statusIdx):
        """Kills the knight and drop equiped item

        Args:
            knight (Knight)
            statusIdx (int): index of knight's status

        Returns:
            item, position
        """
        item = knight.item
        knight_pos = knight.position
        knight.update_knight_status(statusIdx)
        knight.position = None
        knight.attack_score = 0
        knight.defence_score = 0
        knight.item = None

        return item, knight_pos
