

// Bulk of set flag code
CodedSetPermFlag:
    // a0 is parameter for encoded flag
    SW      ra, @ReturnAddress3
    LI      a1, 1
    JAL     @SetFlag
    LI      a2, 0
    LW      ra, @ReturnAddress3
    JR      ra
    NOP

.align
GunBitfields:
    .word 0x807FC952 // DK
    .word 0x807FC9B0 // Diddy
    .word 0x807FCA0E // Lanky
    .word 0x807FCA6C // Tiny
    .word 0x807FCACA // Chunky

.align
HandStatesNoGun:
    .byte 1 // DK
    .byte 0 // Diddy
    .byte 1 // Lanky
    .byte 1 // Tiny
    .byte 1 // Chunky

.align
HandStatesGun:
    .byte 2 // DK
    .byte 3 // Diddy
    .byte 2 // Lanky
    .byte 2 // Tiny
    .byte 2 // Chunky

.align
KeyAddress:
    .word 0x800258FA
    .word 0x8002C136
    .word 0x80035676
    .word 0x8002A0C2
    .word 0x8002B3F6
    .word 0x80025C4E
    .word 0x800327EE

.align
KeyMaps:
    .byte 0x08
    .byte 0xC5
    .byte 0x9A
    .byte 0x6F
    .byte 0x53
    .byte 0xC4
    .byte 0xC7

.align
FTTFlags:
    .half 355 // Bananaporter
    .half 358 // Crown Pad
    .half 359 // T&S (1)
    .half 360 // Mini Monkey
    .half 361 // Hunky Chunky
    .half 362 // Orangstand Sprint
    .half 363 // Strong Kong
    .half 364 // Rainbow Coin
    .half 365 // Rambi
    .half 366 // Enguarde
    .half 367 // Diddy
    .half 368 // Lanky
    .half 369 // Tiny
    .half 370 // Chunky
    .half 372 // Snide's
    .half 373 // Buy Instruments
    .half 374 // Buy Guns
    .half 376 // Wrinkly
    .half 382 // B Locker
    .half 392 // T&S (2)
    .half 775 // Funky
    .half 776 // Snide's
    .half 777 // Cranky
    .half 778 // Candy
    .half 779 // Japes
    .half 780 // Factory
    .half 781 // Galleon
    .half 782 // Fungi
    .half 783 // Caves
    .half 784 // Castle
    .half 785 // T&S (3)
    .half 786 // Helm
    .half 787 // Aztec
    .half 282 // Caves CS
    .half 194 // Galleon CS
    .half 256 // Daytime
    .half 257 // Fungi CS
    .half 303 // DK 5DI
    .half 349 // Castle CS
    .half 27 // Japes CS
    .half 95 // Aztec CS
    .half 93 // Lanky Help Me
    .half 94 // Tiny Help Me
    .half 140 // Chunky Help Me / Factory CS
    .half 195 // Water Raised
    .half 196 // Water Lowered
    .half 255 // Clock CS
    .half 277 // Rotating Room
    .half 299 // Giant Kosha
    .half 378 // Training Grounds Intro
    .half 0x5C // Llama CS
    .half 0x45 // Tiny Temple Ice Melted
    .half 0xA1 // Peanut Gate Opened in Galleon
    .half 0 // Null Terminator

.align
Lobbies:
    .byte 0xA9 // Japes
    .byte 0xAD // Aztec
    .byte 0xAF // Factory
    .byte 0xAE // Galleon
    .byte 0xB2 // Fungi
    .byte 0xC2 // Caves
    .byte 0xC1 // Castle
    .byte 0xAA // Helm
    .byte 0x00 // Terminator

.align
LobbyExits:
    .byte 0x2 // Japes
    .byte 0x3 // Aztec
    .byte 0x4 // Factory
    .byte 0x5 // Galleon
    .byte 0x6 // Fungi
    .byte 0xA // Caves
    .byte 0xB // Castle
    .byte 0x7 // Helm
    .byte 0x0 // Terminator

.align
KongTagAnywhereFlags:
    .half 385
    .half 6
    .half 70
    .half 66
    .half 117
    .half 0

.align
TrainingBarrelFlags:
    .half 0x182 // Dive
    .half 0x183 // Vine
    .half 0x184 // Orange
    .half 0x185 // Barrel
    .half 0 // Terminator

.align
KeyFlags_Normal:
    .half 0x001A
    .half 0x004A
    .half 0x008A
    .half 0x00A8
    .half 0x00EC
    .half 0x0124
    .half 0x013D


// Loops through a flag array and sets all of them
// Credit: Isotarge (Tag Anywhere V5)
SetAllFlags:
    // Params:
    // a0 = Array
    ADDIU   sp, sp, -0x18 // Push S0
    SW      s0, 0x10(sp)
    SW      ra, 0x14(sp)
    NOP

    // Load flag array base into register to loop with
    ADDIU   s0, a0, 0

    SetAllFlagsLoop:
        LHU     a0, 0(s0) // Load the flag index from the array
        BEQZ    a0, FinishSettingAllFlags // If the flag index is 0, exit the loop
        NOP
        JAL     CodedSetPermFlag
        NOP
        B       SetAllFlagsLoop
        ADDIU   s0, s0, 2 // Move on to the next flag in the array

    FinishSettingAllFlags:
        LW      s0, 0x10(sp)  // Pop S0
        LW      ra, 0x14(sp)
        JR
        ADDIU   sp, sp, 0x18

.org 0x80000A30 // 0x000A30 > 0x0010BC

LoadInAdditionalFile:
    JAL     @DMAFileTransfer
    ADDIU   a0, a0, 0x13F0
    LI      a1, 0x20049A0
    LI      a2, 0x805DAE00
    JAL     @DMAFileTransfer       
    LUI     a0, 0x200 // 0x2000000
    J       0x80000734
    NOP

