
class Phoneme():
    def __init__(self, word, arpabet:str, in_rhyming_part):
        self.word = word
        self.arpabet = arpabet
        self.symbol = arpabet[:2]
        if len(self.symbol) == 1:
            self.symbol = ' ' + self.symbol
        if len(arpabet) == 3:
            self.stress = int(arpabet[2:])
        else:
            self.stress = -1
        self.in_rhyming_part = in_rhyming_part
        self.text = ''

    def is_vowel(self):
        return self.stress != -1

    def is_consonant(self):
        return self.stress == -1

    def start_of_rhyming_part(self):
        return self.in_rhyming_part and self.stress > 0

    def end_of_word(self):
        return self.text and self.word.text.endswith(self.text)

