# Ex.05 Design a Website for Server Side Processing
## Date:26.11.2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html

<!DOCTYPE html>
<html>
<head>
    <title>Power Calculator</title>
    <style>
        * {
            padding: 0;
            margin: 0;
            box-sizing: border-box;
        }

        body {
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Arial', sans-serif;
            background: linear-gradient(to right, rgba(170, 218, 221, 255), rgba(146, 237, 149, 255));
            height: 100vh;
            background-size: cover;
            margin: 0;
        }

        h1 {
            margin-bottom: 20px;
            text-align: center;
            font-size: 32px;
            color: #333;
        }

        .container {
            background-color: rgba(255, 255, 255, 0.8);
            padding: 40px;
            width: 400px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            border-radius: 8px;
            text-align: center;
        }

        .inputline {
            display: flex;
            justify-content: space-between;
            margin-bottom: 15px;
            align-items: center;
        }

        .inputline input {
            padding: 10px;
            width: 70%;
            border-radius: 4px;
            border: 1px solid #ccc;
            font-size: 14px;
        }

        .inputline label {
            font-size: 16px;
            color: #333;
        }

        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 12px 20px;
            border: none;
            cursor: pointer;
            border-radius: 4px;
            font-size: 16px;
            width: 80%;
            margin-top: 20px;
        }

        input[type="submit"]:hover {
            background-color: #45a049;
        }

        .inputline input[type="text"]:focus {
            outline: none;
            border-color: #4CAF50;
        }

        .power-result {
            margin-top: 20px;
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }

        .inputline input[type="text"]:disabled {
            background-color: #f2f2f2;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>Power Calculator</h1>
        <form method="post">
            {% csrf_token %}
            <div class="inputline">
                <label for="resistance">Resistance (R):</label>
                <input type="text" name="Resistance" id="resistance" placeholder="Enter Resistance (in ohms)" value="{{R}}">
            </div>
            <div class="inputline">
                <label for="intensity">Intensity (I):</label>
                <input type="text" name="Intensity" id="intensity" placeholder="Enter Intensity (in amps)" value="{{I}}">
            </div>
            <div class="inputline">
                <input type="submit" value="Calculate">
            </div>
            <div class="power-result">
                Power (P): 
                <input type="text" name="Power" placeholder="Power calculated" value="{{power}}" disabled>
            </div>
        </form>
    </div>
</body>
</html>

views.py
from django.shortcuts import render 
def Power(request): 
    context={} 
    context['Power'] = "0" 
    context['I'] = "0" 
    context['R'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        I= request.POST.get('Intensity','0')
        R= request.POST.get('Resistance','0')
        print('request=',request) 
        print('Intensity=',I) 
        print('Resistance=',R) 
        Power= int(I)**2 * int(R) 
        context['Power'] = Power
        context['I'] = I
        context['R'] = R 
        print('Power=',Power) 
    return render(request,'mathapp/math.html',context)

urls.py
from django.contrib import admin
from django.urls import path
from mathapp import views 
urlpatterns = [
    path('admin/', admin.site.urls),
     path('Power/',views.Power,name="Power"),
    path('',views.Power,name="Powerroot")
]
```

## SERVER SIDE PROCESSING:
![alt text](<Screenshot 2024-11-26 122126.png>)

## HOMEPAGE:
![alt text](<Screenshot 2024-11-26 122142.png>)

## RESULT:
The program for performing server side processing is completed successfully.
