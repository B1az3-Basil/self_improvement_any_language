#include "person_data.h"
#include "write_things_in_binaryFile.cpp"

vector<string> split(char to_split ,string word){
    vector<string> list; 
    string temp;
    for (char letter: word){
        if (letter == to_split){
            list.push_back(temp);
            temp = "";
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
    while (!feof(pipe)) if (fgets(buffer, 128, pipe) != NULL)  result += buffer;
    pclose(pipe);
    return split('\n',result);
}


bool in(string to_find, auto from){
    int i = 0;
    for(auto a: from){
        if (i == to_find.size() - 1) return true;
        else if (to_find[i] == a) i++;
        else i = 0;
    } 
    return false;
}

string get_date(){
   // current date/time based on current system
    time_t now = time(0);
    tm *ltm = localtime(&now);
    string day = to_string(1900 + ltm->tm_year) + '-' + to_string(1 + ltm->tm_mon) + '-' + to_string(7 + ltm->tm_mday);
    return day;

}


int main(){
    // int command = system("wtc-lms");
    vector<string> all_review_list = run_command("wtc-lms reviews");
    vector<vector<string>> hssd;
    vector<string> hash;
    for (string a: all_review_list) {
        if (in("Assigned", a)){
            hash.push_back(a.substr(a.find('(') + 1, a.find(')') - a.find('(') - 1));
            hssd.push_back(run_command("wtc-lms review_details " + a.substr(a.find('(') + 1, a.find(')') - a.find('(') - 1)));
        }
    }
    printf("%s\n", get_date().c_str());
    int w = 0;
    vector<person> ins;
    for (auto a: hssd){
        string loca;
        string email_name;
        for (auto z: a) {
            if (in("@student", z)) email_name = z.substr(z.find(':') + 2, 100);
            else if (in("Location", z)) loca = z.substr(z.find(' ') + 1, 100);
        }

        printf("hash: %s\n", hash[w].c_str());
        printf("loca: %s\n", loca.c_str());
        printf("email: %s\n", email_name.c_str());
        printf("name: %s\n", email_name.substr(0,  email_name.find('@')).c_str());
        person one;
        one.persons(get_date(), email_name.substr(0,  email_name.find('@')), hash[w], loca,email_name);
        ins.push_back(one);
        w++;
    }
    
    write_file_in(ins);
    // printf("%s", all_review_list[0].c_str());
    return 0;
}