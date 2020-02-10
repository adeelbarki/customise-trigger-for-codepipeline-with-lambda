import boto3

# Map config files to pipelines
config_file_mapping = {
        "config_1.json" : "codepipeline-customization-sandbox-pipeline-1",
        "config_2.json" : "codepipeline-customization-sandbox-pipeline-2"
        }
        
codecommit_client = boto3.client('codecommit')
codepipeline_client = boto3.client('codepipeline')

def lambda_handler(event, context):
    # Extract commits
    old_commit_id = event["detail"]["oldCommitId"]
    new_commit_id = event["detail"]["commitId"]
    # Get commit differences
    codecommit_response = codecommit_client.get_differences(
        repositoryName="codepipeline-customization-sandbox-repo",
        beforeCommitSpecifier=str(old_commit_id),
        afterCommitSpecifier=str(new_commit_id)
    )
    # Search commit differences for files that trigger executions
    for difference in codecommit_response["differences"]:
        file_name = difference["afterBlob"]["path"].lower()
        # If file corresponds to pipeline, execute pipeline
        if file_name in config_file_mapping:
            codepipeline_response = codepipeline_client.start_pipeline_execution(
                name=config_file_mapping["file_name"]
                )