'''
Custom Iterator Objects to handle Pagination of API results for 
easy iteration of document records

Currently Experimental, no test coverage
'''

import logging

class EqentiaRestIterator(object):
    
    def __init__(self, client=None, end_point=None, **kwargs):
        self.client = client
        self.end_point = end_point
        self.results = None
        self.internal_document_index = 0
        ## if start_page set inject
        print kwargs
        if 'start_page' in kwargs:
            self.start_page = kwargs['start_page']
        else:
            self.start_page = 1
        
        ## set current_page to start where the start_page was defined
        self.current_page = self.start_page
        
        ## debated this issue, decided if implementor did not pass in per_page then
        ## default to 200 to reduce the number of API requests for pagination
        ## however if per_page was set by user then they are doing it for a reason
        ## hopefully, or they need smacked upside their skull
        if 'per_page' not in kwargs:
            ## setting to 200 which is stated in eqentia api as of v0.9.5
            kwargs['per_page'] = 200
        self.iterator_kwargs = kwargs
        
        if 'max_page' in kwargs:
            self.max_page = kwargs['max_page']
        else:
            self.max_page = 10
        
    def __iter__(self):
        return self
        
    def next(self):
        
        if not self.results or (self.internal_document_index == len(self.results['documents'])):
            ## always reset our internal_document pointer when a new page is fetched
            self.internal_document_index = 0
            ## inject our pagination in here
            self.iterator_kwargs['page'] = self.current_page
            #print '** kwargs check'
            #print self.iterator_kwargs
            self.results = self.client._request(end_point=self.end_point, **self.iterator_kwargs)
            logging.info('-------- Current Results Page  %d ----------'% self.current_page)
            logging.info('-------- Accessed Documents    %d ----------'% len(self.results['documents']))
            ## because we set current page to start page in _init_ don't increment till
            ## after our api call
            self.current_page += 1
        
        ## Stop iteration if we hit our max_page limit
        if self.current_page > self.max_page:
            raise StopIteration
        
        ## Stop iteration when the API returns an empty list of 'Documents'
        if len(self.results['documents']) == 0:
            raise StopIteration
        
        self.internal_document_index += 1
        return self.results['documents'][self.internal_document_index-1]
        