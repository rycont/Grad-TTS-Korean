_pad        = '_'
_punctuation = '!\'(),.:;? '
_special = '-'

JAMO_LEADS = [chr(_) for _ in range(0x1100, 0x1113)]
JAMO_VOWELS = [chr(_) for _ in range(0x1161, 0x1176)]
JAMO_TAILS = [chr(_) for _ in range(0x11A8, 0x11C3)]

# Export all symbols:
symbols = [_pad] + list(_special) + list(_punctuation) + JAMO_LEADS + JAMO_VOWELS + JAMO_TAILS
