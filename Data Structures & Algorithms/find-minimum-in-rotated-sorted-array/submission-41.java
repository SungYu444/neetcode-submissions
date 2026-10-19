class Solution {
    public int findMin(int[] nums) {
        int mid = nums.length/2;
        int i = 0;
        int l = nums.length - 1;
        if(nums.length == 2){
            if(nums[i]< nums[l]){
                return nums[i];
            }else{
                return nums[l];
            }
        }
        while(nums[mid]!=nums[i] && nums[mid]!=nums[l]){
            if (nums[mid]<nums[mid+1] && nums[mid]<nums[mid-1]){
                return nums[mid];
            }
            if(nums[i]> nums[mid]|| nums[i]<=nums[mid]&& nums[mid]<=nums[l]){
                l = mid;
                mid = (i + l)/2;
            }
            if(nums[mid]> nums[l]){
                i = mid;
                mid = (i + l)/2;
            }
            if (nums[mid]<=nums[i] && nums[mid]<=nums[l]){
                return nums[mid];
            }
        }
        return nums[l];
    }
}
