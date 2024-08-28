pipeline {
    agent any
    tools {
        git 'Default' // Matches the name you set in the Global Tool Configuration
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
    }
}
