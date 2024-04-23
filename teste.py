import unittest
from tree import Tree
class TestFindFunction(unittest.TestCase):

    def test_find_existing_data(self):
        """Test finding existing data"""
        tree = Tree()
        tree.add(5)
        tree.add(3)
        tree.add(7)
        tree.add(2)
        tree.add(4)
        tree.add(6)
        tree.add(8)

        result = tree._find(4, tree.getRoot())
        self.assertIsNotNone(result)
        self.assertEqual(result.data, 4)

    def test_find_non_existing_data(self):
        """Test finding non-existing data"""
        tree = Tree()
        tree.add(5)
        tree.add(3)
        tree.add(7)
        tree.add(2)
        tree.add(4)
        tree.add(6)
        tree.add(8)

        result = tree._find(9, tree.getRoot())
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
