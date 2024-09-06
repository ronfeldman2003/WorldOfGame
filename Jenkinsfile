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

                # Get the workspace path on the host machine
                HOST_WORKSPACE_PATH=$(docker inspect ${NODE_NAME} | grep "Source" | grep "${WORKSPACE}" | awk -F'"' '{print $4}')

                echo "Host Workspace Path: ${HOST_WORKSPACE_PATH}"

                # If HOST_WORKSPACE_PATH is empty, fall back to WORKSPACE
                if [ -z "${HOST_WORKSPACE_PATH}" ]; then
                    echo "Couldn't determine host workspace path, using WORKSPACE"
                    HOST_WORKSPACE_PATH=${WORKSPACE}
                fi

                # Run the container with the host path
                docker run -d --name testflask_container -p 8777:3000 -v ${HOST_WORKSPACE_PATH}/Scores.txt:/app/Scores.txt testflask2

                # Check the contents of the /app directory in the container
                docker exec testflask_container ls -la /app
                docker exec testflask_container cat /app/Scores.txt || echo "Failed to read Scores.txt in container"
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