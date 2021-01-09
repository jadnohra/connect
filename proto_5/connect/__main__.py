import argparse
import os
import logging
import sys
from types import SimpleNamespace
from .util.print_tree import print_tree

def data_to_card_path(card_dir, fpath):
    return os.path.splitext("/" + os.path.relpath(fpath, start=card_dir))[0]

class Card:
    def __init__(self, card_dir, fpath):
        self._fpath = fpath
        self._card_path = data_to_card_path(card_dir, fpath)

    @property
    def card_path(self):
        return self._card_path

    @property
    def card_dir(self):
        return Card.to_card_dir(self._card_path)

    @property
    def card_name(self):
        return Card.to_card_name(self._card_path)

    def to_card_dir(card_path):
        return os.path.dirname(card_path)

    def to_card_name(card_path):
        return os.path.basename(card_path)

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

class CardTree:
    class Node:
        def __init__(self, name):
            self._name = name
        def print(self):
            print_tree(self,
                       lambda node: node.children.values()
                                    if type(node) == CardTree.DirNode
                                    else [],
                       lambda node: node.name)
        @property
        def name(self):
            return self._name

    class DirNode(Node):
        def __init__(self, name):
            super().__init__(name)
            self.children = {}

    class CardNode(Node):
        def __init__(self, card):
            super().__init__(card.card_name)
            self.card = card

    def __init__(self):
        self._root_node = self.DirNode(".")

    def _ensure_child_dir_node(self, parent_dir, nodename):
        if nodename not in parent_dir.children:
            parent_dir.children[nodename] = self.DirNode(nodename)
        return parent_dir.children[nodename]

    def _get_card_dir_node(self, card_dir):
        dir_parts = card_dir.split(os.sep)[1:]
        path_node = self._root_node
        for dirname in dir_parts:
            path_node = self._ensure_child_dir_node(path_node, dirname)
        return path_node

    def add_card_node(self, card):
        dir_node = self._get_card_dir_node(card.card_dir)
        dir_node.children[card.card_name] = self.CardNode(card)

    def get_card(self, card_path):
        dir_node = self._get_card_dir_node(Card.to_card_dir(card_path))
        return dir_node.children.get(Card.to_card_name(card_path), None)

    @property
    def root():
        return self._root_node

    def print(self):
        self._root_node.print()

def apply_connect_script(card_dir, script_file, card_tree):
    def get_card(card_path, card_tree):
        card = card_tree.get_card(card_path)
        if card is None:
            logging.error(f"Card {card_path} mentioned in {script_file} not found")
        return card
    def get_cards(script_card_dir, pattern, card_tree):
        if pattern.startswith("/"):
            return [get_card(pattern, card_tree)]
        elif pattern == "*":
            # TODO this is slow, we need a tree structure
            return []
        else:
            return [get_card(os.path.join(script_card_dir, pattern), card_tree)]
    def apply_relate_cmd(script_card_dir, cmd, card_tree):
        src_pat, rel_pat, target_pat = cmd
        src_cards = get_cards(script_card_dir, src_pat, card_tree)
        rel_cards = get_cards(script_card_dir, rel_pat, card_tree)
        target_cards = get_cards(script_card_dir, target_pat, card_tree)
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
        apply_relate_cmd(script_card_dir, relate_cmd, card_tree)

def parse_card_tree_from_files(card_dir, connect_files):
    card_tree = CardTree()
    script_files = []
    for connect_file in connect_files:
        if is_card_file(connect_file):
            card = Card(card_dir, connect_file)
            card_tree.add_card_node(card)
        elif is_connect_script_file(connect_file):
            script_files.append(connect_file)
    card_tree.print()
    for script_file in script_files:
        apply_connect_script(card_dir, script_file, card_tree)
    return card_tree

def parse_card_tree(data_dir):
    connect_files = parse_connect_files(data_dir)
    print(connect_files)
    card_tree = parse_card_tree_from_files(data_dir, connect_files)
    card_tree.print()

def main(args):
    logging.basicConfig(format='%(levelname)s: %(message)s',
                        level="DEBUG" if args.log_debug else "INFO")
    parse_card_tree(args.data_dir)
    return os.EX_OK

parser = argparse.ArgumentParser()
parser.add_argument("data_dir", help="The directory containing our data")
parser.add_argument("--log-debug", help="Log debug information",
                    default=False, action="store_true")
sys.exit(main(parser.parse_args()))