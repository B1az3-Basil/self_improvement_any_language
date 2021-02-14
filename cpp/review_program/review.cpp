#include "write_things_in_binaryFile.cpp"

using namespace std;


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


int main(){
    // int command = system("wtc-lms");
    vector<string> all_review_list = run_command("wtc-lms reviews");
    for (string a: all_review_list) {
        if (in("Assigned", a)){
            printf("%s\n", a.substr(a.find('(') + 1, a.find(')') - a.find('(') - 1).c_str());
        }
    }
    write_file the_file();
    // printf("%s", all_review_list[0].c_str());
    return 0;
}