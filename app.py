import pickle
from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from recommendation import get_recommendations  # Import the recommendation module

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session management

# Load dataset and train model
data = pd.read_csv('final_co2.csv', index_col=0)
X = data.drop(['CO2_Emissions'], axis=1)
y = data['CO2_Emissions']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

reg = LinearRegression()
reg.fit(X_train, y_train)

# Save and load model
filename = 'finalized_model.pkl'
pickle.dump(reg, open(filename, 'wb'))
model = pickle.load(open('finalized_model.pkl', 'rb'))

# Dummy user credentials for login (for testing)
users = {"admin": "password123"}

@app.route('/')
def landing():
    """Landing Page"""
    return render_template('landing.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login Page"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('calculator'))  # Redirect to CO2 calculator

        return render_template('login.html', error="Invalid Credentials")

    return render_template('login.html')


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    """CO2 Calculator"""
    if 'user' not in session:
        return redirect(url_for('login'))  # Redirect to login if not logged in

    return render_template('calculator.html')


@app.route("/predict", methods=['POST'])
def predict():
    """Handles CO2 prediction and redirects to results page"""
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        try:
            # Extract form data
            Engine_Size = float(request.form['Engine_Size'])
            Cylinders = float(request.form['Cylinders'])
            Fuel_Consumption_City = float(request.form['Fuel_Consumption_City'])
            Fuel_Consumption_Hwy = float(request.form['Fuel_Consumption_Hwy'])
            Fuel_Consumption_Comb = float(request.form['Fuel_Consumption_Comb'])
            Fuel_Consumption_Comb_mpg = float(request.form['Fuel_Consumption_Comb_mpg'])

            Make=request.form['Make']
            if(Make=='Luxury'):
                    Make_Type_Luxury=1
                    Make_Type_Premium=0
                    Make_Type_Sports=0
                    
            elif(Make=='Premium'):
                    Make_Type_Luxury=0
                    Make_Type_Premium=1
                    Make_Type_Sports=0
                    
            elif(Make=='Sports'):
                    Make_Type_Luxury=0
                    Make_Type_Premium=0
                    Make_Type_Sports=1
                    
            else:
                    Make_Type_Luxury=0
                    Make_Type_Premium=0
                    Make_Type_Sports=0
                    

            Vehicle_Class=request.form['Vehicle_Class']
            if(Vehicle_Class=='SUV'):
                    Vehicle_Class_Type_SUV=1
                    Vehicle_Class_Type_Sedan=0 	
                    Vehicle_Class_Type_Truck=0
                
            elif(Vehicle_Class=='Sedan'):
                    Vehicle_Class_Type_SUV=0
                    Vehicle_Class_Type_Sedan=1 	
                    Vehicle_Class_Type_Truck=0
                            
            elif(Vehicle_Class=='Truck'):
                    Vehicle_Class_Type_SUV=0
                    Vehicle_Class_Type_Sedan=0 	
                    Vehicle_Class_Type_Truck=1
                
            else:
                    Vehicle_Class_Type_SUV=0
                    Vehicle_Class_Type_Sedan=0	
                    Vehicle_Class_Type_Truck=0
            


            Transmission=request.form['Transmission']
            if(Transmission=='A4'):
                    Transmission_A4=1 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0  
            elif(Transmission=='A5'):
                    Transmission_A4=0 	
                    Transmission_A5=1 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0  

            elif(Transmission=='A6'):
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=1 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0  

            elif(Transmission=='A7'):
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=1 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0  
                    
            elif(Transmission=='A8'):
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=1 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0  
                
            elif(Transmission=='A9'):
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=1 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0  
                
            elif(Transmission=='AM5'):
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=1 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0  
                
            elif(Transmission=='AM6'):
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=1 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0  
                
            elif(Transmission=='AM7'):
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=1 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0  
                
            elif(Transmission=='AM8'):
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=1 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0  
                
            elif(Transmission=='AM9'):
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=1 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0  
                
            elif(Transmission=='AS4'):
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=1 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0  
                
            elif(Transmission=='AS5'):
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=1 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0  
                
            elif(Transmission=='AS6'):
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=1 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0  
                
            elif(Transmission=='AS7'):
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=1 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0  
                
            elif(Transmission=='AS8'):
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=1 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0  
                
            elif(Transmission=='AS9'):
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=1 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0  
                
            elif(Transmission=='AS10'):
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=1 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0  
                
            elif(Transmission=='AV'):    
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=1 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0  
                    
            elif(Transmission=='AV6'):    
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=1	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0  
                    
            elif(Transmission=='AV8'):    
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=1 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0    
                    
            elif(Transmission=='AV10'):    
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=1 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=0  
                    
            elif(Transmission=='M5'):    
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=1 	
                    Transmission_M6=0 	
                    Transmission_M7=0  
                    
            elif(Transmission=='M6'):    
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=1 	
                    Transmission_M7=0    
                    
            else:    
                    Transmission_A4=0 	
                    Transmission_A5=0 	
                    Transmission_A6=0 	
                    Transmission_A7=0 	
                    Transmission_A8=0 	
                    Transmission_A9=0 	
                    Transmission_AM5=0 	
                    Transmission_AM6=0 	
                    Transmission_AM7=0 	
                    Transmission_AM8=0 	
                    Transmission_AM9=0 	
                    Transmission_AS10=0 	
                    Transmission_AS4=0 	
                    Transmission_AS5=0 	
                    Transmission_AS6=0 	
                    Transmission_AS7=0 	
                    Transmission_AS8=0 	
                    Transmission_AS9=0 	
                    Transmission_AV=0 	
                    Transmission_AV10=0 	
                    Transmission_AV6=0 	
                    Transmission_AV7=0 	
                    Transmission_AV8=0 	
                    Transmission_M5=0 	
                    Transmission_M6=0 	
                    Transmission_M7=1
                                
            
            Fuel_Type=request.form['Fuel_Type']
            if(Fuel_Type=='Type_E'):             
                    Fuel_Type_E=1 	
                    Fuel_Type_X=0 	
                    Fuel_Type_Z=0
                    
            elif(Fuel_Type=='Type_X'):
                    Fuel_Type_E=0	
                    Fuel_Type_X=1	
                    Fuel_Type_Z=0     
                    
            elif(Fuel_Type=='Type_Z'):
                    Fuel_Type_E=0	
                    Fuel_Type_X=0	
                    Fuel_Type_Z=1 
                    
            else:
                    Fuel_Type_E=0 	
                    Fuel_Type_X=0 	
                    Fuel_Type_Z=0	


            def lr(Engine_Size, Cylinders, Fuel_Consumption_City,Fuel_Consumption_Hwy, Fuel_Consumption_Comb,Fuel_Consumption_Comb_mpg,Fuel_Type_E, Fuel_Type_X,Fuel_Type_Z, Transmission_A4, Transmission_A5, Transmission_A6,Transmission_A7, Transmission_A8, Transmission_A9,Transmission_AM5, Transmission_AM6, Transmission_AM7,Transmission_AM8, Transmission_AM9, Transmission_AS10,Transmission_AS4, Transmission_AS5, Transmission_AS6,Transmission_AS7, Transmission_AS8, Transmission_AS9,Transmission_AV, Transmission_AV10, Transmission_AV6,Transmission_AV7, Transmission_AV8, Transmission_M5,Transmission_M6, Transmission_M7, Make_Type_Luxury,Make_Type_Premium, Make_Type_Sports, Vehicle_Class_Type_SUV,Vehicle_Class_Type_Sedan, Vehicle_Class_Type_Truck):
                    c=pd.DataFrame([Engine_Size, Cylinders, Fuel_Consumption_City,Fuel_Consumption_Hwy, Fuel_Consumption_Comb,Fuel_Consumption_Comb_mpg,Fuel_Type_E, Fuel_Type_X,Fuel_Type_Z, Transmission_A4, Transmission_A5, Transmission_A6,Transmission_A7, Transmission_A8, Transmission_A9,Transmission_AM5, Transmission_AM6, Transmission_AM7,Transmission_AM8, Transmission_AM9, Transmission_AS10,Transmission_AS4, Transmission_AS5, Transmission_AS6,Transmission_AS7, Transmission_AS8, Transmission_AS9,Transmission_AV, Transmission_AV10, Transmission_AV6,Transmission_AV7, Transmission_AV8, Transmission_M5,Transmission_M6, Transmission_M7, Make_Type_Luxury,Make_Type_Premium, Make_Type_Sports, Vehicle_Class_Type_SUV,Vehicle_Class_Type_Sedan, Vehicle_Class_Type_Truck]).T
                    return model.predict(c)
                
            
            prediction=lr(Engine_Size, Cylinders, Fuel_Consumption_City,Fuel_Consumption_Hwy, Fuel_Consumption_Comb,Fuel_Consumption_Comb_mpg,Fuel_Type_E, Fuel_Type_X,Fuel_Type_Z, Transmission_A4, Transmission_A5, Transmission_A6,Transmission_A7, Transmission_A8, Transmission_A9,Transmission_AM5, Transmission_AM6, Transmission_AM7,Transmission_AM8, Transmission_AM9, Transmission_AS10,Transmission_AS4, Transmission_AS5, Transmission_AS6,Transmission_AS7, Transmission_AS8, Transmission_AS9,Transmission_AV, Transmission_AV10, Transmission_AV6,Transmission_AV7, Transmission_AV8, Transmission_M5,Transmission_M6, Transmission_M7, Make_Type_Luxury,Make_Type_Premium, Make_Type_Sports, Vehicle_Class_Type_SUV,Vehicle_Class_Type_Sedan, Vehicle_Class_Type_Truck)
            recommendations = get_recommendations(prediction)

            # Store results in session
            session['prediction'] = float(np.round(prediction, 2))
            session['recommendations'] = recommendations

            return redirect(url_for('results'))
        except Exception as e:
            return render_template('calculator.html', error="Invalid input! Please enter valid data.")

@app.route('/result')
def results():
    """Displays Prediction & Recommendations"""
    if 'user' not in session:
        return redirect(url_for('login'))  # Redirect to login if not logged in

    return render_template('result.html', prediction_text=f"CO2 Emissions: {session.get('prediction')} g/km",
                           recommendations_text=session.get('recommendations'))


@app.route('/logout')
def logout():
    """Logout and redirect to login page"""
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
