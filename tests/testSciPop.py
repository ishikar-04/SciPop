"""
This is the test file which tests the SciPop function
"""
import unittest
import pandas as pd
from scipop.scraper import main
from scipop.scraper import key_words
from scipop.scraper import scraping_author
from scipop.scraper import scraping_doi

class TestScraper(unittest.TestCase):

    def test_smoke(self):
        """
        Make sure the function runs at all with user input file.
        """
        df = pd.read_csv('UseCase1_Data.csv')
        main(df)
        return

    def test_df(self):
        """
        Edge test to make sure the function throws a TypeError
        when the df is not a pd.DataFrame.
        """
        df = {
            'Author_Name': 'Kevin',
            'DOI': '10.1123/wspaj.15.1.3',
            'Title': 'The Biology of Sex and Sport'
            }
        with self.assertRaises(TypeError):
            main(df)
        return

    def test_df_cols(self):
        """
        Edge test to make sure the function throws a ValueError
        when the input dataset has less than 3 columns.
        """
        data = {
            'Author_Name': 'Kevin',
            'DOI': '10.1123/wspaj.15.1.3',
            }
        df = pd.DataFrame.from_dict(data)
        with self.assertRaises(ValueError):
            main(df)
        return

    def test_title_col(self):
        """
        Edge test to make sure the function throws a ValueError
        when the df does not have title column.
        """
        df = pd.read_csv('UseCase1_Data.csv')
        df = df.drop(columns=['Article_Title'])
        with self.assertRaises(ValueError):
            key_words(df)
        return

    def test_title_type(self):
        """
        Edge test to make sure the function throws a TypeError
        when the article titles are not in string format.
        """
        data = {
            'Author_Name': 'Kevin',
            'DOI': '10.1123/wspaj.15.1.3',
            'Article_Title': 10086
            }
        df = pd.DataFrame.from_dict(data)
        with self.assertRaises(TypeError):
            key_words(df)
        return

    def test_author_col(self):
        """
        Edge test to make sure the function throws a ValueError
        when the df does not have title column.
        """
        df = pd.read_csv('UseCase1_Data.csv')
        df = df.drop(columns=['Author_Name'])
        with self.assertRaises(ValueError):
            scraping_author(df)
        return

    def test_author_type(self):
        """
        Edge test to make sure the function throws a TypeError
        when the article titles are not in string format.
        """
        data = {
            'Author_Name': 123,
            'DOI': '10.1123/wspaj.15.1.3',
            'Article_Title': 'The Biology of Sex and Sport'
            }
        df = pd.DataFrame.from_dict(data)
        with self.assertRaises(TypeError):
            scraping_author(df)
        return

    def test_doi_col(self):
        """
        Edge test to make sure the function throws a ValueError
        when the df does not have DOI column.
        """
        df = pd.read_csv('UseCase1_Data.csv')
        df = df.drop(columns=['Article_DOI'])
        with self.assertRaises(ValueError):
            scraping_author(df)
        return

    def test_doi_type(self):
        """
        Edge test to make sure the function throws a TypeError
        when the article DOI are not in string format.
        """
        data = {
            'Author_Name': 'Kevin',
            'Article_DOI': 10.12,
            'Article_Title': 'The Biology of Sex and Sport'
            }
        df = pd.DataFrame.from_dict(data)
        with self.assertRaises(TypeError):
            scraping_doi(df)
        return
