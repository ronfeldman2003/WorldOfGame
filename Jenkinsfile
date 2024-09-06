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

                # Use the WORKSPACE variable directly
                echo "Workspace Path: ${WORKSPACE}"

                # Run the container with the workspace path
                docker run -d --name testflask_container -p 8777:3000 -v ${WORKSPACE}/Scores.txt:/app/Scores.txt testflask2

                # Check the contents of the /app directory in the container
                docker exec testflask_container ls -la /app
                docker exec testflask_container cat /app/Scores.txt || echo "Failed to read Scores.txt in container"

                # Print container logs for debugging
                docker logs testflask_container
                '''
            }
        }
    }
    post {
        always {
            sh '''
            docker stop testflask_container || true
            docker rm testflask_container || true
            '''
        }
    }
}