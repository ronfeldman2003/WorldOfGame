pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('build') {
            steps {
                sh "sudo docker build -t flasktest ."
            }
        }
    }
}
