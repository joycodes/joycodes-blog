import urllib.request,json
from .models import Quotes
#Getting the movie base URL
base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTES_API_BASE_URL']
    
def get_quotes():
    '''
    function to get the json response to our url request
    '''
    get_quotes_url = base_url
    
    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)
        
        quotes_results = None
        if get_quotes_response:
            quotes_results_list = get_quotes_response
            quotes_results = process_results(quotes_results_list)
            
    return quotes_results
    

def process_results(quotes_list):
    '''
    function that processes the list of movie details to movie objects
    Args:
        movie_list: Alist of dictionaries that contain movie details
    returns: 
        movie_results: A list of movie objects
    '''
    
    quote_results = []
    
    for quote_item in quotes_list:
        author = quote_item.get('author')
        id = quote_item.get('id')
        quote = quote_item.get('quote')
        permalink = quote_item.get('permalink')
        
        if quote:
            quote_object = Quotes(author,id, quote, permalink)
            quote_results.append(quote_object)
            
    return quote_results