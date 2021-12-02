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

    fp = fopen("Day2ex.txt", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    while ((read = getline(&line, &len, fp)) != -1) {
        printf("DISTANCE: %d DEPTH: %d \n", t_distance, t_depth);
        printf("%s", line);


        if (strstr(line, "forward") != NULL) {
            char* command;
            int distance;
            sscanf(line,"%s %d",&command,&distance);
            printf("%d \n", distance);
            t_distance += distance;

        }

        if (strstr(line, "down") != NULL) {
            char* command;
            int distance;
            sscanf(line,"%s %d",&command,&distance);
            printf("%d \n", distance);
            t_depth += distance;
        }

        if (strstr(line, "up") != NULL) {
            char* command;
            int distance;
            sscanf(line,"%s %d",&command,&distance);
            printf("%d \n", distance);
            t_depth += -1 * distance;
        }

    }

    fclose(fp);
    if (line)
        free(line);

    printf("total: %d \n", t_depth * t_distance);

    return(0);

}
