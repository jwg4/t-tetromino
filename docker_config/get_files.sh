RES_GROUP=t-tetromino
ACI_STORAGE_ACCOUNT_NAME=ttsearchstorage
ACI_SHARE_NAME=search-output

STORAGE_KEY=$(az storage account keys list --resource-group $RES_GROUP --account-name $ACI_STORAGE_ACCOUNT_NAME --query "[0].value" --output tsv)

ID="0002"

az storage file download --share-name $ACI_SHARE_NAME --account-name $ACI_STORAGE_ACCOUNT_NAME --account-key=$STORAGE_KEY --path "output_${ID}.txt" --dest "results/output_${ID}.txt" --output none
