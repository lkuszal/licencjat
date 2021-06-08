from fitting import lang_checker


def solutions_checker(text, cipher_object, results, outcomes=5):
    """magnum opus of library, from cipher_text returns most probable possibilites of solutions (as key and deciphered text)
    and also bool value - True if any solutions has been successful matched to language model or false and sorted 5 results
     by most probable, due to fittness to language model"""
    approved = []
    mismatched = []
    for x in sorted(results[:outcomes]):
        ciphrogram = cipher_object(x)
        deciphered_text = ciphrogram.decipher(text)
        diff = lang_checker(deciphered_text)
        if diff == 0:
            approved.append([x, deciphered_text])
        else:
            mismatched.append([diff, [x, deciphered_text]])
    if approved:
        return True, approved
    else:
        return False, sorted(mismatched)
