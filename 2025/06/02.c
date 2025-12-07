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
	int numbers[5];
} Problem;

int main() {
	FILE *fptr = fopen("input.txt", "r");
	if (fptr == NULL) {
		perror("File not found");
		return 1;
	}
	char *content = NULL;
	size_t len = 0;
	int problemCount = 0;
	int numCount = 0;
	getline(&content, &len, fptr);
	char *number = strtok(content, " \n");
	while (number != NULL) {
		problemCount++;
		int numSize = strlen(number);
		if (numSize > numCount) {
			numCount = numSize;
		}
		number = strtok(NULL, " \n");
	}
	printf("Number count: %d\n", numCount);
	rewind(fptr);
	char lines[5][len] = {};
	int lineCount = 0;
	while (getline(&content, &len, fptr) != -1) {
		if (content[0] == '*' || content[0] == '+') break;
		memcpy(lines[lineCount], content, len);
		lineCount++;
	}
	Problem *problems = malloc((sizeof(Problem) + sizeof(int)) * problemCount + sizeof(int) * numCount);
	int currentProblem = 0;
	int currentNumber = 0;
	for (int i = 0; i < problemCount * numCount + problemCount; ++i) {
		int number = 0;
		for (int j = 0; j < lineCount; ++j) {
			if (i >= sizeof(lines[j]) / sizeof(lines[j][0])) continue;
			const char c = lines[j][i];
			if (isspace(c) || c == '\n' || !isdigit(c)) continue;
			number = number * 10 + (c - '0');
		}
		if (number == 0) {
			currentProblem = (currentProblem + 1) % problemCount;
			currentNumber = 0;
			continue;
		}
		Problem currProb = problems[currentProblem];
		currProb.numbers[currentNumber++] = number;
		problems[currentProblem] = currProb;
	}
	char *operation = strtok(content, " \n");
	int index = 0;
	while (operation != NULL) {
		problems[index].operation = operation[0];
		index++;
		operation = strtok(NULL, " \n");
	}
	rewind(fptr);
	long result = 0;
	for (int i = 0; i < problemCount; ++i) {
		Problem currProb = problems[i];
		printf("Problem %d:", i);
		switch (currProb.operation) {
			case '*': {
				long problemResult = 1;
				for (int j = 0; j < sizeof(currProb.numbers) / sizeof(currProb.numbers[0]); ++j) {
					if (currProb.numbers[j] == 0) continue;
					problemResult *= currProb.numbers[j];
					printf("*%d", currProb.numbers[j]);
				}
				printf(" = %ld\n", problemResult);
				result += problemResult;
				break;
			}
			case '+': {
				long problemResult = 0;
				for (int j = 0; j < sizeof(currProb.numbers) / sizeof(currProb.numbers[0]); ++j) {
					if (currProb.numbers[j] == 0) continue;
					problemResult += currProb.numbers[j];
					printf("+%d", currProb.numbers[j]);
				}
				printf(" = %ld\n", problemResult);
				result += problemResult;
				break;
			}
			default: printf("error\n");
		}
	}
	free(problems);
	fclose(fptr);
	printf("Result: %ld\n", result);
}
