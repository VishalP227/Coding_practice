'''
There are a lot of horses in the yard, and we want to count how many there are.  Unfortunately, we've only got a recording of the sounds from the yard.  All the horses say "neigh".  The problem is they can "neigh" many times.  The recording from the yard is sadly all mixed together.  So, we need to figure out from the overlapping sounds how many horses there could be.
For example, we've got two horses in the yard, and we hear this "neigneighh".  From this recording, we can successfully deduce there are 2 horses.  Another example is "neighneigh".  From this example, we can only tell there is one horse in the yard.
As an additional complexity, our recording might not be perfect.  If it's a bad recording, we should give "Invalid" as the response.
The input will be given as a string on one line.  The output should be printed on it's own line.


Sample Input:
nenigehnieighgh

Sample Output:
2

'''

def horse_counter(sound):
    
    # dictionary to store the characters
    # keys are characters and values are the count of each character
    horse_dict = {};
    
    # variable to keep count of horses
    horse_count = 0;
    
    # iterate through the string    
    for c in sound:
        # check if current char is n
        if c == 'n':
            # if yes check if it is in horse_dict
            if c in horse_dict:
                # if yes check if h is also in horse_dict
                if 'h' in horse_dict:
                    # if yes check if count of h is same as count of horses
                    if horse_dict['h'] == horse_count:
                        # if yes it's the end of one of sound for existing horse
                        # do not increment horse count
                        horse_dict[c] += 1
                    else:
                        # if cout of h is different from count of horses
                        # a new horse is starting to neigh, increment n and horse count
                        horse_count += 1
                        horse_dict[c] += 1
                else:
                    # if h is not in dict
                    # a new horse is starting to neigh, increment n and horse count
                    horse_count += 1
                    horse_dict[c] += 1
            else:
                # if n is not in dict
                # it is the beginning of a new horse neighing
                # add 'n' to dict with value 1
                horse_count += 1
                horse_dict[c] = 1
        else:
            # if char is not 'n' check if char is in horse_dict
            if c in horse_dict:
                # if yes increment the value of that char in horse dict
                horse_dict[c] += 1
            else:
                # if not add the char as key in dict with value 1
                horse_dict[c] = 1
    
    # checking if the sound was valid
    # all the keys will have same value, hence when converted to set, set should have only 1 element
    horse_dict_values = horse_dict.values()
    horse_dict_values_set = set(horse_dict_values)
    
    # check if set has only one element
    if len(horse_dict_values_set) == 1:
        # if yes the sound was valid, return the horse count
        return horse_count
    else:
        # if not then the sound was invalid, return invalid response
        return "Invalid response"
        

print(horse_counter('neigneighh'))
print(horse_counter('neighneigh'))
print(horse_counter('nenigehnieighgh'))
print(horse_counter('neigneigh'))
