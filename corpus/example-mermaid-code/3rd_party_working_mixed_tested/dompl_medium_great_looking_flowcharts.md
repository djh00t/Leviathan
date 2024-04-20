## Simple flowchart built using Mermaid

```mermaid
graph LR
%% Nodes
    1([Start])
    2[Look for lost item]
    3{Did I find it?}
    4([Stop])
%% Node links
    1 --> 2 --> 3 -->|Yes| 4
    3 -.->|No| 2 
```

## Simple gantt chart built using Mermaid

```mermaid
gantt
axisFormat %e%b
todayMarker on
section Activity 1
    TaskA	: TA, 2021-06-14, 4d
    TaskB	: TB, after TA, 2d
section Activity 2
    TaskC	: TC, after TA, 3d
    TaskD	: TD, after TC, 2d
section Activity 3
    TaskE	: TE, after TD, 1d
    TaskF	: TF, after TE, 2d
``` 

## Produce the basic layout of the flowchart
    
```mermaid
graph TD
%% Nodes
    0[Key Variable]
    1[Top Variable 1]
    2[Top Variable 2]
    3[Top Variable 3]
    31[Sub Variable 1]
    32[Sub Variable 2]
    321[Element 1]
    322[Element 2]

%% Links
    0 --- 1
    0 --- 2
    0 --- 3
    3 --- 31
    3 --- 32
    32 --- 321
    32 --- 322
```

## Adding additional detail to each node

```mermaid
graph TD
%% Nodes
    0[Key Variable<br>Target: 100, Actual: 80]
    1[Top Variable 1<br>Tgt: 20, Act: 20]
    2[Top Variable 2<br>Tgt: 30, Act: 30]
    3[Top Variable 3<br>Tgt: 50, Act: 30]
    31[Sub Variable 1<br>Tgt: 25, Act: 25]
    32[Sub Variable 2<br>Tgt: 25, Act: 5]
    321[Element 1<br>Tgt: 20, Act: 1]
    322[Element 2<br>Tgt: 5, Act: 4]

%% Links
    0 --- 1
    0 --- 2
    0 --- 3
    3 --- 31
    3 --- 32
    32 --- 321
    32 --- 322

```

## Assigning colours to each flowchart node

```mermaid
%%{init: {"theme": "default", "flowchart": {"curve": "monotoneY"}}}%%

graph TD
%% Nodes
    0[Key Variable]
    1[Top Variable 1]
    2[Top Variable 2]
    3[Top Variable 3]
    31[Sub Variable 1]
    subgraph SG32 ["Subgraph: Focus in on Sub-Variable"]
        32[Sub Variable 2]
        321[Element 1]
        322[Element 2]
    end

%% Links
    0 --- 1
    0 --- 2
    0 --- 3
    3 --- 31
    3 --- 32
    32 --- 321
    32 --- 322

%% Changing color of links [NOTE: Link arrows will remain black]
    linkStyle default fill: none, stroke: grey;
%% Defining the styles
    classDef Red fill:#FF9999;
    classDef Amber fill:#FFDEAD;
    classDef Green fill:#BDFFA4;

%% Assigning styles to nodes
    class 3,32,321 Red;
    class 322 Amber;
    class 1,2,31 Green;

```

## Encompassing all nodes within a subgraph

```mermaid
%%{init: {"theme": "default", "flowchart": {"curve": "monotoneY"}}}%%

graph TD
%% Adding a title to the flowchart using the SubGraph feature
subgraph SGTitle ["WHAT IS THE ROOT CAUSE OF THE PROBLEM?"]

%% Nodes
    0[Key Variable<br>Target: 100, Actual: 80]
    1[Top Variable 1<br>Tgt: 20, Act: 20]
    2[Top Variable 2<br>Tgt: 30, Act: 30]
    3[Top Variable 3<br>Tgt: 50, Act: 30]
    31[Sub Variable 1<br>Tgt: 25, Act: 25]
    32[Sub Variable 2<br>Tgt: 25, Act: 5]
    321[Element 1<br>Tgt: 20, Act: 1]
    322[Element 2<br>Tgt: 5, Act: 4]

%% Close title subgraph
    end

%% Links
    0 --- 1
    0 --- 2
    0 --- 3
    3 --- 31
    3 --- 32
    32 --- 321
    32 --- 322

%% Changing color of links [NOTE: Link arrows will remain black]
    linkStyle default fill: none, stroke: grey;
%% Defining the styles
    classDef Red fill:#FF9999;
    classDef Amber fill:#FFDEAD;
    classDef Green fill:#BDFFA4;
%% Styling the title subgraph
    classDef Title fill:#FF99FF00, stroke-width:0, color:grey;
    class SGTitle Title;

%% Assigning styles to nodes
    class 3,32,321 Red;
    class 322 Amber;
    class 1,2,31 Green;
```

## Final Product

```mermaid
graph TD
%% Adding a title to the flowchart using the SubGraph feature
subgraph SGTitle ["WHAT IS THE ROOT CAUSE OF THE PROBLEM? ____"]
%% Nodes
    0[Key Variable<br>Target: 100, Actual: 80]
    1[Top Variable 1<br>Tgt: 20, Act: 20]
    2[Top Variable 2<br>Tgt: 30, Act: 30]
    3[Top Variable 3<br>Tgt: 50, Act: 30]
    31[Sub Variable 1<br>Tgt: 25, Act: 25]
    32[Sub Variable 2<br>Tgt: 25, Act: 5]
    321[Element 1<br>Tgt: 20, Act: 1]
    322[Element 2<br>Tgt: 5, Act: 4]
%% Close title subgraph
    end
%% Links
    0 --- 1
    0 --- 2
    0 --- 3
    3 --- 31
    3 --- 32
    32 --- 321
    32 --- 322
%% Defining node styles
    classDef Red fill:#FF9999;
    classDef Amber	fill:#FFDEAD;
    classDef Green fill:#BDFFA4;
%% Assigning styles to nodes
    class 3,32,321 Red;
    class 322 Amber;
    class 1,2,31 Green;
    
%% Changing color of links [NOTE: Link arrows will remain black]
    linkStyle default fill: none, stroke: grey;
    
%% Styling the title subgraph
    classDef Title fill:#FF99FF00, stroke-width:0, color:grey, font-weight:bold, font-size: 17px;
    class SGTitle Title;
```