pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                echo "testing your code"
            }
        }
        stage('Build') {
            parallel {
                stage('Version1') {
                    steps {
                        echo "building version 1"
                    }
                }
                stage('Version2') {
                    steps {
                        echo "building version 2"
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "approval required"'
                sh 'echo "deploying your code"'
            }
        }
    }
}
