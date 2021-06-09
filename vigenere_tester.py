from vigenere_cracker import vigenere_solver
from vigenere_tools import vigenere_generator


def vigenere_tester(length, key_length, sample):
    correct = {True: 0, False: 0}
    mistake = {True: 0, False: 0}
    guessed_length = 0
    common_key_parts = []
    for x in range(sample):
        ciphertext, key = vigenere_generator(length, key_length)
        result, asd = vigenere_solver(ciphertext)
        guess_keys = [a[0] for a in asd]
        if key in guess_keys or key*2 in guess_keys or key*3 in guess_keys or key*4 in guess_keys:
            correct[result] += 1
        else:
            mistake[result] += 1
            if 0 in [b%len(key) for b in set([len(a) for a in guess_keys])]:
                guessed_length += 1
                top_common = 0
                for a in guess_keys:
                    if len(a)%len(key) == 0:
                        new_key = key
                        while len(a) != len(new_key):
                            new_key += key
                        common = 0
                        for b, c in zip(new_key, a):
                            if b == c:
                                common += 1
                        if common/len(new_key) > top_common:
                            top_common = common/len(new_key)
                common_key_parts.append(round(top_common, 4))

    return correct, mistake, guessed_length, sorted(common_key_parts)
    
    
if __name__ == "__main__":
    print(vigenere_tester(150, 3, 100))
    
