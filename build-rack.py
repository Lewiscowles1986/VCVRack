#!/usr/bin/env python3

import json
import subprocess
import multiprocessing

# Rack brew dependencies
# brew install git wget cmake autoconf automake libtool jq python zstd

def github_clone_cmd(user, repo):
    return ['git', 'clone', f'https://github.com/{user}/{repo}.git']

def git_switch_cmd(branch):
    return ['git', 'checkout', branch]

NUM_CORES = multiprocessing.cpu_count()

BUILD_COMMANDS = [
    ['git', 'submodule', 'update', '--init', '--recursive'],
    ['make', '-j', str(NUM_CORES), 'dep'],
    ['make', '-j', str(NUM_CORES)],
    # Address sanitizer (ASAN) build commands
    #['make', '-j', str(NUM_CORES), 'dep', 'EXTRA_FLAGS=-fsanitize=address', 'EXTRA_LDFLAGS=-fsanitize=address'],
    #['make', '-j', str(NUM_CORES), 'EXTRA_FLAGS=-fsanitize=address', 'EXTRA_LDFLAGS=-fsanitize=address'],
    ]

# Rack
rack_dir = '.'
#subprocess.run(github_clone_cmd('VCVRack', 'Rack'))
#rack_dir = 'Rack'
for command in BUILD_COMMANDS:
    subprocess.run(command, cwd=rack_dir)

with open('modules.json', 'r') as f:
  data = json.load(f)

plugin_array = data['plugins']
plugins_dir = rack_dir + '/plugins'
for plugin in plugin_array:
    subprocess.run(github_clone_cmd(plugin['user'], plugin['repo']), cwd=plugins_dir)

    working_dir = plugins_dir + '/' + plugin['repo']
    if 'branch' in plugin:
        subprocess.run(git_switch_cmd(plugin['branch']), cwd=working_dir)
    for command in BUILD_COMMANDS:
        subprocess.run(command, cwd=working_dir)
