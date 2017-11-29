from bs4 import BeautifulSoup
import os
import urllib2


class GetUrls():

    scan_depth = 0
    scan_width = 0

    def __init__(self, url, depth=2, width=1):
        self.url = url

    def get_urls(self):
        pass


class ValidateUrl(GetUrls):

    """
    Class for digging out urls from websites
    Required Inputs: urls
    Optional Inputs: depth, width
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

