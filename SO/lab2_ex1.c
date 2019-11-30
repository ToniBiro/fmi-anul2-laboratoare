#include <stdio.h>
#include <string.h>

int main()
{
	const char *str = "Hello World\n";
	size_t len = strlen(str);
	write(1, str, len);
	return 0;
}