#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <sstream>

using namespace std;
class Day3{
    private:
        vector<string> inputs, path1, path2;
        map<char, vector<int>> m ={
            {'R',{1,0}},
            {'L',{-1,0}},
            {'U',{0,1}},
            {'D',{0,-1}}
        };
    public:
        Day3(string input_name){
            ifstream infile(input_name);
            string line;
            while (getline(infile, line, '\n'))
            {
                inputs.push_back(line);
            }
            
            stringstream s1(inputs[0]);
            while (getline(s1, line, ',')){
                path1.push_back(line);
            }

            stringstream s2(inputs[1]);
            while (getline(s2, line, ',')){
                path2.push_back(line);
            }
        };

        void print_input(){
            for (auto i:path2){
                cout << i << endl;
            }
        }

        int closest_intersection(){
            map<pair<int,int>, int> trace1, trace2;
            pair<int,int> current_pos = {0, 0};
            int length = 0;
            int iter_num = 0;
            vector<int> direction;
            int distance;
            for (auto i: path1){
                direction = m[i[0]];
                distance = stoi(i.substr(1));
                for (int d = 0; d < distance; d++){
                    current_pos = {current_pos.first + direction[0], current_pos.second + direction[1]};
                    length += 1;
                    trace1[current_pos] = length;
                }
            }

            current_pos = {0, 0};
            length = 0;
            for (auto i : path2){
                vector<int> direction = m[i[0]];
                int distance = stoi(i.substr(1));
                for (int d = 0; d < distance; d++){
                    current_pos = {current_pos.first + direction[0], current_pos.second + direction[1]};
                    length += 1;
                    trace2[current_pos] = length;

                }
            }
            vector<pair<int,int>> intersections;
            
            // This is very slow, use the ordered map to save search time
            // for (auto t1:trace1){
            //     for (auto t2:trace2){
            //         if (t1.first == t2.first){
            //             intersections.push_back(t1.first);   
            //         }
            //     }
            // }

            map<pair<int,int>, int>::const_iterator itr1, itr2;
            itr1 = trace1.begin();
            itr2 = trace2.begin();

            while (itr1 != trace1.end() && itr2 != trace2.end()){
                if (itr1->first < itr2->first){
                    ++itr1;
                }
                else if (itr1->first > itr2->first){
                    ++itr2;
                }
                else {
                    intersections.push_back(itr1->first);
                    ++itr1;
                    ++itr2;
                }

            }
            

            int min_distance = INT32_MAX;

            for (auto intersection: intersections){
                int distance = abs(intersection.first) + abs(intersection.second);
                if (distance < min_distance){
                    min_distance = distance;
                }
            }
            
            int min_total_distance = INT32_MAX;

            for (auto intersection: intersections){
                int distance = trace1[intersection] + trace2[intersection];
                if (distance < min_total_distance){
                    min_total_distance = distance;
                }
            }

            cout << min_distance << endl;
            cout << min_total_distance << endl;

            return min_distance;
        }
};

int main(){
    
    Day3 day3 = Day3("input.txt");


    day3.closest_intersection();
    return 0;
}