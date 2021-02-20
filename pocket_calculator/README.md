# Pocket calculator
This is a imatation of a pocket calculator I made as part of my PCPP coruse (PCPP1 3/5 GUI 3.2.1.1 on edube.org) focussing on GUI using the tkinter libary.

## Brief:
(From edube.org- https://edube.org/learn/pcpp1-4-gui-programming/project-pocket-calculator)
### Objectives
Learn practical skills related to:

- dealing with observable variables,
- working with the Entry widget,
- constructing complex interfaces with many cooperating Button widgets.

### Scenario
Have you ever used an ordinary pocket calculator? We prefer to ask you first as we're aware of the fact that these devices went out of fashion some time ago and they were replaced with computer and smartphone's applications.

This is exactly what we want you to implement - a simple, four-function "pocket" calculator. Feel free to equip it with many extra functions, but adding, subtracting, multiplying and dividing is a must - there is no calculator without these operations.

Moreover, the calculator needs a change sign function, a decimal point button and the clear button. We don't have to mention that your calculator should be resistant to zero-division attempts, in which case it should display an error message instead of producing any garbage result or raising an exception.

The screenshots we present below are just a suggestion. You can design the UI in a different way, and it will be good as long as your calculator works properly. We aren't able to collect all strict requirements in one place - we can only say that each time you have doubts about how to implement a particular behavior, you should just pick up a real pocket calculator and check how it works in the specific context.

See how we've implemented our GUI (initial state, presenting a result, and handling zero-division attempt) - do you like it?

![Calculator at initial state](./images/intended_initial.png) ![Calculator presenting a result](./images/intended_result.png) ![Calculator after zero-divide attempt](./images/intended_error.png)

Here are some of our assumptions:

- respond only to mouse clicks; keyboard presses can be silently ignored,
- the display's width is 10 - use a fixed-width font to work with it,
- you are not allowed to fill the display with more than 10 characters (including the decimal point and minus sign if it is needed); if the result needs more characters to be presented, you should display an error message,
- you are allowed to remove some less significant digits located after the decimal point to shorten the result in effect,
- if the result has no significant digits after the decimal point, the point should not appear on the display.

## My results:  

Initial:  
![Initial](./images/initial.png)  
Full display (10 charecters, inc. decimal and negative):  
![Full display](./images/full_display.png)  
Full display 2 (all numbers):  
![Full display 2](./images/full_display_nums.png)  
Chain addition (1+2+3=6):  
![Chain addition 1](./images/chain_add_1.png)
![Chain addition +2](./images/chain_add_2.png)
![Chain addition +3](./images/chain_add_3.png)
![Chain addition =4](./images/chain_add_4.png)  
Chain subtraction (10-9-8=-7):  
![Chain subtraction 10](./images/chain_sub_1.png)
![Chain subtraction -9](./images/chain_sub_2.png)
![Chain subtraction -8](./images/chain_sub_3.png)
![Chain subtraction =-7](./images/chain_sub_4.png)  
BackSpace:  
![BackSpace 1](./images/backSpace_1.png)
![BackSpace 2](./images/backSpace_2.png)  
Zero division error:  
![Zero division error](/images/zero_div_error.png)  
Length error:  
![Length error 1](/images/length_error_1.png)
![Length error 2](/images/length_error_2.png)
![Length error 3](/images/length_error_3.png)  
Mulitiplcation:  
![Mulitiplcation 5](/images/multi_1.png)
![Mulitiplcation *3](/images/multi_2.png)
![Mulitiplcation =15](/images/multi_3.png)  
Division whole number:  
![Division whole number 25](/images/div_whole_1.png)
![Division whole number /5](/images/div_whole_2.png)
![Division whole number =5](/images/div_whole_.3png)  
Division decimal number:  
![Division decimal number 1](/images/div_deci_1.png)
![Division decimal number /4](/images/div_deci_2.png)
![Division decimal number =0.25](/images/div_deci_3.png)  