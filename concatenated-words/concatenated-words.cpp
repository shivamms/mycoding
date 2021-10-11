class Solution {
public:
    class Trie{
public:
Trie *children[26] = {NULL};
bool word = false;
}*root;

void insert(string s)
{
    Trie *cur = root;
    for(int i=0;i<s.length();i++)
    {
        if(!cur->children[s[i]-'a'])
        {
            cur->children[s[i]-'a'] = new Trie();
        }
        cur = cur->children[s[i]-'a'];
    }
    cur->word=true;
}

bool search(string s)
{
    int n = s.length();
    vector<bool> dp(n,false);
    Trie *cur = root ;
    for(int i=0;i<n;i++)
    {
        Trie *cur;
        cur = root;
        if(i==0 || dp[i-1])
        for(int j=i;j<n;j++)
        {
            if(!cur->children[s[j]-'a'])break;
            cur = cur->children[s[j]-'a'];
            if(cur->word)dp[j]=true;
            if(j==n-1 && cur->word)
            {
                dp[j]=true;
                if(i!=0)return true;
            }
        }
    }
    return false;
}



vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
    vector<string> ans;
    root = new Trie();
    for(auto it : words)
    {
        if(it.length())
        insert(it);
    }
    for(auto it: words)
    {
        if(it.length())
        {
            if(search(it))ans.push_back(it);
        }
    }
    return ans;
}
};

