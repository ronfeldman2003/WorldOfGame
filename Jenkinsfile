pipeline {
    agent any
    tools {
        tool name: 'Default', type: 'git'
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
