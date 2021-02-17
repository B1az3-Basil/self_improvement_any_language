#ifndef __PERSON_H
#define __PERSON_H
#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
#include <cctype>
#include <cstdio>

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


namespace Color {
    enum Code {
        RED      = 31,
        GREEN    = 32,
        BLUE     = 34,
        DEFAULT  = 39,
    };
    class Modifier {
        Code code;
    public:
        Modifier(Code pCode) : code(pCode) {}
        friend std::ostream&
        operator<<(std::ostream& os, const Modifier& mod) {
            return os << "\033[" << mod.code << "m";
        }
    };
}

using namespace Color;

vector<person> read_file();
void write_file_in(vector<person> temp);

#endif