#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>

int infinite_while(void);

/**
 * main - create zombies
 * Return: 0 success
 */
int main(void)
{
	int i = 0;
	pid_t pid;

	while (i < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			i++;
		}
		else
		{
			exit(0);
		}
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - inifinite loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
