# Git initialization configuration

## Configure git to connect Github:
git config --global user.name "c999"
git config --global user.email "xxx@qq.com"
git config --global color.ui auto

## Generate ssh key:
ssh-keygen -t rsa -C "xxx@qq.com"


## Add ssh public key into Github:
Settings --> SSH and GPG keys --> New SSH key

## Testing:
ssh -T git@github.com

Successful message:
Hi c999! You've successfully authenticated, but GitHub does not provide shell access.


## Clone repositories to local:
git clone git@github.com:c999/aws.git
git clone git@github.com:c999/machine-learning.git
git clone git@github.com:c999/data-analytics.git


