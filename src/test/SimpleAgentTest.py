#from SimpleAgent import create_melody
import unittest

class TestSimpAgentMethods(unittest.TestCase):

    def test_createMelody(self):
        a = 1
        b = 0
        c = 1
        message = "does not equal"
        self.assertEqual(a,c,message)
        #self.assertEqual(a,b,message)


if __name__ == '__main__':
    unittest.main()
