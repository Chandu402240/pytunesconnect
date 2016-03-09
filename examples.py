# standard library
import os
import json
import datetime
import time

# local modules
import pytunesconnect


class PyTunesConnectTests():
    
    def __init__(self, accountName, password):
        self.itc = pytunesconnect.PyTunesConnect(accountName, password)

    def sales_and_trends_example(self):
        filters = {
            'Content' : [],
            'Territory' : ['Argentina'],
            'Device' : [],
            'Category' : [],
            'Content Type' : [],
            'Transaction Type' : [],
            'CMB' : [],
            'Version' : []
        }
        print self.itc.get_sales_and_trends_data('Territory','Units','Days',datetime.date(2003,4,12),datetime.date(2016,12,31), filters)
    
    def sales_and_trends_metadata_example(self):
        print self.itc.get_sales_and_trends_metadata()
        print self.itc.get_sales_and_trends_metadata_options()
    
    def app_analytics_example(self, testadamId):
        print self.itc.get_app_analytics_data(testadamId, datetime.date(2015,12,1), datetime.date(2015,12,31), 'App Store Views', 'Device')
    
    def user_info_example(self):
        print self.itc.get_user_info()
        print self.itc.get_contentproviderids_and_vendornumbers()
    
    def payments_and_financial_reports_example(self, contentProviderId, vendornumber):
        print self.itc.get_latest_reported_earnings()
        self.itc.get_earnings(contentProviderId, vendornumber, 2016, 1) # this will save to a local file called 'output.zip'

    def get_apps_example(self):
        print self.itc.get_apps()
        print self.itc.get_adam_ids()


if __name__ == '__main__':
    
    # edit this to where your credentials are stored
    path = os.path.join(os.path.expanduser('~'), 'itunes_connect_credentials.json')
    
    with open(path) as f:
        
        credentials = json.load(f)
    
        accountName = credentials['accounts'][0]['accountName']
        password = credentials['accounts'][0]['password']
        contentProviderId = credentials['accounts'][0]['contentProviderId']
        vendornumber = credentials['accounts'][0]['vendornumber']
        testadamId = credentials['accounts'][0]['adamIds'][0]
        
        itc = PyTunesConnectTests(accountName, password)
        
        # uncomment the below to test the code
        
        #itc.sales_and_trends_example()
        #itc.sales_and_trends_metadata_example()
        #itc.app_analytics_example(testadamId)
        #itc.payments_and_financial_reports_example(contentProviderId, vendornumber)
        #itc.get_apps_example()
