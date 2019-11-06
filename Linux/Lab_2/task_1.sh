# sudo vim /etc/pam.d/sshd -> account requisite pam_time.so
# sudo vim /etc/security/time.conf -> sshd;*;@admins;!Al0000-2400


sudo groupadd admins
sudo useradd -m user1 -p qwe
sudo passwd user1
sudo useradd -m user2 -p qwe
sudo passwd user2
sudo usermod -a -G admins user1
sudo usermod -a -G admins user2