pipeline {
    agent { label 'home-lab' }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'homol', url: 'https://github.com/davieduardo001/mysql-sgbdweb-api.git'
            }
        }
        
        stage('Setup Environment') {
            steps {
                script {
                    // Create .env file dynamically
                    writeFile file: '.env', text: '''
                    DB_HOST=****
                    DB_USER=****
                    DB_PASSWORD=****
                    DB_DATABASE=****
                    MYSQL_ROOT_PASSWORD=****
                    '''
                }
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