#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

//Part 1
int main()
{
    ifstream inFile;
    inFile.open("Puzzle_Input_Day_1.txt");
    int num;
    int sum = 0;
    while (inFile >> num)
    {
        int fuel = floor(num/3) - 2;
        sum += fuel;
    }
    cout << sum << endl;
    inFile.close();
    return 0;
    
}
