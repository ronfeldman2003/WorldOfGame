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
                echo "Contents of Scores.txt:"
                cat Scores.txt
                echo "Directory listing:"
                echo "Current working directory:"
                pwd
                echo "Mac Workspace Path: ${MAC_WORKSPACE}"
                # Run the container with the Mac workspace path
                docker run -d --name testflask_container -p 8777:3000 -v ${MAC_WORKSPACE}/Scores.txt:/app/Scores.txt testflask2
                '''
            }
        }
        stage('test') {
            stage('test') {
                steps {
                    sh '''
                        python3 --version
                        which python3
                        pip3 install virtualenv
                        virtualenv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install selenium webdriver_manager
                        python3 -c 'import e2e; e2e.main_function("http://127.0.0.1:8777")'
                        deactivate
                        TEST_EXIT_CODE=$?
                        if [ $TEST_EXIT_CODE -ne 0 ]; then
                            echo "Tests failed with exit code $TEST_EXIT_CODE"
                            exit 1
                        else
                            echo "Tests passed"
                        fi
                    '''
                }
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