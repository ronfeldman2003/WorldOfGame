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
                docker run -d --name flasktest_container -u 1000:1000 -p 8777:3000 -v $(pwd)/tmp:/app/tmp flasktest
                docker exec flasktest_container ls -la
                '''
            }
        }
    }
    post {
        always {
            sh '''
            echo "Cleaning up"
            docker stop flasktest_container || true
            docker rm flasktest_container || true
            '''
        }
    }
}
