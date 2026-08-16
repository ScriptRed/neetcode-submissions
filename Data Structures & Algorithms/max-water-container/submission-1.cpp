class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0, r = heights.size()-1, maxArea = 0;
        while (l < r) {
            maxArea = max(min(heights[l],heights[r])*(r-l),maxArea);
            if (heights[l] < heights[r]) {
                l++;
            } else {
                r--;
            }
        }
        return maxArea;
    }
};
