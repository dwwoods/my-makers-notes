# AWS Deployment Guide: From Flask to Live App

This guide provides a step-by-step walkthrough for deploying a Python Flask application to the AWS cloud. We will start by packaging the app with Docker, then launch it on a cloud server (EC2), automate the deployment, and finally connect it to a managed database (RDS).

## Phase 1: Containerizing Your Flask App with Docker

Summary: Before we can run our app in the cloud, we must package it and all its dependencies into a self-contained, portable unit. We use Docker to create this package, which is called a "container image."

### Step 1: Get Your Flask App

You can either build a simple "Hello, world!" Flask app or use the pre-made version by cloning the repository:

```bash
git clone [https://github.com/makersacademy/cloud-deployment.git](https://github.com/makersacademy/cloud-deployment.git)
cd cloud-deployment/codebases/simple_server
```

Your app should have an app.py file and a requirements.txt file.

### Step 2: Make the App "Container-Ready"

A container is isolated from its host. We must tell Flask to listen for connections from outside its own isolated environment.

Open app.py and ensure the app.run block is updated to listen on host="0.0.0.0" and on the correct port.

```bash
if __name__ == '__main__':
    app.run(
        debug=True,
        port=5001,
        host="0.0.0.0"  # Listen for connections from outside the container
    )
```

Crucial: The 0.0.0.0 host is essential for the container to be reachable. Our AWS security rules will be configured to expect port 5001, so ensure this port is used.

### Step 3: Write the Dockerfile

The Dockerfile is a text file with instructions for Docker to build your image. Create a file named Dockerfile (with no extension) in the same directory:

```python
# Start from an official Python 3.11 base image
FROM python:3.11

# Copy all files from the current directory into the /app directory in the container
COPY . /app

# Set the working directory inside the container to /app
WORKDIR /app

# Install the app's Python dependencies
RUN pip install -r requirements.txt

# Define the command that will run when the container starts
CMD ["python", "app.py"]
```

### Step 4: Build and Run the Container Locally

Now, you can build the image and run it on your own machine to test it.

Build the image: The -t flag "tags" your image with a name.

```bash
docker build -t my-flask-app .
```

Run the container: The -p 5001:5001 flag "publishes" the container's internal port 5001 to your local machine's port 5001.

```bash
docker run -p 5001:5001 my-flask-app
```

You should now be able to visit <http://localhost:5001> in your browser and see your app running.

Summary: Why This Matters

You have successfully packaged your entire application into a single, reliable unit. This "container" will run exactly the same way on your machine, a teammate's machine, or a server in the cloud, eliminating "it works on my machine" problems.

## Phase 2: Launching Your Container on an AWS EC2 Server

Summary: Now that we have a container image, we need a server in the cloud to run it. We will use AWS EC2 (Elastic Compute Cloud) to launch a virtual server, install Docker on it, and run our container, making it accessible to the world.

### Step 1: Launch Your EC2 Instance

Log in to the AWS Console and navigate to the EC2 service.

Ensure your region is set to Europe (London) eu-west-2 (top-right corner).

Click the Launch instances button.

Name: Give it a clear name, e.g., cloud_deployment_your_name.

Tags: Click Add additional tags, then Add new tag. Set the key to Owner and the value to your AWS username. This is critical for permissions.

Application and OS Images: Select Amazon Linux (the default is fine).

Instance Type: Select t3.micro (this is free-tier eligible).

Key pair (login):

Click Create new key pair.

Name it <yourname>_cloud_deployment.

This will download a <yourname>_cloud_deployment.pem file. Keep this file safe; it is your password.

Move this file to your secure .ssh directory:

```bash
mv ~/Downloads/<yourname>_cloud_deployment.pem ~/.ssh/
```

Network Settings:

Click Edit.

Choose Select existing security group.

Find and select CloudDeploymentSecurityGroup. (This group has been pre-configured to allow SSH on port 22 and HTTP on port 5001).

Launch Instance: Click the Launch Instance button.

After a moment, your instance will be running. Click its Instance ID and find its Public IPv4 address (it will look like 18.133.229.223).

### Step 2: Connect to Your Instance (SSH)

Use the .pem key file to securely connect to your new server.

Set key permissions (one-time step):

```bash
chmod 400 ~/.ssh/<yourname>_cloud_deployment.pem
```

Connect via SSH:

```bash
ssh -i ~/.ssh/<yourname>_cloud_deployment.pem ec2-user@<your-ec2-ip>
```

You are now logged into your cloud server!

### Step 3: Install Docker on the EC2 Instance

Your new server is a blank slate. We need to install Docker on it.

```bash
# Update software packages
sudo dnf update -y

# Install Docker
sudo dnf install docker -y

# Start the Docker service
sudo systemctl start docker

# Add your 'ec2-user' to the 'docker' group to run Docker without 'sudo'
sudo usermod -aG docker ec2-user

# Apply the new group membership
newgrp docker
```

To verify, log out (exit) and log back in. Running docker ps should now work without sudo.

### Step 4: Copy Your App Files to the Instance

Open a new terminal tab on your local machine. First, connect to your instance and create a directory for your app files.

```bash
ssh -i ~/.ssh/<yourname>_cloud_deployment.pem ec2-user@<your-ec2-ip> "mkdir -p ~/flask-app"
```

Now, from your local machine, navigate to your app's directory and use `scp` (secure copy) to upload your files to the server.

```bash
scp -i ~/.ssh/<yourname>_cloud_deployment.pem app.py requirements.txt Dockerfile ec2-user@<your-ec2-ip>:~/flask-app/
```

This copies your app files into the `flask-app` directory on the server.

### Step 5: Build and Run the Container on EC2

Go back to your SSH terminal (connected to the EC2 instance).

Navigate to your app directory:

```bash
cd flask-app
ls # You should see your files
```

Build the image (just like you did locally):

```bash
docker build -t my-flask-app .
```

Run the container:

```bash
docker run -p 5001:5001 my-flask-app
```

You should see the familiar Flask output. Now, open your browser and go to: http://<your-ec2-ip>:5001

Your app is live on the internet!

Summary: Why This Matters

You have completed a full, manual deployment. You've seen all the individual parts: a cloud server (EC2), secure access (SSH), file transfer (SCP), and container runtime (Docker). Understanding this manual process is the foundation for automating it.

## Phase 3: Automating Deployment with a Bash Script

Summary: Manually logging in, copying files, and running commands is slow, repetitive, and a common source of errors. We can write a "deployment script" on our local machine to perform all these steps with a single command.

Step 1: Make a Change to Your App

On your local machine, edit app.py to change the "Hello, world!" message to "Hello, from my automated deployment!"

Step 2: Create the Deployment Script

On your local machine, create a file named deploy.sh. This script will automate the file upload and the SSH commands.

Important: Change the EC2_HOST variable to match your server's IP address.

```bash
#!/bin/bash
set -e # Exit immediately if a command exits with a non-zero status.

# --- VARIABLES ---
# Path to your private key
KEY_PATH=~/.ssh/<yourname>_cloud_deployment.pem
# Your EC2 instance's IP
EC2_HOST=ec2-user@<your-ec2-ip>
# The directory on the server where the app will live
REMOTE_DIR=/home/ec2-user/flask-app

# --- SCRIPT ---
echo "> Uploading files to EC2..."
scp -i $KEY_PATH app.py requirements.txt Dockerfile $EC2_HOST:$REMOTE_DIR

echo "> Deploying new version..."
# This 'Here Document' (<< EOF) streams all commands inside it
# to the remote server over SSH.
ssh -i $KEY_PATH $EC2_HOST << EOF
  set -e
  cd $REMOTE_DIR
  
  echo "Building new Docker image..."
  docker build -t my-flask-app:latest .
  
  echo "Stopping and removing old container..."
  # The '|| true' part ensures the script doesn't fail if the container isn't running
  docker stop my-flask-app || true
  docker rm my-flask-app || true
  
  echo "Running new container..."
  # -d runs the container in 'detached' (background) mode
  # --name gives the container a predictable name for easy management
  docker run -d -p 5001:5001 --name my-flask-app my-flask-app:latest
EOF

echo "✅ Deployment complete! Visit: http://<your-ec2-ip>:5001"
```

### Step 3: Run the Script

Make the script executable (one-time step):

```bash
chmod +x deploy.sh
```

Run the script:

```bash
./deploy.sh
```

Wait for the script to finish, then refresh your browser at http://<your-ec2-ip>:5001. You should see your updated message!

Summary: Why This Matters

You have just created a simple, repeatable deployment process. This is the first step toward CI/CD (Continuous Integration / Continuous Deployment). This single script dramatically reduces the risk of human error and makes updating your app trivial.

## Phase 4: Connecting a Production Database with AWS RDS

Summary: Our simple app is live, but most real-world applications need a database. Running a database in a container on EC2 is risky (you could lose all your data). The best practice is to use a managed database service. We will use AWS RDS (Relational Database Service) to create a PostgreSQL database and deploy a new app that connects to it.

This phase uses the app in the codebases/message_server directory.

###  Step 1: Create the PostgreSQL RDS Instance

In the AWS Console, navigate to the RDS service.

Click Create database.

Choose Standard Create and PostgreSQL as the engine.

Templates: Select Dev/Test (this is cheaper).

DB instance identifier: Give it a unique name, e.g., <yourname>-message-server-db.

Master username: postgres

Master password: Create a secure password and save it in a password manager.

Instance configuration: Select Burstable classes and db.t3.micro (free-tier eligible).

Storage autoscaling: Deselect (un-check) this to avoid unexpected costs.

Connectivity: In the "VPC security group" section, click "Choose existing" and add the `CloudDeploymentSecurityGroup`. This is a critical step that allows your EC2 instance (which uses this security group) to communicate with the database.

Click Create database.

This will take 5-10 minutes. When it's ready, click on the database and find its Endpoint. It will look like: <yourname>-app-db.c7c1sxjytrnm.eu-west-2.rds.amazonaws.com.

### Step 2: Create the Deployment Script for the New App

This deployment is more complex. We need to securely pass our database password and endpoint to the application without writing them directly into our code. We do this using Environment Variables (the -e flags in the docker run command).

On your local machine, go to the codebases/message_server directory and create a new deploy.sh:

```bash
#!/bin/bash
set -e

# --- VARIABLES ---
KEY_PATH=~/.ssh/<yourname>_cloud_deployment.pem
EC2_HOST=ec2-user@<your-ec2-ip>
REMOTE_DIR=/home/ec2-user/message-server

# --- !! SECRETS (Replace these) !! ---
YOUR_RDS_PASSWORD="<your_rds_password>"
YOUR_RDS_ENDPOINT="<your_rds_endpoint>"

# --- SCRIPT ---
echo "> Uploading files to EC2..."
# Note: We are now in the message_server directory
scp -i $KEY_PATH app.py requirements.txt Dockerfile $EC2_HOST:$REMOTE_DIR

echo "> Deploying new MESSAGE-SERVER app..."
ssh -i $KEY_PATH $EC2_HOST << EOF
  set -e
  cd $REMOTE_DIR
  
  docker build -t message-server:latest .
  
  docker stop message-server || true # Ignore error if not running
  docker rm message-server || true   # Ignore error if not existing
  
  echo "Running new message-server container..."
  # This app runs on port 5002
  docker run -d -p 5002:5002 \
    --name message-server \
    -e APP_ENV=PRODUCTION \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_PASSWORD=$YOUR_RDS_PASSWORD \
    -e POSTGRES_HOST=$YOUR_RDS_ENDPOINT \
    -e POSTGRES_DB=postgres \
    message-server:latest
EOF

echo "✅ Deployment complete! Visit: http://<your-ec2-ip>:5002"
```

###  Step 3: Deploy the Database-Connected App

Fill in the variables: Edit the new deploy.sh script and replace the <...> placeholders with your real RDS password and endpoint.

Make it executable: chmod +x deploy.sh

Run the script: ./deploy.sh

This script will:

Upload the new app's files.

Build the message-server image.

Run the container, injecting your database credentials as environment variables.

The app will run on port 5002 (our security group must also allow this port).

Visit http://<your-ec2-ip>:5002 to see your new, database-driven message app!

Summary: Why This Matters

You have now built a production-grade architecture. Your application (EC2) is separate from your stateful data (RDS). This is secure, scalable, and robust. You are passing sensitive credentials securely using environment variables, a fundamental best practice.

## Guide Summary

Congratulations! You have successfully:

Packaged a Flask app using Docker.

Launched a cloud server on AWS EC2.

Manually deployed your Docker container to the server.

Automated your deployment process with a bash script.

Provisioned a managed PostgreSQL database with RDS.

Deployed a second, stateful application that securely connects to your database.
