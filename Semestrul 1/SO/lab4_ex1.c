# include<stdio.h>
# include<unistd.h>
#include<errno.h>
int main()
{
	pid_t  pid = fork();

	if (pid < 0)
	{ return errno;}
	else
	{
		if (pid == 0)
		{
			printf("My pid %d Child Pid %d\n", getppid(), getpid());
			char *argv[] = {"ls", NULL};
			execve("/bin/ls", argv, NULL);
			
		}
		else
		{
			printf("My parents PID: %d  My PID: %d", getpid(), pid);
			wait(NULL);
		}
	}
	return 0;
}