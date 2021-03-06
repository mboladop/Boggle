import unittest
from boggle import * # imports everything
from string import ascii_uppercase

import unittest
from boggle import *

from string import ascii_uppercase

class TestBoggle(unittest.TestCase):
    
    def test_empty_grid(self):
        grid = make_grid(0, 0)
        self.assertEqual(grid, {})
        
    def test_non_empty_grid(self):
        grid = make_grid(2, 2)
        self.assertEqual(len(grid), 4)
        
    def test_grid_has_upper_case_letters(self):
        grid = make_grid(2, 2)
        for c in grid.values():
            self.assertIn(c, ascii_uppercase)
            
    def test_neighbours_of_cell(self):
        neighbours = get_neighbours((3,4))
        expected = [
            (2,3),
            (3,3),
            (4,3),
            (4,4),
            (4,5),
            (3,5),
            (2,5),
            (2,4),
            ]
        self.assertEqual(neighbours, expected )
        
    
    def all_grid_neighbours(grid):
        return {pos: [ n for n in get_neighbours(pos) if n in grid] for pos in grid}

    def path_to_word(grid, path):
        return "COD"