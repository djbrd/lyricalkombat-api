
class Rhyme():
    def __init__(self, indices):
        self.indices = indices
        self.pattern = []
        self.color = '#ffffff'
        self.category = ''

    def has_unrelated_phonemes(self):
        return 0 in self.pattern

    def first_unrelated_index(self):
        return self.indices[0] + self.pattern.index(0)

    def length(self):
        return len(self.pattern)

    # Returns indexes of corresponding phonemes in rhyme which don't match
    def unrelated_indices(self, index):
        unrelated = []
        for i, p in enumerate(self.pattern):
            if self.pattern != 0:
                continue
            for index in self.indices:
                unrelated.append(index + i)

    def index_in_rhyme(self, index):
        for i in range(0, 2):
            idx = self.indices[i]
            if index >= idx and index < idx + self.length():
                internal_idx = index - idx
                if self.pattern[internal_idx]:
                    return True
                else:
                    return False
        return False

    def get_all_indices(self):
        all_indices = []
        for index in self.indices:
            for i, p in enumerate(self.pattern):
                all_indices.append(index + i)
        return all_indices