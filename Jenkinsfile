pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'homol', url: 'https://github.com/davieduardo001/mysql-sgbdweb-api.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    sh 'docker-compose build'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh 'docker-compose up -d'
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
