pipeline {
    agent any

    environment {
        PROJECT_NAME = "webapp-ci"
        COMPOSE_FILE = "docker-compose.yml"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/M-Waleed7/flask-app'
            }
        }

        stage('Build & Run Containers') {
            steps {
                script {
                    sh "docker-compose -p ${PROJECT_NAME} -f ${COMPOSE_FILE} up -d --build"
                }
            }
        }
    }
}
