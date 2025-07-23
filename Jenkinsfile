pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/James20-DevOps/Projet_sysDev.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv $VIRTUAL_ENV
                    source $VIRTUAL_ENV/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
                echo '✔️ Environnement Python prêt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                    source $VIRTUAL_ENV/bin/activate
                    python -m unittest discover -s tests
                '''
                echo '✔️ Tests unitaires exécutés'
            }
        }

        stage('Docker Deploy') {
            steps {
                sh '''
                    docker build -t student_age_app .
                    docker run -d -p 5000:5000 student_age_app
                '''
                echo '✔️ Application Flask déployée avec Docker'
            }
        }
    }

    post {
        always {
            echo 'Pipeline terminé'
        }
        success {
            echo 'Pipeline terminé avec succès '
        }
        failure {
            echo 'Le pipeline a échoué '
        }
    }
}
