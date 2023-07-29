#include <stdio.h>
#include <unistd.h>

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
		if (pid != 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			infinite_while();
		}
		i++;
	}
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
