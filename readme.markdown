# Overview

  Python-Eqentia is a low level wrapper REST based client for python to access the JSON data from Eqentia's curation platform.  This library was built to pair with a clients portal to extract headlines and entity data for local storage to seamless integration into an application.  Please consultant the Eqentia API documentation for rules and guidelines for using their API with your application.  

## Eqentia API Support

  Currently v0.3 of Python-Eqentia supports Eqentia's v0.9.5 and the following endpoints
  
  * headlines
  * entities
  * connections
  * connections maps
  * curation
  * news groups
  * navigation
  * hot companies
  * hot connections
  
### Iterators

  As of v0.3 Iterators were added for endpoints that accept the `page` parameter.
  
  * headlines
  * entities
  * connections
  * news groups
  * curation
  
  These iterators provides a seamless interaction with a given api without having to paginate your data requests.  Allowing for easier content digestion.

# Installation

## Using Virtualenv & PIP
  For installation I'm assuming you are using the `virtualenv` way of working with Python projects.  If you're unfamiliar, I highly recommend adopting this technique as it has become a standard development methodology for Pythonistas.
  
  * [Python Hacker Tools, virtualenv, fabric, and pip](http://www.clemesha.org/blog/modern-python-hacker-tools-virtualenv-fabric-pip)
  * [Presentation on Pip & virtualenv](http://mathematism.com/2009/07/30/presentation-pip-and-virtualenv/)

## Installing with pip from Github

    pip install -e git://github.com/mgan59/python-eqentia#egg=python-eqentia


# Usage

## Basic API Endpoint usage 

  First step is to include python-eqentia once installed
  
    from eqentia_client.client import EqentiaRestClient
    

  Instantiate the client using an api_token provided by Eqentia and also designate a portal
  
    ec = EqentiaRestClient(api_token='yourtokengoeshere', portal='portalname')
    
    ## example of several calls
    ## will return all headlines for the first page - by default
    headline_news = ec.headlines(page=1)
    
    ## An endpoint accepts params as keyword arguments (kwargs)
    ## to get second page, pass the page parameter
    ## also change the number of per page
    headline_news_page_two = ec.headlines(page=2, per_page=80)
    
    ## Access Hot Companies
    hot_companies = ec.hot_companies()
    
    ## access the data from headline_news
    for headline in headline_news['documents']:
        ## will print a dictionary obj contain the JSON fields
        print headline
        
    
## Using the Iterators

  Similar to the above include the library and instantiate the RestClient like before.  Note these are new and still need tested fully, use at your own risk :)
  
      from eqentia_client.client import EqentiaRestClient
      ec = EqentiaRestClient(api_token='yourtokengoeshere', portal='portalname')
      
  To use a given headline as an iterator just make the call without the `page` and by default an iterator is returned
  
    for headline in client.headlines():
        ## will print the dictionary
        print headline
        
  For the Iterators there are additional params to control the start and max pages
  
      for headline in client.headlines(start_page=2, max_page=4):
          ## will print the dictionary
          print headline
          
  
# Todo

  * Add unittest support for generators
  * Add support for timers for iterators/generators
  * Add Param validation
  * Add decorator to do a proxy for page/not-page calls in client
