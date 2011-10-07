import unittest
import logging
import test_settings
from eqentia_client.client import EqentiaRestClient

'''
Currently low level tests to ensure the API responds without Exception for each endpoint and that the
response-key in data is set to True for valid response.

In order to enable the test-harnass please define an api_token and portal in the test_settings
'''

class ClientTestCase(unittest.TestCase):

    def setUp(self):
        self.api_token = test_settings.api_token
        self.portal = test_settings.portal
        self.cl = EqentiaRestClient(api_token=self.api_token,portal=self.portal)
    
    def test_headine(self):
        print 'Running test_headline'
        headlines = self.cl.headlines()
        if headlines:
            self.assertTrue(headlines['response'], msg='A response was returned but the field response was False')
        else:
            self.assertTrue(headlines, msg='The API request failed due to an exception')
            
    def test_connections(self):
        print 'Running test_connections'
        connections = self.cl.connections(connection_id=50901)
        if connections:
            self.assertTrue(connections['response'], msg='A response was returned but the field response was False')
        else:
            self.assertTrue(connections, msg='The API request failed due to an exception')
            
    def test_connection_maps(self):
        print 'Running test_connection_maps'
        connection_maps = self.cl.connection_maps()
        if connection_maps:
            self.assertTrue(connection_maps['response'], msg='A response was returned but the field response was False')
        else:
            self.assertTrue(connection_maps, msg='The API request failed due to an exception')
            
    def test_curation(self):
        print 'Running test_curation'
        curation = self.cl.curation()
        if curation:
            self.assertTrue(curation['response'], msg='A response was returned but the field response was False')
        else:
            self.assertTrue(curation, msg='The API request failed due to an exception')
    
    def test_news_groups(self):
        print 'Running test_news_groups'
        news_groups = self.cl.news_groups()
        if news_groups:
            self.assertTrue(news_groups['response'], msg='A response was returned but the field response was False')
        else:
            self.assertTrue(news_groups, msg='The API request failed due to an exception')
            
    def test_navigation(self):
        print 'Running test_navigation'
        navigation = self.cl.navigation()
        if navigation:
            self.assertTrue(navigation['response'], msg='A response was returned but the field response was False')
        else:
            self.assertTrue(navigation, msg='The API request failed due to an exception')
            
    def test_hot_companies(self):
        print 'Running test_hot_companies'
        hot_companies = self.cl.hot_companies()
        if hot_companies:
            self.assertTrue(hot_companies['response'], msg='A response was returned but the field response was False')
        else:
            self.assertTrue(hot_companies, msg='The API request failed due to an exception')
            
    def test_hot_connections(self):
        print 'Running test_hot_connections'
        hot_connections = self.cl.hot_connections()
        if hot_connections:
            self.assertTrue(hot_connections['response'], msg='A response was returned but the field response was False')
        else:
            self.assertTrue(hot_connections, msg='The API request failed due to an exception')

if __name__ == '__main__':
    unittest.main()