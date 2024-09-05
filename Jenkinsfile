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
                echo "running docker file for test"
                mkdir -p tmp
                cd tmp
                echo 99999 > Scores121.txt
                cat Scores.txt
                cd ..
                ls -l $(pwd)/tmp/Scores121.txt
                ls -la
                ls -la $(pwd)/tmp
                docker run -d --name flasktest_container -p 8777:3000 -v /var/jenkins_home/workspace/Wog_flask/tmp/Scores121.txt:/app/file.txt flasktest
                docker exec flasktest_container pwd
                docker exec flasktest_container ls -la
                docker exec flasktest_container ls -la /app/tmp

                '''
            }
        }
    }

}