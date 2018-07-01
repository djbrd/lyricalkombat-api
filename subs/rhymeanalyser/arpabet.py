# constants as defined in http://www.speech.cs.cmu.edu/cgi-bin/cmudict#phones
vowel_sounds = ['AA', # odd
                'AE', # at
                'AH', # hut
                'AO', # ought
                'AW', # cow
                'AY', # hide
                'EH', # Ed
                'ER', # hurt
                'EY', # ate
                'IH', # it
                'IY', # eat
                'OW', # oat
                'OY', # toy
                'UH', # hood
                'UW', # two
                ]
# How vowel sounds may be represented in text
text_for_vowels = {
    'AA': ['o', 'a', 'au', 'ah', 'aw', 'ow', 'ea', 'ough', 'augh', 'oi', 'ua', 'ho'],
    'AE': ['a', 'au', 'eah'],
    'AH': ['a', 'ai', 'ae', 'au', 'e', 'i', 'io', 'ia', 'iu', 'oe', 'o', 'u', 'ui', 'ou', 'oo', 'y', 'ah', 'er', 'hi', ''],
    'AO': ['ou', 'au', 'a', 'oa', 'oo', 'o', 'aw', 'awe', 'eo', 'al', 'ough', 'augh', 'hau'],
    'AW': ['ow', 'ou', 'au', 'ao', 'hou'],
    'AY': ['i', 'ey', 'y', 'uy', 'igh', 'ui', 'is', 'ie', 'ia', 'eye', 'aye', 'eigh', 'oi', 'ai', 'ye'],
    'EH': ['e', 'ei', 'ea', 'ay', 'ey', 'u', 'ue', 'ua', 'ai', 'a', 'ie', 'eh'],
    'ER': ['er', 'ear', 'r', 'ur', 'ir', 'urr', 'ur', 'ure', 'or', 'our', 'ar', 'arr', 'orr', 'err', 're', 'ro', 'ere', 'eur', 'yr', 'olo', 'aur', 'her', 'urh'],
    'EY': ['ai', 'ei', 'ea', 'a', 'ay', 'ey', 'ee', 'ez', 'e', 'eigh', 'aigh', 'et', 'au'],
    'IH': ['i', 'a', 'e', 'ea', 'ee', 'y', 'u', 'eo', 'ei', 'o', 'ui', 'ia', 'ie'],
    'IY': ['ee', 'ei', 'i', 'ie', 'eo', 'ea', 'y', 'ey', 'e', 'ay', 'a', 'is', 'ix', 'eigh'],
    'OW': ['eaux', 'eau', 'au', 'ew', 'oa', 'ow', 'ou', 'oe', 'o', 'ough', 'oh', 'og', 'ot'],
    'OY': ['oi', 'oy', 'eu', 'oj', 'ouy', 'oll', 'eu', 'ois'],
    'UH': ['oo', 'u', 'o', 'ou', 'eu', 'or'],
    'UW': ['oo', 'wo', 'ew', 'uw', 'ue', 'oe', 'ou', 'au', 'ui', 'u', 'ut', 'o', 'ough', 'ugh']
 }

consonant_sounds = ['B',
                    'CH',
                    'D',
                    'DH', # thee
                    'F',
                    'G',
                    'HH',
                    'JH', # gee
                    'K',
                    'L',
                    'M',
                    'N',
                    'NG',
                    'P',
                    'R',
                    'S',
                    'SH',
                    'T',
                    'TH',
                    'V',
                    'W',
                    'Y',
                    'Z',
                    'ZH'
                    ]

# How consonant sound may be represented in text
text_for_consonants = {
    'B': ['b', 'bb', 'be'],
    'CH': ['ch', 'tch', 'ti', 'ci', 'si', 't', 'cc', 'cz', 'c'],
    'D': ['d', 'dd', 'de', 'ld', 'ed'],
    'DH': ['th', 'the'],
    'F': ['ff', 'f', 'ph', 'gh', 'v', 'w', 'fe', 'lf', 'pph'],
    'G': ['g', 'gg', 'x', 'gue', 'gh', ''], # luxury
    'HH': ['h', 'wh', 'j'],
    'JH': [ 'ge', 'dg', 'gg', 'gi', 'dge', 'g', 'j', 'di', 'dj', 'dz', 'd'],
    'K': ['k', 'ck', 'cq', 'ch', 'c', 'cc', 'x', 'g', 'q', 'ke', 'que', 'lk'],
    'L': ['ll', 'l', 'lle', 'le', 'all', 'ull', 'ol'],
    'M': ['mm', 'm', 'me', 'mme', 'lm', 'mb', 'mn'],
    'N': ['nn', 'n', 'ne', 'nne', 'kn', 'gn', 'hn', 'dn', 'mn', 'in'],
    'NG': ['n', 'ng', 'ngue'],
    'P': ['pp', 'p', 'pe', 'ph'],
    'R': ['rh', 'rr', 'r', 're', 'er', 'wr', 'rt', 'or', 'ar', 'rre'],
    'S': ['s', 'ss', 's', 'se', 'sc', 'ps', 'c', 'ce', 'x', 'z', 'st', 'sw', ''],
    'SH': ['sh', 'ti', 'ci', 'cia', 'ss', 'xi', 'x', 'ch', 'che', 'ce', 'si', 'sci', 'sch', 'tu', 's', 't', ''],
    'T': ['t', 'tt', 'te', 'tte', 'ed', 'z', 'th', 'bt', 'cht', 'pt'],
    'TH': ['th'],
    'V': ['v', 've', 'f', 'w'],
    'W': ['w', 'wh', 'u', 'ju', ''],
    'Y': ['y', '', 'u', 'i', 'r', 'e'], # February
    'Z': ['z', 'zz', 'ze', 's', 'ss', 'es', 'x', 'si', 'se', ''],
    'ZH': ['si', 'ti', 'ge', 's', 'j', 'g']
}

# two phonemes, one letter: 'x' = 'G  S', 'K SH', 'z' = 'T  S', 'o' = 'W AH'
# 'qu'
# Y is between consonant and 'u', or between consonant and 'i'
# W is between consonant and 'u'

# can be silent: l (talk, palm, half), g (design), s (island), t (mortgage, christmas), d (wednesday), w (answer), b (debt, dumb), a (automatically), h (shepherd), n (column), p (psychology)
# ch (yacht)
phoneme_set = vowel_sounds + consonant_sounds