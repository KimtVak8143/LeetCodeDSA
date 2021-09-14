// 383. Ransom Note

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int set[26]={};
        for(int i =0; i< magazine.size();++i)
            ++set[magazine[i]-'a'];

        int ransom[26]={};
        for(int j=0;j<ransomNote.size();++j)
            ++ransom[ransomNote[j]-'a'];

        for(int k = 0;k<26;++k)
            if(set[k]<ransom[k])
                return false;
        return true;
    }
};


/*
//19ms solution
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> map(26);
        for(int i=0;i<magazine.size();++i)
            ++map[magazine[i]];

        for(int j=0;j<ransomNote.size();++j)
        {   if(--map[ransomNote[j]]<0)
                return false;
        }
        return true;
    }
};

*/