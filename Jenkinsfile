pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/James20-DevOps/Projet_sysDev.git'
    }
        }
        stage('Build') {
            steps {
                sh 'mvn clean install'
                echo '---------------- Building...'
                // Add your build commands here
            }
        }
        stage('Test') {
            steps {
                sh 'mvn test'
                echo 'Testing...'
                // Add your test commands here
            }
        }
        stage('Test integration') {
            steps {
                sh 'mvn verify' //test d'integration
                echo '---------------- Running integration tests...'
                
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker build -t student_age.py .'
                sh 'docker run -d -p 5000:5000 student_age.py'
                echo 'Deploying...'
                // Add your deployment commands here
            }
        }
    }

    post {
        always {
            echo 'This will always run after the stages.'
        }
        success {
            echo 'This will run only if the pipeline succeeds.'
        }
        failure {
            echo 'This will run only if the pipeline fails.'
        }
    }
}
