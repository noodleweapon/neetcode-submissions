#include <stack>

class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<int> s;
        for (const string& operation : operations) {
            if (operation == "D") {
                s.push(s.top() * 2);
            } else if (operation == "+") {
                int a = s.top();
                s.pop();
                int b = s.top();
                s.push(a);
                s.push(a + b);
            } else if (operation == "C") {
                s.pop();
            } else {
                int n = stoi(operation);
                s.push(n);
            }
        }

        int total = 0;
        while (!s.empty()) {
            total += s.top();
            s.pop();
        }
        return total;
    }
};