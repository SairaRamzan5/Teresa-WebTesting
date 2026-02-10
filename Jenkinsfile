// Jenkinsfile - Declarative Pipeline
pipeline {
    agent {
        docker {
            image 'mcr.microsoft.com/playwright/python:v1.40.0-focal'
            args '-u root --shm-size=2gb'
        }
    }
    
    environment {
        BASE_URL = credentials('base-url')
        TEST_USER = credentials('test-user')
        TEST_PASSWORD = credentials('test-password')
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install pytest pytest-html
                '''
            }
        }
        
        stage('Run Playwright Tests') {
            steps {
                sh '''
                    python -m pytest tests/ \
                        --html=report.html \
                        --self-contained-html \
                        --junitxml=report.xml \
                        -v
                '''
            }
        }
        
        stage('Publish Results') {
            steps {
                junit 'report.xml'
                publishHTML([
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Playwright Test Report'
                ])
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
            cleanWs()
        }
        failure {
            emailext (
                subject: "Playwright Tests Failed: ${env.JOB_NAME} - ${env.BUILD_NUMBER}",
                body: "Check console output at ${env.BUILD_URL}",
                to: 'team@example.com'
            )
        }
    }
}
