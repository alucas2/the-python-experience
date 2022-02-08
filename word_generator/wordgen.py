import random
import ast


def load_analysis(filename):
    f = open(filename, "r")
    markov_probs = ast.literal_eval(f.read())
    f.close()
    assert(type(markov_probs) == dict)
    order = len(next(iter(markov_probs)))
    return markov_probs, order


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


import sys

try:
    filename = sys.argv[1]
    num = int(sys.argv[2])
except:
    print("Utilisation: python worgen.py <analysis_file> <number_of_words>")
    sys.exit(-1)

markov_probs, order = load_analysis(filename)

for i in range(num):
    print(generate_word(markov_probs, order, 20))
