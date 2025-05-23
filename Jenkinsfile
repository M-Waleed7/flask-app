pipeline {
    agent any

    stages {
        stage('Clean DevOps directory') {
            steps {
                sh '''
                if [ -d "/var/lib/jenkins/DevOps/" ]; then
                    find "/var/lib/jenkins/DevOps/" -mindepth 1 -delete
                    echo "Cleaned DevOps directory."
                fi
                '''
            }
        }

        stage('Clone from GitHub') {
            steps {
                sh 'git clone https://github.com/M-Waleed7/flask-app /var/lib/jenkins/DevOps/app/'
            }
        }

        stage('Rebuild and Run Docker Compose') {
            steps {
                dir('/var/lib/jenkins/DevOps/app/') {
                    sh '''
                    echo "Stopping and removing old containers..."
                    docker compose -p myflaskapp down

                    echo "Rebuilding image and starting container..."
                    docker compose -p myflaskapp up -d --build
                    '''
                }
            }
        }
    }
}
