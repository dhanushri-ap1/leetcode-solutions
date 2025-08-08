class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        res=[]

        for num in nums1:
            idx=nums2.index(num)
            next=-1

            for j in range(idx+1, len(nums2)):
                if nums2[j]>num:
                    next=nums2[j]
                    break
                   
            res.append(next)

        return res


#this is the brute force method and it is very time complex with runtime about 37ms...so we must use stack for implementation


