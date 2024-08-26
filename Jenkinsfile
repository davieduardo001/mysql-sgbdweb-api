pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'homol', url: 'https://github.com/davieduardo001/mysql-sgbdweb-api.git'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh '/usr/bin/docker-compose up --build'
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}
