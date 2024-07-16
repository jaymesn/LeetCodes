'''
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

'''

'''
how I'll solve this...

step 1:
start a loop that goes through the nums array 

step 2:
add the difference between
each element in nums subtracted by the target
to the diffIdxMap

step 3:
once the loop from step 1 finds an element in nums 
where the element is actually a difference already in
the diffIdx hashmap stop the algorithm 


'''

def twoSum(nums=[3,2,3], target=6): 

    diffIdxMap = {
        #diff : idx
    }
    foundPair = False
    i = 0
    idxArr = []

    while(foundPair == False and i != len(nums)):
        diff = target - nums[i]
        numsIdx = i

        # this rules out the nums[i] being already 
        # calculated as the difference of any previous 
        # number if False; and, when True, we stop the while loop
        if( type( diffIdxMap.get(str(nums[i])) ) != int ):
            diffIdxMap[str(diff)] = numsIdx
        else:
            idx1 = diffIdxMap[str(nums[i])]
            idx2 = numsIdx
            idxArr = [idx1,idx2]
            foundPair = True
        i += 1
 


    return idxArr 

print(twoSum())
