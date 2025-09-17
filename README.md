Simple nmap output file parser to create pretty tables using python.


<img width="414" height="224" alt="image" src="https://github.com/user-attachments/assets/2c66e1ba-2243-4f44-9755-7ca0b38a054a" />


```
nmap.py
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━┓
┃ HOST          ┃ PORTS     ┃ SERVICES ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━┩
│ 10.10.110.3   │ 443 / tcp │ https    │
├───────────────┼───────────┼──────────┤
│ 10.10.110.123 │ 22 / tcp  │ ssh      │
│               │ 80 / tcp  │ http     │
├───────────────┼───────────┼──────────┤
│ 10.10.110.124 │ 80 / tcp  │ http     │
└───────────────┴───────────┴──────────┘
   TCP_1000_10.10.110.3-123-124.gnmap
```
