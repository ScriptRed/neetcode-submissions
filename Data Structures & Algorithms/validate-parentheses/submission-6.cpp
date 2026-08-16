class Solution {
public:
    bool isValid(string s) {
        unordered_map<char,char> bmap = {{'(', ')'},
                        {'{', '}'},
                        {'[', ']'}};
        stack<char> st;
        for (char& c: s) {
            if (bmap.find(c) != bmap.end()) {
                st.push(c);
            } else {
                if (st.size() != 0) {
                    char top = st.top();
                    st.pop();
                    if (bmap[top] != c) {
                        return false;
                    };
                } else {return false;}
            }
        }
        return st.size() == 0;
    }
};
