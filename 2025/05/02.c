#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *substr(char const *input, size_t start, size_t len) {
	char *ret = malloc(len + 1);
	memcpy(ret, input + start, len);
	ret[len] = '\0';
	return ret;
}

typedef struct {
	long start;
	long end;
} Range;

long getOverlap(const Range a, const Range b) {
	long overlap = 0;
	const long overlapStart = (a.start > b.start) ? a.start : b.start;
	const long overlapEnd = (a.end < b.end) ? a.end : b.end;
	overlap = overlapEnd - overlapStart + 1;
	return (overlap > 0) ? overlap : 0;
}

Range mergeRanges(const Range a, const Range b) {
	Range merged;
	merged.start = (a.start < b.start) ? a.start : b.start;
	merged.end = (a.end > b.end) ? a.end : b.end;
	return merged;
}

int compareRanges(const void *a, const void *b) {
	const Range *rangeA = (Range *) a;
	const Range *rangeB = (Range *) b;
	if (rangeA->start < rangeB->start) return -1;
	if (rangeA->start > rangeB->start) return 1;
	return 0;
}

int main() {
	const char *filename = "input.txt";
	FILE *fptr = fopen(filename, "r");
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
	Range ranges[freshLen];
	int count = 0;
	while (getline(&content, &len, fptr) != -1) {
		if (content[0] == '\n') break;
		char *rawRange = substr(content, 0, strcspn(content, "\n"));
		char *startC = substr(rawRange, 0, strcspn(rawRange, "-"));
		char *endC = substr(rawRange, strcspn(rawRange, "-") + 1, strlen(rawRange) - strlen(startC) - 1);
		Range range = {atol(startC), atol(endC)};
		free(rawRange);
		free(startC);
		free(endC);
		ranges[count] = range;
		count++;
	}
	qsort(ranges, freshLen, sizeof(ranges[0]), compareRanges);
	Range newRanges[freshLen];
	int amount = 0;
	newRanges[0] = ranges[0];
	for (int i = 0; i < freshLen; ++i) {
		const Range current = ranges[i];
		if (getOverlap(current, newRanges[amount]) > 0) {
			newRanges[amount] = mergeRanges(current, newRanges[amount]);
			printf("Merged: %ld-%ld and %ld-%ld\n", current.start, current.end, newRanges[amount].start, newRanges[amount].end);
		} else {
			amount++;
			newRanges[amount] = current;
		}
	}
	free(content);
	fclose(fptr);
	long result = 0;
	for (int i = 0; i < amount + 1; ++i) {
		result += newRanges[i].end - newRanges[i].start + 1;
	}
	printf("Size: %ld\n", sizeof(newRanges) / sizeof(newRanges[0]));
	printf("Result: %ld\n", result);
}
