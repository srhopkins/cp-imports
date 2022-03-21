# cp-imports

Outputs Cloud Posse import chains from stack configs. Supports both text concatenation and mermaid flowcharts. 

## Install

```
pip install --user git+https://github.com/srhopkins/cp-imports.git 
```

## Usage

```
usage: imports.py [-h] [-d STACK_DIR] [-f FLOWCHART] [-l LOGGING_LEVEL] [-m | --mermaid | --no-mermaid] [-o | --open-mermaid | --no-open-mermaid] stack

positional arguments:
  stack                 stack file to read imports from

optional arguments:
  -h, --help            show this help message and exit
  -d STACK_DIR, --stack-dir STACK_DIR
                        base stack directory name (default: stacks/)
  -f FLOWCHART, --flowchart FLOWCHART
                        https://mermaid-js.github.io/mermaid/#/flowchart?id=flowchart-orientation (default: LR)
  -l LOGGING_LEVEL, --logging-level LOGGING_LEVEL
                        execution logging level (default: info)
  -m, --mermaid, --no-mermaid
                        output mermaid graph (default: False)
  -o, --open-mermaid, --no-open-mermaid
                        open mermaid graph in browser (default: False)

```



## Example Mermaid Flowchart

```mermaid
flowchart LR
  i1["/core/gbl/audit.yaml"] --> i2["../cptest/infra-test/stacks/core/gbl/globals.yaml"]
  i1 --> i3["../cptest/infra-test/stacks/gbl/audit.yaml"]
  i2 --> i4["../cptest/infra-test/stacks/core/globals.yaml"]
  i4 --> i5["../cptest/infra-test/stacks/globals.yaml"]
  i3 --> i6["../cptest/infra-test/stacks/gbl/globals.yaml"]
  i3 --> i7["../cptest/infra-test/stacks/catalog/iam-delegated-roles.yaml"]
  i6 --> i8["../cptest/infra-test/stacks/catalog/account-settings.yaml"]
  i6 --> i9["../cptest/infra-test/stacks/catalog/compliance/baseline.yaml"]
  i9 --> i10["../cptest/infra-test/stacks/catalog/compliance/regional/ap-south-1.yaml"]
  i9 --> i11["../cptest/infra-test/stacks/catalog/compliance/regional/eu-west-1.yaml"]
  i9 --> i12["../cptest/infra-test/stacks/catalog/compliance/regional/us-west-2.yaml"]
  i9 --> i13["../cptest/infra-test/stacks/catalog/compliance/regional/ap-southeast-2.yaml"]
  i9 --> i14["../cptest/infra-test/stacks/catalog/compliance/regional/ca-central-1.yaml"]
  i9 --> i15["../cptest/infra-test/stacks/catalog/compliance/regional/us-east-1.yaml"]
  i9 --> i16["../cptest/infra-test/stacks/catalog/compliance/regional/eu-north-1.yaml"]
  i9 --> i17["../cptest/infra-test/stacks/catalog/compliance/regional/ap-northeast-1.yaml"]
  i9 --> i18["../cptest/infra-test/stacks/catalog/compliance/regional/ap-northeast-2.yaml"]
  i9 --> i19["../cptest/infra-test/stacks/catalog/compliance/regional/us-east-2.yaml"]
  i9 --> i20["../cptest/infra-test/stacks/catalog/compliance/regional/ap-southeast-1.yaml"]
  i9 --> i21["../cptest/infra-test/stacks/catalog/compliance/regional/ap-northeast-3.yaml"]
  i9 --> i22["../cptest/infra-test/stacks/catalog/compliance/regional/eu-central-1.yaml"]
  i9 --> i23["../cptest/infra-test/stacks/catalog/compliance/regional/eu-west-3.yaml"]
  i9 --> i24["../cptest/infra-test/stacks/catalog/compliance/regional/sa-east-1.yaml"]
  i9 --> i25["../cptest/infra-test/stacks/catalog/compliance/regional/us-west-1.yaml"]
  i9 --> i26["../cptest/infra-test/stacks/catalog/compliance/regional/eu-west-2.yaml"]
  i10 --> i27["../cptest/infra-test/stacks/catalog/compliance/defaults.yaml"]
  i10 --> i28["../cptest/infra-test/stacks/catalog/compliance/compliance-root/defaults.yaml"]
  i11 --> i27
  i11 --> i28
  i12 --> i27
  i12 --> i28
  i13 --> i27
  i13 --> i28
  i14 --> i27
  i14 --> i28
  i15 --> i27
  i15 --> i28
  i16 --> i27
  i16 --> i28
  i17 --> i27
  i17 --> i28
  i18 --> i27
  i18 --> i28
  i19 --> i27
  i19 --> i28
  i20 --> i27
  i20 --> i28
  i21 --> i27
  i21 --> i28
  i22 --> i27
  i22 --> i28
  i23 --> i27
  i23 --> i28
  i24 --> i27
  i24 --> i28
  i25 --> i27
  i25 --> i28
  i26 --> i27
  i26 --> i28

```

## Example Text Concatenation

```
---
###
### stack: stacks/children/grand-children/grand-child.yaml
### chain: stacks/children/grand-children/grand-child.yaml
###


import:
  - children/child

vars:
  type: grand-child

---
###
### stack: stacks/children/child.yaml
### chain: stacks/children/grand-children/grand-child.yaml > stacks/children/child.yaml
###


import:
  - parent

vars:
  type: child

---
###
### stack: stacks/parent.yaml
### chain: stacks/children/grand-children/grand-child.yaml > stacks/children/child.yaml > stacks/parent.yaml
###


import: []

vars:
  type: parent

```