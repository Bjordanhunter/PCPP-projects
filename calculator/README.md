# A very simple calculator

This is a very simple calculator I made as part of my PCPP coruse (PCCP1 3/5 3.1.1.2) on edube.org.
### Breif:

#### Objectives
Learn practical skills related to:

- using the Entry, Radiobutton and Button widgets,
- managing widgets with the grid manager,
- checking the validity of user input and handling errors.

#### Scenario
You need a calculator. A very simple and very specific calculator. Look at the picture - it contains two fields that the user can use to enter arguments, a radio button to select the operation to perform, and a button initiating the evaluation:

![Calculator - reference. cridit:edube.org](https://edube.org/uploads/media/default/0001/01/5c21f12519840cce2abf7efad10dbfcc026b8fde.png)


We expect the calculator to behave in the following way:
- if both fields contain valid (integer or float) numbers, clicking the Evaluate button should display an info window showing the evaluation's result;
- if any of the fields contains invalid data (e.g., a string, or a field is empty), clicking the Evaluate button should present an error window describing the problem, and the focus should be moved to the field causing the problem.   

Don't forget to protect your code from dividing by zero, and use the grid manager to compose the window interior.

### my results:
Inital view of calculator:
![inital view]()
Basic operations:
![addition: 6+4=10.0]()
![subtraction: 6-4=2.0]()
![multiplication: 6*4=24.0]()
![division: 6/4=1.5]()
Catching invalid input:
![zero division error message]()
![letters inputed error message]()
![empty inputs error message]()

