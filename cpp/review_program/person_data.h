#ifndef __PERSON_H
#define __PERSON_H
#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>

using namespace std;

class person{
    public:
        string date;
        string name;
        string ussd;
        string location;
        string email_address;
        person(){
            date = "";
            name = "";
            ussd = "";
            location = "";
            email_address = "";
        }


        person(string date, string name, string ussd, string location, string email){
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


vector<person> read_file();
void write_file_in(vector<person> temp);

#endif