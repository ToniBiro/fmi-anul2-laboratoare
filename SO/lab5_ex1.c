
// shm_open()
// ftruncate(1024*nr arg)
// loop de for de la 1-argc si fac fork
// fie am eroare si ies fie intru in copil
// fac mmap care imi returneaza o adresa
// calculam offset - la ce proces sunt *1024 (i-1 *1024)
// calcules seria si dau exit


#include <unistd.h>
#include <stdio.h>
#include <errno.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>

void coll(int n, int *my_buff)
{
	int i = 1;
	while(n != 1)
	{
		my_buff[i++] = n;
		if(n%2 == 0)
			n = n/2;
		else
			n = 3*n + 1;
	}
	my_buff[i++] = 1;
	my_buff[0] = i;
}

void print_coll(int *my_buff)
{
	int i ;
	for (i = 0; i <= my_buff[0]; ++i)
	{
		printf("%d ", my_buff[i+1]);
	}
	printf("\n");
}

int main(char argc, const char *argv[])
{
	char shm_name[] = "/my_shm";
	int shm_fd = shm_open(shm_name, O_CREAT | O_RDWR, S_IRUSR | S_IWUSR);
	if(shm_fd < 0)
	{
		perror(NULL);
		return errno;
	}
	
	size_t shm_size = argc*1024;
	if(ftruncate(shm_fd, shm_size) == -1)
	{
		perror(NULL);
		shm_unlink(shm_name);
		return errno;
	}
	int i;
	for(i = 0; i < argc-1; ++i)
	{
		pid_t pid = fork();
		if(pid < 0)
		{
			return errno;
		}
		if(pid == 0)
		{
			char *addr =  mmap(0, shm_size, PROT_WRITE, MAP_SHARED, shm_fd, 0);
			if(addr == MAP_FAILED)
			{
				perror(NULL);
				return errno;
			}
			int* my_buff = (int*)(addr + i*1024);
			int n;
			sscanf(argv[i+1], "%d", &n);
			coll(n, my_buff);
			close(shm_fd);
			munmap(addr, shm_size);
			return 0;
			
		}

	}
	for(i = 0; i < argc-1; ++i)
	{
		int pid = wait(NULL);
		printf("My parents pid: %d, my pid: %d", getpid(), pid);
	}
	char* addr = mmap(0, shm_size, PROT_READ, MAP_SHARED, shm_fd, 0);
	
	for(i = 0; i < argc-1; ++i)
	{
		print_coll((int*)(addr+i*1024));
	}
	close(shm_fd);
	munmap(addr,shm_size);

	shm_unlink(shm_name);

}