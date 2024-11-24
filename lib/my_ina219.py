"""
A collection of my frequently used functions for my Educaboard ina219 component
"""

# Do I need this?
def batt_linear_function(adc1=None,U1=None,adc2=None,U2=None):
    """ Get linear function from adc values of the """
    a=(U1-U2)/(adc1-adc2)
    b=U2-a*adc2
    return b


def batt_voltage(batt_u):
    """ Get perc"""
    pass