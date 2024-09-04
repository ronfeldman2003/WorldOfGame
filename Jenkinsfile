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
                docker build -t flasktest .
                '''
            }
        }
         stage('run') {
            steps {
                sh '''
                echo "runing  docker file for test"
                echo 99999 > Scores.txt
                cat Scores.txt
                ls -l $(pwd)/Scores.txt
                docker run -v $(pwd)/Scores.txt:/app/tmp/Scores.txt:ro -p 8777:3000 -t flasktest
                docker run -it --entrypoint /bin/sh -v /var/jenkins_home/workspace/Wog_flask/Scores.txt:/app/tmp/Scores.txt:ro flasktest
                ls -l /app/tmp

                '''
            }
        }
    }
}
