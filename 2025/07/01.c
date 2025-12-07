#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int move(const int x, const int y, int max, char lines[max][max], int visited[max][max]) {
	if (y >= max) {
		return 0;
	}
	if (visited[y][x] == 1) {
		return 0;
	}
	visited[y][x] = 1;
	char current = lines[y][x];
	char* line = lines[y];
	printf("%d %d: %c %s\n", x+1, y+1, current, line);
	if (lines[y][x] == '^') {
		return 1 + move(x+1,y,max,lines,visited) + move(x-1,y,max,lines,visited);
	}
	return move(x,y+1,max,lines,visited);
}

int main() {
	FILE *fptr = fopen("input.txt", "r");
	if (fptr == NULL) {
		perror("File not found");
		return 1;
	}

	char *content = NULL;
	size_t len = 0;
	int lineCount = 0;
	while (getline(&content, &len, fptr) != -1) {
		lineCount++;
	}
	rewind(fptr);
	char lines[lineCount][lineCount] = {};
	int i = 0;
	while (getline(&content, &len, fptr) != -1) {
		memcpy(lines[i], content, lineCount-1);
		i++;
	}
	int visited[lineCount][lineCount] = {};
	const int result = move(lineCount/2-1,0,lineCount,lines,visited);
	printf("%d\n", result);
	free(content);
	fclose(fptr);
}