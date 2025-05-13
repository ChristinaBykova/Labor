#include <syslog.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <ctype.h>
#include <errno.h>
#include <string.h>
#include <math.h>
#include <fcntl.h>
#include <stdint.h>
#include <signal.h>
#include <getopt.h>
#include <time.h>
#include <locale.h>
#include <stdarg.h>
#include <pwd.h>
#include <grp.h>
#include <netdb.h>
#include <utime.h>
#include <sys/wait.h>
#include <sys/time.h>
#include <sys/timex.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/ioctl.h>
#include <sys/socket.h>
#include <sys/poll.h>
#include <dirent.h>
#include <libconfig.h>
#include <linux/limits.h>

int main() {
//	char path0[PATH_MAX] = "/home/eugen";
//	char path[PATH_MAX];
//	strcpy(path, path0);
//	DIR *dir;
//	struct dirent *entry;
//	
//	char *date;
//	int ret;
//	struct stat buf;
//	
//	dir = opendir(path0);
//	while( ( entry = readdir(dir) ) != NULL ) {
//		printf("%d - %s [%d] %d\n", entry -> d_ino, entry -> d_name, entry -> d_type, entry -> d_reclen);
//		strcat(path, "/");	
//		strcat(path, entry -> d_name);	
//		if ((ret = stat(path, &buf)) != 0)
//		{
//			fprintf(stderr, "stat failure error .%d", ret);
//			abort();
//		}
//		date = asctime(localtime(&buf.st_ctime));
//		time_t now = time(0);
//		if (now - 600 <= buf.st_ctime) {
//			printf("%s %s",path, date);
//		}
//	//	printf("%ld date\n", buf.st_ctime);
//	
//		strcpy(path, path0);
//	}
//	closedir(dir);
	

		char path0[PATH_MAX] = "/home/eugen";
		int max_rec = 2;
		char path[max_rec+1][PATH_MAX];
		strncpy(path[0], path0, PATH_MAX);
		DIR *dir[max_rec+1];
		//struct dirent *entry[max_rec];
		struct dirent *entry;
		int n = 0;

M1 : dir[n] = opendir(path[n]);
//		printf("opendir: %s\n", path[n]);
//M2 :     while ((entry[n] = readdir(dir[n])) != NULL || n+1 <= max_rec) {
M2 :     for (entry = readdir(dir[n]); entry != NULL && n+1 <= max_rec; entry = readdir(dir[n])) {
//M2 :     for (entry = readdir(dir[n]); entry != NULL; entry = readdir(dir[n])) {
//		 printf("new file or dir %s\n", entry -> d_name);
		 if(entry -> d_type == 4 && strcmp(entry -> d_name, ".") != 0 && strcmp(entry -> d_name, "..") != 0) {
//			 printf("n = %d and newdir: %s\n", n+1, entry -> d_name);
			 n++;
			 strncpy(path[n], path[n-1], PATH_MAX);
			 strcat(path[n], "/");
			 strncat(path[n], entry -> d_name, PATH_MAX);
			 printf("%s\n", path[n]);
			 goto M1;
		 }
		 else {
			 //printf("it's file, go next\n");
			 goto M2;
		 }
	 }

	 //printf("!!!");
	 closedir(dir[n]);
	 n--;
	 //printf("n--: %d\n", n);
		if(n >= 0) 
	//	 printf("M3");
		 goto M2;

return 0;
}
