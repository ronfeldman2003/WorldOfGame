pipeline {
    agent any
    environment {
        MAC_WORKSPACE = '/Users/ronfeldman/jenkins/workspace/WOG_part4'
        VENV_PATH = '/opt/venv/bin'
        VALUE_FOR_SCORES_FILE = "111"
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
                docker-compose build
                '''
            }
        }
        stage('run') {
            steps {
                sh '''
                echo "running docker file for test"
                echo  ${VALUE_FOR_SCORES_FILE} > Scores.txt
                echo "Contents of Scores.txt:"
                cat Scores.txt
                echo "Directory listing:"
                echo "Current working directory:"
                pwd
                echo "Mac Workspace Path: ${MAC_WORKSPACE}"
                # Run the container with the Mac workspace path
                docker-compose up --detach
                #docker run -d --name testflask_container -p 8777:3000 -v ${MAC_WORKSPACE}/Scores.txt:/app/Scores.txt testflask2



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
    post {
        always {
            sh '''
            echo "Cleaning up"
            docker-compose push
            docker-compose down
            #docker stop testflask_container || true
            #docker rm testflask_container || true
            '''
        }
    }

}