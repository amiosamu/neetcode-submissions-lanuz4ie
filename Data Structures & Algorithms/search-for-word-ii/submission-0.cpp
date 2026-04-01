#include <vector>
#include <string>
#include <functional>
using namespace std;

class Solution {
public:
    class Trie {
    public:
        vector<Trie*> children;
        int wordIndex;

    public:
        Trie() : children(26, nullptr), wordIndex(-1) {}

        void insert(const string& word, int index) {
            Trie* node = this;
            for (char c : word) {
                c -= 'a';
                if (!node->children[c]) {
                    node->children[c] = new Trie();
                }
                node = node->children[c];
            }
            node->wordIndex = index;
        }
    };

    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        Trie* trieRoot = new Trie();
        for (int i = 0; i < words.size(); i++) {
            trieRoot->insert(words[i], i);
        }
        vector<string> foundWords;
        int rows = board.size(), cols = board[0].size();

        function<void(Trie*, int, int)> dfs = [&](Trie* node, int i, int j) {
            int charIndex = board[i][j] - 'a';
            if (!node->children[charIndex]) {
                return;
            }
            node = node->children[charIndex];
            if (node->wordIndex != -1) {
                foundWords.emplace_back(words[node->wordIndex]);
                node->wordIndex = -1;
            }
            int directions[5] = {-1, 0, 1, 0, -1};
            char tempChar = board[i][j];
            board[i][j] = '*';
            for (int k = 0; k < 4; k++) {
                int x = i + directions[k], y = j + directions[k + 1];
                if (x >= 0 && x < rows && y >= 0 && y < cols && board[x][y] != '*') {
                    dfs(node, x, y);
                }
            }
            board[i][j] = tempChar;
        };

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                dfs(trieRoot, i, j);
            }
        }
        return foundWords;
    }
};
