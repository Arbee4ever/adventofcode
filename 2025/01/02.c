#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *substr(char const *input, size_t start, size_t len) {
	char *ret = malloc(len + 1);
	memcpy(ret, input + start, len);
	ret[len] = '\0';
	return ret;
}

int wrap(int n) {
	if (n > 99) {
		n -= 100;
	} else if (n < 0) {
		n += 100;
	}
	return n;
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
				for (int i = 0; i < atoi(string); ++i) {
					current = wrap(current - 1);
					if (current == 0) {
						count += 1;
					}
				}
				break;
			case 'R':
				for (int i = 0; i < atoi(string); ++i) {
					current = wrap(current + 1);
					if (current == 0) {
						count += 1;
					}
				}
				break;
		}
		free(string);
		printf("The dial is rotated %s to point at %d\n", content, current);
	};
	printf("Count: %d\n", count);
	return 0;
}
