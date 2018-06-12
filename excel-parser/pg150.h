#ECC Register Memory Map
#Description: ECC Status Register
#define ECC_STATUS	0x00
#Description: ECC Enable Interrupt Register
#define ECC_EN_IRQ	0x04
#define ECC_ON_OFF	0x08
#Description: Correctable Error Count Register
#define CE_CNT	0x0C
#define RESERVED_01	0x10
#Description: Correctable Error First Failing Data Register
#define CE_FFD_31	0x100
#Description: Correctable Error First Failing Data Register
#define CE_FFD_63	0x104
#Description: Correctable Error First Failing Data Register
#define CE_FFD_95	0x108
#Description: Correctable Error First Failing Data Register
#define CE_FFD_127	0x10C
#define RESERVED_02	0x110
#Description: Correctable Error First Failing ECC Register
#define CE_FFE	0x180
#define UE_FFD_31	0x200
#define UE_FFD_63	0x204
#define UE_FFD_95	0x208
#define UE_FFD_127	0x20C
#define RESERVED_05	0x210
#define UE_FFE	0x280
#define RESERVED_06	0x284
#define UE_FFA_31	0x2C0
#define UE_FFA_63	0x2C4
#define RESERVED_07	0x2C8
#define FI_D_31	0x300
#define FI_D_63	0x304
#define FI_D_95	0x308
#define FI_D_127	0x30C
#define RESERVED_08	0x340
#define FI_ECC	0x380
