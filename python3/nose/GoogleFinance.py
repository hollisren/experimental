#! /usr/bin/env python3

'''
This class is designed to pull down the history of a stock
from Google's Finance Web Site
'''


import urllib.request
import datetime
import logging


class GoogleFinance:

    '''
    This is a class to manage pulling down a stock's history from Google's
    Finance web site
    '''

    def __init__(self, symbol=None, start_date=None):

        # http://stackoverflow.com/questions/5081710/how-to-create-a-stock-quote-fetching-app-in-python

        self.symbol = symbol.upper()
        self.start_date = start_date
        self.base_url = "http://www.google.com/finance/historical?q="
        logging.info("GoogleFinance: %s on %s" % (self.symbol,
                                                  self.start_date))
        return

    def get_historical_stock_data(self, filename=None):
        """
        Get the historical stock prices from the start_date in
        the config file until today
        """
        today = datetime.datetime.today()
        url_string = self.base_url + self.symbol
        url_string += "&startdate=%s-%s-%s" % (self.start_date.tm_year,
                                               self.start_date.tm_mon,
                                               self.start_date.tm_mday)
        url_string += "&enddate=%s-%s-%s" % (today.year,
                                             today.month, today.day)
        url_string += "&output=csv"

        logging.info(url_string)
        url_data = urllib.request.urlopen(url_string)
        # http://stackoverflow.com/questions/18664712/split-function-add-xef-xbb-xbf-n-to-my-list
        csv = (url_data.read()).decode("utf-8-sig").encode("utf-8")

        if filename is not None:
            try:
                file_handle = open(filename, 'w')
                file_handle.write(csv.decode("utf-8"))
                file_handle.close()
            except OSError:
                error_string = "%s: Failed to open %s for writing" %\
                    (__name__, filename)
                logging.error(error_string)
                print("Failed to open %s for writing!" % filename)
        return
