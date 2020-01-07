
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



markov_probs = analyse_dict("francais.txt", 3)
save_analysis(markov_probs, "analyse_francais_ordre3.txt")

markov_probs = analyse_dict("english.txt", 3)
save_analysis(markov_probs, "analyse_english_ordre3.txt")

markov_probs = analyse_dict("deutsch.txt", 3)
save_analysis(markov_probs, "analyse_deutsch_ordre3.txt")
