from .verse import Verse
from .rhyme import Rhyme

class Analyser():
    colors = ['#dfba24',
              '#d87e3b',
              '#57d0ca',
              '#ca3e6b',
              '#278fbd',
              '#a5bb51',
              '#7c8bc5',
              '#fdc47c',
              '#ab4097',
              '#54aa00',
              '#51a587',
              '#ffb0b1',
              '#d4cb8b',
              '#d27481',
              '#b15fc1',
              ]

    def __init__(self, text):
        self.text = text
        self.verse = Verse(self.text)


    def process(self):
        # debug
        #self.print_verse_in_arpabet()

        self.phonemes = self.verse.collect_phonemes()

        self.rhymes = []
        self.matrix = []

        # create a map of the relationships between phonemes
        # distance is how far they are from each other
        self.max_distance = self.verse.get_max_num_phonemes_in_line() + 5
        self.create_relationship_matrix()

        # debug
        #self. print_relationship_matrix()

        self.create_rhymes_from_matrix()

        # debug
        #self.print_words_as_phonemes_and_related_text()

        self.cluster_phonemes()

        self.create_marked_up_text()


    def create_relationship_matrix(self):
        for distance in range(1, self.max_distance):
            similarities = []
            for i in range(0, len(self.phonemes) - distance):
                # Cache representation of similarity of two phonemes
                p0 = self.phonemes[i]
                p1 = self.phonemes[i + distance]
                # Similarities only count if the phonemes are not both part of a repeated word
                if p0.symbol == p1.symbol and (p0.word is p1.word or p0.word.text != p1.word.text):
                    similarities.append(1)
                else:
                    similarities.append(0)
            self.matrix.append(similarities)


    def create_rhymes_from_matrix(self):
        rhyme = None
        # loop through the relationships and gather sequences
        for distance in range(1, self.max_distance):
            similarities = self.matrix[distance - 1]
            for i, similarity in enumerate(similarities):
                p0 = self.phonemes[i]
                if similarity <= 0:
                    # is there a rhyme in progress?
                    if rhyme is not None:
                        #rhyme = self.end_rhyme(rhyme)
                        p1 = self.phonemes[i + distance]
                        if p0.is_vowel() != p1.is_vowel():
                            rhyme = self.end_rhyme(rhyme)
                        # unrelated phonemes are allowed if either consonants or vowels
                        elif rhyme.has_unrelated_phonemes():
                            unrelated_index = rhyme.first_unrelated_index()
                            x = self.phonemes[unrelated_index]
                            if x.is_vowel() != p0.is_vowel():
                                rhyme = self.end_rhyme(rhyme)
                            else:
                                rhyme.pattern.append(0)
                        else:
                            rhyme.pattern.append(0)

                # similarity is > 0
                else:
                    if rhyme is None:
                        rhyme = Rhyme([i, i + distance])
                    rhyme.pattern.append(similarity)

                # A sequence should not overlap with itself
                if rhyme is not None and rhyme.length() >= distance:
                    rhyme = self.end_rhyme(rhyme)

            # End rhyme at the end of the verse
            if rhyme is not None:
                rhyme = self.end_rhyme(rhyme)

        self.rhymes = sorted(self.rhymes, key=lambda rhyme: rhyme.indices[0])


    # deal with rhyme once the end of its sequence has been identified
    def end_rhyme(self, rhyme):
        # remove any dangling unrelated phonemes
        while len(rhyme.pattern) and rhyme.pattern[-1] == 0:
            rhyme.pattern = rhyme.pattern[:-1]

        # # rhymes of length 1 shouldn't be recognised unless perfect
        # if len(rhyme.pattern) <= 1:
        #     p1 = self.phonemes[rhyme.indices[0]]
        #     p2 = self.phonemes[rhyme.indices[1]]
        #     if not(p1.start_of_rhyming_part() and p1.end_of_word() and
        #         p2.start_of_rhyming_part() and p2.end_of_word()):
        #         return None

        i0 = rhyme.indices[0]
        # don't add a rhyme with the same pattern as has already been found
        if any((i0 == r.indices[0] and r.pattern == rhyme.pattern) for r in self.rhymes):
            return None

        self.rhymes.append(rhyme)
        return None


    # Function to initialise map with individual phonemes
    def cluster_phonemes(self):
        self.conassall = [0] * len(self.phonemes)

        current_map = {}
        for i, phoneme in enumerate(self.phonemes):
            if phoneme.symbol in current_map:
                current_map[phoneme.symbol].append(i)
            else:
                current_map[phoneme.symbol] = [i]

        # todo - collapse lists of similar sounding phonemes

        colorIdx = 0
        self.conassall_colors = {}

        # Retain indices which aren't too far from each other
        for symbol, indices in current_map.items():
            found = False
            for i in range(0, len(indices) - 1):
                if indices[i + 1] - indices[i] <= 12:
                    self.conassall[indices[i]] = 1
                    self.conassall[indices[i + 1]] = 1
                    found = True
            if found:
                self.conassall_colors[symbol] = self.colors[colorIdx]
                colorIdx = (colorIdx + 1) % len(self.colors)


    # Debug function to print arpabet representation of verse to console
    def print_verse_in_arpabet(self):
        index = 0
        for line in self.verse.lines:
            text = []
            numbering = []
            for word in line.words:
                for phoneme in word.phonemes:
                    text.append(phoneme.symbol)
                    index_string = str(index)
                    while len(index_string) < 2:
                        index_string = ' ' + index_string
                    numbering.append(index_string)
                    index = (index + 1) % 100
            indexes = ' '.join(numbering)
            print(indexes)

            output = ' '.join(text)
            print(output)
        print()

    # Debug function to print representation of relationships between phonemes
    def print_relationship_matrix(self):
        for index in range(0, len(self.phonemes) - 1):
            print(self.phonemes[index].symbol + ' ', end='')
            print(' ' * ((index ) * 3), end='')
            to_end = len(self.phonemes) - index
            max = self.max_distance if self.max_distance <= to_end else to_end
            for distance in range(1, max):
                print(' ' + str(self.matrix[distance - 1][index]) + ',', end='')
            print()
        print()

    # Debug function to output all words as phonemes and their related text
    def print_words_as_phonemes_and_related_text(self):
        words = self.verse.collect_words()
        for word in words:
            text = []
            arpa = []
            for phoneme in word.phonemes:
                text.append(phoneme.text)
                arpa.append(phoneme.arpabet)

            s = '-'
            print(s.join(text))
            print(s.join(arpa))


    def get_analysed_as_dict(self):
        result = {}
        result['original_text'] = self.text

        # Collect phonemes
        phos = []
        last_index = 0
        for phoneme in self.phonemes:
            pho = {}
            pho['start_index'] = self.text.find(phoneme.text, last_index)
            pho['length'] = len(phoneme.text)
            last_index = pho['start_index'] + len(phoneme.text)
            phos.append(pho)

        # Collect rhymes
        rhys = []
        for i, rhyme in enumerate(self.rhymes):
            rhy = {}
            rhy['indices'] = rhyme.indices[:]
            rhy['pattern'] = rhyme.pattern[:]
            rhys.append(rhy)

        result['phonemes'] = phos
        result['rhymes'] = rhys
        return result


    def create_marked_up_text(self):
        marked_up = ''

        # Assign colors to rhymes
        colorIdx = 0
        idx = 1
        for i, rhyme in enumerate(self.rhymes):
            if rhyme.color == '#ffffff':
                rhyme.color = self.colors[colorIdx]

                marked_up = marked_up + 'Rhyme ' + str(idx) + '</br>'
                colorIdx = (colorIdx + 1) % len(self.colors)
                idx = idx + 1

                marked_up = marked_up + self.create_marked_up_text_for_rhyme(rhyme)
                marked_up = marked_up + '</br></br>'

        marked_up = marked_up + 'And finally... consonance, assonance, and alliteration</br>'
        marked_up = marked_up + self.create_marked_up_text_for_conassall()

        marked_up = marked_up.replace("\n", '\n\t\t\t</br>')
        self.marked_up = marked_up


    def create_marked_up_verse(self, result):
        marked_up = ''
        original_text = result['original_text']
        last_index = 0
        for i, pho in enumerate(result['phonemes']):
            start_index = pho['start_index']
            if start_index != last_index:
                marked_up = marked_up + original_text[last_index:start_index]

            last_index = start_index + pho['length']
            marked_up = marked_up + '<span id="p' + str(i) + '">' + original_text[start_index:last_index] + '</span>'

        marked_up = marked_up + original_text[last_index:]
        return marked_up.replace('\n', '</br>')


    def create_marked_up_text_for_rhyme(self, rhyme):
        marked_up = ''
        for line in self.verse.lines:
            # If line containing first part of rhyme has not been reached
            if rhyme.indices[0] > line.end_phoneme_count:
                marked_up = '... '
                continue

            # Loop through the line
            last_index = 0
            for i in range(line.start_phoneme_count, line.end_phoneme_count):
                phoneme = self.phonemes[i]

                # Add any text which isn't represented by phonemes
                next_index = line.original_text.find(phoneme.text, last_index)
                if next_index != last_index:
                    marked_up = marked_up + line.original_text[last_index:next_index]

                # Indexed phoneme is either in a rhyme...
                if rhyme.index_in_rhyme(i):
                    text = phoneme.text if phoneme.text else '^'
                    marked_up = marked_up + '<span style="color:' + rhyme.color + '">' + text + '</span>'
                # ... or not
                else:
                    marked_up = marked_up + phoneme.text
                last_index = next_index + len(phoneme.text)
            marked_up = marked_up + line.original_text[last_index:]

            # If line containing second part of rhyme has been passed
            if line.get_cumulative_phoneme_count() >= rhyme.indices[1] + rhyme.length():
                break

            else:
                marked_up = marked_up + '</br>'

        # If the rhyme wasn't in the last line
        if rhyme.indices[1] + rhyme.length() <= self.verse.lines[-1].start_phoneme_count:
            marked_up = marked_up.rstrip() + '...'
        return marked_up


    def create_marked_up_text_for_conassall(self):
        marked_up = ''
        last_index = 0
        for i, phoneme in enumerate(self.phonemes):
            # Add any text which isn't represented by phonemes
            next_index = self.text.find(phoneme.text, last_index)
            if next_index != last_index:
                marked_up = marked_up + self.text[last_index:next_index]

            if self.conassall[i]:
                marked_up = marked_up + '<span style="color:' + self.conassall_colors[phoneme.symbol] + '">' + phoneme.text + '</span>'
            else:
                marked_up = marked_up + phoneme.text
            last_index = next_index + len(phoneme.text)
        marked_up = marked_up + self.text[last_index:]
        return marked_up
