#!/usr/bin/python

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here

    errors = abs(predictions - net_worths)
    tmp_data = sorted(zip(ages, net_worths, errors),
                      key=lambda point:point[2], reverse=True)
    rm_nums = int(0.1 * len(tmp_data))
    cleaned_data = tmp_data[rm_nums :]    
    return cleaned_data

