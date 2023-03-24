import pytest
from fool_card_game import Fool_enc


class TestFool_pytest:

    def setup(self):
        self.fool_game = Fool_enc()
        print('Start test')

    def teardown(self):
        self.fool_game.my_card = []
        self.fool_game.pc_card = []
        print('Test done!')

# Проверка количества карт после инициализации
    def test_len_card(self):
        assert len(self.fool_game.my_card) == 6
        assert len(self.fool_game.pc_card) == 6

# Проверка ручной установки карт через сеттер
# Проверка срабатывания ошибки при неверном количестве карт
    def test_fool_setter_1(self):
        self.fool_game.my_card = [2, 4, 8, 3, 6, 9]
        self.fool_game.pc_card = [3, 1, 6, 1, 9, 2]
        assert (self.fool_game.my_keys == [2, 4, 8, 3, 6, 9]) & (self.fool_game.pc_keys == [3, 1, 6, 1, 9, 2])

        with pytest.raises(ValueError):
            # Код, вызывающий ошибку ValueError - количество карт больше 6
            self.fool_game.pc_card = [3, 1, 6, 1, 9, 2, 8]

# Проверка срабатывания ошибки при неверном значении любой карты
    def test_fool_setter_2(self):
        with pytest.raises(ValueError):
            # Код, вызывающий ошибку ValueError - значение карты больше 9
            self.fool_game.pc_card = [3, 10, 6, 1, 9, 2]

# Проверка количества карт после Вашего хода
    def test_len_after_my_move(self):
        self.fool_game.my_card = [2, 4, 8, 3, 6, 9]
        self.fool_game.pc_card = [3, 1, 6, 1, 9, 2]
        self.fool_game.my_move()
        assert len(self.fool_game.my_card) == 5

# Проверка количества карт после хода компьютера
    def test_len_after_pc_move(self):
        self.fool_game.my_card = [2, 4, 8, 3, 6, 9]
        self.fool_game.pc_card = [3, 1, 6, 1, 9, 2]
        self.fool_game.pc_move()
        assert len(self.fool_game.my_card) == 5

