import random


class InitGame:
    player_hand = 7

    def __init__(self):
        self.element_set = None
        self.user = None
        self.bot = None
        self.first_player = None
        self.snake = None
        self._generate()

    def _generate(self):
        while not self.first_player:
            self._generate_status()
            self.first_player = self._define_first_player()

    def _define_first_player(self):
        user_doubles = sorted(
            filter(lambda x: x[0] == x[1], self.user),
            reverse=True
        )
        bot_doubles = sorted(
            list(filter(lambda x: x[0] == x[1], self.bot)),
            reverse=True
        )

        if not (user_doubles or bot_doubles):
            return None

        if user_doubles and (not bot_doubles or
                             user_doubles[0] > bot_doubles[0]):
            self.snake = user_doubles[0]
            self.user.remove(self.snake)
            return "computer"

        self.snake = bot_doubles[0]
        self.bot.remove(self.snake)
        return "player"

    def _generate_status(self):
        self.element_set = self._generate_set()
        self.user = self._get_piece(self.element_set, self.player_hand)
        self.bot = self._get_piece(self.element_set, self.player_hand)

    def _generate_set(self):
        element_set = []
        for i in range(7):
            for j in range(i, 7):
                element_set.append([i, j])
        return element_set

    def _get_piece(self, element_set, n):
        piece = []
        for i in range(n):
            element = random.choice(element_set)
            element_set.remove(element)
            piece.append(element)
        return piece


class Game:
    def __init__(self):
        self._init_game = InitGame()
        self._player = self._init_game.user
        self._computer = self._init_game.bot
        self._element_set = self._init_game.element_set
        self._turn = self._init_game.first_player
        self._snake = [self._init_game.snake]

    def run(self):
        self._print_status()
        while True:
            if self._turn == "player":
                self._player_turn()
            else:
                self._computer_turn()

            if self._is_end_game():
                if not self._player:
                    status = "The game is over. You won!"
                elif not self._computer:
                    status = "The game is over. The computer won!"
                else:
                    status = "The game is over. It's a draw!"
                self._print_status(status)
                break

            self._turn = "computer" if self._turn == "player" else "player"
            self._print_status()

    def _is_end_game(self):
        if not self._player or not self._computer:
            return True
        return self._analyse_snake()

    def _analyse_snake(self):
        if len(self._snake) < 7:
            return False

        element_dict = {}
        for x, y in self._snake:
            element_dict[x] = element_dict.get(x, 0) + 1
            element_dict[y] = element_dict.get(y, 0) + 1
        if sorted(list(element_dict.values()))[-1] == 8:
            return True
        return False

    def _computer_turn(self):
        input()
        rare_dict = self._generate_numbers_rarity()
        element_scores = [[el, rare_dict[el[0]] + rare_dict[el[1]]] for el in self._computer]
        element_scores = sorted(element_scores, key=lambda item: item[1], reverse=True)

        for el, _ in element_scores:
            index = self._computer.index(el)
            if self._move_element(self._snake, self._computer, index, True):
                return
            if self._move_element(self._snake, self._computer, index, False):
                return
        self._move_element(self._computer, self._element_set)

    def _generate_numbers_rarity(self):
        rarity = {}
        for x, y in self._snake + self._computer:
            rarity[x] = rarity.get(x, 0) + 1
            rarity[y] = rarity.get(y, 0) + 1
        return rarity

    def _player_turn(self):
        res = False
        while not res:
            turn = self._player_input_validation()
            if turn == 0:
                self._move_element(self._player, self._element_set)
                break
            res = self._move_element(self._snake, self._player, abs(turn) - 1, turn > 0)
            if not res:
                print("Illegal move. Please try again.")

    def _player_input_validation(self):
        turn = None
        while turn is None or abs(turn) > len(self._player):
            try:
                turn = int(input())
                if abs(turn) > len(self._player):
                    raise ValueError
            except ValueError:
                print("Invalid input. Please try again.")
        return turn

    def _move_element(self, dst, src, el_number=None, dst_end=True):
        if len(src) < 1:
            return False

        element = random.choice(src) if el_number is None else src[el_number]

        if el_number is None:
            dst.append(element)
            src.remove(element)
            return True

        set_element = self._player_choise_validation(element, dst_end)
        if set_element is None:
            return False
        src.remove(element)

        dst.append(set_element) if dst_end else dst.insert(0, set_element)
        return True

    def _player_choise_validation(self, element, dst_end):
        connect_element = self._snake[-1][1] if dst_end else self._snake[0][0]
        if connect_element not in element:
            return None
        if dst_end and connect_element == element[0]:
            return element
        if not dst_end and connect_element == element[-1]:
            return element
        return [element[-1], element[0]]

    def _print_status(self, status=None):
        snake = self._snake
        if len(snake) > 6:
            snake = list(map(str, self._snake[:3])) + ["..."]
            snake += list(map(str, self._snake[-3:]))
        snake = "".join(list(map(str, snake)))

        player_pieces = "\n".join([
            f"{i}:{self._player[i - 1]}"
            for i in range(1, len(self._player) + 1)
        ])

        if status is None:
            status_player = "It's your turn to make a move. " \
                            "Enter your command."
            status_computer = "Computer is about to make a move. " \
                              "Press Enter to continue..."
            status = status_player if self._turn == 'player' else status_computer

        print('\n'.join([
            "=" * 70,
            f"Stock size: {len(self._element_set)}",
            f"Computer pieces: {len(self._computer)}\n",
            f"{snake}\n",
            f"Your pieces:\n",
            f"{player_pieces}\n",
            f"Status: {status}"
        ]))


def main():
    domino = Game()
    domino.run()


if __name__ == "__main__":
    main()
