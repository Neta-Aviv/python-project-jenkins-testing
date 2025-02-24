pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'
    }

    parameters {
        choice(name: 'SERVICE', choices: ['EC2', 'S3', 'Route53'], description: 'AWS Service to manage')

        string(name: 'INSTANCE_NAME', defaultValue: 'my-instance', description: 'EC2 Instance Name')
        string(name: 'INSTANCE_TYPE', defaultValue: 't2.micro', description: 'EC2 Instance Type')

        string(name: 'S3_BUCKET_NAME', defaultValue: 'my-bucket', description: 'S3 Bucket Name')
        string(name: 'S3_FILE_PATH', defaultValue: 'file.txt', description: 'File Path to Upload')

        string(name: 'DOMAIN_NAME', defaultValue: 'example.com', description: 'Route 53 Domain Name')
    }

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
            }
        }

        stage('Execute AWS Operations') {
            steps {
                script {
                    def cliToolPath = "${WORKSPACE}/main.py"

                    if (params.SERVICE == 'EC2') {
                        sh "python3 ${cliToolPath} ec2 create --name ${params.INSTANCE_NAME} --type ${params.INSTANCE_TYPE} --region ${AWS_REGION}"
                    } else if (params.SERVICE == 'S3') {
                        sh "python3 ${cliToolPath} s3 create --name ${params.S3_BUCKET_NAME} --region ${AWS_REGION}"
                    } else if (params.SERVICE == 'Route53') {
                        sh "python3 ${cliToolPath} route53 create --domain ${params.DOMAIN_NAME}"
                    }
                }
            }
        }
    }
}
