.PHONY:
git-push:
	@echo "${HEADER}"
	@echo "Pushing commit for ${PROJECT_NAME}"
	git status
	git add .
	git diff
	read -p "* Set your Commit description message :  " commit_message
	git commit -m "feat: new wrappered version of ${PROJECT_NAME}.wheel, description: $$commit_message"
	git push origin ${BRANCH_NAME}

.ONESHELL:
git:
	git status
	git add .
	git diff
	read -p "* Set your Commit message : " commit_message
	git commit -m "$$commit_message"
	git push origin ${BRANCH_NAME}

security-credentials:
	@echo Installing aws security Hooks
	@echo "${PWD}/${HOOK}"
	aws s3 cp s3://${BUCKET_NAME}/pre-commit ${PWD}/${HOOK}/pre-commit
	chmod +x ${PWD}/${HOOK}/pre-commit

global-hook: security-credentials
	git config --global init.templatedir '~/.git-templates'
	mkdir -p ~/.git-templates/hooks
	aws s3 cp s3://${BUCKET_NAME}/pre-commit ~/.git-templates/hooks/pre-commit
	chmod a+x ~/.git-templates/hooks/pre-commit
	git init