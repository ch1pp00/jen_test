pipeline {
    agent any

    options {
        // This is required if you want to clean before build
        skipDefaultCheckout(true)
    }

    // All parameters are used from parameters of jenkins job
    // parameters{
    //     string(name: 'app_name', defaultValue: 'app_test', description: 'Name of repository for application')
    //     string(name: 'app_file', defaultValue: 'app_script.sh', description: 'The name of the application file to be called') 
    //     string(name: 'git_url', defaultValue: 'https://github.com/ch1pp00/app_test.git', description: '')
    //     string(name: 'git_branch', defaultValue: 'main', description: '')
    // }

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
                    git branch: "${git_branch}",
                        // credentialsId: 'token from Jenkins key manager'
                        url: "${git_url}"
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
        
        stage ('Starting another Jenkins job') {
            steps {
                build job: 'job1', parameters: [
                string(name: 'var1', value: "Man")
                ]
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