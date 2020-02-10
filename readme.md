# Customizing triggers for AWS CodePipeline with AWS Lambda and Amazon CloudWatch Events

## Description

Recently I came across a certain issue. Whenever I commit a change to unimportant files like READme.md, it causes the whole pipeline to trigger again. Lot of people in different companies overlook that. When working in cloud, it seems we are charged on each deployment and build. So, actual purpose of this repo is to create an aws cloud lambda function that will be triggered when code is pushed to Code Commit. This will allow Code Pipeline to avoid reacting to unimportant files. 

This code provides certain files just for the sake of creating a pipeline. 

* index.html - sample file to show some deployment results on our public ip
* Buildspec.yml - build configurations
* appspec.yml - For deployment
* CODEDEPLOY.md - For installing code deploy on certain EC2 instance.
* lamdba-function.py - Python code for single pipeline 
* lambda-for-multiple-pipeline.py - Python code for multiple pipelines.


## Resources

You should have an aws account and understanding on how to create and run aws Pipeline. Knowledge of cloudwatch events and logs.

## Run the code

* Create a repository in code commit, push this code to code commit. 
* Create build and deploy stage and finally create a pipeline.
* Test if the pipeline is working. 
* Create a lambda function and paste single pipeline code into the function and save it.
* Goto cloudwatch events. You will see an event created in cloudwatch.
* Edit cloudwatch event and delete codepipeline trigger. Add a new trigger that is lambda function we just created. 


## Testing

* Push some new code into index.html and test if pipeline is executing automatically
* Push some new text in readme.md and see if the same pipeline executes again. 

## Reference

Original article:
https://aws.amazon.com/blogs/devops/adding-custom-logic-to-aws-codepipeline-with-aws-lambda-and-amazon-cloudwatch-events/

--------------------------------------

* Adeel Ahmed Khan (Adeel Barki) <br />
  __ _Full Stack Web Developer_ <br />
  _Front End Web Developer_ <br />
  _React Web Developer_ __ <br />
