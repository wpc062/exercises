#include <sys/mman.h>
#include <unistd.h>
#include <stdint.h>
 
int main()
{
    /* mmap 50MiB of shared anonymous memory */
    char *p = (char*)mmap(NULL, 50 << 20, PROT_READ | PROT_WRITE,
                   MAP_ANONYMOUS | MAP_SHARED, -1, 0);
 
    /* Touch every single page to make them resident */
    for (int i = 0; i < (50 << 20) / 4096; i++) {
        p[i * 4096] = 1;
    }
 
    /* Let us see the process in top */
    sleep(1000000);
 
    return 0;
}
