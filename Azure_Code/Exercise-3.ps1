###################PowerShell - Create an Azure Blob Storage and integrate it with VNet.

# Create Resource Group 
New-AzResourceGroup -Name 'ABT-Exercise-rg' -Location 'centralus'

# Create Storage Account with Blob Storage  (For VNET Connectivity)
New-AzureRmStorageAccount -ResourceGroupName ABT-Exercise-rg -AccountName abtsg -Location centralus -SkuName Standard_GRS -Kind BlobStorage -AccessTier Hot

# Create VNet
$vnet = @{
    Name = 'abtVNet'
    ResourceGroupName = 'ABT-Exercise-rg'
    Location = 'centralus'
    AddressPrefix = '10.0.0.0/16'    
}
$virtualNetwork = New-AzVirtualNetwork @vnet

# Add subnet 

$subnet = @{
    Name = 'app'
    VirtualNetwork = $virtualNetwork
    AddressPrefix = '10.0.0.0/24'
}
$subnetConfig = Add-AzVirtualNetworkSubnetConfig @subnet

# Associate subnet to Vnet
$virtualNetwork | Set-AzVirtualNetwork

# Set the default rule to deny network access by default.

Update-AzStorageAccountNetworkRuleSet -ResourceGroupName "ABT-Exercise-rg" -Name "abtsg" -DefaultAction Deny

#Display the status of the default rule for the storage account.
(Get-AzStorageAccountNetworkRuleSet -ResourceGroupName "ABT-Exercise-rg" -AccountName "abtsg").DefaultAction


# List virtual network rules
(Get-AzStorageAccountNetworkRuleSet -ResourceGroupName "ABT-Exercise-rg" -AccountName "abtsg").VirtualNetworkRules

# Enable service endpoint for Azure Storage on an existing virtual network and subnet
Get-AzVirtualNetwork -ResourceGroupName "ABT-Exercise-rg" -Name "abtVNet" | Set-AzVirtualNetworkSubnetConfig -Name "app" -AddressPrefix "10.0.0.0/24" -ServiceEndpoint "Microsoft.Storage" | Set-AzVirtualNetwork

# Add a network rule for a virtual network and subnet
$subnet = Get-AzVirtualNetwork -ResourceGroupName "ABT-Exercise-rg" -Name "abtVNet" | Get-AzVirtualNetworkSubnetConfig -Name "app"
Add-AzStorageAccountNetworkRule -ResourceGroupName "ABT-Exercise-rg" -Name "abtsg" -VirtualNetworkResourceId $subnet.Id


# Create Storage Account with Blob Storage  (For Private Endpoint )

New-AzureRmStorageAccount -ResourceGroupName ABT-Exercise-rg -AccountName abtsgpend -Location centralus -SkuName Standard_GRS -Kind BlobStorage -AccessTier Hot

# Create VNet
$vnet = @{
    Name = 'abtVNetend'
    ResourceGroupName = 'ABT-Exercise-rg'
    Location = 'centralus'
    AddressPrefix = '10.0.0.0/16'    
}
$virtualNetwork = New-AzVirtualNetwork @vnet

# Add subnet 

$subnet = @{
    Name = 'append'
    VirtualNetwork = $virtualNetwork
    AddressPrefix = '10.0.0.0/24'
}
$subnetConfig = Add-AzVirtualNetworkSubnetConfig @subnet

# Associate subnet to Vnet
$virtualNetwork | Set-AzVirtualNetwork

# Set the default rule to deny network access by default.
Update-AzStorageAccountNetworkRuleSet -ResourceGroupName "ABT-Exercise-rg" -Name "abtsgpend" -DefaultAction Allow

#create Private Link 
# Create Private Link  between Storage account and VNet using UI 




