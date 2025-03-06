pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = "mtalal12/mlopsa1" 
        DOCKER_CREDENTIALS_ID = "96eb60ee-95d2-4b2a-b26c-73c8f5ebc362"  
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'dev', url: 'https://github.com/mtalal517/MLOPS-A1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script 
                {
                    bat "docker build -t ${DOCKER_HUB_REPO}:latest ."
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS_ID}", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        bat "echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin"
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    bat "docker push ${DOCKER_HUB_REPO}:latest"
                }
            }
        }

        stage('Cleanup') {
            steps {
            script {
            // Stop and remove any running containers using the image
            bat 'docker ps -q --filter ancestor=${DOCKER_HUB_REPO}:latest | for /f %i in (\'more\') do docker stop %i'
            bat 'docker ps -aq --filter ancestor=${DOCKER_HUB_REPO}:latest | for /f %i in (\'more\') do docker rm %i'

            // Remove the image forcefully
            bat "docker rmi -f ${DOCKER_HUB_REPO}:latest"
        }

            }
        }
    }
}
