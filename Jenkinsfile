pipeline {
    agent {
        docker {
            image 'hugomods/hugo:exts'
            args '--user root'
        }
    }
    
    environment {
        GIT_SUBMODULE_STRATEGY = 'recursive'
        THEME_URL = 'github.com/adityatelange/hugo-PaperMod'
    }
    
    options {
        // Keep builds for 30 days
        buildDiscarder(logRotator(daysToKeepStr: '30'))
        // Timeout after 10 minutes
        timeout(time: 10, unit: 'MINUTES')
        // Clean workspace before build
        skipDefaultCheckout()
    }
    
    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout with submodules
                    checkout([
                        $class: 'GitSCM',
                        branches: scm.branches,
                        doGenerateSubmoduleConfigurations: false,
                        extensions: [
                            [$class: 'SubmoduleOption',
                             disableSubmodules: false,
                             parentCredentials: true,
                             recursiveSubmodules: true,
                             reference: '',
                             trackingSubmodules: false]
                        ],
                        submoduleCfg: [],
                        userRemoteConfigs: scm.userRemoteConfigs
                    ])
                }
            }
        }
        
        stage('Test Build') {
            when {
                not {
                    anyOf {
                        branch 'main'
                        branch 'master'
                    }
                }
            }
            steps {
                echo 'Building Hugo site for testing...'
                sh 'hugo --buildDrafts=false --buildFuture=false'
            }
            post {
                always {
                    // Clean up test build artifacts
                    sh 'rm -rf public'
                }
            }
        }
        
        stage('Build for Production') {
            when {
                anyOf {
                    branch 'main'
                    branch 'master'
                }
            }
            steps {
                echo 'Building Hugo site for production...'
                sh 'hugo --buildDrafts=false --buildFuture=false --minify'
                
                // Copy CNAME file if it exists
                script {
                    if (fileExists('CNAME')) {
                        sh 'cp CNAME public/'
                    }
                }
            }
        }
        
        stage('Deploy') {
            when {
                anyOf {
                    branch 'main'
                    branch 'master'
                }
            }
            steps {
                echo 'Deploying to production...'
                
                // Archive the build artifacts
                archiveArtifacts artifacts: 'public/**/*', fingerprint: true
                
                // Example deployment steps - customize based on your deployment target
                script {
                    // If deploying to GitHub Pages
                    if (env.DEPLOY_TO_GITHUB_PAGES == 'true') {
                        sshagent(['github-ssh-key']) {
                            sh '''
                                cd public
                                git init
                                git config user.name "Jenkins"
                                git config user.email "jenkins@yourdomain.com"
                                git add .
                                git commit -m "Deploy from Jenkins - Build #${BUILD_NUMBER}"
                                git remote add origin ${GITHUB_PAGES_REPO}
                                git push -f origin main:gh-pages
                            '''
                        }
                    }
                    
                    // If deploying via rsync/ssh
                    if (env.DEPLOY_VIA_SSH == 'true') {
                        sshagent(['deploy-ssh-key']) {
                            sh '''
                                rsync -avz --delete public/ ${DEPLOY_USER}@${DEPLOY_HOST}:${DEPLOY_PATH}
                            '''
                        }
                    }
                    
                    // If deploying to AWS S3
                    if (env.DEPLOY_TO_S3 == 'true') {
                        withAWS(region: env.AWS_REGION, credentials: 'aws-credentials') {
                            s3Upload(bucket: env.S3_BUCKET, 
                                   path: '', 
                                   includePathPattern: '**/*', 
                                   workingDir: 'public',
                                   acl: 'PublicRead')
                        }
                    }
                }
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed'
            // Clean workspace
            cleanWs()
        }
        
        success {
            echo 'Pipeline succeeded!'
            // You can add notification steps here
            // emailext subject: "✅ Hugo Site Deploy Success - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            //          body: "The Hugo site has been successfully built and deployed.",
            //          to: "${env.NOTIFICATION_EMAIL}"
        }
        
        failure {
            echo 'Pipeline failed!'
            // You can add notification steps here
            // emailext subject: "❌ Hugo Site Deploy Failed - ${env.JOB_NAME} #${env.BUILD_NUMBER}",
            //          body: "The Hugo site build or deployment failed. Please check the logs.",
            //          to: "${env.NOTIFICATION_EMAIL}"
        }
    }
}
