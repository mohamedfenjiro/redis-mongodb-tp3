# Dockerized MongoDB and Redis Cluster Configuration and Testing

This Python script provides functionality to set up and test MongoDB and Redis clusters using Docker containers. The script allows you to specify the number of nodes in each cluster and performs basic connectivity tests.

## Prerequisites

Before running the script, ensure that you have the following installed:

- Docker: [Installation guide](https://docs.docker.com/get-docker/)
- Python 3.x

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/your-repo.git
```

2. Navigate to the directory containing the script:

```bash
cd your-repo
```

3. Modify the script if necessary to adjust the number of nodes in the MongoDB and Redis clusters:

```python
num_mongodb_nodes = 3
num_redis_nodes = 5
```

4. Run the Python script:

```bash
python setup_clusters.py
```

5. The script will create Docker containers for MongoDB and Redis clusters with the specified number of nodes. It will then test the connectivity to each node in the clusters.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This script was inspired by the need to easily set up and test MongoDB and Redis clusters for distributed database comparison experiments.

---
