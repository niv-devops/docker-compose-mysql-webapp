# Docker Compose - Flask & MySQL WebAPP

A Docker Compose Web Application with MySQL and Flask, Initializing SQL `office` database with `employees` table and a Flask webapp to fetch and display the data.
Both services run as non-root users.

# Table of Contents
1. [Prerequisites](#prerequisites)
2. [Getting Started](#getting-started)
3. [Features](#features)
4. [Stopping the Application](#stopping-the-application)
5. [Troubleshooting & Managing the SQL Database](#troubleshooting--managing-the-sql-database)
6. [Run on K8s Locally Using Minikube](#run-on-k8s-locally-using-minikube)

## Prerequisites
- [Docker & Docker Compose](https://docs.docker.com/engine/install/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/?arch=%2Flinux%2Fx86-64%2Fstable%2Fbinary+download)

## Getting Started

1. **Clone the repository:**

   ```bash
    git clone https://github.com/niv-devops/docker-compose-mysql-webapp.git
    cd docker-compose-mysql-webapp
    ```

2. **Create or edit `.env` file in the project's root path** with the following:

    ```
    MYSQL_ROOT_PASSWORD=<your-root-password>
    MYSQL_USER=<non-root-user>
    MYSQL_PASSWORD=<non-root-password>
    MYSQL_DATABASE=office
    ```

3. **Build and start the services** using Docker Compose:

    ```bash
    docker compose up -d
    ```

4. **Access the Flask web application** in your browser at:

    ```
    http://localhost:5000
    ```

## Features

An overview on the project's components and dependencies:

1. **Database initialization** - The SQL DB container runs with SQL script `init-db/init.sql` to create the table:

   | ID | Name     | Role                          |
   | -- | -------- | ----------------------------- |
   | 1  | Michael  | Regional Manager              |
   | 2  | Jim      | Sales Representative          |
   | 3  | Dwight   | Assistant to Regional Manager |
   | 4  | Toby     | HR                            |

2. **Web Application** - Python application that uses 2 libraries: 
   [Flask](https://pypi.org/project/Flask/) and [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)

## Stopping the Application

To stop the services, run:

```bash
docker compose down
```

## Troubleshooting & Managing the SQL Database

To view and alter users and databases, start with the following commands:

```bash
docker exec -it db bash  # Enter the MySQL container
mysql -u root -p         # Login to MySQL as root
SELECT User, Host FROM mysql.user;  # List MySQL users
USE office;              # Switch to the 'office' database
SELECT * FROM employees;  # View data in the employees table
```

## Run on K8's Locally Using Minikube

To run this project with Kubernetes locally in Minikube cluster, follow these steps:

1. **Start Minikube and configure it to use Docker daemon:**

   ```bash
    minikube start
    eval $(minikube docker-env)
    ```

2. **Create or edit secret.yaml** so that it will match `.env` file, values in base64:

    ```
    echo -n "example" | base64
    echo "ZXhhbXBsZQ==" | base64 -d # To decode the text
    ```

3. **Apply all K8's manifest files**:

    ```bash
    kubectl apply -f ./k8s/
    ```

4. **Check the resources status:**:

    ```
    kubectl get po
    kubectl get svc
    kubectl get secret
    kubectl get cm
    ```

5. **Obtain the IP address and access the application** in your browser at:

    ```
    minikube ip
    http://<your-minikube-ip>:30001
    ```
