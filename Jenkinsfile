pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = '1'
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
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest \
                      --html=reports/html/report.html \
                      --self-contained-html \
                      -v
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'

            publishHTML([
                target: [
                    [
                        reportDir: 'reports/html',
                        reportFiles: 'report.html',
                        reportName: 'Pytest HTML Report',
                        allowMissing: false,
                        keepAll: true,
                        alwaysLinkToLastBuild: true
                    ]
                ]
            ])
        }
    }
}
