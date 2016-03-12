def share_price(invested, changes):
    return "%.2f" % reduce(lambda p,x: p * (100.0+x)/100, changes, invested)

##from __future__ import division
##def share_price(invested, changes):
##    # magic here
##    current_price = invested
##    
##    # calculating the latest price
##    for ch in changes:
##        latest_price = (current_price * (ch/100)) + current_price
##        current_price = latest_price
##        
##    #rounding the result to 2 decimal places and then to string format
##    result = str(format(current_price, '.2f'))
##    return result

##test.assert_equals(share_price(100, []), '100.00')
##test.assert_equals(share_price(100, [-50, 50]), '75.00')
##test.assert_equals(share_price(100, [-50, 100]), '100.00')
##test.assert_equals(share_price(100, [-20, 30]), '104.00')
##test.assert_equals(share_price(1000, [0, 2, 3, 6]), '1113.64')

print share_price(1000, [0, 2, 3, 6])
