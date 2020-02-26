#include <stdio.h>
#include<errno.h>
#include<stdlib.h>
#include<pthread.h>
#include<time.h>

#define MAXRESOURCES 5

pthread_mutex_t mtx;

int available_resources = MAXRESOURCES;

int decrease_count(int count)
{
    pthread_mutex_lock(&mtx);
    if(available_resources < count)
    {
        pthread_mutex_unlock(&mtx);
        return -1;
    }
    else
        available_resources -= count;
    printf("Got %d Resources %d remaining\n", count, available_resources);

    pthread_mutex_unlock(&mtx);
    return 0;
}

int increase_count(int count)
{
    pthread_mutex_lock(&mtx);
    available_resources += count;
        printf("Released %d Resources %d remaining\n", count, available_resources);
    pthread_mutex_unlock(&mtx);
    return 0;
}

void* consum(void* v)
{
	int res = (int)v;
    if(decrease_count(res) != -1)
    {
        increase_count(res);

    }
}

int start_threaduri(int nr_th)
{
    int i;
    pthread_t *thr = malloc(sizeof(pthread_t)*nr_th);
    for (i = 0; i < nr_th; ++i)
    {
        int res_cons = rand() % MAXRESOURCES;

        if(pthread_create(&thr[i], NULL, consum, (void*)res_cons))
        {
            perror(NULL);
            return errno;
        }
    }

    for(i = 0; i < nr_th; ++i)
    {
        if(pthread_join(thr[i], NULL))
        {
            perror(NULL);
            return errno;
        }
    }
    free(thr);
    return 0;
}

int main()
{
    srand(time(0));
    if(pthread_mutex_init(&mtx, NULL))
    {
        perror(NULL);
        return errno;
    }

    start_threaduri(rand()%10);

    return 0;
}
