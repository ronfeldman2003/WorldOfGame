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
                sh '''
                echo "building docker file for test"
                docker build -t flasktest .
                '''
            }
        }
        stage('run') {
            steps {
                sh '''
                echo "running docker file for test"
                echo 99999 > Scores.txt
                cat Scores.txt
                ls -l $(pwd)/Scores.txt
                docker run -v ${PWD}/Scores.txt:/app/tmp/Scores.txt -p 8777:3000 flasktest
                '''
            }
        }
    }
}
