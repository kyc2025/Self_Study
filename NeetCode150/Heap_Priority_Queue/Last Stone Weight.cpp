class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        // 使用 max-heap (priority_queue 預設是 max-heap)
        priority_queue<int> maxHeap;
        // 將所有石頭放入 max-heap
        for(int stone : stones) {
            maxHeap.push(stone);
        }
        // 當堆積中有兩個以上的石頭時，持續進行操作
        while(maxHeap.size() > 1) {
            // 取出最大的兩塊石頭
            int stone1 = maxHeap.top(); maxHeap.pop();
            int stone2 = maxHeap.top(); maxHeap.pop();
            // 如果兩塊石頭重量相同，則它們都被摧毀，不需要放回堆積
            if(stone1 != stone2) {
                // 如果不相同，將剩餘的石頭放回堆積
                maxHeap.push(stone1 - stone2);
            }
        }
        // 如果堆積中還有石頭，返回其重量；否則返回 0
        return maxHeap.empty() ? 0 : maxHeap.top();
    }
};