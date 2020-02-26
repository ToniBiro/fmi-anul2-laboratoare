#include<stdio.h>
#include<string.h>
#include<pthread.h>
#include<stdlib.h>
#include<errno.h>


void* reverse(void* v)
{
	char* sir = (char*)v;
	char* rez= (char*) malloc(100);
	int i, k = 0;
	for (i = strlen(sir)-1;i >= 0 ; i--)
		rez[k++] = sir[i];
	return rez;
}

int main(int argc,char** argv)
{
	char* sir = argv[1];
	pthread_t thr;
	char* rez;
	if(pthread_create(&thr, NULL, reverse, (void*)sir))
	{
		perror(NULL);
		return errno;
	}
	
	if(pthread_join(thr, (void**)&rez))
	{
		perror(NULL);
		return errno;
	}
	printf("\nrezultatul threadului: %s\n", rez);
	free(rez);
	return 0;
}