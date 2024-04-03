import subprocess
import time
import subprocess
import time
import sys
import subprocess
import time
import subprocess
import time
import sys
def create_docker_cluster(container_prefix, image, network_name, num_nodes):
    # Create Docker cluster with the specified number of nodes
    for i in range(num_nodes):
        container_name = f"{container_prefix}_{i}"
        subprocess.run(["docker", "run", "-d", "--name", container_name, image])
        time.sleep(2)  # Wait for containers to start
    # Connect containers on the same network
    subprocess.run(["docker", "network", "create", network_name])
    for i in range(num_nodes):
        container_name = f"{container_prefix}_{i}"
        subprocess.run(["docker", "network", "connect", network_name, container_name])


def test_container_connection(container_prefix, command, num_nodes):
    # Test connection for each container
    for i in range(num_nodes):
        container_name = f"{container_prefix}_{i}"
        result = subprocess.run(["docker", "exec", container_name] + command, capture_output=True)

        output = result.stdout.decode()  # Decode the output
        with open("output.log", "a") as f:
            f.write(output)  # Write the output to the log file

def run_ycsb_workload(database_type, container_prefix, num_nodes):
    # Function to run YCSB workload on the specified database
    workload_types = ["workloada", "workloadb", "workloadc"]
    for workload in workload_types:
        for i in range(num_nodes):
            container_name = f"{container_prefix}_{i}"
            # Example YCSB command for MongoDB
            if database_type == "mongodb":
                ycsb_command = ["ycsb", "load", "mongodb", "-s", "-P", f"workloads/{workload}", "-p", f"mongodb.url=mongodb://{container_name}:27017/ycsb"]
            # Example YCSB command for Redis
            elif database_type == "redis":
                ycsb_command = ["ycsb", "load", "redis", "-s", "-P", f"workloads/{workload}", "-p", f"redis.host={container_name}", "-p", "redis.port=6379"]
            
            # Execute YCSB workload command
            subprocess.run(ycsb_command)
            time.sleep(5)  # Add a delay between workload executions

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <num_mongodb_nodes> <num_redis_nodes>")
        sys.exit(1)

    num_mongodb_nodes = int(sys.argv[1])
    num_redis_nodes = int(sys.argv[2])

    create_docker_cluster("mongodb_node", "mongo:latest", "mongodb_network", num_mongodb_nodes)
    create_docker_cluster("redis_node", "redis:latest", "redis_network", num_redis_nodes)
    
    # Test connection and execute commands for MongoDB nodes
    test_container_connection("mongodb_node", ["mongosh", "--eval", "'printjson(db.serverStatus())'"], num_mongodb_nodes)
    # Test connection and execute commands for Redis nodes
    test_container_connection("redis_node", ["redis-cli", "ping"], num_redis_nodes)

    # Run YCSB workload for MongoDB
    run_ycsb_workload("mongodb", "mongodb_node", num_mongodb_nodes)
    # Run YCSB workload for Redis
    run_ycsb_workload("redis", "redis_node", num_redis_nodes)
