class KthLargest {
public:
    priority_queue<int, vector<int>, greater<int>> top_k;
    int k;
    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (int i=0; i<min((int)nums.size(),k); i++){
            top_k.push(nums[i]);
        }
        if (k<nums.size()){
            for (int i=k; i< nums.size(); i++){
                if (nums[i] > top_k.top()){
                    top_k.pop();
                    top_k.push(nums[i]);
                }
            }
        }
    }

    int add(int val) {
        if (top_k.size()<k){
            top_k.push(val);
        }
        else if (val > top_k.top()){
            top_k.pop();
            top_k.push(val);
        }

        return top_k.top();
    }
};
