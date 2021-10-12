# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, 
# where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


def merge(nums1, nums2, m, n):
        """
        modify nums1 in-place instead.
        """
        last_indx= m+n-1
        
        while  m>0 and n>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last_indx] = nums1[m-1]
                m =m-1
            else:
                nums1[last_indx] = nums2[n-1]
                n = n-1
            last_indx = last_indx - 1
            
            
        while n >0:
            nums1[last_indx] = nums2[n-1]
            n = n-1
            last_indx = last_indx-1
            
        return nums1

# print(merge([1,2,3,0,0,0],[2,5, 6], 3, 3))
print(merge([4,5,6,0,0,0],[1,2, 3], 3, 3))