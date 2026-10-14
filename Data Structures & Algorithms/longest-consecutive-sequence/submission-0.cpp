class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> num(nums.begin(), nums.end());
        int ans = 0;

        for(int x: num){
            if(num.find(x -1) == num.end()){
                int l = 1;
                int c = 1;
                while(num.find(x+c) != num.end()){
                    l++;
                    c++;
                }
                ans = max(ans, l);
            }
        }
        return ans;
    }
};
