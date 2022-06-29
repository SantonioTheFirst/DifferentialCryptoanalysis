from HeysCipher import Heys
import subprocess
import os
import concurrent.futures


total_keys_number = 20
key = ''
curdir = os.path.abspath(os.curdir)
cipher = Heys(0x0)
threads = 4
texts = 1000
keys = 2**16


def write_(alpha: int, texts: int) -> None:
    for text in range(texts):
        with open(f'{curdir}/texts/pt.txt', 'wb') as f:
            f.write(int(text).to_bytes(2, 'big'))
        subprocess.Popen(
            f'{curdir}/heys.bin e 3 {curdir}/texts/pt.txt {curdir}/texts/ct_{text}.bin {key} >> /dev/null',
            stdin=subprocess.PIPE, shell=True
        ).communicate(input="\x0a".encode())
        with open(f'{curdir}/texts/pt.txt', 'wb') as pt:
            pt.write(int(text ^ alpha).to_bytes(2, 'big'))
        subprocess.Popen(
            f'{curdir}/heys.bin e 3 {curdir}/texts/pt.txt {curdir}/texts/cta_{text}.bin {key} >> /dev/null',
            stdin=subprocess.PIPE, shell=True
        ).communicate(input="\x0a".encode())


def read_(texts: int) -> list[list[int]]:
    result = []
    for text in range(texts):
        ct = 0
        cta = 0
        with open(f'{curdir}/texts/ct_{text}.bin', 'rb') as f:
            ct = int.from_bytes(f.read(), 'big')
        with open(f'{curdir}/texts/cta_{text}.bin', 'rb') as f:
            cta = int.from_bytes(f.read(), 'big')
        result.append([ct, cta])
    return result


def calc_beta(cts: list[int], key: int) -> int:
    ct, cta = cts[0], cts[1]
    pt, pta = cipher.round_(ct, key), cipher.round_(cta, key)
    return pt ^ pta


def write_results(cts: list[list[int]], betas: list[int], key: int) -> None:
    # if key != 0 and key % 10000 == 0:
    #     print(key)
    cnt = 0
    for ct in cts:
        beta = calc_beta(ct, key)
        if beta in betas:
            # print(beta)
            # with open(f'{curdir}/{beta}.txt', 'w') as f:
            #     f.write(str(beta))
            cnt += 1
    with open(f'{curdir}/all_results/{cnt}_{key}.txt', 'w') as f:
        f.write(f'Key: {key} Count: {cnt}\n')


def do_all_stuff(alpha: int, betas: list[int], keys_cnt: int, texts_cnt: int) -> None:
    output = []
    write_(alpha, texts_cnt)
    cts = read_(texts_cnt)
    print('Threading')
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        for key in range(keys_cnt):
            # if key != 0 and key % 10000 == 0:
            #     print(key)
            futures.append(executor.submit(write_results, cts=cts, betas=betas, key=key))

    files = os.listdir(f"{curdir}/all_results")
    files = sorted(
        [[int(file.split('_')[0]), int(file.split('_')[1])] for file in files],
        reverse=True
    )[:total_keys_number]
    
    for file in files:
        with open(f'{curdir}/all_results/{file[0]}_{file[1]}.txt', 'r') as f:
            output.append(f.readline())
    with open(f'{curdir}/final_output.txt', 'w') as f:
        for line in output:
            f.write(line)


if __name__ == '__main__':
    # write_(1, range(5))
    # print(read_(range(5)))
    alpha = 0x1
    # betas = [1, 16, 15, 3, 8]
    betas = [4352, 4097, 4353, 4368, 256]
    do_all_stuff(alpha, betas, keys, texts)
