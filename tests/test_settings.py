# Import local settings if there are any
# create your own local settings or put your api/portal here
try:
    from test_settings_local import *
except ImportError:
    api_token = 'api_token_here'
    portal = 'portal_here'