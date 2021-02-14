#include <iostream>
#include <vector>
#include <sstream> 

using namespace std;

vector<string> split(char to_split ,string word){
    vector<string> list; 
    string temp;
    for (char letter: word){
        if (letter == to_split){
            list.push_back(temp);
            temp = "";
            continue;
        }
        temp += letter;
    }
    list.push_back(temp);
    temp = "";
    return list;
}


int main(){
    int row;
    int colunm;
    vector<vector<int>> linear_equation;
    printf("Number of row: ");
    cin >> row;

    while(row != 0){
        vector<int> int_num;
        string equation;
        printf("Enter the number separated by ',': ");
        cin >> equation;
        int a;
        for(auto num: split(',', equation)) {
            stringstream ins(num);
            ins >> a;
            int_num.push_back(a);
        }
        linear_equation.push_back(int_num);
        row --;
    }
    for (auto row: linear_equation){
        printf("[");
        for(int a = 0; a < row.size(); a++) {
            printf("%d ", row[a]);
            if (a == row.size() - 2 ) printf("|");
        }
        printf("]\n");
    }
    
    return 0;
}