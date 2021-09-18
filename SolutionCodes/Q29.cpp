// 9. Palindrome Number

class Solution {
public:
    bool isPalindrome(int x) {
        if (x<0 || (x!=0 && x%10==0))
            return false;
        int sum = 0;
        while(x>sum)
        {   sum = sum*10 + x%10;
            x/=10;
        }
        return (x==sum||x==sum/10);
    }
};

/*
//sample 0 ms submission

class Solution {
public:
    bool isPalindrome(long int x) {
       long int r,sum=0,t;
        t=x;
        while(t>0)
        {
            r=t%10;
            sum=sum*10+r;
            t/=10;
        }
        if(sum==x)
            return true;
        return false;
    }
};

*/