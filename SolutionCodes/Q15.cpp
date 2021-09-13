// 36. Valid Sudoku

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board)
    {   int rows[9][9] = {0}; //rows[5][0] means whether number 1('0'+1) in row 5 has appeared.
        int cols[9][9] = {0};  //cols[3][8] means whether number 9('8'+1) in col 3 has appeared.
        int boxs[3][3][9] = {0};  //blocks[0][2][5] means whether number '6' in block 0,2 (row 0~2,col 6~8) has appeared.

        for(int r=0; r<9;r++)   //traverse board r,c
        {   for(int c = 0; c<9 ; c++)
            {   if(board[r][c]=='.')  //skip all number '.'
                    continue;
                int num = board[r][c]-'1';  //calculate the number's index(board's number minus 1)
                //if the number has already appeared once, return false.
                if(cols[num][c]++ || rows[r][num]++ || boxs[r/3][c/3][num]++)
                    return false;
            }

        }
        return true;
    }
};


/*
// sample 4 ms submission

class Solution {
public:

    bool isValidSudoku(vector<vector<char>>& board) {
        vector<set<char>>row(9),col(9),box(9);

        for(int i=0;i<9;i++)
        {
            for(int j=0;j<9;j++)
            {
                if(board[i][j] == '.')
                    continue;
                if(row[i].count(board[i][j])
                   || col[j].count(board[i][j])
                   || box[(i/3)*3+j/3].count(board[i][j]))
                    return false;
                row[i].insert(board[i][j]);
                col[j].insert(board[i][j]);
                box[(i/3)*3+j/3].insert(board[i][j]);
            }
        }
        return true;
    }
};

*/

/*
// sample 12 ms submission
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int used1[9][9] = {0}, used2[9][9] = {0}, used3[9][9] = {0};
        for(int i = 0; i < board.size(); ++ i)
            for(int j = 0; j < board[i].size(); ++ j)
                if(board[i][j] != '.'){
                    int num = board[i][j] - '0' - 1, k = i / 3 * 3 + j / 3;
                    if(used1[i][num] || used2[j][num] || used3[k][num])return false;
                    used1[i][num] = used2[j][num] = used3[k][num] = 1;
                }
        return true;
    }
};

*/