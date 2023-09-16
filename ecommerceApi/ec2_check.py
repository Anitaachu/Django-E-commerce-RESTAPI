# def is_ec2_linux():
#     """Detect if we are running on an EC2 Linux Instance
#        See http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/identify_ec2_instances.html
#     """
#     import os
#     if os.path.isfile("/sys/hypervisor/uuid"):
#         with open("/sys/hypervisor/uuid") as f:
#             uuid = f.read()
#             return uuid.startswith("ec2")
#     if os.path.isdir("/sys/hypervisor"):
#         return True
#     return False


# def get_linux_ec2_private_ip():
#     """Get the private IP Address of the machine if running on an EC2 linux server"""
#     from urllib.request import urlopen, Request
#     if not is_ec2_linux():
#         return None

#     token_request = Request("http://169.254.169.254/latest/api/token", method='PUT')
#     token_request.add_header("X-aws-ec2-metadata-token-ttl-seconds", "21600")
    
#     try:
#         token = urlopen(token_request).read()
#     except Exception as e:
#         print("Failed to get EC2 Metadata Token: %s" % e)
#         return None
    
    
#     ip_request = Request("http://169.254.169.254/latest/meta-data/local-ipv4")
#     ip_request.add_header("X-aws-ec2-metadata-token", token)

#     response = None
#     try:

#         response = urlopen(ip_request)
#         return response.read().decode()
#     except Exception as e: 
#         print("Error getting EC2 private IP: %s" % e)
#         return None
#     finally:
#         if response:
#             response.close()