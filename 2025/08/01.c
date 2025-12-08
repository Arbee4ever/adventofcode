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
	Junction junctions[2];
	double distance;
} Connection;

typedef struct {
	int size;
	Junction junctions[500];
} Network;

double calcDistance(const Junction a, const Junction b) {
	return round(sqrt(pow(a.x - b.x, 2.0) + pow(a.y - b.y, 2.0) + pow(a.z - b.z, 2.0)));
}

int compareConnections(const void *a, const void *b) {
	const Connection *connectionA = (Connection *) a;
	const Connection *connectionB = (Connection *) b;
	return connectionA->distance < connectionB->distance ? -1 : 1;
}

int compareNetworks(const void *a, const void *b) {
	const Network *networkA = (Network *) a;
	const Network *networkB = (Network *) b;
	return networkA->size > networkB->size ? -1 : 1;
}

int find(const Junction junction, const Network *network) {
	for (int i = 0; i < network->size; ++i) {
		if (network->junctions[i].x == junction.x && network->junctions[i].y == junction.y && network->junctions[i].z == junction.z) {
			return 1;
		}
	}
	return 0;
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
			if (junctions[i].x == junctions[j].x && junctions[i].y == junctions[j].y && junctions[i].z == junctions[j].
			    z)
				continue;
			possibleConnections[count] = (Connection){
				{junctions[i], junctions[j]}, calcDistance(junctions[i], junctions[j])
			};
			count++;
		}
	}
	qsort(possibleConnections, count, sizeof(possibleConnections[0]), compareConnections);

	Network networks[lineCount] = {};

	for (int i = 0; i <= 999; ++i) {
		const Connection currConnection = possibleConnections[i];
		int networkIdA = -1;
		int networkIdB = -1;
		for (int j = 0; j < lineCount; ++j) {
			const Network *currNetwork = &networks[j];
			if (currNetwork->size > 0) {
				if (networkIdA == -1 && find(currConnection.junctions[0], currNetwork)) {
					networkIdA = j;
				}
				if (networkIdB == -1 && find(currConnection.junctions[1], currNetwork)) {
					networkIdB = j;
				}
			}
		}
		if (networkIdA == -1 && networkIdB == -1) {
			for (int j = 0; j < lineCount; ++j) {
				if (networks[j].size == 0) {
					Network *currNetwork = &networks[j];
					currNetwork->junctions[0] = currConnection.junctions[0];
					currNetwork->junctions[1] = currConnection.junctions[1];
					currNetwork->size = 2;
					break;
				}
			}
		} else if (networkIdA != -1 && networkIdB == -1) {
			Network *currNetwork = &networks[networkIdA];
			currNetwork->junctions[currNetwork->size++] = currConnection.junctions[1];
		} else if (networkIdA == -1 && networkIdB != -1) {
			Network *currNetwork = &networks[networkIdB];
			currNetwork->junctions[currNetwork->size++] = currConnection.junctions[0];
		} else if (networkIdA != networkIdB) {
			Network *currNetworkA = &networks[networkIdA];
			Network *currNetworkB = &networks[networkIdB];
			for (int j = 0; j < currNetworkB->size; ++j) {
				currNetworkA->junctions[currNetworkA->size++] = currNetworkB->junctions[j];
			}
			currNetworkB->size = 0;
		}
	}

	qsort(networks, sizeof(networks) / sizeof(networks[0]), sizeof(networks[0]), compareNetworks);

	int result = 1;
	for (int i = 0; i < 3; ++i) {
		if (networks[i].size == 0) continue;
		result = result * networks[i].size;
	}
	printf("%d\n", result);

	free(possibleConnections);
	free(content);
	fclose(fptr);
}