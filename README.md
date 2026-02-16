# Pico-Devboard

A custom rp2040 devboard, but with 16MB flash and a lot of extra features!

<img alt="Back Render" src="Images/BackRender.png" width="400">

| Front Render                            | PCB                    |
| --------------------------------------- | ---------------------- |
| ![Front Render](Images/FrontRender.png) | ![PCB](Images/PCB.png) |

## Motivation

I wanted a more capable RP2040 board with significantly more flash memory and USB-C. Most dev boards limit storage and input options, so I designed one that supports USB-C, battery input, higher current capability, and voltage monitoring while staying in the same form factor.

## Features

- RP2040 microcontroller
- 16MB QSPI Flash
- USB-C
- Battery input (Schottky diode OR-ing with USB)
- 500mA LDO (10V max input)
- VSYS voltage monitoring via resistor divider on ADC3
- Onboard power LED
- Onboard GPIO25 LED
- Bootsel + Reset button
- Fully labeled GPIO pins

## Future Improvements

- Buck-boost regulator for better efficiency + larger voltage range
- Exposed VSYS pin
- 3V3_EN pin breakout

## How to Use

Like a normal Pico:

1. Power the board via USB-C or VBAT input.
2. Flash firmware using BOOTSEL mode (or make your own)
3. Use onboard GPIO headers as you would with a standard Pico.

## BOM

A complete `BOM.csv` with direct links is provided in BOM.csv in the root directory.
| Id | Designator | Footprint | Quantity | Comment | Supplier and Ref |
|----|------------|------------|----------|----------|------------------|
| 1 | SW2, SW1 | SW_Push_SPST_NO_Alps_SKRK | 2 | SW_Push | |
| 2 | C16, C15 | C_0402_1005Metric | 2 | 33pF | |
| 3 | U2 | SOT-23-5_L3.0-W1.6-P0.95-LS2.8-BR | 1 | TPSPX3819M5-L-3-3 | |
| 4 | R11 | R_0402_1005Metric | 1 | 100K | |
| 5 | R10 | R_0402_1005Metric | 1 | 200K | |
| 6 | D4, D3 | SOD-123FL_L2.8-W1.8-LS3.8-RD | 2 | FMBR120VLSFT1G | |
| 7 | C9 | C_0402_1005Metric | 1 | 1nF | |
| 8 | J1 | USB_C_Receptacle_HRO_TYPE-C-31-M-12 | 1 | USB_C_Receptacle_USB2.0_14P | |
| 9 | C11, C8, C3, C10, C17, C5, C7, C6, C12, C2 | C_0402_1005Metric | 10 | 0.1uF | |
| 10 | R4, R3 | R_0402_1005Metric | 2 | 27 | |
| 11 | C1, C4 | C_0402_1005Metric | 2 | 1uF | |
| 12 | R1, R2 | R_0402_1005Metric | 2 | 5.1K | |
| 13 | J4 | PinHeader_1x03_P2.54mm_Vertical | 1 | Conn_01x03 | |
| 14 | C14, C13 | C_0603_1608Metric | 2 | 10uF | |
| 15 | D2, D1 | LED_0805_2012Metric | 2 | LED | |
| 16 | R7 | R_0402_1005Metric | 1 | 10K | |
| 17 | R9, R8, R5, R6 | R_0402_1005Metric | 4 | 1K | |
| 18 | J3, J2 | PinHeader_1x20_P2.54mm_Vertical | 2 | Conn_01x20 | |
| 19 | Y1 | Crystal_SMD_3225-4Pin_3.2x2.5mm | 1 | 12 MHz | |
| 20 | U1 | QFN-56-1EP_7x7mm_P0.4mm_EP3.2x3.2mm | 1 | RP2040 | |
| 21 | U3 | SOIC-8_5.3x5.3mm_P1.27mm | 1 | W25Q128JVS | |
