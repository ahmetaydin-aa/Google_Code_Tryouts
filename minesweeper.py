
class MinesweeperBoard:
    __board = None
    __row_count = 0
    __column_count = 0
    __mine_count = 0

    def __init__(self, row_count: int, column_count: int, mine_count: int) -> None:
        if mine_count > (row_count * column_count):
            raise Exception("Too much mines!")

        self.__row_count = row_count
        self.__column_count = column_count
        self.__mine_count = mine_count
        self._create_board()
        self._place_mines()
    
    def _create_board(self) -> None:
        column_count = self.get_column_size()
        row_count = self.get_row_size()
        self.__board = [[0 for _ in range(column_count)] for __ in range(row_count)]
    
    def _place_mines(self) -> None:
        import random
        mine_count = self.get_mine_count()
        column_count = self.get_column_size()
        row_count = self.get_row_size()
        for _ in range(mine_count):
            while True:
                random_row_position = random.randint(0, row_count-1)
                random_column_position = random.randint(0, column_count-1)
                if not self._is_there_a_mine(random_row_position, random_column_position):
                    break
            self._place_mine(random_row_position, random_column_position)
            
    def _place_mine(self, i: int, j: int) -> None:
        import itertools
        column_count = self.get_column_size()
        row_count = self.get_row_size()
        self.__board[i][j] = 9
        i_indexes = [x for x in range(i-1, i+2) if x>=0 and x < row_count]
        j_indexes = [x for x in range(j-1, j+2) if x>=0 and x < column_count]
        surrounding_indexes = list(itertools.product(i_indexes, j_indexes))
        for i_index, j_index in surrounding_indexes:
            if not self._is_there_a_mine(i_index, j_index):
                self.__board[i_index][j_index] += 1
    
    def _is_there_a_mine(self, i: int, j:int) -> bool:
        return self.__board[i][j] == 9

    def get_row_size(self) -> int:
        return self.__row_count

    def get_column_size(self) -> int:
        return self.__column_count

    def get_mine_count(self) -> int:
        return self.__mine_count

    def print_board(self) -> None:
        for i in range(self.get_row_size()):
            row = [str(x) for x in self.__board[i]]
            print(" ".join(row))


if __name__ == "__main__":
    board = MinesweeperBoard(100, 100, 999)
    board.print_board()