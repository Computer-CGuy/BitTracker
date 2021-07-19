#include <iostream>

using namespace std;

class Operators{
	public:
		int state;
	void assign(int state2){
		state = state2;
	}
}
/*
	^ = 1
	& = 2
	| = 3
*/
class Bogus{
	public:
		int val = 0;
		std::vector<int> history;
	Bogus operator^(const Bogus& b){
		history.push_back(b);
	}
	
};


std::ostream& operator<< (std::ostream &out, Bogus const& data) {
    out << data.val << ':';    
    return out;
}



int main(){
	Bogus b;
	cout << b;


	cout << endl;
}