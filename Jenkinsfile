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
                    source venv/bin/activate
                    pytest --html=report.html --self-contained-html
                """
            }
        }
    }

    post {
        always {
			echo 'Pipeline finished'
            publishHTML([[
                allowMissing: false,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Pytest HTML Report'
            ]])
        }
		failure {
            echo 'Tests failed!'
        }
    }
}
