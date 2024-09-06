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
                docker build -t testflask .
                '''
            }
        }
        stage('run') {
            steps {
                sh '''
                echo "running docker file for test"
                echo 99999 > Scores.txt
                chmod 777 Scores.txt
                cat Scores.txt
                ls -la
                docker run -d --name testflask_container -p 8777:3000 -v ./Scores.txt:/app/Scores.txt testflask
                docker exec testflask_container ls -la

                '''
            }
        }
    }

}