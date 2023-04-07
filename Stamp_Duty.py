# Example house value: £340,000

# Tax Band                %       Taxable Sum     Tax
# £0 - £145,000	       | 0%	  |    £145,000     | £0.00
# £145,001 - £250,000  | 2%	  |    £105,000	    | £2,100.00
# £250,001 - £325,000  | 5%	  |    £75,000	    | £3,750.00
# £325,001 - £750,000  | 10%  |    £15,000	    | £1,500.00
# £750,001 +	       | 12%  |    £0	        | £0.00

class StampDuty:
    # Initialisation of Class
    def __init__(self, house_value=422000):
        self.house_value = house_value
        # self.house_value = float(input("Enter house value: "))

    def run_function(self):
        # Prompt user to input house value
        house_value = float(input("Enter the property value: "))
        print(self.calculate_tax_percent(house_value))

    # Function to calculate the percentage of each bracket and updat the overall value
    def calculate_tax_percent(house_value):
        lower_bounds = [145001, 250000, 325001]
        upper_bounds = [250001, 325000, 750000]
        tax_rates = [0.02, 0.05, 0.1, 0.12]
        try:
            if isinstance(house_value, int):
            # Check house value is above the lowest threshhold to pay tax
                if house_value > lower_bounds[0]:
                    # Deduct the non-taxable amount from the value of the house (145000)
                    counter = house_value - lower_bounds[0]
                    taxed_amount = 0

                    # Iterate through every value of both tax bands and work out price of tax
                    for i in range(len(lower_bounds)):
                        if counter > 0:
                            # Check that taxable value of the house is greater than the difference in each band
                            if counter >= (upper_bounds[i] - lower_bounds[i]):
                                taxed_amount += (upper_bounds[i] - lower_bounds[i]) * tax_rates[i]


                                # Deduct the difference from the counter to prepare for next iteration
                                counter -= (upper_bounds[i] - lower_bounds[i])
                            else:
                                taxed_amount += counter * tax_rates[i]
                                counter = 0

                    # Checks tax amount for house value over 750k
                    if house_value >= 750001:
                        taxed_amount += (house_value - 750001) * 0.12
                    return round(taxed_amount)
                else:
                    return 0
            else:
                return 'Invalid type'
        except:
            return 'Invalid Type'