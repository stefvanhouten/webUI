pipeline {
    agent {
    docker { image 'python:2.7.16-stretch' }
    }
    stages {
        stage('build') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python --version'
                    sh 'pip install --user pylint'
                    sh 'pip install --user flask'
                    sh 'pip install --user flask_cors'
                    sh 'pip install --user marshmallow'
                }
            }
        }
        stage('analysis') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    script {
                        try {
                            sh '''
                            #!/bin/bash
                            find . -name \\*.py| grep -v test | grep -v \\.local | grep -v env | xargs python2 -m pylint --rcfile=.pylintrc --exit-zero --output-format=parseable --reports=y | tee pylint.log
                            '''
                        } catch(Exception e) {
                            echo "EXCEPTION: ${e}" 
                        } finally {
                            def pyLintIssues = scanForIssues tool: pyLint(pattern: 'pylint.log')
                            publishIssues id: 'pyLint', qualityGates: [[threshold: 1, type: 'TOTAL_ERROR', unstable: true], [threshold: 15, type: 'TOTAL_HIGH', unstable: true]], issues: [pyLintIssues], name: 'pyLint'
                        }
                    }
                }
            }
        }
    }
}