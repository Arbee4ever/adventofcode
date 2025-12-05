#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *substr(char const *input, size_t start, size_t len) {
	char *ret = malloc(len + 1);
	memcpy(ret, input + start, len);
	ret[len] = '\0';
	return ret;
}

int main() {
	FILE *fptr = fopen("input.txt", "r");
	if (fptr == NULL) {
		perror("File not found");
		return 1;
	}
	char *content = NULL;
	size_t len = 50;
	int freshLen = 0;
	while (getline(&content, &len, fptr) != -1) {
		if (content[0] == '\n') break;
		freshLen++;
	}
	rewind(fptr);
	char *fresh[freshLen] = {};
	int count = 0;
	while (getline(&content, &len, fptr) != -1) {
		if (content[0] == '\n') break;
		char* newContent = substr(content, 0, strcspn(content, "\n"));
		fresh[count] = newContent;
		count++;
		printf("%s\n", newContent);
	}
	int result = 0;
	while (getline(&content, &len, fptr) != -1) {
		long id = atol(content);
		//printf("ID: %ld\n", id);
		for (int i = 0; i < freshLen; ++i) {
			char* start = substr(fresh[i], 0, strcspn(fresh[i], "-"));
			char* end = substr(fresh[i], strcspn(fresh[i], "-") + 1, strlen(fresh[i]));
			long startLong = atol(start);
			long endLong = atol(end);
			free(start);
			free(end);
			//printf("%ld < %ld < %ld\n", startLong, id, endLong);
			if (id >= startLong && id <= endLong) {
				result++;
				break;
			}
		}
	}
	printf("Fresh: %d\n", result);
}
