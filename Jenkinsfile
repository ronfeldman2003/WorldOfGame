pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ronfeldman2003/WorldOfGame'
            }
        }
        stage('build') {
            agent {
                docker {
                    image 'docker:dind'
                    args '-v /var/run/docker.sock:/var/run/docker.sock'
                }
            }
            steps {
                sh 'docker-compose build'
            }
        }
    }
}
