from icecream import ic        
import time
def longestConsecutive(nums) -> int:
    if len(nums) == 0: return 0
    #build ele_conections
    ele_connections = {}
    for i in range(len(nums)):
        #the tuple is index, -1 connection index, +1 connection index
        curr_num = nums[i]
        if curr_num not in ele_connections:
            ele_connections[curr_num] = {"idx":i,"prev":-1,"next":-1, "seen":-1}

        potential_last_number = curr_num - 1
        if potential_last_number in ele_connections:
            last_num_index = ele_connections[potential_last_number]["idx"]
            ele_connections[curr_num]["prev"]=last_num_index
            ele_connections[potential_last_number]["next"] = i
        
        potential_next_number = curr_num + 1
        if potential_next_number in ele_connections:
            next_num_index = ele_connections[potential_next_number]["idx"]
            ele_connections[curr_num]["next"]=next_num_index
            ele_connections[potential_next_number]["prev"] = i
    
    #ic(ele_connections)

    # traverse ele_connections
    longest_len = 1
    curr_len = 0
    for ele_key in ele_connections:
        ele = ele_connections[ele_key]
        if ele["seen"] == 1:
            continue
        
        #ic(ele_key)
        ele["seen"] = 1
        curr_len = 1
        
        # add all subsequent
        next_ele_idx = ele["next"]
        while next_ele_idx != -1:
            curr_len += 1
            next_ele_val = nums[next_ele_idx]
            #ic(next_ele_idx, next_ele_val, curr_len)
            ele_connections[next_ele_val]["seen"] = 1
            next_ele_idx = ele_connections[next_ele_val]["next"]
            #ic(ele_connections)

        
        # add all previous
        prev_ele_idx = ele["prev"]
        while prev_ele_idx != -1:
            curr_len += 1
            prev_ele_val = nums[prev_ele_idx]
            #ic(prev_ele_idx, prev_ele_val, curr_len)
            ele_connections[prev_ele_val]["seen"] = 1
            prev_ele_idx = ele_connections[prev_ele_val]["prev"]
            #ic(ele_connections)
            time.sleep(.1)
        
        longest_len = max([longest_len, curr_len])
    
    return longest_len

nums=[0,3,2,5,4,6,1,1]
print(longestConsecutive(nums))