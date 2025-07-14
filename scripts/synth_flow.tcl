# Read design
read_verilog rtl/counter.v

# Elaborate design
hierarchy -top counter

# Do synthesis
proc; opt; techmap; abc; opt

# Report area
stat

# Write synthesized netlist
write_verilog logs/counter_syn.v

# Save report
tee -o logs/counter.log stat
