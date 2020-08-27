import unittest
from numberdisplay import NumberDisplay 

class TestsNumberDisplay(unittest.TestCase):
    def setUp(self):
        self.numberdisplay = NumberDisplay()
    
    def test_size(self):
        #check less than 1 
        self.assertRaises(ValueError, self.numberdisplay.display_numbers,'123', 0 )
        #check larger than 10
        self.assertRaises(ValueError, self.numberdisplay.display_numbers,'123', 11 )
    
    def test_target(self):
        #check negative 
        self.assertRaises(ValueError, self.numberdisplay.display_numbers,'-1', 3 )
        self.assertRaises(ValueError, self.numberdisplay.display_numbers,'1-23', 3 )
        #check another kind of char
        self.assertRaises(ValueError, self.numberdisplay.display_numbers,'a1', 3 )
        self.assertRaises(ValueError, self.numberdisplay.display_numbers,'1|23', 3 )
        #Empty target
        self.assertRaises(ValueError, self.numberdisplay.display_numbers,'', 3 )
    
    def test_size2(self):
        self.assertEqual(['      --   --        --  ', 
                          '   |    |    | |  | |    ',
                          '   |    |    | |  | |    ', 
                          '      --   --   --   --  ', 
                          '   | |       |    |    | ', 
                          '   | |       |    |    | ', 
                          '      --   --        --  '],
                          self.numberdisplay.display_numbers('12345',2))
    def test_size5(self):
        self.assertEqual([' ---   ---   ---   ---   ---  ', 
                          '|         | |   | |   | |   | ', 
                          '|         | |   | |   | |   | ', 
                          '|         | |   | |   | |   | ', 
                          ' ---         ---   ---        ', 
                          '|   |     | |   |     | |   | ', 
                          '|   |     | |   |     | |   | ', 
                          '|   |     | |   |     | |   | ', 
                          ' ---         ---   ---   ---  '],
                          self.numberdisplay.display_numbers('67890',3))

if __name__ == '__main__':
    unittest.main()