pipeline {
    agent any
    environment {
        MAC_WORKSPACE = '/Users/ronfeldman/jenkins/workspace/WOG_part4'
        VENV_PATH = '/opt/venv/bin'
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
                curl curl http://host.docker.internal:8777



                '''
            }
        }
        stage('test') {
            steps {
                sh '''


                    ${VENV_PATH}/python3 -c 'import e2e; e2e.main_function("http://host.docker.internal:8777")'
                    TEST_EXIT_CODE=$?


                    # Check test result
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