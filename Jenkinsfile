pipeline {
    agent any
    tools {
        git 'Default' // Use the name set in Global Tool Configuration
    }
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'https://github.com/ronfeldman2003/WorldOfGame']]
                ])
            }
        }
    }
}
