pipeline {
    agent any
    environment {
        // Replace this with the actual path on your Mac where Jenkins workspace is mapped
        MAC_WORKSPACE = '/Users/ronfeldman/jenkins/workspace/WOG_part4'
    }
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
                echo "Contents of Scores.txt:"
                cat Scores.txt
                echo "Directory listing:"
                ls -la
                echo "Current working directory:"
                pwd

                echo "Mac Workspace Path: ${MAC_WORKSPACE}"

                # Run the container with the Mac workspace path
                docker run -d --name testflask_container -p 8777:3000 -v ${MAC_WORKSPACE}/Scores.txt:/app/Scores.txt testflask2

                echo "Container directory listing:"
                docker exec testflask_container ls -la /app

                echo "Container file contents:"
                docker exec testflask_container cat /app/Scores.txt || echo "Failed to read Scores.txt in container"

                echo "Container logs:"
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