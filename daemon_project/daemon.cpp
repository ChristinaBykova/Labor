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
	else {
	//	printf("Read config success\n");
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
 
int main()
{
	// set defaults and read config	
	strncpy(cfg_dirlocate, DEFAULT_CFG_DIRLOCATE, PATH_MAX);
	cfg_timecheck = DEFAULT_CFG_TIMECHECK;
	read_cfg(); //read config
	
	printf("daemon was started with next parameters:\n");
	printf("timecheck = %i\n", cfg_timecheck);
	printf("dirlocate = %s\n", cfg_dirlocate);


	openlog("checkdir.d", LOG_ODELAY, LOG_DAEMON);
	//catch the specific signals
	signal(SIGHUP, signal_handler);
	signal(SIGTERM, signal_handler);

	
	//demonisation
	pid_t pid, sid;
	/* ответвление от родительского процесса*/
	pid = fork();
	if (pid < 0) {
		// фиксируем ошибку
		syslog(LOG_INFO, "Error on fork");
		printf("Error on fork()\n");
		exit(EXIT_FAILURE);
	}	
	//если получилось, то родительский процесс закрываем
	if (pid > 0) {
		exit (EXIT_SUCCESS);
	}
	//изменяем файловую маску
	umask (0);
	
	//создание нового SID для дочернего процесса
	sid = setsid();
	if (sid < 0) {
	//журналируем любые сбои
		syslog(LOG_INFO, "Error in SETSID");
		exit(EXIT_FAILURE);
	}
	
	//изменяем текущий каталог (рабочий каталог)
	if ((chdir ("/")) < 0) {
	//журналируем сбой
		syslog(LOG_INFO, "Error in CHDIR");
		exit(EXIT_FAILURE);
	}
	
	//закрываем стандартные дескрипторы
	close(STDIN_FILENO);
	close(STDOUT_FILENO);
	close(STDERR_FILENO);

	//основной рабочий цикл
	while (1) {
		char path[PATH_MAX];
		strncpy(path, cfg_dirlocate, PATH_MAX);
		DIR *dir;
		struct dirent *entry;

		char *date;
		int ret;
		struct stat buf;

		dir = opendir(cfg_dirlocate);
		while( ( entry = readdir(dir) ) != NULL ) {
			strcat(path, "/");
			strncat(path, entry -> d_name, PATH_MAX);
			if ((ret = stat(path, &buf)) != 0)
			{
				//fprintf(stderr, "stat failure error .%d", ret);
				syslog(LOG_INFO, "Stat failyre error");
				abort();
			}
			date = asctime(localtime(&buf.st_ctime));
			time_t now = time(0);
			if (now - cfg_timecheck <= buf.st_ctime) {
				//printf("%s %s",path, date);
				syslog(LOG_INFO, path);
			}
			strncpy(path, cfg_dirlocate, PATH_MAX);
		}
		closedir(dir);
	sleep(cfg_timecheck); //выжидание перед повторной операцией
	}
}
