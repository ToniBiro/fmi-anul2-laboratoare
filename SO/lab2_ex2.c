# include<stdio.h>
# include<sys/stat.h>
# include<sys/types.h>
# include<fcntl.h>
#include<errno.h>
int main(int argc, char** argv)
{
	if(argc != 3)
	{ printf("error!");}
	
	const char *fsrc = argv[1];
	const char *fdst = argv[2];
	int src = open(fsrc, O_RDONLY);
	if(src < 0)
	{
		perror("open src");
		return errno;
	}
	
	
	int dst = open(fdst, O_WRONLY|O_CREAT);
	if(dst<0)
	{
		perror("open dst");
		return errno;
	}
	
	char buf[1024];
	int nread = read(src, buf, 1024);
	int nwrite;
	if(nread<0)
	{
		perror("read buf");
		return errno;
	}
	int nread_total = 0;
	while(nread)
	{
		nwrite = write(dst, buf + nread_total, nread - nread_total);
		if(nwrite<0)
		{perror("write buf"); return errno;}
		nread_total += nread;
		while(nwrite)
		{
			nwrite = write(dst, buf + nread_total, nread - nread_total);
			if(nwrite<0)
			{perror("write buf"); return errno;}
		}
		nread = read(src, buf, 1024);
		if(nread<0)
		{perror("read buf"); return errno;}
	}
	return 0;
}