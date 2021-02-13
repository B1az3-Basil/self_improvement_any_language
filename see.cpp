#include <iostream>
#include <fstream>
#include <cstring>
#include <vector>
using namespace std;

class Person{
char name[80];
int age;
public:
    Person(){
    strcpy(name,"noname");
    age = 0;
    }
   Person(char *name,int age){
    strcpy(this->name,name);
    this->age = age;
    }

    void whoAreYou(){
        cout << "hi am "<<name<<" and i am "<<  age<< " nyears old"<< endl;
    }
    void change(){
        strcpy(name,"xxxx");
        age = 1000;
    }

};


int main()
{
    vector<Person> test;
    
    Person anil("basil",24);
    test.push_back(anil);
    fstream file("person.bin",ios::binary | ios::in | ios::out | ios::trunc );
    if(!file.is_open()){
        cout << "error while opening the file";
    }else{
        file.write((vector<Person>)&test,sizeof(vector<Person>));

        file.seekg(0);

        vector<Person> tests;
        file.read((vector<Person>)&test,sizeof(vector<Person>));

        printf("%d", test.size());
        

        // test[0].change();

        // test[0].whoAreYou();
       
        file.close();
    }

   return 0;
}
