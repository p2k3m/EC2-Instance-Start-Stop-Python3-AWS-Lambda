import boto3


def kick_off_ec2(event, context):

    # Get list of regions
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2_client.describe_regions()['Regions']]

    # Iterate over each region
    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)

        print("Region:", region)

        # Get only running instances
        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name',
                      'Values': ['stopped']},{'Name':'tag:dev', 'Values':['true']}])

        # Start the instances
        for instance in instances:
            instance.start()
            print('started instances: ', instance.id)

def end_ec2(event, context):

    # Get list of regions
    ec2_client = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2_client.describe_regions()['Regions']]

    # Iterate over each region
    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)

        print("Region:", region)

        # Get only running instances
        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name',
                      'Values': ['running']},{'Name':'tag:dev', 'Values':['true']}])

        # Stop the instances
        for instance in instances:
            instance.stop()
            print('Stopped instance: ', instance.id)
