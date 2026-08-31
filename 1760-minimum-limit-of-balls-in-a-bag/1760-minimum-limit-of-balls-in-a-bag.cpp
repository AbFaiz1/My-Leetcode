class Solution {
public:
    int minimumSize(vector<int>& nums, int maxOperations) {
        int l = 1;
        int r = *max_element(nums.begin(), nums.end());
        int ans = r;

        while(l <= r){
            int mid = (l + r) / 2;

            long long ops = 0;

            for(int x : nums){
                if(x > mid){
                    ops += (x - 1) / mid;
                }
            }

            if(ops <= maxOperations){
                ans = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return ans;
    }
};
