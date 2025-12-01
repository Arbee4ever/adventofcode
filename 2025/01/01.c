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
	int current = 50;
	int count = 0;
	size_t len = 3;
	while (getline(&content, &len, fptr) != -1) {
		content = substr(content, 0, strcspn(content, "\r\n"));
		char *string = substr(content, 1, strcspn(content, "\r\n") - 1);
		switch (content[0]) {
			case 'L':
				current -= atoi(string);
				break;
			case 'R':
				current += atoi(string);
				break;
		}
		free(string);
		while (current < 0 || current > 99) {
			if (current > 99) {
				current -= 100;
			} else {
				current += 100;
			}
		}
		printf("The dial is rotated %s to point at %d.\n", content, current);
		if (current == 0) {
			count += 1;
		}
	};
	printf("Count: %d\n", count);
	return 0;
}
