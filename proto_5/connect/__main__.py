import argparse
import types
import os

class Card:
    def __init__(self, root_path, fpath):
        self._fpath = fpath
        self._card_path = "/" + os.path.relpath(fpath, start=root_path)

    @property
    def card_path(self):
        return self._card_path

def parse_cards_from_files(card_dir):
    def is_card_file(filename):
        return filename.endswith('.yaml')
    card_files = []
    for dirpath, dirnames, filenames in os.walk(card_dir):
        for filename in filenames:
            if is_card_file(filename):
                card = Card(card_dir, os.path.join(dirpath, filename))
                card_files.append(card)
    return card_files

def process_connect_scripts(card_files):
    return

def build_graph(data_dir):
    cards = parse_cards_from_files(data_dir)
    card_dict = {card.card_path:card for card in cards}
    print(card_dict)
    process_connect_scripts(cards)


parser = argparse.ArgumentParser()
parser.add_argument("data_dir", help="The directory containing our data")
args = parser.parse_args()

build_graph(args.data_dir)