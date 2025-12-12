pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --html=reports/html/report.html --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            publishHTML(
                reportDir: 'reports/html',
                reportFiles: 'report.html',
                reportName: 'Pytest HTML Report',
                allowMissing: false,
                keepAll: true,
                alwaysLinkToLastBuild: true
            )
        }
    }
}
