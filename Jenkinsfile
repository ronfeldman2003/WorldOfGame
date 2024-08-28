pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ronfeldman2003/WorldOfGame'
            }
        }
        stage('Install Docker Compose') {
            steps {
                sh '''
                    sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
                    sudo chmod +x /usr/local/bin/docker-compose
                '''
            }
        }
        stage('build') {
            steps {
                sh 'docker-compose build'
            }
        }
    }
}
