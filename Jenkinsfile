pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}/venv"  // Path for virtual environment
        AWS_REGION = "us-east-1"  // Set the AWS region
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Neta-Aviv/python-project-jenkins-testing.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv $VENV_DIR  # Create virtual environment
                source $VENV_DIR/bin/activate
                pip install --upgrade pip
                pip install boto3
                '''
            }
        }

        stage('Execute AWS Operations') {
            steps {
                sh '''
                source $VENV_DIR/bin/activate
                python3 main.py ec2 create --name my-instance --type t2.micro --region $AWS_REGION
                '''
            }
        }
    }
}
