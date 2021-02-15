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
    cout << "hi am "<<name<<" and i am "<<age<<" nyears old"<<endl;
    }
    void change(){
        strcpy(name,"xxxx");
    age = 1000;
    }

};


int main()
{
vector<Person> temp;

Person anil("anil",24);
temp.push_back(anil);
Person a("basil",24);
temp.push_back(a);

fstream file("person.bin",ios::binary | ios::in | ios::out | ios::trunc );
if(!file.is_open()){
    cout << "error while opening the file";
}else{
    for(Person& y: temp) file.write((char *)y,&sizeof(Person));

    file.seekg(0);
    vector<Person> test;
    Person temp;
    while(file.read((char *)&temp,sizeof(Person))) test.push_back(temp);

// anil.whoAreYou();
    for (Person& a: test) a.whoAreYou();


file.close();
}

   return 0;
}

 