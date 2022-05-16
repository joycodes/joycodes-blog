from flask import render_template
from . import main as main
@main.app_errorhandler(404)
def error_page(error):
    '''
    function to render the 404 error page
    '''
    return render_template('error.html'),404