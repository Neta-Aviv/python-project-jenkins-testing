pipeline {
    agent any

    parameters {
        choice(name: 'RESOURCE_TYPE', choices: ['ec2', 's3', 'route53'], description: 'Select the AWS resource to manage')
        
        choice(name: 'EC2_ACTION', choices: ['Create', 'Start', 'Stop', 'List'], description: 'Select an EC2 action')
        choice(name: 'INSTANCE_TYPE', choices: ['t3.nano', 't4g.nano'], description: 'Choose an EC2 instance type')
        choice(name: 'AMI_TYPE', choices: ['AmazonLinux', 'Ubuntu'], description: 'Choose an AMI')
        
        string(name: 'INSTANCE_NAME', defaultValue: 'my-instance', description: 'Enter the name for the EC2 instance')

        choice(name: 'S3_ACTION', choices: ['Create', 'Upload', 'List'], description: 'Select an S3 action')
        choice(name: 'S3_ACCESS', choices: ['Private', 'Public'], description: 'Choose access type for S3 (only for Create)')
        string(name: 'S3_BUCKET_NAME', defaultValue: 'my-bucket', description: 'Enter S3 bucket name')

        choice(name: 'ROUTE53_ACTION', choices: ['Create Zone', 'Manage DNS Records'], description: 'Select a Route53 action')
        string(name: 'ROUTE53_ZONE', defaultValue: 'example.com', description: 'Enter the domain name for the Route53 zone')
    }

    environment {
        AWS_REGION = "us-east-1"
        AWS_DEFAULT_REGION = "us-east-1"
        PATH = "${WORKSPACE}/venv/bin:${env.PATH}"
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
                script {
                    if (params.RESOURCE_TYPE == 'ec2') {
                        if (params.EC2_ACTION == 'Create') {
                            sh """
                            source venv/bin/activate
                            python3 main.py ec2 create --name ${params.INSTANCE_NAME} --type ${params.INSTANCE_TYPE} --ami ${params.AMI_TYPE} --region us-east-1
                            """
                        } else if (params.EC2_ACTION == 'Start') {
                            sh """
                            source venv/bin/activate
                            python3 main.py ec2 start --name ${params.INSTANCE_NAME}
                            """
                        } else if (params.EC2_ACTION == 'Stop') {
                            sh """
                            source venv/bin/activate
                            python3 main.py ec2 stop --name ${params.INSTANCE_NAME}
                            """
                        } else if (params.EC2_ACTION == 'List') {
                            sh """
                            source venv/bin/activate
                            python3 main.py ec2 list
                            """
                        }
                    }

                    if (params.RESOURCE_TYPE == 's3') {
                        if (params.S3_ACTION == 'Create') {
                            if (params.S3_ACCESS == 'Public') {
                                input message: "Are you sure you want to create a public S3 bucket?", ok: "Yes"
                            }
                            sh """
                            source venv/bin/activate
                            python3 main.py s3 create --name ${params.S3_BUCKET_NAME} --access ${params.S3_ACCESS}
                            """
                        } else if (params.S3_ACTION == 'Upload') {
                            sh """
                            source venv/bin/activate
                            python3 main.py s3 upload --bucket ${params.S3_BUCKET_NAME} --file somefile.txt
                            """
                        } else if (params.S3_ACTION == 'List') {
                            sh """
                            source venv/bin/activate
                            python3 main.py s3 list
                            """
                        }
                    }

                    if (params.RESOURCE_TYPE == 'route53') {
                        if (params.ROUTE53_ACTION == 'Create Zone') {
                            sh """
                            source venv/bin/activate
                            python3 main.py route53 create --domain ${params.ROUTE53_ZONE}
                            """
                        } else if (params.ROUTE53_ACTION == 'Manage DNS Records') {
                            sh """
                            source venv/bin/activate
                            python3 main.py route53 manage --domain ${params.ROUTE53_ZONE}
                            """
                        }
                    }
                }
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
