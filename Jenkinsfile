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
                bat "docker rmi ${DOCKER_HUB_REPO}:latest"

            }
        }
    }
    post 
    {
    success {
        echo 'Docker image successfully built and pushed to Docker Hub!'
        emailext (
            subject: "Pipeline Success: ${env.JOB_NAME} - Build #${env.BUILD_NUMBER}",
            body: """
            The pipeline ${env.JOB_NAME} - Build #${env.BUILD_NUMBER} completed successfully.
            View the build details: ${env.BUILD_URL}
            """,
            to: 'mtalalqureshi5@gmail.com'
        )
    }
    failure {
        echo 'Docker build or push failed  :('
        emailext (
            subject: "Pipeline Failed: ${env.JOB_NAME} - Build #${env.BUILD_NUMBER}",
            body: """
            The pipeline ${env.JOB_NAME} - Build #${env.BUILD_NUMBER} failed.
            View the build details: ${env.BUILD_URL}
            """,
            to: 'mtalalqureshi5@gmail.com'
        )
    }
    
    always {
        // Clean up workspace
        cleanWs()
    }
}
}