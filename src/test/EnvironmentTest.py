import unittest

#from src\main\Environment.py import extract_int, convert_midi_to_txt, convert_txt_to_midi

class TestEnvironmentMethods(unittest.TestCase):
    def test_extractInt(self):
        a = 1
        b = 0
        c = 1
        message = "does not equal"
        self.assertEqual(a,c,message)
        #self.assertEqual(a,b,message)
    
    def test_convertMidiToText(self):
        return 0
    
        
    def test_convertTextToMidi(self):
        return 0


if __name__ == '__main__':
    unittest.main()