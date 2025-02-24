import argparse
from ec2_manager import *
from s3_manager import *
from route53_manager import *

def main():
    parser = argparse.ArgumentParser(description="AWS Resource Management")
    parser.add_argument("--action", choices=["EC2", "S3", "Route53"], required=True)
    parser.add_argument("--instance-name", type=str, help="Name of EC2 instance")
    parser.add_argument("--instance-type", type=str, help="EC2 instance type")
    parser.add_argument("--s3-bucket", type=str, help="S3 bucket name")

    args = parser.parse_args()

    if args.action == "EC2":
        if args.instance_name and args.instance_type:
            print(f"Launching EC2: {args.instance_name} ({args.instance_type})")
            get_new_instance_details(args.instance_name, args.instance_type)
        else:
            print("Missing instance name or type!")

    elif args.action == "S3":
        if args.s3_bucket:
            print(f"Creating S3 bucket: {args.s3_bucket}")
            create_s3_bucket(args.s3_bucket)
        else:
            print("Missing bucket name!")

    elif args.action == "Route53":
        print("Managing Route 53")
        manage_dns_record()

if __name__ == "__main__":
    main()
