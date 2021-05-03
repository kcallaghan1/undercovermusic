import unittest

#from src\main\Environment.py import extract_int, convert_midi_to_txt, convert_txt_to_midi

class TestEnvironmentMethods(unittest.TestCase):
    def test_extractInt(self):
        a = 1
        b = 1
        message = "not equal"
        self.assertEquals(a,b,message)
    
    def test_convertMidiToText(self):
        return 0
    
        
    def test_convertTextToMidi(self):
        return 0


""" def main():
    extractIntTest(0)
    convertMidiToTextTest(0)
    convertTextToMidiTest(0) """


if __name__ == '__main__':
    unittest.main()