# This module contains functions that create AWS tags and extract AWS tag values

def make_aws_tag(tag_key, tag_value):
    
    # Returns a one-element dictionary in the form used by AWS tags with specific keywords:
        #   'Key' is used as the key for the key pair
        #   'Value" is used as the key for the value pair
        
    return [{'Key': tag_key, 'Value': tag_value}]

def get_aws_tag_value(aws_tag_search_key, aws_tag_dict_list):
    
    # Finds a value in a list of AWS key-value pairs in the form of:
    #    [{u'Value': 'TAG_VALUE_1', u'Key': 'TAG_KEY_1'}, {u'Value': 'TAG_VALUE_2', u'Key': 'TAG_KEY_2'}]
    # Returns the value associated with the search key if the search key is found
    # Returns None if the search key is not found
    
    # Set the debug flag to control debug print statements
    debug = False
    
    # Return immediately if the list of key-value pairs is empty
    if aws_tag_dict_list is None:
        return
   
    if debug:    
        print 'aws_tag_dict_list:        ', aws_tag_dict_list
        print 'len(aws_tag_dict_list):   ', len(aws_tag_dict_list), '\n'
        
    # Allocate an empty dictionary in which to store a local key-value dictionary
#     aws_tag_key_value_dict = dict()

    # Initialize dictionary element counter
    elem_index = 0
    
    # Search each key-value pair for the desired key
    for aws_tag_dict in aws_tag_dict_list:

        if debug:
            elem_prefix = '[' + str(elem_index) + ']: '
            print elem_prefix, 'aws_tag_dict = ', aws_tag_dict

        # The AWS key-value structure contains a list of dictionaries with specific keywords:
        #   'Key' is used as the key for the key pair
        #   'Value" is used as the key for the value pair
        my_aws_tag_key   = aws_tag_dict['Key']
        my_aws_tag_value = aws_tag_dict['Value']
        
        if debug:
            print elem_prefix, 'my_aws_tag_key:    ', my_aws_tag_key
            print elem_prefix, 'my_aws_tag_value:  ', my_aws_tag_value
        
        # Return if the current key is the same as the search key 
        if my_aws_tag_key == aws_tag_search_key:
            if debug:
                print elem_prefix, 'key found: ',
                print 'aws_tag_key_value_dict[' + aws_tag_search_key + '] = ', my_aws_tag_value
            return my_aws_tag_value
        
        # If the key is not found then add it to a running dictionary of key-value pairs
        # TODO: 1. Decide if it's worth keeping a new and separate ephemeral dictionary when the function
        #       just returns when the key is found.  The only time the dictionary will be complete is when
        #       the loop has iterated over the entire set of keys and the search key has not been found. 
#         aws_tag_key_value_dict[my_aws_tag_key] = my_aws_tag_value
                
        elem_index = elem_index + 1
    
    # The function should only get this far if the search key has *not* been found.
    # TODO: 2. If the function gets to this point then the following statement should always evaluate to
    #       'False' and will return 'None'
#     if aws_tag_search_key in aws_tag_key_value_dict.keys():
#         if debug:
#             print elem_prefix, 'aws_tag_key_value_dict[' + aws_tag_search_key + '] = ', aws_tag_key_value_dict[aws_tag_search_key]
#         return aws_tag_key_value_dict[aws_tag_search_key]
#     else:
#         return
    
    return