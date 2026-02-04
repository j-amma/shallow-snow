# Input to all functions is rioxarray datacube with x,y, and time dimensions

def time_average():
    pass
    # Average each pixel across time

def percentile():
    pass
    # For each snapshot in time, calculate snow depth percentile for each pixel
    # Average each pixel percentiles across time

def standard_depth_value():
    pass
    # for each snapshot in time
        # calculate pixel mean (mu)
        # calculate pixel standard deviation (sigma)
        # calculate standard depth value for each pixel (depth - mu) / sigma
    # Time average pixel SDV values

def robust_standard_depth_value():
    pass
    # same as stadard depth value but using median and MAD instead of mu and sigma
    # Time average robust pixel SDV values