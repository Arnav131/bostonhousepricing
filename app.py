import pickle
# importing flask as flask is used to create lightweight web application
from flask import Flask, jsonify , request , render_template,app,url_for
import numpy as np
import pandas as pd

# creating an obeject app of class Flask
app = Flask(__name__)

# integrating thr main model engin in the flask app
regmodel=pickle.load(open('regmodel.pkl' , 'rb'))
scaler = pickle.load(open('scaling.pkl' , 'rb'))
# creating a home page for the flask app using render template and home.html is the name of the html file which is created in the templates folder
@app.route('/')
def home():
    return render_template('home.html')

# creating a predict api using postman to predict the price of the house based on the input given by the user in json format
@app.route('/predict_api' , methods=['POST']) ## post means some sort of request given from the user side and ans is given to user via an api call

def predict_api():
    data = request.json['data'] ## data is given in json format and we are fetching the data from the json file
    print(data) ## these will be in the key value pair format and we are fetching the data from the json file
    print(np.array([list(data.values())]).reshape(1,-1)) # what i have done here is that i have converted the data into numpy array and reshaped it to 1, -1 because we are giving the data in 2D array format to the model


    # now we got the data but first we have STANDARDIZE the data and convert it into numpy array and reshape it to 1, -1 because we are giving the data in 2D array format to the model
    new_data = scaler.transform(np.array([list(data.values())]).reshape(1,-1))
    output = regmodel.predict(new_data)
    print(output[0])

    # now we have to return the output in json format so that it can be used in the front end ... this joson is the output as the result of the api call and it will be used in the front end to display the result to the user
    return jsonify(output[0])


@app.route('/predict' ,  methods=['POST']) ## post means some sort of request given from the user side and ans is given to user via an api call
def predict():
    data = [float(x) for x in request.form.values()]
    final_imput = scaler.transform(np.array(data).reshape(1,-1))
    print(final_imput)
    output = regmodel.predict(final_imput)[0]
    return render_template("home.html" , prediction_text = "The House Price Prediction is{}".format(output))



#now to test the api we have to run the flask app and we can do that by running the command flask run in the terminal and then we can use postman to test the.
if __name__ == "__main__":
    app.run(debug=True) # what debug=True does is that it will automatically reload the flask app whenever we make any changes in the code and it will also show us the error in the terminal if there is any error in the code
