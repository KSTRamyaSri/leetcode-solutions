class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] arr = new int[nums1.length + nums2.length];
        System.arraycopy(nums1, 0, arr, 0, nums1.length);
        System.arraycopy(nums2, 0, arr, nums1.length, nums2.length);

        
        Arrays.sort(arr);
        int n = arr.length;

        if(n%2==0)
            return ( arr[n/2] + arr[n/2-1] ) /2.0;
        else 
            return arr[n/2];

    }
}

// ============================================================
// Approach 2 — Binary Search on Partition
// Added: 07 October 2026
// ============================================================


class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // Always binary search on the smaller array to ensure O(log(min(m, n)))
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int m = nums1.length;
        int n = nums2.length;
        int low = 0;
        int high = m;

        while (low <= high) {
            int partition1 = low + (high - low) / 2;
            int partition2 = (m + n + 1) / 2 - partition1;

            // Edge cases: if partition is 0, use -INF; if partition is length, use +INF
            int maxLeft1 = (partition1 == 0) ? Integer.MIN_VALUE : nums1[partition1 - 1];
            int minRight1 = (partition1 == m) ? Integer.MAX_VALUE : nums1[partition1];

            int maxLeft2 = (partition2 == 0) ? Integer.MIN_VALUE : nums2[partition2 - 1];
            int minRight2 = (partition2 == n) ? Integer.MAX_VALUE : nums2[partition2];

            if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
                // Correct partition found
                if ((m + n) % 2 == 0) {
                    return (Math.max(maxLeft1, maxLeft2) + Math.min(minRight1, minRight2)) / 2.0;
                } else {
                    return Math.max(maxLeft1, maxLeft2);
                }
            } else if (maxLeft1 > minRight2) {
                // Too far to the right in nums1
                high = partition1 - 1;
            } else {
                // Too far to the left in nums1
                low = partition1 + 1;
            }
        }

        throw new IllegalArgumentException("Input arrays are not sorted.");
    }
}
