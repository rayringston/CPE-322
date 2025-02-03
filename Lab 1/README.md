# Half Adder Example
```bash
ghdl -a ha.vhdl
ghdl -a ha_tb.vhdl
ghdl -e ha_tb
ghdl -r ha_tb --vcd=ha.vcd
gtkwave ha.vcd
```
![ha gtkwave output](https://github.com/user-attachments/assets/20ea8983-742f-4d31-a207-0e57efaaced0)

# 4-to-1 Multiplexer Example
```bash
ghdl -a mux.vhdl
ghdl -a mux_tb.vhdl
ghdl -e mux_tb
ghdl -r mux_tb --vcd=mux.vcd
gtkwave mux.vcd
```
![4to1 mux gtkwave output](https://github.com/user-attachments/assets/3d7e042b-0711-4127-8a52-9ed36eccc103)
