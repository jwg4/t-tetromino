ACR_LOGIN_SERVER=ttdocker.azurecr.io
RES_GROUP=t-tetromino
AKV_NAME=ttkeyvalut
ACR_NAME=ttdocker
ACI_STORAGE_ACCOUNT_NAME=ttsearchstorage
ACR_REPO=tt_repository

ACI_SHARE_NAME=minimal-output
TAG=27d583f1
IMAGE_NAME=minimal
CONTAINER_NAME=minimalcontainer

ACR_USERNAME=$(az keyvault secret show --vault-name $AKV_NAME -n $ACR_NAME-pull-usr --query value -o tsv)
ACR_PASSWORD=$(az keyvault secret show --vault-name $AKV_NAME -n $ACR_NAME-pull-pwd --query value -o tsv)
STORAGE_KEY=$(az storage account keys list --resource-group $RES_GROUP --account-name $ACI_STORAGE_ACCOUNT_NAME --query "[0].value" --output tsv)


az container create \
--resource-group $RES_GROUP \
--name $CONTAINER_NAME \
--image $ACR_NAME.azurecr.io/$ACR_REPO/$IMAGE_NAME:$TAG \
--registry-login-server $ACR_LOGIN_SERVER \
--registry-username $ACR_USERNAME \
--registry-password $ACR_PASSWORD \
--restart-policy Never
--azure-file-volume-account-name $ACI_PERS_STORAGE_ACCOUNT_NAME \
--azure-file-volume-account-key $STORAGE_KEY \
--azure-file-volume-share-name $ACI_PERS_SHARE_NAME \
--azure-file-volume-mount-path /aci/output/

az container show --resource-group $RES_GROUP --name $CONTAINER_NAME --out table
