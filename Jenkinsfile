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
                docker build -t testflask2 .
                '''
            }
        }
        stage('run') {
            steps {
                sh '''
                echo "running docker file for test"
                echo 123 > Scores.txt
                chmod 777 Scores.txt
                cat Scores.txt
                ls -la
                pwd
                WORKSPACE_PATH=$(pwd)
                docker run -d --name testflask_container -p 8777:3000 -v ${WORKSPACE_PATH}/Scores.txt:/app/Scores.txt testflask2
                docker exec testflask_container ls -la

                '''
            }
        }
    }

}