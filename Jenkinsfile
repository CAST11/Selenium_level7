pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/CAST11/Selenium_level7'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh """
					echo "Python version:"
                    python3 --version
					
					echo "Creating virtual env"
                    python3 -m venv venv
					
					echo "Activating virtualenv"
                    . venv/bin/activate
					
					echo "Upgrading pip"
                    pip install --upgrade pip
					
                    echo "Installing requirements"
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh """
					echo "Activating virtualenv"
                    . venv/bin/activate
                    pytest --html=report.html --self-contained-html
                """
            }
        }
    }

    post {
        always {
			echo 'Pipeline finished'
            publishHTML(target: [
    reportDir: 'reports/html',
    reportFiles: 'report.html',
    reportName: 'Automation Test Report',
    keepAll: true,
    alwaysLinkToLastBuild: true,
    allowMissing: false)
        }
		failure {
            echo 'Tests failed!'
        }
    }
}
