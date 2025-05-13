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
#include <linux/limits.h>
#include <dirent.h>
#include <libconfig.h>

//config default constants
const char* DEFAULT_CFG_DIRLOCATE = "/usr/bin";
const int   DEFAULT_CFG_TIMECHECK = 100;
/* config values */
char cfg_dirlocate[PATH_MAX];
int  cfg_timecheck;
//constant for deep recursiion. better move it to config file
int max_rec = 50;

void read_cfg(); 

void signal_handler(int sig);

void checkdir(char *path0);

void checkdirrec(char *path0);

void demonisation();

int main()
{
	// set defaults and read config	
	strncpy(cfg_dirlocate, DEFAULT_CFG_DIRLOCATE, PATH_MAX);
	cfg_timecheck = DEFAULT_CFG_TIMECHECK;
	read_cfg(); //read config
	
	printf("Daemon was started with next parameters:\n");
	printf("timecheck = %i\n", cfg_timecheck);
	printf("dirlocate = %s\n", cfg_dirlocate);

	openlog("checkdird", LOG_ODELAY, LOG_DAEMON);
	//catch the specific signals
	signal(SIGHUP, signal_handler);
	signal(SIGTERM, signal_handler);

	demonisation();
	//main work cycle
	while (1) {
		checkdirrec(cfg_dirlocate); //main function, checkdir() - without recursion, checkdirrec() with one; better make flags for config file
		sleep(cfg_timecheck); //timeout before next check
	}
}

//function for read config
void read_cfg() {
	char config_file[PATH_MAX] = "/etc/daemon.cfg";
	config_t cfg;
	
	config_init(&cfg);
	
	//config read check
	if(config_read_file(&cfg, config_file) != CONFIG_TRUE) {
		printf("Read config error\n");
		config_error_text(&cfg);
		config_error_line(&cfg);
	}

	//write dirlocate
	const char *tmp_string;
	if(config_lookup_string(&cfg, "dirlocate", &tmp_string) == CONFIG_TRUE) {
		strncpy(cfg_dirlocate, tmp_string, PATH_MAX);
	}
	else {
		printf("Error lookup dirlocate!\n");
		strncpy(cfg_dirlocate, DEFAULT_CFG_DIRLOCATE, PATH_MAX);
	}

	//write timecheck
	if(config_lookup_int(&cfg, "timecheck", &cfg_timecheck) == CONFIG_TRUE); 	
	else {
		printf("Error lookup timecheck!\n");
	}

	config_destroy(&cfg);

}

//function for correct catch signals from "kill"
void signal_handler(int sig)	{
	switch (sig) {
	case SIGHUP:
	syslog(LOG_INFO, "sighup signal catched: reread config file");
	read_cfg();
	break;
	case SIGTERM:
	syslog(LOG_INFO, "terminate signal catched");
	exit(0);
	break;
	closelog();
	}
}	

//easily check directory
void checkdir(char *path0) {
	char path[PATH_MAX];
	strncpy(path, path0, PATH_MAX);
	DIR *dir;
	struct dirent *entry;

	char *date;
	int ret;
	struct stat buf;


	dir = opendir(path0);
	while( ( entry = readdir(dir) ) != NULL) {
		if( strcmp(entry -> d_name, ".") != 0 && strcmp(entry -> d_name, "..") != 0 ) {
			strcat(path, "/");
			strncat(path, entry -> d_name, PATH_MAX);
			if ((ret = stat(path, &buf)) != 0)
			{
				syslog(LOG_INFO, "Stat failyre error");
				abort();
			}
			date = asctime(localtime(&buf.st_ctime));
			time_t now = time(0);
			if (now - cfg_timecheck <= buf.st_ctime) {
				syslog(LOG_INFO, path);
			}
			strncpy(path, path0, PATH_MAX);
		}
	}
	closedir(dir);
}

//check directory recursive
void checkdirrec(char *path0) {
	char path[max_rec+1][PATH_MAX];
	strncpy(path[0], path0, PATH_MAX);
	DIR *dir[max_rec+1];
	struct dirent *entry;
	int n = 0;
	checkdir(path[0]);

M1 : dir[n] = opendir(path[n]);
M2 :     for (entry = readdir(dir[n]); entry != NULL && n+1 <= max_rec; entry = readdir(dir[n])) {
		 if(entry -> d_type == 4 && strcmp(entry -> d_name, ".") != 0 && strcmp(entry -> d_name, "..") != 0) {
			 n++;
			 strncpy(path[n], path[n-1], PATH_MAX);
			 strcat(path[n], "/");
			 strncat(path[n], entry -> d_name, PATH_MAX);
			 checkdir(path[n]);
			 goto M1;
		 }
		 else 
			 goto M2;
	 }
	 closedir(dir[n]);
	 n--;
	 if(n >= 0)
		goto M2; 
}

//function for make daemon in the system
void demonisation() {
	pid_t pid, sid;
	//fork from parent process
	pid = fork();
	if (pid < 0) {
		// fix the error
		syslog(LOG_INFO, "Error on fork");
		printf("Error on fork()\n");
		exit(EXIT_FAILURE);
	}	
	//close the parent process if success
	if (pid > 0) {
		exit (EXIT_SUCCESS);
	}
	//change file mask
	umask (0);
	
	//make new sid for child process
	sid = setsid();
	if (sid < 0) {
	//logging any error
		syslog(LOG_INFO, "Error in SETSID");
		exit(EXIT_FAILURE);
	}
	
	//change directory to work one 
	if ((chdir ("/")) < 0) {
	//log error
		syslog(LOG_INFO, "Error in CHDIR");
		exit(EXIT_FAILURE);
	}
	
	//closing standart descriptors
	close(STDIN_FILENO);
	close(STDOUT_FILENO);
	close(STDERR_FILENO);


//	syslog(LOG_INFO, "Daemon is working");
}
