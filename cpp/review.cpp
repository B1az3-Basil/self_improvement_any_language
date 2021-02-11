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

vector<string> run_command(string command){
    char buffer[128];
    vector<string> result;
    FILE *pipe = popen(command.c_str(),"r");
    // if (!pipe) return  vector<string>;
    while (!feof(pipe)) if (fgets(buffer, 128, pipe) != NULL) { result.push_back(buffer);}
    pclose(pipe);
    return result;
}

int main(){
    // int command = system("wtc-lms");
    printf("%s", run_command("wtc-lms")[1].c_str());
    return 0;
}