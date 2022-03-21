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
  i1["gbl/globals.yaml"] --> i2["catalog/account-settings.yaml"]
  i1 --> i3["catalog/compliance/baseline.yaml"]
  i3 --> i4["catalog/compliance/regional/ap-south-1.yaml"]
  i3 --> i5["catalog/compliance/regional/eu-west-1.yaml"]
  i3 --> i6["catalog/compliance/regional/us-west-2.yaml"]
  i3 --> i7["catalog/compliance/regional/ap-southeast-2.yaml"]
  i3 --> i8["catalog/compliance/regional/ca-central-1.yaml"]
  i3 --> i9["catalog/compliance/regional/us-east-1.yaml"]
  i3 --> i10["catalog/compliance/regional/eu-north-1.yaml"]
  i3 --> i11["catalog/compliance/regional/ap-northeast-1.yaml"]
  i3 --> i12["catalog/compliance/regional/ap-northeast-2.yaml"]
  i3 --> i13["catalog/compliance/regional/us-east-2.yaml"]
  i3 --> i14["catalog/compliance/regional/ap-southeast-1.yaml"]
  i3 --> i15["catalog/compliance/regional/ap-northeast-3.yaml"]
  i3 --> i16["catalog/compliance/regional/eu-central-1.yaml"]
  i3 --> i17["catalog/compliance/regional/eu-west-3.yaml"]
  i3 --> i18["catalog/compliance/regional/sa-east-1.yaml"]
  i3 --> i19["catalog/compliance/regional/us-west-1.yaml"]
  i3 --> i20["catalog/compliance/regional/eu-west-2.yaml"]
  i4 --> i21["catalog/compliance/defaults.yaml"]
  i4 --> i22["catalog/compliance/compliance-root/defaults.yaml"]
  i5 --> i21
  i5 --> i22
  i6 --> i21
  i6 --> i22
  i7 --> i21
  i7 --> i22
  i8 --> i21
  i8 --> i22
  i9 --> i21
  i9 --> i22
  i10 --> i21
  i10 --> i22
  i11 --> i21
  i11 --> i22
  i12 --> i21
  i12 --> i22
  i13 --> i21
  i13 --> i22
  i14 --> i21
  i14 --> i22
  i15 --> i21
  i15 --> i22
  i16 --> i21
  i16 --> i22
  i17 --> i21
  i17 --> i22
  i18 --> i21
  i18 --> i22
  i19 --> i21
  i19 --> i22
  i20 --> i21
  i20 --> i22

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