def findMedianSortedArrays(nums1, nums2):
    median = 0
    nums3 = sorted(nums1+nums2)
    length_nums3 = len(nums3)
    mid_index = length_nums3/2

    if length_nums3 %2 != 0:
        median = nums3[int(mid_index-0.5)]
    else:
        median = (nums3[int(mid_index)] + nums3[int(mid_index-1)])/2

    return median

print(findMedianSortedArrays([1,3,4], [2]))