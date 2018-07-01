from .word import Word

class Line():
    def __init__(self, verse, original_text: str, word_text: str, start_phoneme_count):
        self.verse = verse
        self.words = []
        self.original_text = original_text
        self.word_text = word_text
        self.start_phoneme_count = start_phoneme_count
        # split line into words
        for word in word_text.split():
            self.words.append(Word(self, word))
        self.end_phoneme_count = start_phoneme_count + self.get_phoneme_count()

    def get_phoneme_count(self):
        return sum(len(word.phonemes) for word in self.words)

    def get_cumulative_phoneme_count(self):
        return self.start_phoneme_count + self.get_phoneme_count()
