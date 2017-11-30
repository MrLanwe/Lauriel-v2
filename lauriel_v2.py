from bs4 import BeautifulSoup
import os
from urllib3 import PoolManager


class GetUrls():

    """
    Class responsible for extracting possible url's from websites
    Input: str  | website address
    Output: str | list of possible websites and internal pages
    """

    scan_depth = 0
    scan_width = 0

    def __init__(self, url, depth=2, width=1):
        self.url = url

    def get_urls(self):
        self.http = PoolManager()
        self.html = self.http.request('GET', self.url)
        self.parsed_web = BeautifulSoup(self.html.data, 'html.parser')
        self.possible_urls = [link['href'] for link in
                              self.parsed_web.find_all('a', href=True)]


class ValidateUrl(GetUrls):

    """
    Class responsible for checking if urls are correct and that they are
    accesible.
    Input: str  | url
    Output: str | valid url
    """

    correct_syntax_pattern = ".*http.*"
    ok_status_code = '200'

    def __init__(self):
        pass

    def validate_url_syntax(self):
        pass

    def validate_url_access(self):
        pass


class Results(GetUrls):

    def __init__(self):
        pass

    def all_websites(self):
        pass


class Output(Results):

    def __init__(self):
        pass

    def to_text_file(self):
        pass

    def to_excel_file(self):
        pass

    def to_csv_file(self):
        pass

