#include "person_data.h"


vector<person> read_file(){
    vector <person> ofter;
    string myText;
    string array[5];
    ifstream MyReadFile("data.txt");
    getline (MyReadFile, myText);
    while (myText == "*") {
       getline (MyReadFile, array[0]);
       getline (MyReadFile, array[1]);
       getline (MyReadFile, array[2]);
       getline (MyReadFile, array[3]);
       getline (MyReadFile, array[4]);
       getline (MyReadFile, myText);
       person one(array[2], array[0], array[3], array[4], array[1]);
       ofter.push_back(one);
    }
    
    MyReadFile.close();
    return ofter;
} 


void write_file_in(vector<person> temp){
    ofstream myfile;
    myfile.open ("data.txt");
    for (auto a: temp){
        myfile << "*\n";
        myfile << a.name + "\n";
        myfile << a.email_address + "\n";
        myfile << a.date + "\n";
        myfile << a.ussd + "\n";
        myfile << a.location + "\n";
       
    }
    myfile.close();
  
}
