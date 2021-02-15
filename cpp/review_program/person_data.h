#ifndef __PERSON_H
#define __PERSON_H
#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>


using namespace std; 


class person{
    private:
        string date;
        string name;
        string ussd;
        string location;
        string email_address;
    public:
        person(){
            date = "";
            name = "";
            ussd = "";
            location = "";
            email_address = "";
        }


        void persons(string date, string name, string ussd, string location, string email){
            this->date = date;
            this->name = name;
            this->ussd = ussd;
            this->location = location;
            this->email_address = email; 
        }
        

        string print(){
            return name;
        }
};
void write_file_in(vector<person> temp);

#endif