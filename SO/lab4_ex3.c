#include<stdio.h>
#include<unistd.h>
#include<errno.h>

int main(int argc, const char *argv[])
{
	int i;
	if(argc <= 1)
	{
		printf("trebuie dat un nr");
		return 0;
	}
	for (i = 0; i < argc-1; ++i)
	{
		printf("ARGC: %d\n", argc);
		pid_t pid = fork();
		
		if (pid < 0)
			return errno;
		else
		{
			if(pid == 0)
			{	
				int n;
				sscanf(argv[i+1], "%d", &n);
				while(n > 1)
				{
					printf("%d ", n);
					if(n % 2 == 0)
					{
						n = n/2;
					}
					else
					{
						n = 3 * n + 1;
					}
				}
				printf("1\n");		
				return 0;
			}
		}
	}
	for (i = 0; i < argc-1; ++i)
	{
		int pid = wait(NULL);
		printf("My parents pid: %d  My pid: %d\n", getpid(), pid);
	}
	printf("\n");
	return 0;
}