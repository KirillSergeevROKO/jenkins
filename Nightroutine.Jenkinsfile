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

        stage('Read config file'){
            script{
                    load "${CONFIG_PATH}"

                    echo "From Config File"
                    echo "${env.IFP_MSSQL}"
                    echo "${env.IFP_PGSQL}"
                    echo "${env.IFP_VALIDATION}"
                    echo "${env.CIF_REPORTS}"
                    echo "${env.FIRSTKEY_REPORTS}"
                    def today = new Date()
                    def yesterday = today.previous()
                    def env.formated_date = today.format("yyyy-MM-dd")

            }
        }

    } 

       post {
        success {
            mail to: "${MAIL_TO}",
            subject: "Status of pipeline: ${currentBuild.fullDisplayName}",
            body: """
                <html>
                <p>===========================================</p>
                <p>NightRoutin Process - <strong>${env.formated_date}</strong></p>
                <h3><span style="background-color: #00ff00; color: #003366;">${currentBuild.result}</span></h3>
                <table style="height: 250px; width: 365px; background-color: #000000; float: left;" border="1" cellspacing="0" cellpadding="3">
                <thead><tr style="height: 4px; text-align: left;"><td style="width: 139.925px; height: 4px;"><span style="color: #ffffff;">IFP MsSQL</span></td>
                <td style="width: 97.0755px; height: 4px;"><br />
                <div><div><span style="color: #ffffff;">${env.IFP_MSSQL}</span></div>
                </div></td></tr><tr style="height: 29.1368px; text-align: left;"> <td style="width: 139.925px; height: 29.1368px;"><span style="color: #ffffff;">IFP PgSQL</span></td>
                <td style="width: 97.0755px; height: 29.1368px;">&nbsp;<div>
                <div><span style="color: #ffffff;">${env.IFP_PGSQL}</span></div></div></td> </tr>
                <tr style="height: 24px; text-align: left;"><td style="width: 139.925px; height: 24px;"><span style="color: #ffffff;">IFP Validation</span></td>
                <td style="width: 97.0755px; height: 24px;">&nbsp;<div>
                <div><span style="color: #ffffff;">${env.IFP_VALIDATION}</span></div></div></td></tr><tr style="height: 10px; text-align: left;">
                <td style="width: 139.925px; height: 10px;"><span style="color: #ffffff;">CIF Reports</span></td> <td style="width: 97.0755px; height: 10px;">&nbsp;
                <div><div><span style="color: #ffffff;">${env.CIF_REPORTS}</span></div></div></td></tr><tr style="height: 10px; text-align: left;">
                <td style="width: 139.925px; height: 10px;"><span style="color: #ffffff;">FirstKey Reports</span></td><td style="width: 97.0755px; height: 10px;">
                <div><div><span style="color: #ffffff;">${env.FIRSTKEY_REPORTS}</span></div></div></td></tr></thead></table><p>&nbsp;</p>
                <p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>The total time it took to complite the process -</p>
                <div><div><strong>${currentBuild.number}</strong></div><div>&nbsp;</div><div><strong>=========================================</strong></div>
                <div>&nbsp;</div><div>You can find additional details on this link:<br /><div><div>${env.BUILD_URL}</div></div>
                <br /><br /></div>
                </div>
                </html>
                 """,
            mimeType: 'text/html'
        }
         failure {
            mail to: "${MAIL_TO}",
            subject: "FAILED in pipeline: ${currentBuild.fullDisplayName} ${currentBuild.result} ",
            body: """
                <html>
                <p>===========================================</p>
                <p>NightRoutin Process - <strong>${env.formated_date}</strong></p>
                <h3><span style="background-color: #ff0000; color: #003366;">${currentBuild.result}</span></h3>
                <table style="height: 250px; width: 365px; background-color: #000000; float: left;" border="1" cellspacing="0" cellpadding="3">
                <thead><tr style="height: 4px; text-align: left;"><td style="width: 139.925px; height: 4px;"><span style="color: #ffffff;">IFP MsSQL</span></td>
                <td style="width: 97.0755px; height: 4px;"><br /><div><div><span style="color: #ffffff;">${env.IFP_MSSQL}</span></div>
                </div></td></tr><tr style="height: 29.1368px; text-align: left;"><td style="width: 139.925px; height: 29.1368px;"><span style="color: #ffffff;">IFP PgSQL</span></td>
                <td style="width: 97.0755px; height: 29.1368px;">&nbsp;<div><div><span style="color: #ffffff;">${env.IFP_PGSQL}</span></div>
                </div></td></tr><tr style="height: 24px; text-align: left;"><td style="width: 139.925px; height: 24px;"><span style="color: #ffffff;">IFP Validation</span></td>
                <td style="width: 97.0755px; height: 24px;">&nbsp;<div><div><span style="color: #ffffff;">${env.IFP_VALIDATION}</span></div>
                </div></td></tr><tr style="height: 10px; text-align: left;"><td style="width: 139.925px; height: 10px;"><span style="color: #ffffff;">CIF Reports</span></td>
                <td style="width: 97.0755px; height: 10px;">&nbsp;<div><div><span style="color: #ffffff;">${env.CIF_REPORTS}</span></div></div>
                </td></tr><tr style="height: 10px; text-align: left;"><td style="width: 139.925px; height: 10px;"><span style="color: #ffffff;">FirstKey Reports</span></td>
                <td style="width: 97.0755px; height: 10px;"><div>
                <div><span style="color: #ffffff;">${env.FIRSTKEY_REPORTS}</span></div></div></td></tr></thead>
                </table><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p>
                <p>&nbsp;</p><p>The total time it took to complite the process -</p>
                <div><div><strong>${currentBuild.number}</strong></div>
                <div>&nbsp;</div><div><strong>=========================================</strong></div><div>We have a some problem, please check it on this link:<br />
                <div><div>${env.BUILD_URL}</div> </div><br /><br /></div></div>
                </html>
                 """,
            mimeType: 'text/html'
                    
        }
    }  
}     