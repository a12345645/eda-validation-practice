#!/bin/bash

for file in rtl/*.v; do
    design=$(basename "$file" .v)
    yosys -p "
        read_verilog $file
        hierarchy -top $design
        proc; opt; techmap; abc; opt
        stat
        write_verilog logs/${design}_syn.v
    " > logs/${design}.log
done
