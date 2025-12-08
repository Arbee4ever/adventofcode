#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
	int x;
	int y;
	int z;
} Junction;

typedef struct {
	int u;
	int v;
	double distance;
} Connection;

double calcDistance(const Junction a, const Junction b) {
	return sqrt(pow(a.x - b.x, 2.0) + pow(a.y - b.y, 2.0) + pow(a.z - b.z, 2.0));
}

int compareConnections(const void *a, const void *b) {
	const Connection *connectionA = (Connection *) a;
	const Connection *connectionB = (Connection *) b;
	return connectionA->distance < connectionB->distance ? -1 : 1;
}

int findRoot(int i, int *parent) {
	if (parent[i] == i)
		return i;
	parent[i] = findRoot(parent[i], parent);
	return parent[i];
}

void unionNetworks(int i, int j, int *parent) {
	int root_i = findRoot(i, parent);
	int root_j = findRoot(j, parent);
	if (root_i != root_j) {
		parent[root_i] = root_j;
	}
}

int main() {
	FILE *fptr = fopen("input.txt", "r");
	if (fptr == NULL) {
		perror("File not found");
		return 1;
	}

	char *content = NULL;
	size_t len = 0;
	int lineCount = 0;
	while (getline(&content, &len, fptr) != -1) {
		lineCount++;
	}
	rewind(fptr);

	Junction junctions[lineCount];
	const int connectionsCount = (lineCount * (lineCount - 1)) / 2;
	Connection *possibleConnections = malloc(connectionsCount * sizeof(Connection));
	if (possibleConnections == NULL) {
		perror("Memory allocation failed");
		free(content);
		fclose(fptr);
		return 1;
	}
	int count = 0;
	while (getline(&content, &len, fptr) != -1) {
		char *number = strtok(content, ",\n");
		junctions[count].x = atoi(number);
		number = strtok(NULL, ",\n");
		junctions[count].y = atoi(number);
		number = strtok(NULL, ",\n");
		junctions[count].z = atoi(number);
		count++;
	}

	count = 0;
	for (int i = 0; i < lineCount; ++i) {
		for (int j = i + 1; j < lineCount; ++j) {
			possibleConnections[count++] = (Connection){i, j, calcDistance(junctions[i], junctions[j])};
		}
	}
	qsort(possibleConnections, count, sizeof(possibleConnections[0]), compareConnections);

	int parents[lineCount];
	long result = 1;
	for (int i = 0; i < lineCount; i++) parents[i] = i;

	int networkCount = lineCount;
	for (int i = 0; i < count; ++i) {
		const Connection currConnection = possibleConnections[i];
		int rootU = findRoot(currConnection.u, parents);
		int rootV = findRoot(currConnection.v, parents);

		if (rootU != rootV) {
			unionNetworks(rootU, rootV, parents);
			networkCount--;
			if (networkCount == 1) {
				result *= (long) junctions[currConnection.u].x;
				result *= (long) junctions[currConnection.v].x;
				printf("%ld\n", result);
				break;
			}
		}
	}

	free(possibleConnections);
	free(content);
	fclose(fptr);
}