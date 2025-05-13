#include <stdio.h>
#include <stdio.h>
#include <time.h>
#include <sys/stat.h>
#include <string.h>
#include <stdlib.h>

int main() {
	char *date;
	int ret;
	struct stat buf;
	while ((ret = stat("/home/eugen/.profile", &buf)) != 0)
	{
		fprintf(stderr, "stat failure error .%d", ret);
		abort();
	}
	date = asctime(localtime(&buf.st_ctime));
	printf("%s", date);
	printf("%ld date\n", buf.st_ctime);
	return 0;
}
