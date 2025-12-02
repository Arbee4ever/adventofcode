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

int checkNum(int num[], int index, int elLen) {
	int check = 1;
	for (int i = 0; i < elLen; ++i) {
		if (num[index] != num[index+elLen]) check = 0;
		else check = 1;
		if (check == 0) break;
		index = index + 1;
	}
	return check;
}

int checkRepeated(int num[], int len) {
	int check = 0;
	for (int i = 1; i <= len/2; ++i) {
		if (len%i != 0) continue;
		for (int j = 0; j < len/i - 1; ++j) {
			check = checkNum(num, i*j, i);
			if (check == 0) break;
		}
		if (check == 1) break;
	}
	return check;
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
			//printf("Checking %ld\n", i);
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