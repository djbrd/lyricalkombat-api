import pronouncing
from .phoneme import Phoneme
from .arpabet import *

class Word():
    def __init__(self, line, text: str):
        self.line = line
        self.text = text
        self.init_arpabet(text)
        self.phonemes = []
        phones = self.arpabet.split()
        in_rhyming_part = False
        for phone in phones:
            if not in_rhyming_part and phone in self.rhyming_part:
                in_rhyming_part = True
            phomeme = Phoneme(self, phone, in_rhyming_part)
            self.phonemes.append(phomeme)

        text = self.text.replace("'", '')
        text = text.replace("-", '')
        # Assign text to phonemes
        if not self.assign_text_to_phonemes(text, self.phonemes):
            self.crude_assign_text_to_phonemes()


    def init_arpabet(self, text:str):
        # Handle a common abbreviation
        abbreviated = False
        if text.lower().endswith("in'"):
            text = text.replace("in'", "ing")
            abbreviated = True
        arpabet = pronouncing.phones_for_word(text.lower())
        if not arpabet:
            self.arpabet = ''
            self.rhyming_part = ''
        else:
            self.arpabet = arpabet[0]
            if abbreviated and self.arpabet.endswith('NG'):
                self.arpabet = self.arpabet[:-2] + 'N'
            self.rhyming_part = pronouncing.rhyming_part(self.arpabet)


    # Recursive function which does a depth first search for a fitting match of text to phonemes using
    # definitions in the arpabet module
    def assign_text_to_phonemes(self, text: str, phonemes):
        if not text and not phonemes:
            return True

        # It's possible that the final phoneme is not represented by text, i.e. sex
        if not phonemes:
            return False

        p = phonemes[0]
        candidates = text_for_vowels[p.symbol] if p.is_vowel() else text_for_consonants[p.arpabet]
        for candidate in candidates:
            if text.lower().startswith(candidate):
                p.text = text[:len(candidate)]
                if self.assign_text_to_phonemes(text[len(candidate):], phonemes[1:]):
                    return True

        p.text = ''
        return False

    # First attempt and fall back - just loops through the phonemes and assigns the next consonant if it is
    # a consonant sound and the next vowel if it's a vowel sound
    def crude_assign_text_to_phonemes(self):
        if (not len(self.phonemes)):
            return

        index = 0
        text = self.text[:]

        for i in range(0, len(self.phonemes) - 1):
            p0 = self.phonemes[i]
            p1 = self.phonemes[i + 1]
            if p0.is_vowel():
                vowels = 'aeiou'
                if p1.symbol != ' Y':
                    vowels = vowels + 'y'
                while index < len(text) and text[index] in vowels:
                    p0.text = p0.text + text[index]
                    index = index + 1
                    if p1.is_vowel():
                        break
            else:
                vowels = 'aeiou'
                if p0.symbol != ' Y':
                    vowels = vowels + 'y'
                while (index < len(text) and text[index] not in vowels and (p0.symbol == ' L' or text[index] != 'l')):
                    p0.text = p0.text + text[index]
                    index = index + 1
                    if p1.is_consonant():
                        while index < len(text) and text[index] in vowels:
                            p0.text = p0.text + text[index]
                            index = index + 1
                        break

        self.phonemes[-1].text = text[index:]







