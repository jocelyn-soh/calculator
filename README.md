# Calculator User Guide 

Welcome to Calculator! This is a simple calculator web application that allows users to perform addition and subtraction of two numbers.  

## Setting up 
1. Clone the repository: `git clone https://github.com/jocelyn-soh/calculator`
2. Navigate to the project directory: `cd calculator`
3. Create a virtual environment: `python -m venv calculator_venv`
4. Activate the virtual environment: 
- On Windows: `calculator_venv\Scripts\activate`
- On macOS/Linux:  `source calculator_venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Run the Flask application: `python calculator.py`
7. After running the application, you should see a message like `Running on http://127:0.0.1:<port-number>`. `Ctrl + Click` on the link generated in the terminal to access the calculator interface on a web browser. 

## Features 
### Adding two numbers together 
1. Click on the `Enter the first number` box and enter the first number.
2. Repeat step 1 for the second number. 
3. Click on the `Add` button to perform addition.
4. The result is generated on a separate line below. 
<br/> 
Note: The two input values should be of type float, and smaller than 1e308. The result will be rounded to 10 d.p. 

### Subtracting two numbers
1. Click on the `Enter the first number` box and enter the first number.
2. Repeat step 1 for the second number. 
3. Click on the `Subtract` button to perform subtraction.
4. The result is generated on a separate line below. 
<br/> 
Note: The two input values should be of type float, and smaller than 1e308. The result will be rounded to 10 d.p. 