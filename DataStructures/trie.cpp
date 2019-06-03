#include <iostream>
#include <unordered_map>

#define hashmap unordered_map<char, node *>

using namespace std;

class node
{
public:
    char data;
    hashmap h;
    bool isTerminal;
    node(char n)
    {
        data = n;
        isTerminal = false;
    }
};

class Trie
{
    node *root;

public:
    Trie()
    {
        root = new node('\0');
    }
    void addWord(char *word)
    {
        node *temp = root;
        for (int i = 0; word[i] != '\0'; i++)
        {
            char ch = word[i];
            if (temp->h.count(ch) == 0)
            {
                node *child = new node(ch);
                temp->h[ch] = child;
                temp = child;
            }
            else
            {
                temp = temp->h[ch];
            }
        }
        temp->isTerminal = true;
    }

    bool search(char *word)
    {
        node *temp = root;
        for (int i = 0; word[i] != '\0'; i++)
        {
            char ch = word[i];
            if (temp->h.count(ch))
            {
                temp = temp->h[ch];
            }
            else
            {
                return false;
            }
            cout << temp->data << " ";
        }
        cout<<endl;
        return (temp->isTerminal);
    }
};

int main()
{
    char words[10][100] = {"apple", "ape", "no", "not", "coder", "coding"};
    Trie t;

    // Add words to trie
    for (int i = 0; i < 6; i++)
    {
        t.addWord(words[i]);
    }

    // Get the query from user
    char searchWord[100];
    cin.getline(searchWord, 100);

    // Search word in trie
    if (t.search(searchWord))
    {
        cout << searchWord << " is in trie" << endl;
    }
    else
    {
        cout << searchWord << " is not in trie" << endl;
    }

    return 0;
}