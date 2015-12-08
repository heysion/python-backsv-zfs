#command
```bash
zfs snapshot -r tank/home/ahrens@friday

zfs list -t snapshot

```

[ZFS Snapshots](http://docs.oracle.com/cd/E19253-01/819-5461/6n7ht6r4f/index.html)

```bash
zfs rollback -r tank/home/ahrens@tuesday

```

[Rolling Back a ZFS Snapshot](http://docs.oracle.com/cd/E19253-01/819-5461/gbcxk/index.html)

## pre install pakcage

```bash
apt-get install sudo tmux htop rsync build-essential bash-completion smartmontools

sudo apt-get install linux-headers-3.16.0-4-amd64 automake libtool

sudo apt-get install build-essential gawk alien fakeroot linux-headers-$(uname -r)

sudo apt-get install zlib1g-dev uuid-dev libblkid-dev libselinux-dev parted lsscsi wget

```

## build spl

```bash
cd spl
./autogen.sh
./configure
make deb-utils deb-kmod
sudo dpkg -i *.deb

```


## build zfs

```bash
cd zfs
./autogen.sh
./configure
make deb-utils deb-kmod
sudo dpkg -i *.deb

```
