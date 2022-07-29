class Solution:
    def findMaxLength(self, nums) -> int:
        max_length =0
        hash={}
        count=0
        for i in range(len(nums)):
            print("Hashmap {}".format(hash))
            current=nums[i]
            if current==0:
                count-=1 # decrement our count if our current element is 0
            else:
                # increment our count if current element is 1
                count+=1

            if count==0:
                # if count is 0, we have a new subarray with length+1
                max_length=i+1
            if count in hash:
                max_length=max(max_length,i-hash[count])
            else:
                hash[count]=i
        return max_length

sool = Solution()
print(sool.findMaxLength([0,1,0,0,1,1,0]))