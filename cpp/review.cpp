#include <iostream>
#include <vector>

using namespace std;
class person{
    private:
        string date;
        int id;
        string name;
        string ussd;
        string location;
        string email_address;
    public:
        person(){
            id += 1;
            date = "";
            name = "";
            ussd = "";
            location = "";
            email_address = "";
        }
};

vector<string> split(char to_split ,string word){
    vector<string> list; 
    string temp;
    for (char letter: word){
        if (letter == to_split){
            temp = "";
            list.push_back(temp);
            continue;
        }
        temp += letter;
    }
    return list;
}

vector<string> run_command(string command){
    char buffer[128];
    string result;
    FILE *pipe = popen(command.c_str(),"r");
    // if (!pipe) return  vector<string>;
    // cout << fgets(buffer, 128, pipe) << endl;
    while (!feof(pipe)) if (fgets(buffer, 128, pipe) != NULL)  result += buffer;
    pclose(pipe);
    return split('\n',result);
}

int main(){
    // int command = system("wtc-lms");
    printf("%s", run_command("wtc-lms")[0].c_str());
    return 0;
}