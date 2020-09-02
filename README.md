# Quickbooks-Python-API
A sinple Quickbooks Api to get the invoice details and print them out in the kernel.

## Run Instructions
To run the Application. This instruction assumes that you already have a Developer account and a sandbox setup.Follow the steps in order   
1.) Get the ClientID and ClientSecretKeys from the keys subsection in the developer dashboard of the application and add them to the config.py file.  
2.) Copy the Redirect URL from the config.py file and add it to the application.  
3.) Launch the application by running the app.py file.  
4.) Open a Webbrowser and type in the IP http://localhost:5000/ into it.  
5.) Press the connect to Quickbooks icon and connect the server to a database online.  
6.) The HTML file will give you the available operations after sucessfully authorizing it.  

## Requirements
The project is developed using  
Python v3.6  
requests v2.13.0  
Flask v0.12  
Werkzeug v0.11.15  
openpyxl v2.4.4  
requests_oauthlib v0.8.0  
Pandas v1.1.0  
You can install any missing files by running 'pip3 install -r requirements.txt'.

## Further Reference
For further information on each class and files, please refer each file for comments.
