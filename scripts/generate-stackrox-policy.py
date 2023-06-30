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
        
def build_policy(root):
    policy = {}
    policy['name'] = "GTFOBins component in image"
    policy['description'] = "Alert on deployments with GTFOBins components present"
    policy['rationale'] = "Leaving GTFOBins components inside container images makes it easier for attackers to 'live off the land' inside a container environment"
    policy['remediation'] = "Use your package manager's \"remove\", \"purge\" or \"erase\" command to remove GTFOBins components from the image build for production containers."
    policy['disabled'] = False
    policy['categories'] = ["Security best practices"]
    policy['lifecycleStages'] = ["BUILD","DEPLOY"]
    policy['eventSource'] = "NOT_APPLICABLE"
    policy['exclusions'] = []
    policy['scope'] = []
    policy['severity'] = "LOW_SEVERITY"
    policy['enforcementActions'] = []
    policy['notifiers'] = []
    policy['SORTName'] = "GTFOBins component in image"
    policy['SORTLifecycleStage'] = "BUILD,DEPLOY"
    policy['SORTEnforcement'] = False
    policy['policyVersion'] = "1.0"
    section = {}
    section['sectionName'] = ""
    section['policyGroups'] = []
    section['policyGroups'].append({})
    section['policyGroups'][0]['fieldName'] = "Image Component"
    section['policyGroups'][0]['booleanOperator'] = "OR"
    section['policyGroups'][0]['negate'] = False
    section['policyGroups'][0]['values'] = []

    names = get_gtfobins(root)
    for name in names:
        section['policyGroups'][0]['values'].append({"value": '%s' % "".join([name,"="])})

    policy['policySections'] = section
    policy['mitreAttackVectors'] = []
    policy['criteriaLocked'] = True
    policy['mitreVectorsLocked'] = True
    policy['isDefault'] = False
    return policy

if __name__ == '__main__':
    policy = build_policy("_gtfobins/")
    print(json.dumps({"policies": [ policy ]}))