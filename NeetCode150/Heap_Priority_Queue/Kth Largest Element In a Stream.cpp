#include <bits/stdc++.h>

using namespace std;

class KthLargest {
public:
    int k_; 
    // 使用 min-heap 儲存前 k 個最大的元素
    priority_queue<int, vector<int>, greater<int>> minHeap;
    // 這是C++的優先隊列(priority queue), 預設是最大堆（最大的元素在頂部）
    // 這裡使用了（min-heap），所以我們使用 greater<int> 使得最小的元素在頂部。
    KthLargest(int k, vector<int>& nums): k_(k)
    {
        // 直接遍歷，不用排序
        for (int x : nums) 
        {
            add(x);
        }
    }
    int add(int val) 
    {
        // 1. 先把新元素丟進去
        minHeap.push(val);
        // 2. 如果堆積超過 k 個，把最小的（頂部）踢掉
        // 這樣剩下的就是「目前最大的 k 個元素」
        if (minHeap.size() > k_) {
            minHeap.pop();
        }
        // 3. 堆積頂端就是這 k 個當中最小的，也就是第 k 大的元素
        return minHeap.top();
    }
};
//  conclusion: 加入 Heap 不會幫你把整個陣列排好，
//  它只會保證 top() 永遠是目前這堆數字裡的最小值。
