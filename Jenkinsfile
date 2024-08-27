pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "yourdockerhubusername/yourimagename:latest"
        APP_PORT = "8777"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    // Build the Docker image from the Dockerfile in the repository
                    sh "docker build -t \${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    // Run the Docker container
                    sh """
                    docker run -d --name scores_app -p \${APP_PORT}:5000 \
                    -v \$(pwd)/Scores.txt:/app/Scores.txt \${DOCKER_IMAGE}
                    """
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run the e2e tests using Selenium
                    sh "python3 e2e.py"

                    // Fail the build if tests fail
                    catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                        sh "pytest --maxfail=1 --disable-warnings"
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    // Stop and remove the Docker container
                    sh "docker stop scores_app && docker rm scores_app"

                    // Push the Docker image to DockerHub
                    sh "docker login -u <your-username> -p <your-password>"
                    sh "docker push \${DOCKER_IMAGE}"
                }
            }
        }
    }

    post {
        always {
            // Cleanup: remove the Docker container if still running
            sh "docker rm -f scores_app || true"
        }
    }
}
