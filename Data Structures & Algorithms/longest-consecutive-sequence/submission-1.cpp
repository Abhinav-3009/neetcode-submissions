class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> num(nums.begin(), nums.end());
        int ans = 0;
        for(int x: num){
            if(num.find(x -1) == num.end()){
                int l = 1;
                while(num.find(x+l) != num.end()){
                    l++;
                }
                ans = max(ans, l);
            }
        }
        return ans;
    }
};
