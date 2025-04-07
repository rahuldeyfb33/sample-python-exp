pipeline {
    agent any

    stages {
        stage('SCM Checkout: Github') {
            steps {
                git credentialsId: 'github-creds', url: 'https://github.com/rahuldeyfb33/sample-python-exp.git'
            }
        }

        stage('Build Python Script') {
            steps {
                sh 'pwd'
                sh 'cd $JENKINS_HOME/workspace/sample-python-pipeline && poetry install && python src/sample_pkg/module_one.py'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'cd $JENKINS_HOME/workspace/sample-python-pipeline && poetry run pytest tests/'
            }
        }

        stage('Cleanup') {
            steps {
                sh 'rm -rf $JENKINS_HOME/workspace/sample-python-pipeline/*'
            }
        }
    }

    post {
        always {
            echo 'Post-build action: Cleaning up and notifying...'
        }
        success {
            echo 'The build was successful!'
        }
        failure {
            echo 'The build failed. Check logs for details'
        }
    }
}