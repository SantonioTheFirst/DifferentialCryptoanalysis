from math import log2, ceil
import time


class Heys:
    def __init__(self, key: int) -> None:
        self.__key = key
        assert self.__key >= 0 and self.__key < 2**112, 'Incorrect key'
        self.__block_size = 16
        self.__rounds = 7
        #                0     1    2    3    4    5    6    7    8    9    A    B    C    D    E    F  
        self.__S =     [0xF, 0x6, 0x5, 0x8, 0xE, 0xB, 0xA, 0x4, 0xC, 0x0, 0x3, 0x7, 0x2, 0x9, 0x1, 0xD]
        self.__S_inv = [0x9, 0xE, 0xC, 0xA, 0x7, 0x2, 0x1, 0xB, 0x3, 0xD, 0x6, 0x5, 0x8, 0xF, 0x4, 0x0]


    def encrypt(self, block: int) -> int:
        keys = self.get_round_keys()
        for i in range(self.__rounds - 1):
            output = self.round(output, keys[i])
        return keys[-1] ^ output


    def round(self, block: int, round_key: int) -> int:
        y = block ^ round_key
        y_s = self.substitute(y)
        y_p = self.permute(y_s)
        return y_p


    def round_(self, block: int, round_key: int) -> int:
        y_k = block ^ round_key
        # print(y_k)
        y_p = self.permute(y_k)
        # print(f'Perm: {hex(y_p)}')
        y_s = self.substitute_(y_p)
        # print(hex(y_s))
        return y_s


    def split_block(self, block: int) -> list[int]:
        return [(block >> i) & 0xF for i in range(0, 16, 4)]


    def unite_block(self, splitted_block: list[int]) -> int:
        result = 0
        for i, quart in enumerate(splitted_block):
            result |= quart << (4 * i)
        return result


    def permute(self, block: int) -> int:
        result = 0
        for i in range(4):
            for j in range(4):
                # result |= ((((block >> (i * 4) & 0xF) >> j) & 1) << (j * 4)) << i 
                result |= (block >> (i * 4 + j) & 1) << (j * 4 + i) 
        return result
                

    def get_bit(self, number: int, index: int) -> bool:
        return (number >> index) & 1

    
    def substitute(self, block: int) -> int:
        return (self.__S[(block >> 12) & 0xF] << 12) | (self.__S[(block >> 8) & 0xF] << 8) |\
             (self.__S[(block >> 4) & 0xF] << 4) | (self.__S[block & 0xF])


    def substitute_(self, block: int) -> int:
        return (self.__S_inv[(block >> 12) & 0xF] << 12) | (self.__S_inv[(block >> 8) & 0xF] << 8) |\
             (self.__S_inv[(block >> 4) & 0xF] << 4) | (self.__S_inv[block & 0xF])


    def get_round_keys(self) -> list[int]:
        return [(self.__key >> i) & 0xF for i in range(0, 112, 16)]


    def get_text_blocks(self, text: int):
        pass


    def pad(self, text: int):
        pass


if __name__ == '__main__':
    c = Heys(0)
    print(hex(c.permute(0x191)))
