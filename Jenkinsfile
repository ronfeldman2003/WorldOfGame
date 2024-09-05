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
                echo 99999 > Scores12.txt
                chmod 644 Scores12.txt
                cat Scores12.txt
                cd ..
                ls -l $(pwd)/tmp/Scores12.txt
                ls -la
                ls -la $(pwd)/tmp
                docker run -d --name flasktest_containerScores12 -p 8777:3000 -v /var/jenkins_home/workspace/Wog_flask/tmp/Scores12.txt:/app/Scores12.txt flasktest
                docker exec flasktest_containerScores12 pwd
                docker exec flasktest_containerScores12 ls -la
                docker exec flasktest_containerScores12 ls -la /app/testfile

                '''
            }
        }
    }

}