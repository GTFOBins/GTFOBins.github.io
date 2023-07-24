import json
import os
import re

def get_gtfobins(root):
    root, _, files = next(os.walk(root))
    names = []
    for name in files:
        if not name.endswith('.md'):
            continue
        names.append(re.split("(.*)\.md",name)[1])
    return names
        
def build_policies(root):
    policies = []

    polmap = {'build': {}, 'runtime': {}}
    polmap['build']['name'] = "GTFOBins component in image"
    polmap['build']['description'] = "Alert on deployments with GTFOBins components present"
    polmap['build']['lifecycleStages'] = ["BUILD","DEPLOY"]
    polmap['build']['sortName'] = "GTFOBins component in image"
    polmap['build']['sortLifecycleStage'] = "BUILD,DEPLOY"
    polmap['build']['eventSource'] = "NOT_APPLICABLE"
    polmap['build']['fieldName'] = "Image Component"

    polmap['runtime']['name'] = "GTFOBins component execution detected"
    polmap['runtime']['description'] = "Detects contains running a GTFOBins component"
    polmap['runtime']['lifecycleStages'] = ["RUNTIME"]
    polmap['runtime']['sortName'] = "GTFOBins component execution"
    polmap['runtime']['sortLifecycleStage'] = "RUNTIME"
    polmap['runtime']['eventSource'] = "DEPLOYMENT_EVENT"
    polmap['runtime']['fieldName'] = "Process Name"

    for key in polmap:
        policy = {}
        policy['name'] = polmap[key]['name']
        policy['description'] = polmap[key]['description']
        policy['rationale'] = "Leaving GTFOBins components inside container images makes it easier for attackers to 'live off the land' inside a container environment"
        policy['remediation'] = "Use your package manager's \"remove\", \"purge\" or \"erase\" command to remove GTFOBins components from the image build for production containers."
        policy['disabled'] = False
        policy['categories'] = ["Security Best Practices"]
        policy['lifecycleStages'] = polmap[key]['lifecycleStages']
        policy['eventSource'] = polmap[key]['eventSource']
        policy['exclusions'] = []
        policy['scope'] = []
        policy['severity'] = "LOW_SEVERITY"
        policy['enforcementActions'] = []
        policy['notifiers'] = []
        policy['SORTName'] = polmap[key]['sortName']
        policy['SORTLifecycleStage'] = polmap[key]["sortLifecycleStage"]
        policy['SORTEnforcement'] = False
        policy['policyVersion'] = "1.1"
        section = {}
        section['sectionName'] = "Policy Section 1"
        section['policyGroups'] = []
        section['policyGroups'].append({})
        section['policyGroups'][0]['fieldName'] = polmap[key]["fieldName"]
        section['policyGroups'][0]['booleanOperator'] = "OR"
        section['policyGroups'][0]['negate'] = False
        section['policyGroups'][0]['values'] = []

        names = get_gtfobins(root)
        for name in names:
            if(key == "build"):
                section['policyGroups'][0]['values'].append({"value": '%s' % "".join([name,"="])})
            else:
                section['policyGroups'][0]['values'].append({"value": '%s' % name })

        policy['policySections'] = [section]
        policy['mitreAttackVectors'] = []

        # TA0002 - Execution. Many of the GTFOBins components enable execution
        # in various contexts.
        policy['mitreAttackVectors'].append({
            "tactic": "TA0002",
            "techniques": ["T1059.004"]
        })

        # TA0007 - Discovery. Binaries like dmidecode can be used to provide information
        # on the environment
        policy['mitreAttackVectors'].append({
            "tactic": "TA0007",
            "techniques": ["T1046"]
        }) 

        # TA0008 - Lateral movement. Binaries like ssh and netcat can be used 
        # to enable lateral movement.
        policy['mitreAttackVectors'].append({
            "tactic": "TA0008",
            "techniques": ["T1570"]
        })

        # TA0010 - Exfiltration. Binaries like tar, curl and tftp can be used to exfiltrate
        # data from environments.
        policy['mitreAttackVectors'].append({
            "tactic": "TA0010",
            "techniques": ["T1567"]
        })

        # TA0043 - Reconnaissance. 
        policy['mitreAttackVectors'].append({
            "tactic": "TA0043",
            "techniques": ["T1592"]
        })

        policy['criteriaLocked'] = False
        policy['mitreVectorsLocked'] = False
        policy['isDefault'] = False
        policies.append(policy)

    return policies

if __name__ == '__main__':
    policy = build_policies("_gtfobins/")
    print(json.dumps({"policies": [ policy ]}))