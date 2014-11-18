[2~[2~// new_handler example 
#include <iostream> // std::cout 
#include <cstdlib> // std::exit 
#include <new> // std::set_new_handler 

void no_memory () { 
std::cout << "Failed to allocate memory!\n"; 
std::exit (1); 
} 

int main () { 
std::set_new_handler(no_memory); 
long len = 4*1024*1024*1024; 
std::cout << "Attempting to allocate " << len << " GiB..."; 
char* p = new char[len]; 

//std::cout << "size of p: " << sizeof (p); 
memset(p, 0, len); 

std::cout << "Ok\n"; 
delete[] p; 
return 0; 
}
