from re import template
import yaml, sys, subprocess
from jinja2 import Environment, FileSystemLoader

print('Script agrs:')
print(sys.argv)
print()

try:
    sys.argv[1]
except IndexError:
    print('Please select manifest file and run command like:')
    print('python3 templates.py file.yml')
    print()
    print('The list of manifest files:')
    subprocess.run(['ls', '../manifests'])
    sys.exit(1)

#### Manifest file parser ####
print('Manifest file parser')
mnfst_file = sys.argv[1]
from_mnfst = yaml.safe_load(open('../manifests/'+mnfst_file))
# print(from_mnfst)
# print(from_mnfst['app_name'])
app_name = from_mnfst['app_name']
app_file = from_mnfst['app_file']
git_url = from_mnfst['git']['git_url']
build_branch = from_mnfst['git']['build_branch']
hotfix_branch = from_mnfst['git']['hotfix_branch']
try:
    from_mnfst['git']['promote_branch']
except KeyError:
    promote_branch = build_branch
else:
    promote_branch = from_mnfst['git']['promote_branch']

print('app_name -', app_name)
print('git_url -', git_url)
print('build_branch -', build_branch)
print('hotfix_branch -', hotfix_branch)
print('promote_branch -', promote_branch)
print('app_file -', app_file)
print()

#### Craete jenkinsfile and JJB pipeline ####
print('Craete jenkinsfile for application -', app_name)
env = Environment(loader=FileSystemLoader('../templates'), trim_blocks=True, lstrip_blocks=True)
template_jf = env.get_template('build-jenkinsfile.j2')
file_jf_app = '%s%s%s' % ('../jenkinsfiles/Jenkinsfile_', app_name, '_build')
items = {'app_name': app_name, 'app_file': app_file, 'git_url': git_url, 'build_branch': build_branch, 'hotfix_branch': hotfix_branch, 'promote_branch': promote_branch, 'file_jf_app': file_jf_app}
file_jf = open(file_jf_app, 'w')
file_jf.write(template_jf.render(items))
file_jf.close()
subprocess.run(['ls', '-l', file_jf_app])
print()

print('JJB pipeline')
env = Environment(loader=FileSystemLoader('../templates'), trim_blocks=True, lstrip_blocks=True)
template_jjb = env.get_template('build-jenkins-job.j2')
file_jjb_yaml = '%s%s%s' % ('../jobs/', app_name, '-build-job.yaml')
file_jjb = open(file_jjb_yaml, 'w')
file_jjb.write(template_jjb.render(items))
file_jjb.close()
subprocess.run(['ls', '-l', file_jjb_yaml])
print()