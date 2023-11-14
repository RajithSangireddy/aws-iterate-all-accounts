 for p in $(aws configure list-profiles | grep baseline); do echo $p && export AWS_PROFILE=$p && python3 wiz_script_v2.py --data; done
