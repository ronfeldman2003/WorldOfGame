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
                echo 99999 > Scores112.txt
                chmod 644 Scores112.txt
                cat Scores.txt
                cd ..
                ls -l $(pwd)/tmp/Scores112.txt
                ls -la
                ls -la $(pwd)/tmp
                docker run -d --name flasktest_container -p 8777:3000 -v /var/jenkins_home/workspace/Wog_flask/tmp/Scores112.txt:/app/testfile.txt flasktest
                docker exec flasktest_container pwd
                docker exec flasktest_container ls -la

                '''
            }
        }
    }

}