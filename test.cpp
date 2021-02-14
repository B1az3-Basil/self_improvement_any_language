#include <iostream>
#include <ctime>

using namespace std;

int main() {
   // current date/time based on current system
    
    const char *time_details = "16:35:12";
    struct tm tm;
    // now = time(NULL);
    
    strptime(time_details, "%H:%M:%S", &tm);
    time_t now = mktime(&tm); 
    cout << now << endl;
    // time_t now = time(2020,11,18);

   cout << "Number of sec since January 1,1970 is:: " << now << endl;

   localtime(&now);

   // print various components of tm structure.
   cout << "Year:" << 1900 + localtime(&now)->tm_year<<endl;
   cout << "Month: "<< 1 + localtime(&now)->tm_mon<< endl;
   cout << "Day: "<< localtime(&now)->tm_mday << endl;
   cout << "Time: "<< 5+localtime(&now)->tm_hour << ":";
   cout << 30+localtime(&now)->tm_min << ":";
   cout << localtime(&now)->tm_sec << endl;
}