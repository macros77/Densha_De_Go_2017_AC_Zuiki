# Densha_De_Go_2017_AC_Zuiki

This script maps movements of ZUKI Master Controller to up and down mouse wheel movement events
allowing accelaration and breaking control in Densha de Go!! AC 2017 (tested with version 5.80.02)
running natively on Windows, without Teknoparrot emulation and key mappings.
Train horn is mapped to Zuiki controller A button (same as Nintendo Switch version of Densha).
 
Due to pygame compatibility problems with newer versions of Python (as of late December 2025)
Python 3.13 is the highest recommended version.
  
Tested with pygame 2.6.1 (SDL 2.28.4, Python 3.13.11) and pydirectinput-rgx 2.1.3
(standard pydirectinput does not support mouse scroll functionality)
https://pypi.org/project/pydirectinput-rgx/

Required Python packages:
- pygame
- pydirectinput-rgx

Tested with the following Zuiki controllers:
- Densha de GO! edition (ZKNS-001)
- ZUIKI Mascon Black (ZKNS-013)

Should work correctly with the other editions:
- Densha de GO! 1st anniversary translucent edition (ZKNS-002)
- ZUIKI Mascon Red (ZKNS-011)
- ZUIKI Mascon Blue (ZKNS-012)
