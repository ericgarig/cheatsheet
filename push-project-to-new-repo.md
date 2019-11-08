# About
Steps for pushing an existing project to a new git repository.

[Original post/source](https://stackoverflow.com/questions/3311774/how-to-convert-existing-non-empty-directory-into-a-git-working-directory-and-pus)



### Initialize Local Repository
 - first initialize Git with
```shell
git init
```

 - Add all Files for version control with
```shell
git add .
```

 - Create a commit with message of your choice

```shell
git commit -m 'initial commit'
```

### Initialize Remote Repository
 - Create a project on Github and copy the URL

### Link Remote repo with Local repo
 - Now use copied URL to link your local repo with remote GitHub repo. When you clone a repository with git clone, it automatically creates a remote connection called origin pointing back to the cloned repository. The command remote is used to manage set of tracked repositories.
```shell
git remote add origin «repo_url»
```

### Synchronize

 - Now we need to merge local code with remote code. This step is critical otherwise we won be able to Push Code on Github. You must call 'git pull' before pushing your code.

```shell
git pull origin master --allow-unrelated-histories
```

### Commit your code

 - Finally push all changes on Github

```shell
git push -u origin master
```
