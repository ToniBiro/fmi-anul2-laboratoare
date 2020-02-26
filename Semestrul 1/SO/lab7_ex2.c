#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <errno.h>
#include <semaphore.h>
#include <time.h>

#define MAX 5
pthread_mutex_t mtx;

sem_t sem;

int cnt = 0;

void barrier_point();

void* tfun(void* v)
{
    int tid = (int)v;

    printf("%d reached the barrier\n", tid);
    barrier_point();
    printf("%d passed the barrier\n", tid);

    return NULL;
}

void barrier_point()
{
    int i;
    pthread_mutex_lock(&mtx);
    cnt += 1;
    if(cnt == MAX)
    {
        for (i = 0; i < cnt-1; ++i)
            sem_post(&sem);
        cnt = 0;
        pthread_mutex_unlock(&mtx);
        return;
    }
    pthread_mutex_unlock(&mtx);
    sem_wait(&sem);
}


int start_threaduri(int nr_th)
{
    int i;
    pthread_t *thr = malloc(sizeof(pthread_t)*nr_th);
    for (i = 0; i < nr_th; ++i)
    {
        if(pthread_create(&thr[i], NULL, tfun, (void*)i))
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
    if(pthread_mutex_init(&mtx, NULL))
    {
        perror(NULL);
        return errno;
    }
    if(sem_init(&sem, 0, 0))
    {
        perror(NULL);
        return errno;
    }

    start_threaduri(MAX);

    return 0;
}
