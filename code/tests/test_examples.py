# see https://github.com/CleanCut/green#unit-test-structure-tutorial
import unittest


class TestExamples(unittest.TestCase):

  def test_equals(self):
    "Example test using equality"
    self.assertEqual(2, 2)

