# Jenkins CI/CD Setup Guide

This guide will help you set up Jenkins CI/CD for your Hugo static site, replacing your current GitLab CI/CD pipeline.

## Prerequisites

1. Jenkins server with Docker support
2. Jenkins plugins installed:
   - Pipeline plugin
   - Docker Pipeline plugin
   - Git plugin
   - SSH Agent plugin (if deploying via SSH)
   - AWS Steps plugin (if deploying to S3)

## Setup Steps

### 1. Create a New Pipeline Job

1. In Jenkins, click "New Item"
2. Enter a name for your job (e.g., "hugo-funny-moments")
3. Select "Pipeline" and click "OK"

### 2. Configure the Pipeline

1. In the job configuration, scroll to the "Pipeline" section
2. Select "Pipeline script from SCM"
3. Choose "Git" as SCM
4. Enter your repository URL
5. Set credentials if your repository is private
6. Set the branch specifier to `*/main` (or `*/master` if using master branch)
7. Set "Script Path" to `Jenkinsfile`

### 3. Configure Environment Variables

In the job configuration, under "Build Environment":

1. Check "Use secret text(s) or file(s)" if you need secure credentials
2. Add environment variables based on your deployment method:

#### For GitHub Pages Deployment:
```
DEPLOY_TO_GITHUB_PAGES=true
GITHUB_PAGES_REPO=git@github.com:yourusername/funny_moments.git
```

#### For SSH/Rsync Deployment:
```
DEPLOY_VIA_SSH=true
DEPLOY_USER=your-server-user
DEPLOY_HOST=your-server.com
DEPLOY_PATH=/var/www/html
```

#### For AWS S3 Deployment:
```
DEPLOY_TO_S3=true
AWS_REGION=us-east-1
S3_BUCKET=your-bucket-name
```

### 4. Set Up Credentials

Depending on your deployment method, add credentials in Jenkins:

#### For GitHub Pages:
1. Go to "Manage Jenkins" > "Manage Credentials"
2. Add a new SSH Username with private key credential
3. ID: `github-ssh-key`
4. Upload your GitHub SSH private key

#### For SSH Deployment:
1. Add SSH Username with private key credential
2. ID: `deploy-ssh-key`
3. Upload your server SSH private key

#### For AWS S3:
1. Add AWS Credentials
2. ID: `aws-credentials`
3. Enter your AWS Access Key ID and Secret Access Key

### 5. Configure Webhooks (Optional)

To trigger builds automatically on code pushes:

1. In your Git repository settings, add a webhook
2. URL: `http://your-jenkins-server/git/notifyCommit?url=YOUR_REPO_URL`
3. Select "Push events"

### 6. Test the Pipeline

1. Save the job configuration
2. Click "Build Now" to test the pipeline
3. Check the console output for any issues

## Pipeline Behavior

The Jenkins pipeline replicates your GitLab CI behavior:

- **Non-main branches**: Only builds Hugo site for testing
- **Main branch**: Builds Hugo site and deploys to production
- **Docker**: Uses the same `hugomods/hugo:exts` image as GitLab CI
- **Submodules**: Automatically checks out Git submodules (for your Hugo theme)

## Customization

### Modify Build Commands

Edit the `Jenkinsfile` to customize Hugo build commands:

```groovy
sh 'hugo --buildDrafts=false --buildFuture=false --minify'
```

### Add Build Steps

You can add additional steps like:
- Running tests
- Linting
- Security scans
- Performance checks

### Change Deployment Method

Uncomment and configure the deployment method you prefer in the `Deploy` stage.

## Troubleshooting

### Common Issues:

1. **Docker permission errors**: Ensure Jenkins user has Docker permissions
2. **Git submodule errors**: Check SSH keys and repository access
3. **Hugo build errors**: Verify Hugo version compatibility
4. **Deployment failures**: Check credentials and target server accessibility

### Debugging:

1. Check Jenkins console output
2. Enable debug logging in Jenkins
3. Test deployment commands manually on the Jenkins server

## Migration from GitLab CI

1. Remove `.gitlab-ci.yml` from your repository
2. Add `Jenkinsfile` to your repository root
3. Configure Jenkins job as described above
4. Update any deployment scripts to work with Jenkins environment variables
5. Test thoroughly before switching production deployments

## Security Considerations

1. Use Jenkins credentials store for sensitive data
2. Limit Jenkins agent access to necessary resources
3. Regularly update Jenkins and plugins
4. Use HTTPS for Jenkins web interface
5. Configure proper authentication and authorization
