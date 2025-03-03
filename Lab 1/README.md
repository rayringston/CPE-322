# Lab 1 - GHDL and GTKWave

## Half Adder Example
```console
ghdl -a ha.vhdl
ghdl -a ha_tb.vhdl
ghdl -e ha_tb
ghdl -r ha_tb --vcd=ha.vcd
gtkwave ha.vcd
```
![ha gtkwave output](https://github.com/user-attachments/assets/20ea8983-742f-4d31-a207-0e57efaaced0)

## 4-to-1 Multiplexer Example
```console
ghdl -a mux.vhdl
ghdl -a mux_tb.vhdl
ghdl -e mux_tb
ghdl -r mux_tb --vcd=mux.vcd
gtkwave mux.vcd
```
![4to1 mux gtkwave output](https://github.com/user-attachments/assets/3d7e042b-0711-4127-8a52-9ed36eccc103)

## Notes
- Must install GHDL and GTKWave to generate waveforms
- Shown terminal commands were done on the Windows Powershell
- Source files can be found on [Professor Lu's Repository](https://github.com/kevinwlu/dsd/tree/master/ghdl)

---

I pledge my honor that I have abided by the Stevnes Honor System - _Ray Ringston_
