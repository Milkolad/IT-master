# Отчет по лабораторной работе 3

## Посмотрим какие дисковые устройства и партиции есть в системе

### lsblk

```bash

sda      8:0    0  40G  0 disk
└─sda1   8:1    0  40G  0 part /

```

### blkid

```
/dev/sda1: UUID="8ac075e3-1124-4bb6-bef7-a6811bf8b870" TYPE="xfs"
```

### fdisk -l

```
Disk /dev/sda: 42.9 GB, 42949672960 bytes, 83886080 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0x0009ef88

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048    83886079    41942016   83  Linux
```

