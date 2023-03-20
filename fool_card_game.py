import random


class Fool_enc:

    def __init__(self):
        cards = {1: 6, 2: 7, 3: 8, 4: 9, 5: 10, 6: 'Jack', 7: 'Queen', 8: 'King', 9: 'Ace'}

        self.__my_card = []
        self.my_keys = []

        self.__pc_card = []
        self.pc_keys = []

        for i in range(6):
            random_card = random.choice(list(cards.items()))
            self.__my_card.append(random_card[1])
            self.my_keys.append(random_card[0])

        for i in range(6):
            random_card = random.choice(list(cards.items()))
            self.__pc_card.append(random_card[1])
            self.pc_keys.append(random_card[0])

    #        print('Ваши карты: ', str(self.my_keys))
    #        print('Карты компьютера: ', str(self.pc_keys))

    def set_my_card(self, card1, card2, card3, card4, card5, card6):
        if (card1 or card2 or card3 or card4 or card5 or card6 > 0) & (card1 or card2 or card3 or card4 or card5 or card6 < 10):
            self.__my_card.append(card1)
            self.__my_card.append(card2)
            self.__my_card.append(card3)
            self.__my_card.append(card4)
            self.__my_card.append(card5)
            self.__my_card.append(card6)
        else:
            print('Карты введены неверно! Введите шесть карт от 1 до 9')

    def get_my_card(self):
        return self.__my_card

    def set_pc_card(self, card1, card2, card3, card4, card5, card6):
        if (card1 or card2 or card3 or card4 or card5 or card6 > 0) & (card1 or card2 or card3 or card4 or card5 or card6 < 10):
            self.__pc_card.append(card1)
            self.__pc_card.append(card2)
            self.__pc_card.append(card3)
            self.__pc_card.append(card4)
            self.__pc_card.append(card5)
            self.__pc_card.append(card6)
        else:
            print('Карты введены неверно! Введите шесть карт от 1 до 9')

    def get_pc_card(self):
        return self.__pc_card

    def my_move(self):
        move_random_card = random.choice(self.__my_card)
        index_card = self.__my_card.index(move_random_card)
        print("Ваш ход:", self.__my_card[index_card])
        my_move = self.my_keys[index_card]

        for i in self.pc_keys:
            if i > my_move:
                index_card_pc = self.pc_keys.index(i)
                self.pc_keys.remove(i)
                self.__pc_card.pop(index_card_pc)
                index_card_my = self.my_keys.index(my_move)
                self.my_keys.remove(my_move)
                self.__my_card.pop(index_card_my)
                return "Карты отбиты!"
                break
            elif i < my_move:
                continue
            else:
                index_card_my = self.my_keys.index(my_move)
                card_my_move = self.__my_card[index_card_my]
                self.pc_keys.append(my_move)
                self.__pc_card.append(card_my_move)
                self.my_keys.remove(i)
                self.__my_card.pop(index_card_my)
                return 'Карты приняты!'

    def pc_move(self):
        move_random_card = random.choice(self.__pc_card)
        index_card = self.__pc_card.index(move_random_card)
        print("Ход компьютера:", self.__pc_card[index_card])
        pc_move = self.pc_keys[index_card]

        for i in self.my_keys:
            if i > pc_move:
                index_card_my = self.my_keys.index(i)
                self.my_keys.remove(i)
                self.__my_card.pop(index_card_my)
                index_card_pc = self.pc_keys.index(pc_move)
                self.pc_keys.remove(pc_move)
                self.__pc_card.pop(index_card_pc)
                return "Карты отбиты!"
                break
            elif i < pc_move:
                continue
            else:
                index_card_pc = self.pc_keys.index(pc_move)
                card_pc_move = self.__pc_card[index_card_pc]
                self.my_keys.append(pc_move)
                self.__my_card.append(card_pc_move)
                self.pc_keys.remove(i)
                self.__pc_card.pop(index_card_pc)
                return 'Карты приняты!'

    def mode_game(self):
        if len(self.__my_card) < len(self.__pc_card):
            return 'Вы выиграли!'
        if len(self.__my_card) > len(self.__pc_card):
            return 'Вы проиграли!'
        if len(self.__my_card) == len(self.__pc_card):
            return 'Ничья!'


if __name__ == '__main__':
    fool_game = Fool_enc()
    #    print(fool_game.my_card, fool_game.pc_card)
    print(fool_game.get_my_card(), fool_game.get_pc_card())

    fool_game.set_my_card(6, 7, 4, 9, 6, 7)
    fool_game.set_pc_card(9, 1, 7, 9, 8, 7)
    print(fool_game.get_my_card(), fool_game.get_pc_card())

#    print(fool_game.my_move())
#    print(fool_game.pc_move())
#    print(fool_game.mode_game())
