#include<stdio.h>
#include<errno.h>
#include<stdlib.h>
#include<pthread.h>
#include<time.h>



typedef struct {
	int **m;
	int rows, cols;
}matrix;

typedef struct{
	int len;
	matrix *m1, *m2, *mr;
	pthread_t thr;
}argumente;

matrix* m_alloc(int r, int c)
{
	matrix *m = malloc(sizeof(matrix));
	m->rows = r;
	m->cols = c;

	m->m = malloc(sizeof(int*)*r);
	int i;
	for (i = 0; i < r; ++i)
	{
		m->m[i] = malloc(c*sizeof(int));
	}
	return m;
}

void m_free(matrix* m)
{
	int i;
	for(i = 0; i < m->rows; ++i)
	{
		free(m->m[i]);
	}
	free(m->m);
}

void m_print(matrix* m)
{
	int i, j;
	for(i = 0; i < m->rows; ++i)
	{
		for(j = 0; j < m->cols; ++j)
			printf("%d ", m->m[i][j]);
		printf("\n");
	}
}

void m_rand(matrix *m)
{
	srand(time(0));
	int i, j;
	for(i = 0; i < m->rows; ++i)
	{
		for(j = 0; j < m->cols; ++j)
			m->m[i][j] = rand() % 10;
	}
}

void * multiply(void* v)
{
	argumente* arg = (argumente*) v;

	int i;
	for (i = 0; i < arg->len; ++i)
		arg->rez = arg->rez + arg->m1[i] * arg->m2[i];
	return arg->rez;
}

void m_test()
{
	matrix *m = m_alloc(3, 4);
	m_rand(m);
	m_print(m);
	m_free(m);
}

int main()
{
	int i, j, k;
	int n = 3, m = 5, p = 4;

	matrix *mat_1 = m_alloc(n, p);
	matrix *mat_2 = m_alloc(p, m);
	matrix *mat_rez = m_alloc(n, m);
	m_rand(mat_1);
	m_rand(mat_2);
	m_print(mat_1);
	m_print(mat_2);


	argumente* arg = (argumente**)malloc(m*n * sizeof(argumente*));
	 int argi = 0;

	for (i = 0; i < mat_1->rows; ++i)
		for(j = 0; j < mat_2->cols; ++j)
		{
			arg[argi].m1 = 


			if(pthread_create(&arg[argi]->thr, NULL, multiply, &arg[argi++])
            {
                perror(NULL);
                return errno;
            }
		}
	argi = 0;
	for (i = 0; i < mat_1->rows; ++i)
		for(j = 0; j < mat_2->cols; ++j)
		{
            if(pthread_join(arg[argi++]->thr, (void**)mat_rez->m[i][j]))
            {
                perror(NULL);
                return errno;
            }
		}
    m_print(mat_rez);
    m_free(mat_1);
	m_free(mat_2);
    m_free(mat_rez);

	free(arg);
	return 0;
}
