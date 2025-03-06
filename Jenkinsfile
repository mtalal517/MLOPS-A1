pipeline {
    agent any
    
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials') // Set up in Jenkins
        DOCKER_IMAGE = "yourusername/ml-iris-classifier" // Replace with your Docker Hub username
        EMAIL_RECIPIENT = "admin@example.com" // Replace with admin's email
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE}:${env.BUILD_NUMBER} ."
                sh "docker tag ${DOCKER_IMAGE}:${env.BUILD_NUMBER} ${DOCKER_IMAGE}:latest"
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                sh "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin"
                sh "docker push ${DOCKER_IMAGE}:${env.BUILD_NUMBER}"
                sh "docker push ${DOCKER_IMAGE}:latest"
            }
        }
        
        stage('Clean Up') {
            steps {
                sh "docker rmi ${DOCKER_IMAGE}:${env.BUILD_NUMBER}"
                sh "docker rmi ${DOCKER_IMAGE}:latest"
            }
        }
    }
    
    post {
        success {
            emailext (
                subject: "SUCCESSFUL: Pipeline '${currentBuild.fullDisplayName}'",
                body: """SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'. 
                Check console output at ${env.BUILD_URL}""",
                to: "${EMAIL_RECIPIENT}"
            )
        }
        failure {
            emailext (
                subject: "FAILED: Pipeline '${currentBuild.fullDisplayName}'",
                body: """FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'. 
                Check console output at ${env.BUILD_URL}""",
                to: "${EMAIL_RECIPIENT}"
            )
        }
    }
}