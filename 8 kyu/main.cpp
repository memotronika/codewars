//Remove First and Last Character
#include <string>

using namespace std; 

string sliceString (string str )
{
  return str.substr(1, str.length() - 2);
}

//Miles per gallon to kilometers per liter
#include <cmath>

double converter(int mpg) {
    double kpl = (mpg * 1.609344) / 4.54609188;
    kpl = round(kpl * 100) / 100.0;
return kpl;
}

// Grasshopper - Messi goals function
int goals (int laLigaGoals, int copaDelReyGoals, int championsLeagueGoals) {
    return laLigaGoals+copaDelReyGoals+championsLeagueGoals;
}

// Quadrants
int quadrant(int x, int y) {
    if (x>0) {
        if (y>0){
            return 1;
        }else{return 4;}
    }else{
        if (y>0){
            return 2;
        }else{return 3;}
    }
}

// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
