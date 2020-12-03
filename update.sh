LANYXSOFT_DIVISION="Alya"
PROGRAM="meets"
MACHINE_TYPE="`uname -m`"
USER="kali"

is_user_root() { [ "$(id -u)" -eq 0 ]; }
if is_user_root; then
    echo "Starting install script."
else
    echo "Please run with root."
    exit;
fi

case $MACHINE_TYPE in
    'x86_64')
        MACHINE_TYPE='x86_64'
        ;;
    *)
        MACHINE_TYPE='unknown'
        ;;
esac

# Linux Core Functions
lm_core_d() {
    if [ ! -d "/usr/share/lanyxsoft" ]
    then
        echo "[ERROR]: Base directory 'lanyxsoft' was not found. Creating it now in [/usr/share]..."
        mkdir "/usr/share/lanyxsoft"
    fi
    if [ -d "/usr/share/lanyxsoft" ]
    then
        if [ ! -d "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION" ]
        then
            echo "[ERROR]: Core directory '${LANYXSOFT_DIVISION}' was not found. Creating driectory '${LANYXSOFT_DIVISION}' in [/usr/share/lanyxsoft]"
            mkdir "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION"
        fi
    fi
    if [ -d "/usr/share/lanyxsoft" ]
    then
        if [ ! -d "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION/$PROGRAM" ]
        then
            echo "[ERROR]: Core directory '${PROGRAM}' was not found in [/usr/share/lanyxsoft/${LANYXSOFT_DIVISION}] Creating driectory '${PROGRAM}' in [/usr/share/lanyxsoft/${LANYXSOFT_DIVISION}]"
            mkdir "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION/$PROGRAM"
        fi
    fi
}

ld_core_f() {
    if ! ls "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION/$PROGRAM/crontab_template.txt" > /dev/null
    then
        wget -q "https://raw.githubusercontent.com/LanyxSoft-Industries/Alya_Google-Meets-Automation/main/crontab_template.txt"
    else
        echo "Removing outdated file..."
        rm "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION/$PROGRAM/crontab_template.txt"
        wget -q "https://raw.githubusercontent.com/LanyxSoft-Industries/Alya_Google-Meets-Automation/main/crontab_template.txt"
    fi
    if ! ls "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION/$PROGRAM/meet.py" > /dev/null
    then
        wget -q "https://raw.githubusercontent.com/LanyxSoft-Industries/Alya_Google-Meets-Automation/main/meet.py"
    else
        echo "Removing outdated file..."
        rm "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION/$PROGRAM/meet.py"
        wget -q "https://raw.githubusercontent.com/LanyxSoft-Industries/Alya_Google-Meets-Automation/main/meet.py"
    fi
    if ! ls "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION/$PROGRAM/schedule.json" > /dev/null
    then
        wget -q "https://raw.githubusercontent.com/LanyxSoft-Industries/Alya_Google-Meets-Automation/main/schedule.json"
    else
        echo "Removing outdated file..."
        rm "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION/$PROGRAM/schedule.json"
        wget -q "https://raw.githubusercontent.com/LanyxSoft-Industries/Alya_Google-Meets-Automation/main/schedule.json"
    fi
    if ! ls "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION/$PROGRAM/schedule_reset.py" > /dev/null
    then
        wget -q "https://raw.githubusercontent.com/LanyxSoft-Industries/Alya_Google-Meets-Automation/main/schedule_reset.py"
    else
        echo "Removing outdated file..."
        rm "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION/$PROGRAM/schedule_reset.py"
        wget -q "https://raw.githubusercontent.com/LanyxSoft-Industries/Alya_Google-Meets-Automation/main/schedule_reset.py"
    fi
    if ! ls "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION/$PROGRAM/scheduler.py" > /dev/null
    then
        wget -q "https://raw.githubusercontent.com/LanyxSoft-Industries/Alya_Google-Meets-Automation/main/scheduler.py"
    else
        echo "Removing outdated file..."
        rm "/usr/share/lanyxsoft/$LANYXSOFT_DIVISION/$PROGRAM/scheduler.py"
        wget -q "https://raw.githubusercontent.com/LanyxSoft-Industries/Alya_Google-Meets-Automation/main/scheduler.py"
    fi
    echo "File download complete!"
}

case "`uname`" in
    'Linux')
        OS='Linux'
        
        cd "/usr/share"
        lm_core_d
        cd "lanyxsoft/$LANYXSOFT_DIVISION/$PROGRAM"
        echo "Updating initialization log file."
        echo "Timestamp: `date`\n------> User: $USER\n------> `sudo dmidecode | grep -A3 '^System Information'`\n`uname -r` | `uname -v` on `uname -o`\n------> Node Name: `uname -n`\n" >> "LanyxSoft Alya Initialization.log"
        echo "Updating files from Github [https://github.com/LanyxSoft-Industries/Alya_Google-Meets-Automation]..."
        ld_core_f
        if [ ! -e "/etc/cron.d/lanyxsoft_${LANYXSOFT_DIVISION}_google-meets-automation" ]
        then
            echo "[ERROR]: Cron task not found in [/etc/cron.d]. Creating cron task [/etc/cron.d/lanyxsoft_${LANYXSOFT_DIVISION}_google-meets-automation]"
            echo "Creating cron task [/etc/cron.d/lanyxsoft_${LANYXSOFT_DIVISION}_google-meets-automation]"
            # echo "*/5 0-15 * * 1-5 root export DISPLAY=:0 && export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/bin && /usr/bin/python3 /usr/share/lanyxsoft/${LANYXSOFT_DIVISION}/${PROGRAM}/scheduler.py >> /usr/share/lanyxsoft/${LANYXSOFT_DIVISION}/${PROGRAM}/scheduler.log\n20 14 * * 1-5 root export DISPLAY=:0 && export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/bin && /usr/bin/python3 /usr/share/lanyxsoft/${LANYXSOFT_DIVISION}/${PROGRAM}/schedule_reset.py >> /usr/share/lanyxsoft/${LANYXSOFT_DIVISION}/${PROGRAM}/schedule_reset.log" >> "/etc/cron.d/lanyxsoft_${LANYXSOFT_DIVISION}_google-meets-automation"
            # echo "*/5 0-15 * * 1-5 root export DISPLAY=:0 && export PATH=\$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/bin && /usr/bin/python3 /usr/share/lanyxsoft/${LANYXSOFT_DIVISION}/${PROGRAM}/scheduler.py >> /usr/share/lanyxsoft/${LANYXSOFT_DIVISION}/${PROGRAM}/scheduler.log\n20 14 * * 1-5 root export DISPLAY=:0 && export PATH=\$PATH:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/bin && /usr/bin/python3 /usr/share/lanyxsoft/${LANYXSOFT_DIVISION}/${PROGRAM}/schedule_reset.py >> /usr/share/lanyxsoft/${LANYXSOFT_DIVISION}/${PROGRAM}/schedule_reset.log" >> "/etc/cron.d/lanyxsoft_${LANYXSOFT_DIVISION}_google-meets-automation"
            # echo "*/5 0-15 * * 1-5 root export DISPLAY=:0 && export PATH=\$PATH:/usr/local/bin && /usr/bin/python3 /usr/share/lanyxsoft/${LANYXSOFT_DIVISION}/${PROGRAM}/scheduler.py >> /usr/share/lanyxsoft/${LANYXSOFT_DIVISION}/${PROGRAM}/scheduler.log\n20 14 * * 1-5 root export DISPLAY=:0 && export PATH=\$PATH:/usr/local/bin && /usr/bin/python3 /usr/share/lanyxsoft/${LANYXSOFT_DIVISION}/${PROGRAM}/schedule_reset.py >> /usr/share/lanyxsoft/${LANYXSOFT_DIVISION}/${PROGRAM}/schedule_reset.log" >> "/etc/cron.d/lanyxsoft_${LANYXSOFT_DIVISION}_google-meets-automation"
           echo "*/5 0-15 * * 1-5 root DISPLAY=:0 XAUTHORITY=~${USER}/.Xauthority python3 /usr/share/lanyxsoft/${LANYXSOFT_DIVISION}/${PROGRAM}/scheduler.py >> /usr/share/lanyxsoft/${LANYXSOFT_DIVISION}/${PROGRAM}/scheduler.log\n20 14 * * 1-5 root DISPLAY=:0 XAUTHORITY=~${USER}/.Xauthority python3 /usr/share/lanyxsoft/${LANYXSOFT_DIVISION}/${PROGRAM}/schedule_reset.py >> /usr/share/lanyxsoft/${LANYXSOFT_DIVISION}/${PROGRAM}/schedule_reset.log" >> "/etc/cron.d/lanyxsoft_${LANYXSOFT_DIVISION}_google-meets-automation"
        fi
        ;;
    'FreeBSD')
        OS='FreeBSD'

        echo "Not implimented yet. :\\"
        exit;
        ;;
    'WindowsNT')
        OS='Windows'

        echo "Not implimented yet. :\\"
        exit;
        ;;
    'Darwin') 
        OS='Mac'

        echo "Not implimented yet. :\\"
        exit;
        ;;
    'SunOS')
        OS='Solaris'

        echo "Not implimented yet. :\\"
        exit;
        ;;
    'AIX')
        OS='AIX'

        echo "Not implimented yet. :\\"
        exit;
        ;;
    *)
        OS='unknown'

        echo "Not implimented yet. :\\"
        exit;
        ;;
esac
