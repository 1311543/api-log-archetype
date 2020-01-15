#!/usr/bin/env bash
PROJECT_TAG ?= 0.0.1
PROJECT_ADDRESS ?= ${PROJECT_NAME}:${PROJECT_TAG}
BRANCH_NAME ?= belc-dlk-library
PROJECT_NAME ?= belc_log
BUCKET_NAME ?= repository-python-archetype
HOOK ?= .git/hooks
HEADER ?= ***************************