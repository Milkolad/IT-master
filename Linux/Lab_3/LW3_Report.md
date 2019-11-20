# Отчет по лабораторной работе 3

## Посмотрим какие дисковые устройства и партиции есть в системе

### lsblk

```bash
sda      8:0    0  40G  0 disk
└─sda1   8:1    0  40G  0 part /

```

### blkid

```bash
/dev/sda1: UUID="8ac075e3-1124-4bb6-bef7-a6811bf8b870" TYPE="xfs"
```

### fdisk -l

```bash
Disk /dev/sda: 42.9 GB, 42949672960 bytes, 83886080 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0x0009ef88

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048    83886079    41942016   83  Linux
```

### parted -l

```bash
Model: ATA VBOX HARDDISK (scsi)
Disk /dev/sda: 42.9GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags:

Number  Start   End     Size    Type     File system  Flags
 1      1049kB  42.9GB  42.9GB  primary  xfs          boot

```

* Какой размер дисков?
    * 40 GB (41921540 bytes)
* Есть ли неразмеченное место на дисках?
    * Нет
* Какой размер партиций?
    * 
        ```bash
        /dev/sda1   *        2048    83886079    41942016   83  Linux
        ```
* Какая таблица партционирования используется?
    * msdos
* Какой диск, партция или лвм том смонтированы в /
    *sda1

## Создадим сжатую файловую систему для чтения squashfs

### mksquash mai/* mai.sqsh
```bash
Parallel mksquashfs: Using 1 processor
Creating 4.0 filesystem on mai.sqsh, block size 131072.
[===============================================================================================================================================|] 27/27 100%

Exportable Squashfs 4.0 filesystem, gzip compressed, data block size 131072
        compressed data, compressed metadata, compressed fragments, compressed xattrs
        duplicates are removed
Filesystem size 50.94 Kbytes (0.05 Mbytes)
        64.88% of uncompressed filesystem size (78.51 Kbytes)
Inode table size 385 bytes (0.38 Kbytes)
        22.36% of uncompressed inode table size (1722 bytes)
Directory table size 379 bytes (0.37 Kbytes)
        65.12% of uncompressed directory table size (582 bytes)
Xattr table size 54 bytes (0.05 Kbytes)
        100.00% of uncompressed xattr table size (54 bytes)
Number of duplicate files found 1
Number of inodes 32
Number of files 28
Number of fragments 1
Number of symbolic links  0
Number of device nodes 0
Number of fifo nodes 0
Number of socket nodes 0
Number of directories 4
Number of ids (unique uids + gids) 1
Number of uids 1
        root (0)
Number of gids 1
        root (0)
```

### После монтирования сжатой файловой системы mai.squash в директорию /mnt/mai

#### df -h
```bash
/dev/sda1        40G  3.3G   37G   9% /
devtmpfs        488M     0  488M   0% /dev
tmpfs           496M     0  496M   0% /dev/shm
tmpfs           496M  6.7M  489M   2% /run
tmpfs           496M     0  496M   0% /sys/fs/cgroup
tmpfs           100M     0  100M   0% /run/user/1000
/dev/loop0      128K  128K     0 100% /mnt/mai
```

#### df -i 

```
/dev/sda1      20971008 36760 20934248    1% /
devtmpfs         124867   309   124558    1% /dev
tmpfs            126871     1   126870    1% /dev/shm
tmpfs            126871   381   126490    1% /run
tmpfs            126871    16   126855    1% /sys/fs/cgroup
tmpfs            126871     1   126870    1% /run/user/1000
/dev/loop0           32    32        0  100% /mnt/mai
```
#### mount

```
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime,seclabel)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
devtmpfs on /dev type devtmpfs (rw,nosuid,seclabel,size=499468k,nr_inodes=124867,mode=755)
securityfs on /sys/kernel/security type securityfs (rw,nosuid,nodev,noexec,relatime)
tmpfs on /dev/shm type tmpfs (rw,nosuid,nodev,seclabel)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,seclabel,gid=5,mode=620,ptmxmode=000)
tmpfs on /run type tmpfs (rw,nosuid,nodev,seclabel,mode=755)
tmpfs on /sys/fs/cgroup type tmpfs (ro,nosuid,nodev,noexec,seclabel,mode=755)
cgroup on /sys/fs/cgroup/systemd type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,xattr,release_agent=/usr/lib/systemd/systemd-cgroups-agent,name=systemd)
pstore on /sys/fs/pstore type pstore (rw,nosuid,nodev,noexec,relatime)
cgroup on /sys/fs/cgroup/cpu,cpuacct type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,cpuacct,cpu)
cgroup on /sys/fs/cgroup/freezer type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,freezer)
cgroup on /sys/fs/cgroup/devices type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,devices)
cgroup on /sys/fs/cgroup/net_cls,net_prio type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,net_prio,net_cls)
cgroup on /sys/fs/cgroup/hugetlb type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,hugetlb)
cgroup on /sys/fs/cgroup/pids type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,pids)
cgroup on /sys/fs/cgroup/perf_event type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,perf_event)
cgroup on /sys/fs/cgroup/blkio type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,blkio)
cgroup on /sys/fs/cgroup/cpuset type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,cpuset)
cgroup on /sys/fs/cgroup/memory type cgroup (rw,nosuid,nodev,noexec,relatime,seclabel,memory)
configfs on /sys/kernel/config type configfs (rw,relatime)
/dev/sda1 on / type xfs (rw,relatime,seclabel,attr2,inode64,noquota)
selinuxfs on /sys/fs/selinux type selinuxfs (rw,relatime)
systemd-1 on /proc/sys/fs/binfmt_misc type autofs (rw,relatime,fd=24,pgrp=1,timeout=0,minproto=5,maxproto=5,direct,pipe_ino=13390)
mqueue on /dev/mqueue type mqueue (rw,relatime,seclabel)
hugetlbfs on /dev/hugepages type hugetlbfs (rw,relatime,seclabel)
debugfs on /sys/kernel/debug type debugfs (rw,relatime)
sunrpc on /var/lib/nfs/rpc_pipefs type rpc_pipefs (rw,relatime)
tmpfs on /run/user/1000 type tmpfs (rw,nosuid,nodev,relatime,seclabel,size=101500k,mode=700,uid=1000,gid=1000)
/home/vagrant/mai.sqsh on /mnt/mai type squashfs (ro,relatime,seclabel)
```

* Какая файловая система примонтирована в /
    * sda1
* С какими опциями примонтирована файловая система в /
    * type - xfs, rw,relatime,seclabel,attr2,inode64,noquota
* Какой размер файловой системы приментированной в /mnt/mai
    * 128K

## Попробуем создать файлик в каталоге /dev/shm

### dd if=/dev/zero of=/dev/shm/mai bs=1M count=100

```
100+0 records in
100+0 records out
104857600 bytes (105 MB) copied, 0.0303084 s, 3.5 GB/s
```

### free -h
```
             total        used        free      shared  buff/cache   available
Mem:           991M         83M        125M        106M        782M        602M
Swap:          2.0G          0B        2.0G
```

### free -h после rm -f /dev/shm/mai
```
              total        used        free      shared  buff/cache   available
Mem:           991M         83M        225M        6.7M        682M        703M
Swap:          2.0G          0B        2.0G
```

* Что такое tmpfs
    * Временное файловое хранилище для монтирования файловых систем, размещаемых в ОЗУ
* Какая часть памяти изменялась? 
    * Свободная

## Изучим процессы запущенные в системе

### ps -eF

```
UID        PID  PPID  C    SZ   RSS PSR STIME TTY          TIME CMD
root         1     0  0 32025  6672   0 08:15 ?        00:00:01 /usr/lib/systemd/systemd --switched-root --system --deserialize 21
root         2     0  0     0     0   0 08:15 ?        00:00:00 [kthreadd]
root         3     2  0     0     0   0 08:15 ?        00:00:00 [ksoftirqd/0]
root         5     2  0     0     0   0 08:15 ?        00:00:00 [kworker/0:0H]
root         6     2  0     0     0   0 08:15 ?        00:00:00 [kworker/u2:0]
root         7     2  0     0     0   0 08:15 ?        00:00:00 [migration/0]
...
postfix  28046  2545  0 22440  4044   0 09:55 ?        00:00:00 pickup -l -t unix -u
root     28050  4750  0 25711  5500   0 09:59 ?        00:00:00 /sbin/dhclient -d -q -sf /usr/libexec/nm-dhcp-helper -pf /var/run/dhclient-eth0.pid -lf /var/l
root     28174  2397  0 38665  5556   0 10:00 ?        00:00:00 sshd: vagrant [priv]
vagrant  28177 28174  0 38665  2424   0 10:00 ?        00:00:00 sshd: vagrant@pts/0
vagrant  28178 28177  0 29092  3032   0 10:00 pts/0    00:00:00 -bash
root     28238 28178  0 47976  2392   0 10:02 pts/0    00:00:00 su
root     28242 28238  0 29098  3052   0 10:02 pts/0    00:00:00 bash
root     28295     2  0     0     0   0 10:27 ?        00:00:00 [kworker/0:2]
root     28317     2  0     0     0   0 10:30 ?        00:00:00 [loop0]
root     28349     2  0     0     0   0 10:53 ?        00:00:00 [kworker/0:1]
root     28366     2  0     0     0   0 11:01 ?        00:00:00 [kworker/0:0]
root     28367 28242  0 38841  1856   0 11:01 pts/0    00:00:00 ps -eF
```

### ps rx 
```
  PID TTY      STAT   TIME COMMAND
    9 ?        R      0:00 [rcu_sched]
28366 ?        R      0:00 [kworker/0:0]
28368 pts/0    R+     0:00 ps rx
```

### ps -e --forest 
```
...
 2393 ?        00:00:01 tuned
 2395 ?        00:00:00 rsyslogd
 2397 ?        00:00:00 sshd
28174 ?        00:00:00  \_ sshd
28177 ?        00:00:00      \_ sshd
28178 pts/0    00:00:00          \_ bash
28238 pts/0    00:00:00              \_ su
28242 pts/0    00:00:00                  \_ bash
28369 pts/0    00:00:00                      \_ ps
 2545 ?        00:00:00 master
 2554 ?        00:00:00  \_ qmgr
28046 ?        00:00:00  \_ pickup
 4750 ?        00:00:00 NetworkManager
28050 ?        00:00:00  \_ dhclient
 5607 ?        00:00:00 crond
 5715 ?        00:00:00 lvmetad
 5870 ?        00:00:00 auditd
```

### ps -efL

```
UID        PID  PPID   LWP  C NLWP STIME TTY          TIME CMD
root         1     0     1  0    1 08:15 ?        00:00:01 /usr/lib/systemd/systemd --switched-root --system --deserialize 21
root         2     0     2  0    1 08:15 ?        00:00:00 [kthreadd]
root         3     2     3  0    1 08:15 ?        00:00:00 [ksoftirqd/0]
root         5     2     5  0    1 08:15 ?        00:00:00 [kworker/0:0H]
root         6     2     6  0    1 08:15 ?        00:00:00 [kworker/u2:0]
root         7     2     7  0    1 08:15 ?        00:00:00 [migration/0]
root         8     2     8  0    1 08:15 ?        00:00:00 [rcu_bh]
root         9     2     9  0    1 08:15 ?        00:00:00 [rcu_sched]
root        10     2    10  0    1 08:15 ?        00:00:00 [lru-add-drain]
...
```

* Какие процессы в системе порождают дочерние процессы через fork
    *
* Какие процессы в системе являются мультитредовыми
    *

