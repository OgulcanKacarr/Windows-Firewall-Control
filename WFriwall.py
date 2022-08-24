import argparse
import os


os.system("cls")

print("""

	created by Ogulcan KACAR
	www.github.com/OgulcanKacarr


--------------------------------------
	allow/deny port required
	-n :  RuleName:   myRule
	-t :  RuleType:   in/out
	-ac:  RuleAction: allow/block/bypass
	-pr:  protocol:   tcp/udp
	-p :  port:       ports  

	allow/deny program required +
	-pt:  path:       program_path
	-pp:  profile:    any


	""")


def blockOrAllowPort(name,type,action,protocol,localport):
	os.popen(f'netsh advfirewall firewall add rule name={name.capitalize().strip()} dir={type.lower()} action={action.lower()} protocol={protocol.upper()} localport={localport}')
	rule = f'netsh advfirewall firewall add rule name={name.capitalize().strip()} dir={type.lower()} action={action.lower()} protocol={protocol.upper()} localport={localport}'
	print(f'rule > {rule} added')


def blockOrAllowProgram(name,type,path,action, profile='any'):
	os.popen(f'netsh advfirewall firewall add rule name={name} dir={type} program={path} profile={profile} action={action}')
	rule = f'netsh advfirewall firewall add rule name={name} dir={type} program={path} profile={profile} action={action}'
	print(f'rule > {rule} added')


ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True, help="Rule name")
ap.add_argument("-t", "--type", required=True, help="Rule type: in/out")
ap.add_argument("-ac", "--action", required=True, help="action: allow/block/bypass")
ap.add_argument("-pr", "--protocol", required=True, help="protocol: tcp/udp")
ap.add_argument("-p", "--port", required=True, help="local port")
ap.add_argument("-pt", "--path", required=False, help="Program path")
ap.add_argument("-pp", "--profile", required=False, help="Profile")

args = vars(ap.parse_args())

ruleName =args["name"]
ruleType = args["type"]
ruleAction = args["action"]
ruleProtocol = args["protocol"]
rulePort = args["port"]
rulePath = args["path"]
ruleProfile = args["profile"]


try:
	if(rulePath == "path"):
		blockOrAllowProgram(ruleName,ruleType,rulePath,ruleProfile,ruleAction)
	else:
		blockOrAllowPort(ruleName,ruleType,ruleAction,ruleProtocol,rulePort)
except Exception as e:
	print(f'error > {e}')
