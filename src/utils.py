import os
import random

__author__ = 'Carlos Gonzales'


def exist_path(path):
    """Return true if exist a specific path

    Keyword arguments:
    path -- name of the path to be verified

    """
    return os.path.exists(path)


def is_valid_path(path):
    """Return true if a specific path is valid

    Keyword arguments:
    path -- name of the path to be verified

    """
    return os.path.isabs(path)


def exist_file(path_file):
    """Return true if a specific file esist is the path

    Keyword arguments:
    path_file -- name of the path to be verified

    """
    return os.path.isfile(path_file)


def cross(list_a, list_b):
    """Cross product of elements in A and elements in B and return a new list.
    e.g.
    A = ['A', 'B'] and B = ['1', '2']
    return ['A1', 'A2', 'B1', 'B2']

    Keyword arguments:
    list_a -- list of elements of A
    list_b -- list of elements of B

    """
    return [a + b for a in list_a for b in list_b]


def get_element_exists_in_sequence(sequence):
    """Return some element of sequence that is true.

    Keyword arguments:
    sequence -- sequence of values to search the element with true value

    """
    for element in sequence:
        if element:
            return element
    return False


def generate_random_number():
    """Return a random number between 1 and 9"""
    return random.randint(1, 9)
