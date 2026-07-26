pipeline {
    agent any

    stages {
        stage('System Check') {
            steps {
                echo "Starting System Check"

                sh 'pwd'
                sh 'whoami'
                sh 'hostname'
                sh 'date'
            }
        }

        stage('Build') {
            steps {
                echo "Starting Build"
                sh 'python3 --version'
            }
        }

        stage('Test') {
            steps {
                echo "Starting Test"
                sh 'python3 test.py'
            }
        }

        stage('Deploy') {
            steps {
                echo "Starting Container Deployment"

                sh 'podman --version'

                sh 'podman build -t git-practice-app .'

                sh 'podman rm -f git-practice-container || true'

                sh 'podman run -d --name git-practice-container -p 8000:8000 git-practice-app'

                sh 'podman ps'
            }
        }

        stage('Health Check') {
            steps {
                echo "Checking Application Health"

                sh 'sleep 3'

                sh 'curl -f http://localhost:8000/health'
            }
        }
    }
}