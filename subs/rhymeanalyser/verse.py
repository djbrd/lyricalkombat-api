import string
from .line import Line

class Verse():
    def __init__(self, text: str):
        self.text = text
        self.lines = []
        # Remove all punctuation apart from apostrophes
        translator = str.maketrans('', '', string.punctuation.replace("'", ""))
        start_phoneme_count = 0
        for line in text.splitlines():
            sanitised_line = line.translate(translator)
            line_object = Line(self, line, sanitised_line, start_phoneme_count)
            self.lines.append(line_object)
            start_phoneme_count = line_object.end_phoneme_count

    # Just returns an array of all the syllables in the vers
    def collect_syllables(self):
        syllables = []
        for line in self.lines:
            for word in line.words:
                for syllable in word.syllables:
                    syllables.append(syllable)
        return syllables

    # Returns an array of all the phonemes in the verse
    def collect_phonemes(self):
        phonemes = []
        for line in self.lines:
            for word in line.words:
                for phoneme in word.phonemes:
                    phonemes.append(phoneme)
        return phonemes

    def collect_words(self):
        words = []
        for line in self.lines:
            for word in line.words:
                words.append(word)
        return words

    def get_max_num_phonemes_in_line(self):
        return max(line.get_phoneme_count() for line in self.lines)

