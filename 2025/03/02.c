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
	long result = 0;
	FILE *fptr = fopen("input.txt", "r");
	if (fptr == NULL) {
		perror("File not found");
		return 1;
	}
	char *content = NULL;
	size_t len = 50;
	while (getline(&content, &len, fptr) != -1) {
		const int len = strlen(content);
		content = substr(content, 0, len - 1);
		long num = 0;
		int index = -1;
		for (int i = 0; i < 12; ++i) {
			int biggest = 0;
			for (int j = index + 1; j < len - (12 - i); ++j) {
				char *currentStr = substr(content, j, 1);
				int current = atoi(currentStr);
				free(currentStr);
				if (current > biggest) {
					biggest = current;
					index = j;
				}
			}
			num *= 10;
			num += biggest;
			biggest = 0;
		}
		printf("%s %ld\n", content, num);
		result += num;
	}
	printf("Result: %ld\n", result);
}
