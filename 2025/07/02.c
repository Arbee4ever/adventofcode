#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long long move(const int x, const int y, const int max, char lines[max][max], long long visited[max][max]) {
	if (y >= max) {
		return 1;
	}
	if (visited[y][x] != 0) {
		return visited[y][x];
	}
	const char current = lines[y][x];
	char* line = lines[y];
	printf("%d %d: %c %s\n", x+1, y+1, current, line);
	long long count = 0;
	if (lines[y][x] == '^') {
		count += move(x+1,y,max,lines,visited);
		count += move(x-1,y,max,lines,visited);
	} else {
		count = move(x,y+1,max,lines,visited);
	}
	visited[y][x] = count;
	return count;
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
	long long visited[lineCount][lineCount] = {};
	const long long result = move(lineCount/2-1,0,lineCount,lines,visited);
	printf("%lld\n", result);
	free(content);
	fclose(fptr);
}