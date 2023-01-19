""" from https://github.com/keithito/tacotron """

import re
from text.symbols import symbols


_symbol_to_id = {s: i for i, s in enumerate(symbols)}
_id_to_symbol = {i: s for i, s in enumerate(symbols)}


def text_to_sequence(text):
    sequence = []
    space = _symbols_to_sequence(' ')[0]
    
    text = text.strip()

    while len(text):
        sequence += _symbols_to_sequence(text)
        break
  
    sequence = sequence[:-1] if sequence[-1] == space else sequence
    sequence = sequence[1:] if sequence[0] == space else sequence

    return sequence


def sequence_to_text(sequence):
    '''Converts a sequence of IDs back to a string'''
    result = ''
    
    for symbol_id in sequence:
        if symbol_id in _id_to_symbol:
            s = _id_to_symbol[symbol_id]
            result += s

    return result

def _symbols_to_sequence(symbols):
    return [_symbol_to_id[s] for s in symbols if _should_keep_symbol(s)]

def _should_keep_symbol(s):
    return s in _symbol_to_id and s != '_' and s != '~'
