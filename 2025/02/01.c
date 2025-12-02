#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *substr(char const *input, size_t start, size_t len) {
	char *ret = malloc(len + 1);
	memcpy(ret, input + start, len);
	ret[len] = '\0';
	return ret;
}

int numPlaces (long n) {
	if (n < 0) return numPlaces ((n == LONG_MIN) ? LONG_MAX: -n);
	if (n < 10) return 1;
	return 1 + numPlaces (n / 10);
}

int checkRepeated(int num[], int len) {
	if (len%2 != 0) {
		return 0;
	}
	int *firstHalf = num;
	int *secondHalf = num + len / 2;
	for (int i = 0; i < len/2; ++i) {
		if (firstHalf[i] != secondHalf[i]) {
			return 0;
		}
	}
	return 1;
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
	while (getdelim(&content, &len, 44, fptr) != -1) {
		content = substr(content, 0, strcspn(content, ","));
		const int minus = strcspn(content, "-");
		char *first = substr(content, 0, minus);
		char *second = substr(content, minus + 1, len - minus - 1);
		printf("%s - %s\n", first, second);
		for (long i = atol(first); i <= atol(second); i++) {
			long num = i;
			const int len = numPlaces(i);
			int arr[len];
			for (int j = len-1; j >= 0; j--) {
				arr[j] = num % 10;
				num = num / 10;
			}
			const int arrLen = sizeof(arr) / sizeof(arr[0]);
			const int repeated = checkRepeated(arr, arrLen);
			if (repeated) {
				printf("Repeated: %ld\n", i);
				result += i;
			}
		}
		free(first);
		free(second);
	}
	printf("Result: %ld\n", result);
}