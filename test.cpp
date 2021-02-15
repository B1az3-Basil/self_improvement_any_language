#include <iostream>
#include <ctime>

using namespace std;

int main() {
   // current date/time based on current system
   time_t now = time(0);

   tm *ltm = localtime(&now);

   // print various components of tm structure.
   printf("%s", to_string(1900 + ltm->tm_year).c_str());
   cout << "Month: "<< 1 + ltm->tm_mon<< endl;
   cout << "Day: "<< 7 + ltm->tm_mday << endl;
   cout << "Time: "<< 5+ltm->tm_hour << ":";
   cout << 30+ltm->tm_min << ":";
   cout << ltm->tm_sec << endl;
}