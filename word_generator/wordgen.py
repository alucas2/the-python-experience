import random
import ast


def load_analysis(filename):
    f = open(filename, "r")
    result = ast.literal_eval(f.read())
    f.close()
    assert(type(result) == dict)
    return result


def sample_distribution(distribution):
    r = random.random()
    for (key, value) in distribution.items():
        if r < value:
            return key
        r -= value

    return ' '


def generate_word(markov_probs, order, truncate, begin=""):
    word = order*' ' + begin
    for i in range(truncate):
        word += sample_distribution(markov_probs.get(word[-order:], {}))
        if word[-1] == ' ':
            break

    return word.strip()


markov_probs = load_analysis("analyse_francais_ordre3.txt")
#markov_probs = load_analysis("analyse_english_ordre3.txt")
#markov_probs = load_analysis("analyse_deutsch_ordre3.txt")

for i in range(20):
    print(generate_word(markov_probs, 3, 20))
