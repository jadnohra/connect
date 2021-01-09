import argparse
import types
import os
import logging
import sys

def data_to_card_path(card_dir, fpath):
    return os.path.splitext("/" + os.path.relpath(fpath, start=card_dir))[0]

class Card:
    def __init__(self, card_dir, fpath):
        self._fpath = fpath
        self._card_path = data_to_card_path(card_dir, fpath)

    @property
    def card_path(self):
        return self._card_path

def is_connect_script_file(filename):
    return os.path.basename(filename) == "CONNECT"

def is_card_file(filename):
    return filename.endswith('.yaml') or filename == "CONNECT"

def is_connect_file(filename):
    return any([predicate(filename)
                for predicate in [is_card_file, is_connect_script_file]])

def parse_connect_files(card_dir):
    connect_files = []
    for dirpath, dirnames, filenames in os.walk(card_dir):
        for filename in filenames:
            if is_connect_file(filename):
                connect_files.append(os.path.join(dirpath, filename))
    return connect_files

def apply_connect_script(card_dir, script_file, card_graph):
    def get_card(card_path, card_graph):
        if card_path in card_graph:
            return card_graph[card_path]
        logging.error(f"Card {card_path} mentioned in {script_file} not found")
        return None
    def get_cards(script_card_dir, pattern, card_graph):
        if pattern.startswith("/"):
            return [get_card(pattern, card_graph)]
        elif pattern == "*":
            # TODO this is slow, we need a tree structure
            return []
        else:
            return [get_card(os.path.join(script_card_dir, pattern), card_graph)]
    def apply_relate_cmd(script_card_dir, cmd, card_graph):
        src_pat, rel_pat, target_pat = cmd
        src_cards = get_cards(script_card_dir, src_pat, card_graph)
        rel_cards = get_cards(script_card_dir, rel_pat, card_graph)
        target_cards = get_cards(script_card_dir, target_pat, card_graph)
    script_lines = open(script_file).readlines()
    line_index = 0
    relate_cmds = []
    while line_index < len(script_lines):
        line = script_lines[line_index]
        if line.strip() == "relate":
            cmd = tuple([arg.strip()
                        for arg in script_lines[line_index+1: line_index+4]])
            relate_cmds.append(cmd)
            line_index = line_index + 4
        else:
            line_index = line_index + 1
    script_card_dir = data_to_card_path(card_dir, os.path.dirname(script_file))
    for relate_cmd in relate_cmds:
        apply_relate_cmd(script_card_dir, relate_cmd, card_graph)

def parse_card_graph(card_dir, connect_files):
    card_graph = {}
    script_files = []
    for connect_file in connect_files:
        if is_card_file(connect_file):
            card = Card(card_dir, connect_file)
            card_graph[card.card_path] = card
        elif is_connect_script_file(connect_file):
            script_files.append(connect_file)
    print(card_graph)
    for script_file in script_files:
        apply_connect_script(card_dir, script_file, card_graph)
    return card_graph

def build_graph(data_dir):
    connect_files = parse_connect_files(data_dir)
    print(connect_files)
    card_graph = parse_card_graph(data_dir, connect_files)
    print(card_graph)

def main(args):
    logging.basicConfig(format='%(levelname)s: %(message)s',
                        level="DEBUG" if args.log_debug else "INFO")
    build_graph(args.data_dir)
    return os.EX_OK

parser = argparse.ArgumentParser()
parser.add_argument("data_dir", help="The directory containing our data")
parser.add_argument("--log-debug", help="Log debug information",
                    default=False, action="store_true")
sys.exit(main(parser.parse_args()))