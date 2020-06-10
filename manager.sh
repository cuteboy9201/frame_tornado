#!/bin/bash 
### 
# @Author: Youshumin
# @Date: 2019-11-15 12:01:01
 # @LastEditors: YouShumin
 # @LastEditTime: 2020-06-10 12:18:04
# @Description: 
###

workdir=$(cd $(dirname $0); pwd) 
export PYTHONPATH=$PYTHONPATH:${workdir} 
export RUN_ENV=prod
pyenv="python"
start_main(){
    cd $workdir
    ${pyenv} run_server.py
}

case "$1" in 
    start)
        start_main
        ;;
    *)
        echo "start"
        ;;
esac