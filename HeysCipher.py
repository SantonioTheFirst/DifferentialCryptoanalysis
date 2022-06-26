from math import log2, ceil


class Heys:
    def __init__(self, key: int) -> None:
        self.__key = key
        assert self.__key > 0 and self.__key < 2**112, 'Incorrect key'
        self.__block_size = 16
        self.__rounds = 7
        #                0     1    2    3    4    5    6    7    8    9    A    B    C    D    E    F  
        self.__S =     [0xF, 0x6, 0x5, 0x8, 0xE, 0xB, 0xA, 0x4, 0xC, 0x0, 0x3, 0x7, 0x2, 0x9, 0x1, 0xD]
        self.__S_inv = [0x9, 0xE, 0xC, 0xA, 0x7, 0x2, 0x1, 0xB, 0x3, 0xD, 0x6, 0x5, 0x8, 0xF, 0x4, 0x0]


    def encrypt(self, text: int):
        pass


    def round(self, block: int, round_key: int):
        y = block ^ round_key
        # splitted = self.split_block(y)
        y_s = self.substitute(y)


    def split_block(self, block: int):
        return [(block >> i) & 0xF for i in range(0, 16, 4)]


    def unite_block(self, splitted_block: int):
        result = 0
        for i, quart in enumerate(splitted_block):
            result |= quart << (4 * i)
        return result


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
        return [(self.__key >> i) & 0xF for i in range(0, 112, 16)]


    def get_text_blocks(self, text: int):
        pass


    def pad(self, text: int):
        pass


if __name__ == '__main__':
    c = Heys(2)

    a = 915
    print(hex(a))
    print(bin(a))

    splitted = c.split_block(a)

    print([bin(i) for i in splitted])

    united = c.unite_block(splitted)
    print(hex(united))