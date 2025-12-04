#include <stdio.h>

int checkMatrix(int size, char matrix[size][size]) {
	int result = 0;
	char current = {};
	for (int i = 0; i < size*size; ++i) {
		const int x = i % size;
		const int y = i / size;
		current = matrix[y][x];
		if (matrix[y][x] == '@') {
			int localCount = 0;
			for (int j = 0; j < 9; ++j) {
				const int xLocal = (x-1)+j%3;
				const int yLocal = (y-1)+j/3;
				if (xLocal == x && yLocal == y) continue;
				if (xLocal < 0 || xLocal >= size || yLocal < 0 || yLocal >= size) continue;
				if (matrix[yLocal][xLocal] == '@') {
					localCount++;
				}
			}
			if (localCount < 4) {
				current = 'x';
				matrix[y][x] = '.';
				result++;
			}
		}
		if (x == size - 1) {
			printf("%c\n", current);
		} else {
			printf("%c", current);
		}
	}
	return result;
}

int main() {
	FILE *fptr = fopen("input.txt", "r");
	if (fptr == NULL) {
		perror("File not found");
		return 1;
	}
	char *content = NULL;
	size_t len = 50;
	const int size = getline(&content, &len, fptr) - 1;
	rewind(fptr);
	char matrix[size][size] = {};
	int x = 0;
	int y = 0;
	for (char c = getc(fptr); c != EOF; c = getc(fptr)) {
		if (c == '\n') {
			x = 0;
			y++;
		} else {
			matrix[y][x] = c;
			x++;
		}
	}
	int result = 0;
	int count = 0;
	while ((count = checkMatrix(size, matrix)) != 0) {
		result += count;
	}
	printf("%d", result);
}
