pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        tage('build') {
            steps {
                sh "docker build flasktest ."
            }
        }
    }
}
