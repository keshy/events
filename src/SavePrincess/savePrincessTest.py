'''
Created on Jun 27, 2013
Unit test suite for the save princess solution
@author: Krishnan_Narayan
'''
import unittest
import savePrincess

class SavePrincessTest(unittest.TestCase):
    grid = [];
    n = 0;
    
    def setup(self):
        grid = ['---', '-m-', 'p--'];
        n = 3;
    @unittest.skip("already tested")    
    def test_invalid(self):
        
        self.assertEqual(savePrincess.displayPathtoPrincess(0, None), None, "Passed null test case");
        
    @unittest.skip("already tested")   
    def test_grid(self):    
        test = ['avc', 'sadas'];
        self.assertEqual(savePrincess.displayPathtoPrincess(1, ['m']), savePrincess.Moves.NONE, "Passed invalidation of grid size 1");
        self.assertEqual(savePrincess.displayPathtoPrincess(2, test), None, "Passed test for invalid grid entry");
            
    def test_success(self):
        self.assertNotEqual(savePrincess.displayPathtoPrincess(3, ['---', '-m-', '--p']), ['DOWN', 'RIGTH'], "Successfully saved the princess");    

if __name__ == '__main__':
    unittest.main()
        
        
        
               

