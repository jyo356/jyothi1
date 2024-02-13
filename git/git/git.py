pipeline {

agent any

stages {

  stage ("Git") {

     steps {
        echo "we will clone git"
        sh "git init"
        sh "git pull https://github.com/jyo356/jyothi1.git"
        sh "ls"
        sh "git log --oneline"
     }
   }

  stage ("Build") {

     steps {
        echo "lets build a code" 
     }
   }

  stage ("Test") {

     steps {
        echo "lets test a code"
     }
   }

  stage ("Deploy") {

     steps {
        echo "lets deploy a code"
     }
   }
}
}
