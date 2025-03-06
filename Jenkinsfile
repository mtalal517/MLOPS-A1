pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = "mtalal12/mlopsa1"  // Replace with your Docker Hub username & repo
        DOCKER_CREDENTIALS_ID = "your-jenkins-docker-credentials-id"  // Replace with your stored credentials ID
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/mtalal517/MLOPS-A1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_HUB_REPO}:latest ."
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS_ID}", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh "echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin"
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    sh "docker push ${DOCKER_HUB_REPO}:latest"
                }
            }
        }

        stage('Cleanup') {
            steps {
                sh "docker rmi ${DOCKER_HUB_REPO}:latest"
            }
        }
    }
}
