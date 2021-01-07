ACR_LOGIN_SERVER=ttdocker.azurecr.io
RES_GROUP=t-tetromino
TAG=27d583f1
AKV_NAME=ttkeyvalut
ACR_NAME=ttdocker

az container create --resource-group $RES_GROUP --name mycontainer --image $ACR_NAME.azurecr.io/tt_repository/minimal:$TAG --registry-login-server $ACR_LOGIN_SERVER --registry-username $(az keyvault secret show --vault-name $AKV_NAME -n $ACR_NAME-pull-usr --query value -o tsv) --registry-password $(az keyvault secret show --vault-name $AKV_NAME -n $ACR_NAME-pull-pwd --query value -o tsv) --restart-policy Never

az container show --resource-group $RES_GROUP --name mycontainer --out table
