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
                echo 99999 > Scores.txt
                cat Scores.txt
                cd ..
                ls -l $(pwd)/tmp/Scores.txt
                docker run -d --name flasktest_container -p 8777:3000 -v $(pwd)/tmp:/app/tmp flasktest
                docker exec flasktest_container ls -l /app/tmp/Scores.txt
                '''
            }
        }
    }
}
