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
        if (i == to_find.size()) return true;
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

bool the_late_ones(string date){
    time_t now = time(0);
    tm *ltm = localtime(&now);
    string dt = to_string(1900 + ltm->tm_year) + '-' + to_string(1 + ltm->tm_mon) + '-' + to_string(ltm->tm_mday);
    return strcmp(date.c_str(), dt.c_str()) < 0;
}

pair<vector<person>, vector<person>> late_cool(vector<person> the_list){
    vector<person> late;
    vector<person> the_cool_ones;
    for (person& each: the_list){
        if (the_late_ones(each.date)) {
            late.push_back(each); 
            continue;
        }
        the_cool_ones.push_back(each);
    }

    return make_pair(late, the_cool_ones);
}

void invite(){
    // choose = ['hangman', 'pyramid', 'outline', 'robot', 'mastermind', 'accounting', 'word', 'fix', 'recursion']
    vector<string> all_review_list = run_command("wtc-lms reviews");
    vector<string> check_num = {
            "Mastermind - Iteration 1", 
            "Mastermind - Iteration 2", 
            "Mastermind - Iteration 3", 
            "Outline", 
            "Word", 
            "Toy Robot - Iteration 1", 
            "Toy Robot - Iteration 2", 
            "Toy Robot - Iteration 3", 
            "Toy Robot - Iteration 4", 
            "Toy Robot - Iteration 5", 
            "Pyramid",
            "Accounting App", 
            "Hangman - Iteration 1", 
            "Hangman - Iteration 2",
            "Hangman - Iteration 3", 
            "Recursion", 
            "Bug",
            "Encapsulation > Mastermind",
            "Unit Testing with Java > FizzBuzz",
            "Encapsulation > Hangman"
        };
    vector<string> hssd;
    vector<string> hash;
    for (string that: check_num){
            vector<string> the_one;
            cout << that << " - ";
            for (string a: all_review_list) if (in(that, a) && in("Invited" , a)) the_one.push_back(a);
            printf("%d\n", the_one.size());
    }
    int y = 0;
    while (true){
        string choose;
        string chooses = "";
        
        
        char num;
        cout << "Topic: ";
        cin >> choose >> num;
        string topic = "hangmanpyramidoutlinerobotmastermindaccountingwordfixrecursionencapsulation>hangmanencapsulation>mastermindfizzBuzz";
    
        if (!in(choose, topic)) continue;
        
        char a = choose.c_str()[0] - 32; 
        chooses = a + choose.substr(1, choose.size() - 1);
        for (string a: all_review_list) {
            if (in("Invited", a) && in(chooses, a)){
                if (num != '0' && in("Iteration " + to_string(num), a)){
                    hash.push_back(a.substr(a.find('(') + 1, a.find(')') - a.find('(') - 1));
                    continue;
                }
                hash.push_back(a.substr(a.find('(') + 1, a.find(')') - a.find('(') - 1));
            }
        }

        string the_hash;
        if (hash.size() == 0)
            continue;
        the_hash = hash[y];
        run_command("wtc-lms accept " + the_hash);
        hssd = run_command("wtc-lms review_details " + the_hash);
        for (auto a: hssd)  cout << a << endl;

        string loca;
        string email_name;
        for (auto a: hssd){
            if (in("@student", a)) email_name = a.substr(a.find(':') + 2, 100);
            else if (in("Location", a)) loca = a.substr(a.find(' ') + 1, 100); 
        }

        system("echo '*' >> /home/basil/bin/data.txt");
        string d = "echo " + email_name.substr(0,  email_name.find('@')) + " >> /home/basil/bin/data.txt";
        system(d.c_str());
        d = "echo " + email_name + " >> /home/basil/bin/data.txt";
        system(d.c_str());
        d = "echo " + get_date() + " >> /home/basil/bin/data.txt";
        system(d.c_str());
        d = "echo " + the_hash + " >> /home/basil/bin/data.txt";
        system(d.c_str());
        d = "echo " + loca + " >> /home/basil/bin/data.txt";
        system(d.c_str());
        string ans;
        cout << "Do you want more: ";
        cin >> ans;
        if (ans == "no") break;
        y++;
    }   
}


void sync(){
    vector<string> all_review_list = run_command("wtc-lms reviews");
    vector<vector<string>> hssd;
    vector<string> hash;
    for (string a: all_review_list) {
        if (in("Assigned", a)){
            hash.push_back(a.substr(a.find('(') + 1, a.find(')') - a.find('(') - 1));
            hssd.push_back(run_command("wtc-lms review_details " + a.substr(a.find('(') + 1, a.find(')') - a.find('(') - 1)));
        }
    }

    int w = 0;
    vector<person> ins;
    for (auto a: hssd){
        string loca;
        string email_name;
        for (auto z: a) {
            if (in("@student", z)) email_name = z.substr(z.find(':') + 2, 100);
            else if (in("Location", z)) loca = z.substr(z.find(' ') + 1, 100);
        }

        string sync_ = "wtc-lms sync_review " + hash[w];
        system(sync_.c_str());
        person one(get_date(), email_name.substr(0,  email_name.find('@')), hash[w], loca,email_name);
        ins.push_back(one);
        w++;
    }
    write_file_in(ins);
}



void review(vector<person> the_list){
    while (true){
        string name;
        string code = "";
        Modifier red(RED);
        Modifier def(DEFAULT);
        cout << "Enter the name: ";
        cin >> name;
        string location;
        int i = 1;
        if (name == "exit") break;
        for (person& each: the_list) if (each.name == name) {location = each.location; string run = "code " + each.location; system(run.c_str()); code = each.ussd;}
        if (code == "") cout << red << "NO MATCH" << def << endl;
        else{ 
            while (true){
                string command = "";
                cout << "What to do: ";
                getline(cin, command);
                if (command == "comment"){
                    cout << "say!: ";
                    getline(cin, command);
                    string run = "wtc-lms add_comment " + code + ' ' + '"' +  command + '"';
                    system(run.c_str());
                }
                
                else if (command == "grade"){
                    cout << "grade!: ";
                    cin >> command; 
                    string run = "wtc-lms grade_review " + code + ' ' + command;
                    system(run.c_str());
                    run = "rm -rf " + location;
                    system(run.c_str());
                    vector<person> count = read_file();
                    
                    
                    for (auto a: count) {
                        if (a.name == name) {
                            int sum = i + 5;
                            command = "sed -i '";
                            command.append(to_string(i));
                            command.append(",");
                            command.append(to_string(sum));
                            command.append("d' ");
                            command.append("/home/basil/bin/data.txt");
                        
                            // cout << command << endl;
                            system(command.c_str());
                        }
                        i += 6;
                    }
                    break;
                }
            }
            break;
        }
    }
}


int main(){
    
    pair<vector<person>, vector<person>> the_cool_ones = late_cool(read_file()); 
    Modifier red(RED);
    Modifier green(GREEN);
    Modifier def(DEFAULT);
    cout << "------------------- " << red << "NOT RESPONDING" << def << " -------------------" << endl;
    if (the_cool_ones.first.size() == 0) cout << "............... " << green << "OK" << def << " ............... " << endl;
    else {
        for(person& each: the_cool_ones.first){
            std::string stuff(15 - each.name.size(), ' ');
            cout << each.name << stuff << "| " << each.ussd << endl;
        }
    }

    cout << "----------------------- " << green << "REVIEW" << def << " -----------------------" << endl;
    if (the_cool_ones.second.size() == 0) cout << "............... " << red << "Empty" << def << "............... " << endl;
    else {
        for(person& each: the_cool_ones.second) {
            std::string stuff(15 - each.name.size(), ' ');
            cout << each.name << stuff << "| " << each.ussd << endl;
        }
    }
    printf("\n\n");
    while (true){
        string command;
        cout << "Job: ";
        cin >> command;
        if (command == "review"){
            cout << "which: ";
            cin >> command;
            if (command == "late") review(the_cool_ones.first);
            else review(the_cool_ones.second);
        }
        else if (command == "invite") invite();
        else if (command == "sync") sync();
    }
    
}

