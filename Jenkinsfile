pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'   // Change to your preferred AWS region
    }

    parameters {
        choice(name: 'SERVICE', choices: ['EC2', 'S3', 'Route53'], description: 'Select the AWS service to manage')
        string(name: 'INSTANCE_NAME', defaultValue: '', description: 'Enter EC2 instance name (Only for EC2 option)')
        choice(name: 'INSTANCE_TYPE', choices: ['t2.micro', 't2.small', 't3.medium'], description: 'Select EC2 instance type (Only for EC2)')
        choice(name: 'EC2_ACTION', choices: ['Create', 'Start', 'Stop'], description: 'Choose EC2 action (Only for EC2)')
        string(name: 'BUCKET_NAME', defaultValue: '', description: 'Enter S3 bucket name (Only for S3 option)')
        choice(name: 'S3_ACTION', choices: ['Create', 'Upload'], description: 'Choose S3 action (Only for S3)')
        string(name: 'FILE_PATH', defaultValue: '', description: 'Enter file path to upload (Only for S3 Upload)')
        string(name: 'DOMAIN_NAME', defaultValue: '', description: 'Enter domain name for Route53 (Only for Route53)')
        choice(name: 'ROUTE53_ACTION', choices: ['CreateZone', 'ManageDNS'], description: 'Choose Route53 action')
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/NetaAviv/python_project.git'
            }
        }

        stage('Execute AWS Operations') {
            steps {
                script {
                    if (params.SERVICE == 'EC2') {
                        if (params.EC2_ACTION == 'Create') {
                            sh "python3 cli_tool.py ec2 create --name ${params.INSTANCE_NAME} --type ${params.INSTANCE_TYPE} --region $AWS_REGION"
                        } else if (params.EC2_ACTION == 'Start') {
                            sh "python3 cli_tool.py ec2 start --name ${params.INSTANCE_NAME} --region $AWS_REGION"
                        } else if (params.EC2_ACTION == 'Stop') {
                            sh "python3 cli_tool.py ec2 stop --name ${params.INSTANCE_NAME} --region $AWS_REGION"
                        }
                    }
                    else if (params.SERVICE == 'S3') {
                        if (params.S3_ACTION == 'Create') {
                            sh "python3 cli_tool.py s3 create --name ${params.BUCKET_NAME} --region $AWS_REGION"
                        } else if (params.S3_ACTION == 'Upload') {
                            sh "python3 cli_tool.py s3 upload --bucket ${params.BUCKET_NAME} --file ${params.FILE_PATH} --region $AWS_REGION"
                        }
                    }
                    else if (params.SERVICE == 'Route53') {
                        if (params.ROUTE53_ACTION == 'CreateZone') {
                            sh "python3 cli_tool.py route53 create-zone --domain ${params.DOMAIN_NAME} --region $AWS_REGION"
                        } else if (params.ROUTE53_ACTION == 'ManageDNS') {
                            sh "python3 cli_tool.py route53 manage-dns --domain ${params.DOMAIN_NAME} --region $AWS_REGION"
                        }
                    }
                }
            }
        }
    }
}
