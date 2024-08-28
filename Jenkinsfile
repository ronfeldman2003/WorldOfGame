pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ronfeldman2003/WorldOfGame'
            }
        stage('build') {
            steps {
                    sh "docker-compose build"
                }
        }
    }
}
