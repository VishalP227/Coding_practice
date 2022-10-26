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
