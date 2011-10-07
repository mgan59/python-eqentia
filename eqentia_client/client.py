"""
A RESTClient for Eqentia, currently supports all client endpoints defined
in their documentation v0.9.5 (August 23, 2011)

Rules for Eqentia API
-----------------------------
Total Eqentia API Request:  1 request every 10 seconds
Identical API Requests:     1 request every 5 minutes

These are software numbers and currently are not applied to unittests or generators
so don't abuse this and ruin Eqentia's generosity :)
"""
__version__ = "0.3"


import urllib
import urllib2
import sys
import logging
import simplejson

from iterators import EqentiaRestIterator

# The user agent string sent to eqentias api when making requests. If you are
# using this module in your own application, you should probably fork the library
# and adjust this user-agent and make it your own :)
USER_AGENT = "Python-Eqentia-Rest-Client/%s +github:mgan59" % __version__

class EqentiaRestClient(object):
    
    base_url = 'http://api.eqentia.com/api/%s/%s?%s'
    
    
    def __init__(self, api_token='', portal=''):
        self.api_token = api_token
        self.portal = portal
        
    
    def _request(self, end_point='', **kwargs):
        
        ## parse kwargs for valid params
        end_point = end_point
        params = {'token':self.api_token}
        for key,value in kwargs.items():
            params[key]=value
            
        url = self.base_url % (self.portal, end_point, urllib.urlencode(params))
        
        try:
            request = urllib2.Request(url=url)
            request.add_header("User-agent",USER_AGENT)
            response = urllib2.urlopen(request)
            json_dict = simplejson.loads(response.read())
        except urllib2.URLError:
            logging.error('Invalid URL for API connection')
            return False
        return json_dict
        
    def headlines(self, **kwargs):
        end_point = 'headlines'
        if 'page' not in kwargs:
            return EqentiaRestIterator(client=self, end_point=end_point, **kwargs)
        else:
            return self._request(end_point=end_point, **kwargs)
        
    def entities(self, entity_id=None, **kwargs):
        end_point = 'entity/%d' % entity_id
        if 'page' not in kwargs:
            return EqentiaRestIterator(client=self, end_point=end_point, **kwargs)
        else:
            return self._request(end_point=end_point, **kwargs)
        
    def connections(self, connection_id=None, **kwargs):
        end_point = 'connection/%d' % connection_id
        if 'page' not in kwargs:
            return EqentiaRestIterator(client=self, end_point=end_point, **kwargs)
        else:
            return self._request(end_point=end_point, **kwargs)
        
    def connection_maps(self, **kwargs):
        return self._request(end_point='connections_map', **kwargs)
        
    def curation(self, **kwargs):
        end_point = 'curate'
        if 'page' not in kwargs:
            return EqentiaRestIterator(client=self, end_point=end_point, **kwargs)
        else:
            return self._request(end_point=end_point, **kwargs)
        
    def news_groups(self):
        end_point='newsgroups'
        if 'page' not in kwargs:
            return EqentiaRestIterator(client=self, end_point=end_point, **kwargs)
        else:
            return self._request(end_point=end_point, **kwargs)
        
    def navigation(self):
        return self._request(end_point='navigation')
        
    def hot_companies(self):
        return self._request(end_point='hot_companies')
        
    def hot_connections(self):
        return self._request(end_point='hot_connections')
