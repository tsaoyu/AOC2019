#include <iostream>
#include <map>

using namespace std;


bool is_non_decrease_and_adjecent(const string& number){
    bool adjecent_flag = false;
    for (auto first = number.begin(); first != number.end()-1; first++){
        string::const_iterator second = first + 1;
        if (*first > *second){
            return false;
        }
        else if (*first == *second){
            adjecent_flag = true;
        }

    }
    return true && adjecent_flag;
 }



bool is_non_decrease_and_adjecent_non_matching(const string& number){
    map<char, int> adjecent_group;
    bool adjecent_flag = false;
    for (auto first = number.begin(); first != number.end()-1; first++){
        string::const_iterator second = first + 1;
        if (*first > *second){
            return false;
        }
        else if (*first == *second){
            if (adjecent_group.count(*second)){
                adjecent_group[*second] += 1;
            }
            else {
                 adjecent_group[*second] = 2;   
            }
                
        }
    }
    for (const auto i: adjecent_group){
        if (i.second == 2){
            adjecent_flag =true;
        }
    }
    return true && adjecent_flag;
}

int main(){
    int ans1 = 0;
    int ans2 = 0;
    for (int i=172930; i<683083; i++){
        if (is_non_decrease_and_adjecent(to_string(i))){
            ans1 += 1;
        }
        if (is_non_decrease_and_adjecent_non_matching(to_string(i))){
            ans2 += 1;
        }
    }

    cout << ans1 << endl;
    cout << ans2 << endl;

    return 0;
}
