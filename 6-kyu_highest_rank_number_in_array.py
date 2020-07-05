import unittest
from parameterized import parameterized

def highest_rank(arr):
    rank_dict =  dict((x,arr.count(x)) for x in set(arr))
    return max(keys for keys,values in rank_dict.items() if values == max(rank_dict.values()))

class TestSolution(unittest.TestCase): 
    @parameterized.expand([
        ([12, 10, 8, 12, 7, 6, 4, 10, 12], 12),
        ([12, 10, 8, 12, 7, 6, 4, 10, 10], 10),
        ([1, 1, 2, 2, 3, 3], 3),
        ([ -1, -1, -1, 5, 5], -1),
    ])
    def test_highest_rank_number(self, array, highest_rank_most_freq):
            self.assertEqual(highest_rank(array), highest_rank_most_freq)
    
