#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

    int t_distance = 0;
    int t_depth = 0;
    int t_aim = 0;

    fp = fopen("puzzleinputs/Day2.txt", "r");

    while ((read = getline(&line, &len, fp)) != -1) {

        if (strstr(line, "forward") != NULL) {
            char* command;
            int distance;
            sscanf(line,"%s %d",&command,&distance);
            printf("%d \n", distance);
            t_distance += distance;
            t_depth += distance * t_aim;

        }

        if (strstr(line, "down") != NULL) {
            char* command;
            int distance;
            sscanf(line,"%s %d",&command,&distance);
            printf("%d \n", distance);
            t_aim += distance;
        }

        if (strstr(line, "up") != NULL) {
            char* command;
            int distance;
            sscanf(line,"%s %d",&command,&distance);
            printf("%d \n", distance);
            t_aim += -1 * distance;
        }

    }

    // Clean up mems
    fclose(fp);
    if (line)
        free(line);

    printf("Total: %d \n", t_depth * t_distance);

    return(0);

}
