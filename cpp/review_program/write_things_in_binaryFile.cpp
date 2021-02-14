
#include "person_data.hpp"
// #include "review.cpp"
using namespace std; 

class write_file{
    private:
        vector<person> the_data;
        fstream file;
    public:
        void write_fil(){
            fstream file("data.bin",ios::binary | ios::in | ios::out | ios::trunc);
        }

        void write_fie(vector<person> temp){
            for(person& y: temp) file.write((char *)&y,sizeof(person));
            file.close();
        }
        
        vector<person> read_file(){
            person temp;
            while(file.read((char *)&temp,sizeof(person))) the_data.push_back(temp);
            file.close();
            return the_data;
        } 
};