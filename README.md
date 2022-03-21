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
  i1["gbl/audit.yaml"] --> i2["gbl/globals.yaml"]
  i1 --> i3["catalog/iam-delegated-roles.yaml"]
  i2 --> i4["catalog/account-settings.yaml"]
  i2 --> i5["catalog/compliance/baseline.yaml"]
  i5 --> i6["catalog/compliance/regional/ap-south-1.yaml"]
  i5 --> i7["catalog/compliance/regional/eu-west-1.yaml"]
  i5 --> i8["catalog/compliance/regional/us-west-2.yaml"]
  i5 --> i9["catalog/compliance/regional/ap-southeast-2.yaml"]
  i5 --> i10["catalog/compliance/regional/ca-central-1.yaml"]
  i5 --> i11["catalog/compliance/regional/us-east-1.yaml"]
  i5 --> i12["catalog/compliance/regional/eu-north-1.yaml"]
  i5 --> i13["catalog/compliance/regional/ap-northeast-1.yaml"]
  i5 --> i14["catalog/compliance/regional/ap-northeast-2.yaml"]
  i5 --> i15["catalog/compliance/regional/us-east-2.yaml"]
  i5 --> i16["catalog/compliance/regional/ap-southeast-1.yaml"]
  i5 --> i17["catalog/compliance/regional/ap-northeast-3.yaml"]
  i5 --> i18["catalog/compliance/regional/eu-central-1.yaml"]
  i5 --> i19["catalog/compliance/regional/eu-west-3.yaml"]
  i5 --> i20["catalog/compliance/regional/sa-east-1.yaml"]
  i5 --> i21["catalog/compliance/regional/us-west-1.yaml"]
  i5 --> i22["catalog/compliance/regional/eu-west-2.yaml"]
  i6 --> i23["catalog/compliance/defaults.yaml"]
  i6 --> i24["catalog/compliance/compliance-root/defaults.yaml"]
  i7 --> i23
  i7 --> i24
  i8 --> i23
  i8 --> i24
  i9 --> i23
  i9 --> i24
  i10 --> i23
  i10 --> i24
  i11 --> i23
  i11 --> i24
  i12 --> i23
  i12 --> i24
  i13 --> i23
  i13 --> i24
  i14 --> i23
  i14 --> i24
  i15 --> i23
  i15 --> i24
  i16 --> i23
  i16 --> i24
  i17 --> i23
  i17 --> i24
  i18 --> i23
  i18 --> i24
  i19 --> i23
  i19 --> i24
  i20 --> i23
  i20 --> i24
  i21 --> i23
  i21 --> i24
  i22 --> i23
  i22 --> i24

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