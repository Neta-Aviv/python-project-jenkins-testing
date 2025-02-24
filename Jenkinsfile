pipeline {
    agent any

    environment {
        AWS_REGION = "us-east-1"   // Ensures AWS region is set globally
        AWS_DEFAULT_REGION = "us-east-1"
        PATH = "${WORKSPACE}/venv/bin:${env.PATH}" // Ensures virtualenv is used
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/Neta-Aviv/python-project-jenkins-testing.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install boto3
                '''
            }
        }

        stage('Execute AWS Operations') {
            steps {
                sh '''
                source venv/bin/activate
                python3 main.py ec2 create --name my-instance --type t2.micro --region us-east-1
                '''
            }
        }
    }

    post {
        failure {
            echo "Build failed! Check logs."
        }
        success {
            echo "Build succeeded!"
        }
    }
}
