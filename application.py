from flask import Flask, render_template

#
# application.py
#
# The main application for my website
#
# @author Chris Wolf
# @version 1.0.0 (May 28, 2019)
# @contact chriswolfdesign@gmail.com
#

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Default route for my website
    '''
    return render_template('index.html')

# main functionality
if __name__ == '__main__':
    app.run(debug=True)
