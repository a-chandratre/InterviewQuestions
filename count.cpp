#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    string phrase;
    char letter;
    short int n = 0;
    cin >> letter;
    cin >> phrase;

    for (int i = 0; i < phrase.length(); i++)
    {
        if (phrase.at(i) == letter)
        {
            n++;
        }
    }
    return n;
}
