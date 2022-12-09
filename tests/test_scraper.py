"""
This is the test file which tests the SciPop function
"""

import unittest
import pandas as pd
import scipop.scraper as sc

# Avoid saying df is not a good name
# pylint: disable=invalid-name

class TestScraper(unittest.TestCase):
    """
    This class manage the test for the scraper function.
    """
    test_data_path = 'examples/UseCase1_Data.csv'
    test_res_path = 'examples/UseCase1_res.csv'

    def test_smoke(self):
        """
        Make sure the function runs at all with user input file.
        """
        df = pd.read_csv(self.test_data_path)
        sc.main(df)

    # cannot do one-shot test as the scraping result changes with time

    def test_df(self):
        """
        Edge test to make sure the function throws a TypeError
        when the df is not a pd.DataFrame.
        """
        df = {
            'Author_Name': ['Kevin'],
            'DOI': ['10.1123/wspaj.15.1.3'],
            'Title': ['The Biology of Sex and Sport']
            }
        with self.assertRaises(TypeError):
            sc.main(df)

    def test_df_cols(self):
        """
        Edge test to make sure the function throws a ValueError
        when the input dataset has less than 3 columns.
        """
        data = {
            'Author_Name': ['Kevin'],
            'DOI': ['10.1123/wspaj.15.1.3'],
            }
        df = pd.DataFrame.from_dict(data)
        with self.assertRaises(ValueError):
            sc.main(df)

    def test_title_col(self):
        """
        Edge test to make sure the function throws a ValueError
        when the df does not have title column.
        """
        df = pd.read_csv(self.test_data_path)
        df = df.drop(columns=['Article_Title'])
        with self.assertRaises(ValueError):
            sc.key_words(df)

    def test_title_type(self):
        """
        Edge test to make sure the function throws a TypeError
        when the article titles are not in string format.
        """
        data = {
            'Author_Name': ['Kevin'],
            'DOI': ['10.1123/wspaj.15.1.3'],
            'Article_Title': [10086]
            }
        df = pd.DataFrame.from_dict(data)
        with self.assertRaises(TypeError):
            sc.key_words(df)

    def test_author_col(self):
        """
        Edge test to make sure the function throws a ValueError
        when the df does not have title column.
        """
        df = pd.read_csv(self.test_data_path)
        df = df.drop(columns=['Author_Name'])
        with self.assertRaises(ValueError):
            sc.scraping_author(df)

    def test_author_type(self):
        """
        Edge test to make sure the function throws a TypeError
        when the article titles are not in string format.
        """
        data = {
            'Author_Name': [123],
            'Article_DOI': ['10.1123/wspaj.15.1.3'],
            'Article_Title': ['The Biology of Sex and Sport']
            }
        df = pd.DataFrame.from_dict(data)
        with self.assertRaises(TypeError):
            sc.scraping_author(df)

    def test_doi_col(self):
        """
        Edge test to make sure the function throws a ValueError
        when the df does not have DOI column.
        """
        df = pd.read_csv(self.test_data_path)
        df = df.drop(columns=['Article_DOI'])
        with self.assertRaises(ValueError):
            sc.scraping_author(df)

    def test_doi_type(self):
        """
        Edge test to make sure the function throws a TypeError
        when the article DOI are not in string format.
        """
        data = {
            'Author_Name': ['Kevin'],
            'Article_DOI': [10.12],
            'Article_Title': ['The Biology of Sex and Sport']
            }
        df = pd.DataFrame.from_dict(data)
        with self.assertRaises(TypeError):
            sc.scraping_doi(df)
