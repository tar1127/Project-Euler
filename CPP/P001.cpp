#include <iostream>

int main(){
	int sumOfNum = 0;
	int x;
	for (x = 1; x < 1000; x++){
		if ( x % 3 == 0 || x % 5 ==0 ){
			sumOfNum += x;
		}
	 
	}
	std::cout << std::endl << "total sum: " << sumOfNum << std::endl;
	return 0;
}
