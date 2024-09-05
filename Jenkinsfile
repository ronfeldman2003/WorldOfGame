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
                    sh '''
                    echo "running docker file for test"
                    mkdir -p tmp
                    cd tmp
                    echo 99999 > Scores.txt
                    cat Scores.txt
                    cd ..
                    ls -l $(pwd)/tmp/Scores.txt
                    ls -la
                    ls -la $(pwd)/tmp
                    docker-compose up -d
                    docker-compose exec flaskapp sh -c 'ls -la /app/tmp'
                    '''
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