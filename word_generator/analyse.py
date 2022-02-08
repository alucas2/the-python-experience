
def analyse_dict(word_list_filename, order):
    f = open(word_list_filename, "r")
    
    markov_probs = {}
    words = f.read().split()

    for word in words:
        word = word.strip().lower()
        word = order*' ' + word + ' '

        for i in range(len(word) - order):
            key = ''
            for j in range(order):
                key += word[i + j]

            char = word[i + order]

            if key not in markov_probs: markov_probs[key] = {}
            if char not in markov_probs[key]: markov_probs[key][char] = 0
            markov_probs[key][char] += 1

    for distribution in markov_probs.values():
        normalize = 1/sum(distribution.values())
        for char in distribution:
            distribution[char] *= normalize

    f.close()
    return markov_probs


def save_analysis(markov_probs, filename):
    f = open(filename, "w")
    f.write(str(markov_probs).replace("},", "},\n"))
    f.close()


import sys

try:
    filename = sys.argv[1]
    order = int(sys.argv[2])
except:
    print("Utilisation: python analyse.py <words_file> <order>")
    sys.exit(-1)

markov_probs = analyse_dict(filename, order)
outputname = filename.split(".")[0] + "_order_" + str(order) + ".txt"
save_analysis(markov_probs, outputname)
