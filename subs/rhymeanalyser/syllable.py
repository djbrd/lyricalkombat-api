
class Syllable():
    def __init__(self, word):
        self.word = word
        self.pre = None
        self.vowel = None
        self.post = None
        self.text = None
        self.rhymes = []

    def has_vowel(self):
        return self.vowel is not None

    def has_pre(self):
        return self.pre is not None

    def has_post(self):
        return self.post is not None

    def add_pre(self, phoneme: str):
        if self.pre is None:
            self.pre = phoneme
        else:
            self.pre = phoneme + ' ' + self.pre

    def add_post(self, phoneme: str):
        if self.post is None:
            self.post = phoneme
        else:
            self.post = phoneme + ' ' + self.post

    def set_text(self, text: str):
        self.text = text

    def get_arpa(self):
        text = ''
        if self.has_pre():
            text = self.pre + ' ';
        if self.has_vowel():
            text = text + self.vowel
        if self.has_post():
            text = text + ' ' + self.post
        return text

    def get_stress(self):
        if self.has_vowel():
            return self.vowel[2:]
        return 0

    def get_vowel(self):
        if self.has_vowel():
            return self.vowel[:2]
        return ''

    def has_pre_y(self):
        return self.has_pre() and 'Y' in self.pre

    def has_post_y(self):
        return self.has_post() and 'Y' in self.post