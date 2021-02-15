#include "person_data.h"

void write_file_in(vector<person> temp){
    fstream file("data.bin",ios::binary | ios::in | ios::out | ios::trunc);
    if(!file.is_open()){
        cout << "error while opening the file";
        return;
    }

    for(auto y: temp) {
        file.write((char *)&y,sizeof(person));
    }
    file.seekg(0);
    file.close();
}

vector<person> read_file(){
    fstream file("data.bin",ios::binary | ios::in | ios::out | ios::trunc);
    vector<person> the_data;
    person temp;
    while(file.read((char *)&temp,sizeof(person))) the_data.push_back(temp);
    
    file.close();
    return the_data;
} 
