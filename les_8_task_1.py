import hashlib


def detective(string):
    if len(string) <= 1:
        return len(string)
    hashes = set()
    step = 1
    while step < len(string):
        for i in range(0, len(string), 1):
            spam = hashlib.sha256(string[i:i + step].encode('utf-8')).hexdigest()
            hashes.add(spam)
        step += 1
    return len(hashes)


print(f'Число подстрок: {detective(input("Введите строку для подсчета подстрок: "))}')