pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                git 'https://github.com/example/sample-python-project.git'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'poetry install'
                sh 'poetry run pytest'
            }
        }

        stage('Build') {
            steps {
                sh 'poetry build'
            }
        }

        stage('Publish to PyPI Sandbox') {
            steps {
                withCredentials([string(credentialsId: 'pypi-token', variable: 'TWINE_PASSWORD')]) {
                    sh 'poetry config pypi-token.pypi $TWINE_PASSWORD'
                    sh 'poetry publish -r sandbox'
                }
            }
        }

        stage('Cleanup') {
            steps {
                sh 'rm -rf dist build *.egg-info'
            }
        }
    }
}