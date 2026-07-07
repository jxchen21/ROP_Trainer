#!/bin/bash
set -e

cd /ROP_Trainer

echo "[*] Building binary..."
bash build.sh

# Copy to container filesystem so SUID survives (bind mounts don't honor setuid)
cp ropvuln /usr/local/bin/ropvuln_suid
chown root:root /usr/local/bin/ropvuln_suid
chmod 4755 /usr/local/bin/ropvuln_suid

chmod a+rw /ROP_Trainer

ln -sf /usr/local/bin/ropvuln_suid /ROP_Trainer/ropvuln_suid
echo 'cd /ROP_Trainer' >> /home/wf-user/.bashrc

exec su -s /bin/bash wf-user
