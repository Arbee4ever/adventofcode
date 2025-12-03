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
	int result = 0;
	FILE *fptr = fopen("input.txt", "r");
	if (fptr == NULL) {
		perror("File not found");
		return 1;
	}
	char *content = NULL;
	size_t len = 50;
	while (getline(&content, &len, fptr) != -1) {
		const int len = strlen(content);
		int first = 0;
		int second = 0;
		int firstIndex = 0;
		for (int i = 0; i < len - 2; ++i) {
			char *current = substr(content, i, 1);
			if (atoi(current) > first) {
				first = atoi(current);
				firstIndex = i;
			}
		}
		for (int i = firstIndex + 1; i < len; ++i) {
			char *current = substr(content, i, 1);
			if (first * 10 + atoi(current) > first * 10 + second) {
				second = atoi(current);
			}
			free(current);
		}
		printf("%s %d\n", content, first * 10 + second);
		result += first * 10 + second;
	}
	printf("Result: %d\n", result);
}
