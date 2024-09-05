pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh '''
                echo "Building Docker image for test"
                docker build -t flasktest .
                '''
            }
        }
        stage('Run') {
            steps {
                sh '''
                echo "Preparing and running Docker container for test"
                echo 99999 > ${WORKSPACE}/Scores.txt
                echo "Contents of Scores.txt:"
                cat ${WORKSPACE}/Scores.txt
                echo "File details:"
                ls -l ${WORKSPACE}/Scores.txt

                echo "Running Docker container"
                docker run -d --name flasktest_container \
                    -u 1000:1000 \
                    -v ${WORKSPACE}/Scores.txt:/app/tmp/Scores.txt \
                    -p 8777:3000 \
                    flasktest

                echo "Verifying file mount in container"
                docker exec flasktest_container ls -l /app/tmp/Scores.txt
                docker exec flasktest_container cat /app/tmp/Scores.txt
                '''
            }
        }
    }
    post {
        always {
            sh '''
            echo "Cleaning up"
            docker stop flasktest_container || true
            docker rm flasktest_container || true
            '''
        }
    }
}