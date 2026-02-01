# run in openshift 

oc apply -f k8s

oc expose svc/api-service

oc get route 

## clean 

oc delete all --all

oc delete pvc --all

### images in use 
mysql:8.0
mosh5434/mysql-service:v1