class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> different_elements;

        for (unsigned i = 0; i < nums.size(); i++)
        {
            different_elements.insert(nums[i]);
            if (different_elements.size() == i)
                return true;
        }

        return false;
    }
};