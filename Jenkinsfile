pipeline {
    agent any

    options {
        // This is required if you want to clean before build
        skipDefaultCheckout(true)
    }

    parameters{
        string(name: 'app_name', defaultValue: 'app_test', description: 'Name of repository for application')
        string(name: 'app_file', defaultValue: 'app_script.sh', description: 'The name of the application file to be called') 
    }

    stages {
        stage('Cleanup WS') {
            steps {
                // Clean before build
                cleanWs()
            }
        }

        stage('Pre-build steps') {
            steps {
                echo "Prepare Env:"
                echo "- Installing OS packeges"
                echo "- Creating directories and etc"
            }
        }

        stage('Build') {
            steps {
                dir("${app_name}") {
                    git branch: 'main',
                        // credentialsId: 'token from Jenkins key manager'
                        url: 'https://github.com/ch1pp00/app_test.git'
                }
                sh "ls ${WORKSPACE}"
                sh "ls ${WORKSPACE}/${app_name}"
                sh "chmod u+x ${WORKSPACE}/${app_name}/${app_file}"
                sh '''
                echo "Run code"
                ${WORKSPACE}/${app_name}/${app_file}
                '''
            }
        }

        stage('Build tests'){
            parallel{
                stage('Tests 1') {
                    steps {
                        echo "Test 1 Run"
                    }
                }

                stage('Test 2') {
                    steps {
                        echo "Test 2 Run"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "Create docker container"'
                sh 'echo "Start container"'
            }
        }

        stage('Deploy tests'){
            parallel{
                stage('Tests 1') {
                    steps {
                        echo "Test 1 Run"
                    }
                }

                stage('Test 2') {
                    steps {
                        echo "Test 2 Run"
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'whole pipeline successful'
            echo 'Additional steps in case of job success'
        }

        failure {
            echo 'pipeline failed, at least one step failed'
            echo 'Additional steps in case of job failure'
        }
    }
}
