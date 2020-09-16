# Dot

Dot is the default layout manager of graphviz, focusing on directed graphs and undirected graphs.

## Basic structure

```DOT
digraph pic{
    node [shape = Mrecord];
    start[label = "Start"];
    input[label = "Input"];
    bytecode[label = "Bytecode"];
    bytename[label = "ByteName"];

    start -> input;
    input -> bytecode[label = "compile"];
    bytecode -> bytename;
}
```

## Attributes

node:
