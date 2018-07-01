from .rhyme import Rhyme
from .phoneme import Phoneme

class Categoriser():
    PERFECT = 'perfect'
    SYLLABIC = 'syllabic'

    def __init__(self, rhyme, phonemes):
        self.rhyme = rhyme
        self.phonemes = phonemes

    def process(self):
        if self.is_perfect():
            self.rhyme.category = self.PERFECT
        elif self.is_syllabic():
            self.rhyme.category = self.SYLLABIC


    def is_perfect(self):
        return (self.all_phonemes_match() and
            self.each_group_in_one_word() and
            self.ends_at_ends_of_words() and
            self.starts_at_starts_of_rhyming_parts() and
            self.stresses_match())

    def is_syllabic(self):
        return (self.all_phonemes_match() and
            self.each_group_in_one_word() and
            self.ends_at_ends_of_words() and
            self.stresses_match() and
            self.starts_in_rhyming_partys() and
            self.vowel_count() == 1 and
            self.starts_with_consonant())


    def start_phonemes(self):
        return [self.phonemes[0][0], self.phonemes[1][0]]

    def end_phonemes(self):
        return [self.phonemes[0][-1], self.phonemes[1][-1]]

    def all_phonemes_match(self):
        return not self.rhyme.has_unrelated_phonemes()

    def ends_at_ends_of_words(self):
        return all(p.end_of_word() for p in self.end_phonemes())

    def each_group_in_one_word(self):
        starts = self.start_phonemes()
        ends = self.end_phonemes()
        return all(starts[i].word is ends[i].word for i in range(0, 2))

    def starts_at_starts_of_rhyming_parts(self):
        return all(p.start_of_rhyming_part for p in self.start_phonemes())

    def starts_in_rhyming_partys(self):
        return all(p.in_rhyming_part for p in self.start_phonemes())

    def stresses_match(self):
        return all(self.phonemes[0][i].stress == self.phonemes[1][i].stress for i in range(0, len(self.phonemes[0])))

    def vowel_count(self):
        count = 0
        for p in self.phonemes[0]:
            if p.is_vowel():
                count = count + 1
        return count

    def consonant_count(self):
        return len(self.phonemes[0]) - self.vowel_count()

    def starts_with_consonant(self):
        starts = self.start_phonemes()
        return starts[0].is_consonant
