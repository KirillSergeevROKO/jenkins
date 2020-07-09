//Set variables
def MAIL_TO = "kirill.sergeev@rokolabs.com"
def CONFIG_PATH = "\\\\vm-roko-jenkins\\JENKINS\\STAGING_conf.groovy"
def ENV = STAGING // PROD or DEV

pipeline {
    agent { label 'vm-roko-jenkins' }

    stages {
        stage('Clear and create config file') {
            steps {
                    bat '''
                    del "%CONFIG_PATH"
                    echo. 2> "%CONFIG_PATH"
                    '''
            }
        }
        stage('Run IFP'){
            parallel {
                stage('Run IFP MSSQL'){
                    steps{
                        build job: "Run_IFP_process_MSSQL_${ENV}", wait: true
                    }

                }

                stage('Run IFP PGSQL'){
                    steps{
                       build job: "Run_IFP_process_PGSQL_${ENV}", wait: true 
                    }             

                }


            }

        }

        stage('IFP validation'){
                steps{
                    build job: "Run_IFP_validation_${ENV}", wait: true
               
                }

        }


        stage('Reports'){
            parallel{
                stage('Run CIF'){
                    steps{
                        build job: "Run_CIF_PGSQL_${ENV}", wait: true
                    }
                }

                stage('Run FirstKey'){
                    steps{
                        build job: "Run_FirstKey_PGSQL_${ENV}", wait: true
                    }
                }
            }
        }
    }  
}     