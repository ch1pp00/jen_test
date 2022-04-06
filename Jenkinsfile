pipeline {
    agent any

    options {
        // This is required if you want to clean before build
        skipDefaultCheckout(true)
    }

    parameters{
        string(name: 'myvar2', defaultValue: 'zxc123', description: 'Descr') 
    }

    stages {
        stage('Cleanup WS') {
            steps {
                // Clean before build
                cleanWs()
            }
        }

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

        stage('Postbuild steps'){
            parallel{
                stage('Test Var') {
                    steps {
                        sh 'echo "My var - ${myvar2}"'
                    }
                }
                stage('Test files') {
                    steps {
                        sh '''
                        touch 2.txt
                        ls -l
                        '''
                    }
                }
            }
        }
    }
}
