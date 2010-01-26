#!/bin/bash
# We want to replace all mentions of django.contrib.messages with
# django_messages_framework.

echo 'Replacing all mentions of django.contrib.messages with django_messages_framework...'

find . -name '*.py' -print | xargs sed -i '' 's/django\.contrib\.messages/django_messages_framework/g'

echo 'All done!'
