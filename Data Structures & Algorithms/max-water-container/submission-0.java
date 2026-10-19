class Solution {
    public int maxArea(int[] heights) {
        int ans = 0;
        int smaller = 0;
        int tempAns = 0;
        for (int i = 0; i < heights.length; i++)  {
            for (int l = heights.length - 1; l != i; l--){
                if(heights[i]>heights[l]){
                    smaller = heights[l];
             }else{
                 smaller = heights[i];
                }
                tempAns = (l-i) * smaller;
                if(ans < tempAns){
             ans = tempAns;
            }
            }
        }
        return ans;
    }
}
