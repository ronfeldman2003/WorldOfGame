pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/dev']],
                          userRemoteConfigs: [[url: 'https://github.com/ronfeldman2003/WorldOfGame']]])
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker image with Docker Compose'
                    sh 'docker-compose build'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    echo 'Starting Docker container with Docker Compose'
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Add your test commands here
                    echo 'Running tests'
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    echo 'Stopping and removing Docker containers'
                    sh 'docker-compose down'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace'
            cleanWs()
        }
    }
}