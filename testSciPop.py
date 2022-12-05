"""
This is the test file which tests the SciPop function
"""
import numpy as np
import unittest

from functions_DG import main_function

class TestMain(unittest.TestCase):

    def test_smoke(self):
        """
        Make sure the function runs at all with user input file
        """
        data = pd.read_csv('UseCase1_Data.csv') # use case 1 test file
        main_function(data)
        return

    def test_csv(self):
        """
        Check that input is a .csv file, it cannot be any other file type
        """
        data = pd.read_csv('data.xlsx')
        with self.assertRaises(TypeError):
            main_function(data) #data must be a .csv file
        return

    def test_missing(self):
        """
        Check whether the .csv file has missing data for each column header,
        if Author_Name is missing but all other col's are present, locate author
        name using a scraper
        """
        missing_data = pd.isnull(df) #in process trying to figure out how to account for any missing data input by user










