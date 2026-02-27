class Solution {
public:
    int minOperations(string s, int k) {
        // Position of 0's and 1's dont matter only count
        int n = s.size(), ones = 0;
        set<int> odd, even;
        for (int i=0;i<n;i++) {
            if (s[i]=='1') ones++;
            if (i%2) odd.insert(i); else even.insert(i);
        }
        if (n%2) odd.insert(n); else even.insert(n);

        int ans = 0;
        deque<int> q;
        q.push_back(ones);
        
        if (ones%2) odd.erase(ones); else even.erase(ones);
        while (!q.empty()) {

            int cur_sz = q.size();
            for (int i=0;i<cur_sz;i++) {
                ones = q.front();
                q.pop_front();
                if (ones == n) return ans;
                int zeros = n-ones;
                int st = ones + 2*max(0, k-ones)-k;
                int en = ones + 2*min(zeros, k)-k;
                auto begin = st%2==0? even.lower_bound(st): odd.lower_bound(st);
                auto end = st%2==0? even.upper_bound(en): odd.upper_bound(en);

                vector<int>to_remove;
                for (auto it = begin; it != end; it++) {
                    int new_ones = *it;
                    to_remove.push_back(new_ones);
                    q.push_back(new_ones);
                }

                for (auto x: to_remove) st%2==0? even.erase(x): odd.erase(x);

            }
            ans++;
        }

        return -1;

    }
};