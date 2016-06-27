def makeChange(amnt):
    '''Make change with the smallest number of coins'''
    
    # All the values of coins
    values = [1, 5, 10, 25]
    
    # Dictionary to keep track of the smallest count for each value up to
    # and including amnt
    # Keep track of the combo of coins as well
    full_chain = {val : {'count' : 'x', 'coins' : []} for val in range(1, amnt + 1)}
    full_chain.update({0 : {'count' : 0, 'coins' : []}})
    
    for i in range(1, amnt + 1):
        # Set an initial count to beat
        low_count = i+1
        coins = 'filler'
        for j in values:
            # Look backwards from i
            # Check what the lowest count is for j + previously calculated values
            if i - j >= 0:
                count = i - j + 1
                if count < low_count:
                    low_count = count
                    coins = full_chain[i - j]['coins'][:]
                    coins.append(j)
        full_chain[i]['count'] = low_count
        full_chain[i]['coins'] = coins
        
    return full_chain[amnt]

def main():

    print('Find out the smallest combo of coins for a value.')
    usr_val = int(input('What value would you like? >> '))

    answer = makeChange(usr_val)
    print('The smallest combo is %s' % (answer['count']))
    print('The coin necessary are %s' % (answer['coins']))

main()