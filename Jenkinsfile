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
        stage('Deploy') {
            steps {
                echo "Starting Deployment"
                sh 'echo "Application deployed successfully!"'
                
            }
        }
    }
}