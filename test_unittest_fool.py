import unittest

from fool_card_game import Fool_enc


class TestFool_unittest(unittest.TestCase):

    def setUp(self):
        print('Start test!')
        self.fool_game = Fool_enc()
        self.fool_game.my_card = [2, 4, 8, 3, 6, 9]
        self.fool_game.pc_card = [3, 1, 6, 1, 9, 2]

    def teardown(self):
        # Освобождение кэша
        del self.fool_game
        print('Test completed!')

    # Проверка количества карт после инициализации
    def test_len_card(self):
        self.assertEqual(len(self.fool_game.my_card), 6)
        self.assertFalse(len(self.fool_game.pc_card) > 6)

    # Проверка ручной установки карт через сеттер
    # Проверка срабатывания ошибки при неверном количестве карт
    def test_fool_setter_1(self):
        self.assertTrue((self.fool_game.my_keys == [2, 4, 8, 3, 6, 9]) & (self.fool_game.pc_keys == [3, 1, 6, 1, 9, 2]))

        with self.assertRaises(ValueError):
            # Код, вызывающий ошибку ValueError - количество карт больше 6
            self.fool_game.pc_card = [3, 1, 6, 1, 9, 2, 8]

    # Проверка срабатывания ошибки при неверном значении любой карты
    def test_fool_setter_2(self):
        with self.assertRaises(ValueError):
            # Код, вызывающий ошибку ValueError - значение карты больше 9
            self.fool_game.pc_card = [3, 10, 6, 1, 9, 2]

    # Проверка количества карт после Вашего хода (если выпал Туз(Ace), то будет ошибка)
    def test_len_after_my_move(self):
        self.fool_game.my_move()
        self.assertEqual(len(self.fool_game.my_card), 5)

    # Проверка количества карт после хода компьютера
    def test_len_after_pc_move(self):
        self.fool_game.pc_move()
        self.assertEqual(len(self.fool_game.my_card), 5)
