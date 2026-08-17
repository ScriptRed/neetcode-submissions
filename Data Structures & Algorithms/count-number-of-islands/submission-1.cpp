class Solution {
    int res = 0;
public:
    int numIslands(vector<vector<char>>& grid) {
        int mbound = grid.size() - 1;
        int nbound = grid[0].size() - 1;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == '0') continue;
                grid[i][j] = '0';
                res++;
                dfs(grid, i, j, mbound, nbound);
            }
        }
        return res;
    }
private:
    void dfs(vector<vector<char>>& grid, int m, int n, int mbound, int nbound) {
        if (m < mbound && grid[m+1][n] == '1') {
            grid[m+1][n] = '0';
            dfs(grid, m+1, n, mbound, nbound);
        }
        if (n < nbound && grid[m][n+1] == '1') {
            grid[m][n+1] = '0';
            dfs(grid, m, n+1, mbound, nbound);
        }
        if (n > 0 && grid[m][n - 1] == '1') {
            grid[m][n - 1] = '0';
            dfs(grid, m, n - 1, mbound, nbound);
        }
        if (m > 0 && grid[m-1][n] == '1') {
            grid[m-1][n] = '0';
            dfs(grid, m-1, n, mbound, nbound);
        }
        return;
    }
};
