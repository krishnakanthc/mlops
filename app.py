from flask import Flask
from main import *
app = Flask(__name__)
@app.route('/')
def hello_world():
    training_accuracy,testing_accuracy=main()
    return "Training_accuracy {0}  Testing Accuracy {1}".format(training_accuracy,testing_accuracy)
    
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=False,host="0.0.0.0",port=5000)