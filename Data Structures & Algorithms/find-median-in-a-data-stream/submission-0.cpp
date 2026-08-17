class MedianFinder {
    priority_queue<int> maxHeap;
    priority_queue<int,vector<int>,greater<int>> minHeap;
public:
    MedianFinder() {
    }
    
    void addNum(int num) {
        maxHeap.push(num);
        minHeap.push(maxHeap.top());
        maxHeap.pop();
        if (minHeap.size() - maxHeap.size() == 1) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        } 
    }
    
    double findMedian() {
        if ((maxHeap.size() + minHeap.size()) % 2 == 1) { 
            return maxHeap.top();
        } else {
            return (double)(maxHeap.top() + minHeap.top()) / 2;
        }
    }
};
