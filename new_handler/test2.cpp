// new_handler example
#include <iostream> // std::cout
#include <cstdlib> // std::exit
#include <new> // std::set_new_handler
#include <cstring>

using namespace std;

void no_memory () {
        std::cout << "Failed to allocate memory!\n";
        std::exit (1);
}

void malloc_test(long len)
{
        //crash directly when fail to allocate memory
        char* p = (char*)malloc(len); //over-commit
        std::cout << "after new" << endl;

        memset(p, 0, len); // alloc memory actually now
        std::cout << "after memset" << endl;

        free(p);

}

void new_test(long len)
{
        char* p = new char[len];
        std::cout << "after new" << endl;

        //memset(p, 0, len);
        std::cout << "after memset" << endl;

        delete[] p;
}

int main (int argc, char* argv[]) {
        std::set_new_handler(no_memory); // priority: new_handler > exception
        int len_gb = 1;
        if (argc > 1) len_gb  = atoi(argv[1]);
        long len = len_gb * 1024L*1024L*1024L;
        std::cout << "Attempting to allocate " << len_gb << " GiB..." << endl;

        try {
              new_test(len);
              //malloc_test(len);
        }
        catch (std::exception& e)
        {  
                std::cout << e.what() << endl;
        }
        return 0;
}
