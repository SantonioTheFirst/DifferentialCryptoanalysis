from math import log2, ceil


class Heys:
    def __init__(self, key: int) -> None:
        self.__key = key
        self.__block_size = 16
        self.__rounds = 7
        self.__S = [0xF, 0x6, 0x5, 0x8, 0xE, 0xB, 0xA, 0x4, 0xC, 0x0, 0x3, 0x7, 0x2, 0x9, 0x1, 0xD]


    def encrypt(self, text: int):
        pass


    def round(self, block: int, round_key: int):
        y = block ^ round_key
        # splitted = self.split_block(y)
        y_s = self.substitute(y)


    def split_block(self, block: int):
        pass


    def unite_block(self, splitted_block: int):
        pass


    def permute(self, block: int):
        for i in range(self.__block_size):
            for j in range(self.__block_size):
                pass


    def get_bit(self, number: int, index: int):
        return (number >> index) & 1

    
    def substitute(self, block: int):
        return (self.__S[(block >> 12) & 0xF] << 12) | (self.__S[(block >> 8) & 0xF] << 8) |\
             (self.__S[(block >> 4) & 0xF] << 4) | (self.__S[block & 0xF])


    def get_round_keys(self):
        pass


    def get_text_blocks(self, text: int):
        pass


    def pad(self, text: int):
        pass
