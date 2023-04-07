# Stamp Duty Calculator
 
 
Simple Stamp Duty (LBTT) calculator using Python which takes a variable value as input and calculates the stamp duty owed based on that value. E.g. anything under £145k is under the threshold to pay tax, however a house valued at £175k would pay £600. 

The calculator works by iterating through each value (upper and lower) of tax bands and subtracting the house value from the upper limit of each band. The remaining value is then checked to see if it exceeds the current tax band. If so, the tax is calculated by multiplying the taxable value by the respective tax rate, and appending that to a new list. This process continues for each tax band until the entire taxable amount has been calculated. If the value of the property is over £750,000, an additional 12% tax will be added for any amount over this value.

Once all the tax values have been calculated, they are summed together to give the total stamp duty tax owed on the property. The function returns this value as output, rounded to the nearest whole number.
