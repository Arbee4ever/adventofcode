#include <ctype.h>
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
	char operation;
	int numbers[4];
} Problem;

int main() {
	FILE *fptr = fopen("input.txt", "r");
	if (fptr == NULL) {
		perror("File not found");
		return 1;
	}
	char *content = NULL;
	size_t len = 50;
	int problemCount = 0;
	char lastChar = -1;
	int numCount = 0;
	while (getline(&content, &len, fptr) != -1) {
		if (content[0] == '\n') break;
		numCount++;
	}
	numCount--;
	rewind(fptr);
	for (char c = getc(fptr); c != EOF; c = getc(fptr)) {
		if (c == '\n') break;
		if (lastChar == -1 || (isspace(lastChar) && !isspace(c))) {
			problemCount++;
			lastChar = c;
		} else {
			lastChar = c;
		}
	}
	rewind(fptr);
	Problem *problems = malloc(sizeof(Problem) * problemCount + sizeof(int) * numCount);
	int currentProblem = 0;
	int currentNum = 0;
	while (getline(&content, &len, fptr) != -1) {
		char *number = strtok(content, " \n");
		while (number != NULL) {
			Problem currProb = problems[currentProblem];
			if (number[0] == '*' || number[0] == '+') {
				char operation = number[0];
				currProb.operation = operation;
				problems[currentProblem] = currProb;
				currentProblem = (currentProblem + 1) % problemCount;
			} else {
				if (!atoi(number) > 0) continue;
				currProb.numbers[currentNum] = atoi(number);
				problems[currentProblem] = currProb;
				currentProblem = (currentProblem + 1) % problemCount;
				if (currentProblem == 0) {
					currentNum++;
				}
			}
			number = strtok(NULL, " \n");
		}
	}
	long result = 0;
	for (int i = 0; i < problemCount; ++i) {
		Problem currProb = problems[i];
		switch (currProb.operation) {
			case '*': {
				long problemResult = 1;
				for (int j = 0; j < sizeof(currProb.numbers) / sizeof(currProb.numbers[0]); ++j) {
					if (currProb.numbers[j] == 0) continue;
					problemResult *= currProb.numbers[j];
				}
				printf("Problem %d: %ld\n", i, problemResult);
				result += problemResult;
				break;
			}
			case '+': {
				long problemResult = 0;
				for (int j = 0; j < sizeof(currProb.numbers) / sizeof(currProb.numbers[0]); ++j) {
					if (currProb.numbers[j] == 0) continue;
					problemResult += currProb.numbers[j];
				}
				printf("Problem %d: %ld\n", i, problemResult);
				result += problemResult;
				break;
			}
			default: ;
		}
	}
	free(problems);
	fclose(fptr);
	printf("Result: %ld\n", result);
}
