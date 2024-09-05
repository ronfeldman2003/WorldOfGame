pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile.build'
            additionalBuildArgs "--build-arg UID=${userId}"
            reuseNode true
        }
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
                cat Scores112.txt
                cd ..
                ls -l $(pwd)/tmp/Scores112.txt
                ls -la
                ls -la $(pwd)/tmp
                docker run -d --name flasktest_container2 -p 8777:3000 -v /var/jenkins_home/workspace/Wog_flask/tmp/Scores112.txt:/app/ddddddddd.txt flasktest
                docker exec flasktest_container2 pwd
                docker exec flasktest_container2 ls -la
                docker exec flasktest_container2 ls -la /app/testfile

                '''
            }
        }
    }

}