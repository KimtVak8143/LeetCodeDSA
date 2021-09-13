// 74. Search a 2D matrix
// 4 ms
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target)
    {   int rows = matrix.size();
        int cols = matrix[0].size();
        int i = 0;
        int j = cols-1;

        while(i<rows && j >=0)
        {   if(matrix[i][j]==target)
            {   return true;
            }
            if(matrix[i][j] < target)
            {   i+=1;
            }
            else
            {   j-=1;
            }
        }
        return false;

    }
};


//sample 0 ms submission
/*
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int i=0,n=matrix.size()-1;
        int j=matrix[0].size()-1, x = target;

        while(i<=n && j>=0){
            if(matrix[i][j]==x){
                return true;
            }else if(matrix[i][j]<x){
                i++;
            }else{
                j--;
            }
        }

        return false;
    }
};
*/