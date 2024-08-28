pipeline {
    agent any
    tools {
        git 'Default Git' // Matches the name you set in the Global Tool Configuration
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
    }
}
