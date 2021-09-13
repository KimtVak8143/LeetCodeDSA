//240. Search a 2D Matrix II
//160 ms solution

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int rows = matrix.size();
        int cols = matrix[0].size();
        int i = 0;
        int j = cols-1;

        while(i<rows and j >=0)
        {   int news = matrix[i][j];
            if(news>target)
                j--;
            else if(news< target)
                i++;

            if(news==target)
                return true;
        }
        return false;
    }
};


//sample 64 ms submission
/*
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = 0;
        int col = matrix[0].size() - 1;

        bool found = false;
        while(row < matrix.size() && col >= 0)
        {
            int currentVal = matrix[row][col];
            if (currentVal == target)
            {
                found = true;
                break;
            }

            if (target > currentVal)
                row++;
            else
                col--;
        }
        return found;
    }
};
*/