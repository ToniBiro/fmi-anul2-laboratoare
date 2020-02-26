#include<stdio.h>
#include<errno.h>
#include<stdlib.h>
#include<pthread.h>
#include<time.h>

typedef struct{
	int len;
	int* lin;
	int* col;
}argumente;

typedef struct {
	int **m;
	int rows, cols;
}matrix;

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
	int len = arg->len;
	int* lin = arg->lin;


	int* col = arg->col;
	int i;
	int* rez = (int*) malloc(sizeof(int));
	*rez = 0;
	for (i = 0; i < len; ++i)
		*rez = *rez + lin[i]*col[i];
	return rez;
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
	FILE *f = fopen("matrice.in", "r");
	int a, n, b;

	m_test();
	// fscanf(f, "%d", &a);
	// fscanf(f, "%d", &n);
	// fscanf(f, "%d", &b);
	// int** mat1 = (int**) malloc(a*sizeof(int*));
	// int i, j;
	// for (i = 0; i < a; ++i)
	// 	mat1[i] = (int*)malloc(n*sizeof(int));

	// int** mat2 = (int**) malloc(n*sizeof(int*));

	// for (i = 0; i < n; ++i)
	// 	mat2[i] = (int*)malloc(b*sizeof(int));

	// for (i = 0; i < a; ++i)
	// 	for(j = 0; j < n; ++j)
	// 		fscanf(f, "%d", &mat1[i][j]);

	// for (i = 0; i < n; ++i)
	// 	for(j = 0; j < b; ++j)
	// 		fscanf(f, "%d", &mat2[i][j]);

	// fclose(f);
	// for( i = 0; i < a; ++i)
	// {
	// 	printf("\n");
	// 	for (j = 0; j < n; ++j)
	// 		printf("%d ", mat1[i][j]);
	// }

	// for( i = 0; i < n; ++i)
	// {
	// 	printf("\n");
	// 	for (j = 0; j < b; ++j)
	// 		printf("%d ", mat2[i][j]);
	// }
	// printf("\n");
	// /*argumente* test = (argumente*) malloc(sizeof(argumente));
	// test->len = n;
	// test->lin = mat1[0];
	// test->col = (int*)malloc(n*sizeof(int));

	// for (i = 0; i < n; ++i)
	// {
	// 	test->col[i] = mat2[i][0];
    //     printf("%d ", mat2[i][0]);
	// }
	// int val = *(int*)(multiply(test));
	// printf("aici %d\n", val);*/


	// int** mat = (int**)malloc(a*sizeof(int*));

	// for(i = 0; i < a; ++i)
	// 	mat[i] = (int*)malloc(b*sizeof(int));

	// argumente** arg = (argumente**)malloc(a*sizeof(argumente*));
	// for (i = 0; i < a; ++i)
    //     	arg[i] = (argumente*)malloc(b*sizeof(argumente));

	// int k;
	// pthread_t** thr = (pthread_t**)malloc(a*sizeof(pthread_t*));
	// for (i = 0; i < a; ++i)
    //     	thr[i] = (pthread_t*)malloc(b*sizeof(pthread_t));

	// for (i = 0; i < a; ++i)
	// 	for(j = 0; j < b; ++j)
	// 	{
	// 	    arg[i][j].len = n;
    //         arg[i][j].lin = mat1[i];
    //         arg[i][j].col = (int*)malloc(n*sizeof(int));
    //         for(k = 0; k < n; ++k)
    //             arg[i][j].col[k] = mat2[k][j];
	// 		if(pthread_create(&thr[i][j], NULL, multiply, &arg[i][j]))
    //         {
    //             perror(NULL);
    //             return errno;
    //         }
	// 	}
    // for (i = 0; i < a; ++i)
	// 	for(j = 0; j < b; ++j)
	// 	{
    //         if(pthread_join(thr[i][j], (void**)&mat[i][j]))
    //         {
    //             perror(NULL);
    //             return errno;
    //         }
	// 	}

    // for (i = 0; i < a; ++i)
    // {
    //     for (j = 0; j < b; ++j)
    //     {
    //         printf("%d ", *(int*)mat[i][j]);
    //     }
    //     printf("\n");
    // }
    
    // for (i = 0; i < a; ++i)
	// 	free(mat1[i]);
    // free(mat1);
    
    // for (i = 0; i < b; ++i)
	// 	free(mat2[i]);
    // free(mat2);
	
    //  for (i = 0; i < a; ++i)
	// free(mat[i]);
    // free(mat);

    // for (i = 0; i < a; ++i)
	// free(arg[i]);
    // free(arg);
    // for (i = 0; i < a; ++i)
	// free(thr[i]);
    // free(thr);
    
	return 0;


}
